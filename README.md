### FDE（Forward Deployed Engineer）

行政・大学の現場で、生成AIを動く形にして定着させる仕事をしています。

経歴サイト：https://takashi-101.github.io/

ポートフォリオ（代表実績5件）：https://takashi-101.github.io/portfolio/

### FDE・AXで求められる力と、その根拠

| 求められる力 | 動くもので示す（このGitHub） | 学びの裏付け（Credly） |
|---|---|---|
| 生成AI・LLMの実装（RAG・エージェント・MCP） | [jissoku-agent](https://github.com/takashi-101/jissoku-agent)、[mcp-tool-lock](https://github.com/takashi-101/mcp-tool-lock)、[readonly-mcp](https://github.com/takashi-101/readonly-mcp) | 33件（IBM RAG and Agentic AI Professional Certificate、IBM Generative AI Engineering Professional Certificate ほか） |
| ソフトウェア開発（テスト・CI・コンテナ） | 2026年11月公開の4件は、テストとCIの結果を公開 | 4件（Software Engineering Essentials、Full Stack Software Developer Assessment ほか） |
| データ活用（Python・SQL・BI） | [jissoku-agent](https://github.com/takashi-101/jissoku-agent) | 16件（Data Analysis with Python、Generative AI for Business Intelligence (BI) Analysts Specialization ほか） |
| クラウドと閉域の基盤 | [local-llm-record](https://github.com/takashi-101/local-llm-record)、[fde-checklist](https://github.com/takashi-101/fde-checklist) | 26件（Well-Architected Proficient、AWS Knowledge: Amazon ECS ほか） |
| セキュリティ・ガバナンス | [agent-ledger](https://github.com/takashi-101/agent-ledger)、[mcp-tool-lock](https://github.com/takashi-101/mcp-tool-lock)、[agent-trace-review](https://github.com/takashi-101/agent-trace-review) | 11件（Google Cybersecurity Professional Certificate、AWS Knowledge: Security Champion ほか） |
| 業務改革・AX推進（課題の整理から定着まで） | [gyomu-tanaoroshi](https://github.com/takashi-101/gyomu-tanaoroshi)、[fde-checklist](https://github.com/takashi-101/fde-checklist)、[funding-guide](https://github.com/takashi-101/funding-guide) | 21件（Process Mining - From Theory to Execution、Generative AI for Business Analysts Specialization、Lean Six Sigma White Belt ほか） |
| 生成AIの業務活用 | [ai-decision-audit](https://github.com/takashi-101/ai-decision-audit) | 20件（Google AI Professional Certificate、Generative AI Fundamentals Specialization ほか） |

Credly：https://www.credly.com/users/takashi-higuchi.2d0eec27 （130件とその他1件。2026年11月13日時点。上の表の件数は、この計131件を7分野に1件ずつ振り分けたもの）

JavaScriptを使わずに読める形式（Credlyの一覧に載る130件）：https://www.credly.com/users/takashi-higuchi.2d0eec27/badges.json

生成AIの業務活用に関わる資格：AI業務支援士（特定非営利活動法人IT整備士協会・2026年7月）、生成AIパスポート（一般社団法人生成AI活用普及協会・2023年10月）

データサイエンスの修了：東京大学データサイエンススクール 3コース修了（現在の名称でベーシックコース、概要速習コース、Pythonを使ったデータサイエンス挑戦コース・2019〜2020年。受講当時の分析言語はR）

行政・教育のデジタル活用に関わる役割・認定：デジタル推進委員（デジタル庁任命・2025年12月）、地域DXプロデューサー★（一般社団法人デジタル田園都市国家構想応援団・2025年9月）、教育CIO養成課程 修了（社会構想大学院大学 先端教育研究所・2025年3月）

### 公開しているもの

- [jissoku-agent](https://github.com/takashi-101/jissoku-agent) — 業務量の実測データを分析するAIエージェント。LLMには数値を書かせず指標IDで参照させ、指標の取り違えまで検出する（LangGraph・MCP・ローカルLLM）
- [fde-hybrid-router](https://github.com/takashi-101/fde-hybrid-router) — 機密区分で問い合わせを振り分けるルーター。個人情報を含むものはマスキングしてローカルLLM（Ollama）に送る。クラウド側は差し替え口と見本
- [mcp-tool-lock](https://github.com/takashi-101/mcp-tool-lock) — MCPの道具に仕込まれた指示と、承認後の書き換えを見つける。公式の参照サーバーで検証し、GitHub Actionとしても使える
- [agent-ledger](https://github.com/takashi-101/agent-ledger) — MCPの設定とAgent Skillsから、AIエージェントの道具の台帳を作り、危ない設定に印を付ける
- [agent-trace-review](https://github.com/takashi-101/agent-trace-review) — AIエージェントの行動記録（OpenTelemetry）から、人の承認を経ない書き込み・送信や、繰り返しの暴走を見つける
- [fde-eval-harness](https://github.com/takashi-101/fde-eval-harness) — fde-hybrid-router とローカルLLMを架空の13件で評価し、結果をRESULTS.mdに記録した評価ハーネス
- [pii-guard-gateway](https://github.com/takashi-101/pii-guard-gateway) — AIへ渡す前に氏名・電話・メール・個人番号・住所・金額を目印に置き換え、改ざんに気づける監査ログを残す前処理（検出できない範囲も明記）
- [fde-saas-webhook-bridge](https://github.com/takashi-101/fde-saas-webhook-bridge) — Webhookの汎用の受信サーバー。署名検証・二重処理の防止・再試行・DLQ（処理できなかった通知の退避先）を1コマンドのデモで確かめられる
- [readonly-mcp](https://github.com/takashi-101/readonly-mcp) — AIに決まった文書だけを安全に読ませる、読み取り専用のMCPサーバー
- [ittsukan-tool](https://github.com/takashi-101/ittsukan-tool) — 要件定義から定着までの7工程を1本で通して扱うツール（詰まっている工程だけでも使える）
- [madoguchi-kaito](https://github.com/takashi-101/madoguchi-kaito) — マニュアルや例規の原文を根拠に、窓口・庁内の問い合わせへの回答をそろえるツール
- [shinsei-fubi-check](https://github.com/takashi-101/shinsei-fubi-check) — 申請書の記載漏れ・書式の誤り・添付書類の不足を、受付の時点で確かめるツール
- [local-llm-record](https://github.com/takashi-101/local-llm-record) — 閉域のPCでローカルLLMに規程文書を読ませ、出力を原典と1行ずつ照合した測定記録と、導入・運用のための関連ツール
- [gennai-oss-closed-port](https://github.com/takashi-101/gennai-oss-closed-port) — デジタル庁の源内OSSとローカルLLMを、メモリ16GB・GPUなしのノートPC1台で動かした記録
- [fde-checklist](https://github.com/takashi-101/fde-checklist) — 現場のネットワークに入れない前提で閉域ローカルLLMの導入を進めるチェックリスト（6フェーズ24項目）と、生成AIの配置判定ツール
- [ai-decision-audit](https://github.com/takashi-101/ai-decision-audit) — AIへの依頼文と出力を並べ、依頼文に書かれていないのにAIが決めたことに印を付けて、採る・採らないを記録するWebツール
- [gyomu-tanaoroshi](https://github.com/takashi-101/gyomu-tanaoroshi) — 現場の担当者が業務を棚卸しし、経験が要る業務の判断の分かれ目を事務引継ぎ記録として残すツール
- [scs-star3-selfcheck](https://github.com/takashi-101/scs-star3-selfcheck) — SCS評価制度の★3を自分で点検し、結果を専門家の確認に回せる形で書き出すツール（外部への通信なし）
- [funding-guide](https://github.com/takashi-101/funding-guide) — AI導入・人材育成に使える公的制度28件を、受給者を分けて整理し、条件付きで試算するWebアプリ
- [palantir-applied-notional-project](https://github.com/takashi-101/palantir-applied-notional-project) — Palantir Learn の実践課題を、ブラウザだけで動く1枚のページで作った成果物（データの掃除・車両一覧・不具合の受付箱）
- [remove-keep-marks](https://github.com/takashi-101/remove-keep-marks) — Wordの見出しの行頭に出る黒い点（■）を元の設定ごと外し、ページ最下部に取り残された見出しを検出するスクリプト

### 現場で使う小さな道具

- [fde-ops-doctor](https://github.com/takashi-101/fde-ops-doctor) — Pythonの版・空き容量・設定ファイル・SQLiteの整合性を1コマンドで確かめる、運用の一次切り分けツール
- [fde-rag-chunk-auditor](https://github.com/takashi-101/fde-rag-chunk-auditor) — 文書を決まった文字数で分割し、文の途中で切れたチャンクの数を数える点検ツール
- [fde-prompt-version-registry](https://github.com/takashi-101/fde-prompt-version-registry) — プロンプトを版ごとに内容のハッシュと評価スコアつきで記録し、2つの版のスコアを比べる
- [fde-csv-schema-validator](https://github.com/takashi-101/fde-csv-schema-validator) — 業務CSVのID列の欠損・重複と、日付の表記を確かめる前処理
- [fde-cost-quota-guard](https://github.com/takashi-101/fde-cost-quota-guard) — 見積額と台帳の合計が上限を超えるかを判定する、予算の台帳
- [fde-handover-runbook-gen](https://github.com/takashi-101/fde-handover-runbook-gen) — 日次確認コマンド・連絡先・切り戻し手順から、決まった形の運用引き継ぎ書（Markdown）を作る
