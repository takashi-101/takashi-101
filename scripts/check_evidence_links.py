"""各リポジトリの README と経歴サイトに載せた検証URLが、いまも開けるかを確かめる。

対象：このプロフィールの README がリンクしているリポジトリの README.md と、
経歴サイト（takashi-101.github.io）の index.html・portfolio/index.html。

判定：
- Credly：公開API（Open Badges）で存在を確かめ、公開一覧（badges.json）に載っているかを見る。
  README の表の行は、書いてある名称と発行日も公開一覧と照合する。
  （Credly のバッジのページは、存在しないIDでも開けるため、ページでは判定しない）
- Skilljar：存在しない番号は 404 を返す。README の表の行は修了日も照合する。
- OpenAI Academy：ページの題名に「issued by」が入るかを見る。
- Coursera：存在しない番号でもページが開けるため自動では判定できず、件数だけ出す。

標準ライブラリだけで動く。開けないURLや食い違いがあれば終了コード1で終わる。
通信の一時的な失敗（タイムアウト・5xx）は警告に留め、失敗にはしない。
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

OWNER = "takashi-101"
CREDLY_USER = "takashi-higuchi.2d0eec27"
SITE_PAGES = ["index.html", "portfolio/index.html"]
UA = {"User-Agent": "evidence-link-check (GitHub Actions)"}
ROOT = Path(__file__).resolve().parent.parent

URL_RE = re.compile(
    r"https://(?:www\.credly\.com/badges/[0-9a-f-]{36}"
    r"|verify\.skilljar\.com/c/[A-Za-z0-9]+"
    r"|academy\.openai\.com/public/certificate/[A-Za-z0-9]+"
    r"|(?:www\.)?coursera\.org/(?:verify|account/accomplishments)/[A-Za-z0-9/-]+)"
)
DATE_JA = re.compile(r"(\d{4})年(\d{1,2})月(\d{1,2})日")
NAME_JA = re.compile(r"「([^」]+)」")
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


class Transient(Exception):
    pass


def get(url, timeout=30):
    """(状態コード, 本文) を返す。タイムアウトと5xxは2回まで再試行し、それでも駄目なら Transient。"""
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310  # nosec B310
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code < 500:
                return e.code, ""
            last = f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001
            last = repr(e)
        time.sleep(2 * (attempt + 1))
    raise Transient(last)


def raw(repo, path):
    st, body = get(f"https://raw.githubusercontent.com/{OWNER}/{repo}/HEAD/{path}")
    if st != 200:
        raise RuntimeError(f"{repo}/{path} を取得できません（HTTP {st}）")
    return body


def credly_public_list():
    badges, page = {}, 1
    while True:
        st, body = get(f"https://www.credly.com/users/{CREDLY_USER}/badges.json?page={page}")
        if st != 200:
            raise RuntimeError(f"Credly の公開一覧を取得できません（HTTP {st}）")
        data = json.loads(body)
        for b in data["data"]:
            badges[b["id"]] = (b["badge_template"]["name"], b["issued_at_date"])
        if not data["metadata"].get("next_page_url"):
            return badges
        page += 1


def ja_date(text):
    m = DATE_JA.search(text or "")
    return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}-{int(m.group(3)):02d}" if m else None


def learning_cell(line, url):
    """Markdown の表の行で、URLの入った列の1つ手前（「裏付けになる学習」の列）を返す。表の行でなければ None。"""
    if not line.lstrip().startswith("|"):
        return None
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    for k, c in enumerate(cells):
        if url in c and k > 0:
            return cells[k - 1]
    return None


def skilljar_date(body):
    text = re.sub(r"<[^>]+>", " ", body)
    m = re.search(r"Completion Date\s+([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2}),\s+(\d{4})", text)
    if not m or m.group(1).lower() not in MONTHS:
        return None
    return f"{int(m.group(3)):04d}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}"


def collect_sources():
    """(場所の名前, 本文, Markdownか) の一覧。"""
    profile = (ROOT / "README.md").read_text(encoding="utf-8")
    repos = sorted({r for r in re.findall(rf"https://github\.com/{OWNER}/([\w.-]+)\)", profile)} - {OWNER})
    sources = [(f"{OWNER}/README.md", profile, True)]
    for repo in repos:
        sources.append((f"{repo}/README.md", raw(repo, "README.md"), True))
    for page in SITE_PAGES:
        sources.append((f"{OWNER}.github.io/{page}", raw(f"{OWNER}.github.io", page), False))
    return sources


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    problems, warnings, manual = [], [], set()
    badges = credly_public_list()
    sources = collect_sources()
    cache = {}

    def fetch(url):
        if url not in cache:
            try:
                if "credly.com/badges/" in url:
                    bid = url.rsplit("/", 1)[1]
                    cache[url] = get(f"https://api.credly.com/v1/obi/v2/badge_assertions/{bid}")
                else:
                    cache[url] = get(url)
            except Transient as e:
                cache[url] = ("transient", str(e))
            time.sleep(0.5)
        return cache[url]

    checked = 0
    for where, text, is_md in sources:
        for ln, line in enumerate(text.splitlines(), 1):
            for url in URL_RE.findall(line):
                loc = f"{where}:{ln}"
                if "coursera.org" in url:
                    manual.add(url)
                    continue
                checked += 1
                st, body = fetch(url)
                if st == "transient":
                    warnings.append(f"{loc} {url} 一時的に確かめられません（{body}）")
                    continue
                if "credly.com/badges/" in url:
                    bid = url.rsplit("/", 1)[1]
                    if st != 200:
                        problems.append(f"{loc} {url} Credly に存在しません（HTTP {st}）")
                    elif bid not in badges:
                        problems.append(f"{loc} {url} Credly の公開一覧に載っていません（非公開か取り消し）")
                    elif is_md and learning_cell(line, url):
                        name, date = badges[bid]
                        cell = learning_cell(line, url)
                        stated_name = NAME_JA.search(cell)
                        stated_date = ja_date(cell)
                        if stated_date and stated_date != date:
                            problems.append(f"{loc} 発行日の食い違い：README {stated_date}／Credly {date}（{name}）")
                        if stated_name:
                            a, s = name.lower(), stated_name.group(1).lower()
                            if s not in a and a not in s:
                                problems.append(f"{loc} 名称の食い違い：README「{stated_name.group(1)}」／Credly「{name}」")
                elif "skilljar.com" in url:
                    if st != 200:
                        problems.append(f"{loc} {url} 修了証が見つかりません（HTTP {st}）")
                    elif is_md and ja_date(learning_cell(line, url)):
                        stated = ja_date(learning_cell(line, url))
                        actual = skilljar_date(body)
                        if actual and actual != stated:
                            problems.append(f"{loc} 修了日の食い違い：README {stated}／Skilljar {actual}")
                elif "academy.openai.com" in url:
                    title = re.search(r'"og:title" content="([^"]*)"', body)
                    if st != 200 or not (title and "issued by" in title.group(1)):
                        problems.append(f"{loc} {url} OpenAI Academy の修了証として表示されません")

    lines = [
        "# 検証URLの確認",
        "",
        f"- 対象：{len(sources)} か所、確かめたURL：{checked} 件（重複を含む）、Credly の公開一覧：{len(badges)} 件",
        f"- 問題：{len(problems)} 件、一時的に確かめられなかったもの：{len(warnings)} 件",
        f"- Coursera（自動では判定できないため、ブラウザで確認）：{len(manual)} 件",
        "",
    ]
    if problems:
        lines += ["## 問題", ""] + [f"- {p}" for p in problems] + [""]
    if warnings:
        lines += ["## 一時的に確かめられなかったもの", ""] + [f"- {w}" for w in warnings] + [""]
    report = "\n".join(lines)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(report + "\n")
    for w in warnings:
        print(f"::warning::{w}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
