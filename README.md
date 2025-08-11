# ADK Tutorial - 天気エージェント完全ガイド

このプロジェクトは、Google Agent Development Kit (ADK) を使用した天気検索エージェントの段階的チュートリアル実装です。基本的なエージェントから高度なセーフティ機能まで、5つのステップで学習できます。

## 概要

このチュートリアルでは、以下の内容を段階的に学習できます：

### Step 1: 基本的な天気エージェント
- ✅ **ツール定義と使用法**: エージェントに特定の能力（データ取得など）を付与するPython関数（`tools`）の作成
- ✅ **基本的なエージェント作成**: ADKを使用した天気情報エージェントの実装
- ✅ **セッション管理**: `Runner`と`SessionService`を使用したエージェント実行環境の設定

### Step 2: マルチモデル対応
- ✅ **LiteLLM統合**: GPT-4o、Claude Sonnet等の外部LLMモデルの使用
- ✅ **モデル切り替え**: 複数のLLMプロバイダーの柔軟な選択

### Step 3: エージェントチーム
- ✅ **サブエージェント**: 専門化されたエージェント（挨拶・別れ担当）の作成
- ✅ **エージェント連携**: メインエージェントからサブエージェントへのタスク委譲
- ✅ **専門ツール**: 各エージェント専用のツール実装

### Step 4: セッション状態管理
- ✅ **ステートフルツール**: セッション状態を読み書きする天気ツール
- ✅ **ユーザー設定保存**: 温度単位設定の永続化
- ✅ **履歴管理**: 前回の天気レポートの自動保存・取得
- ✅ **状態初期化**: セッション作成時の初期状態設定

### Step 5: セーフティガードレール
- ✅ **入力検証ガードレール**: 特定キーワード（BLOCK）を含むリクエストのブロック
- ✅ **ツール実行制限**: 特定の都市（Paris）への天気検索の禁止
- ✅ **コールバック機能**: LLM呼び出し前・ツール実行前の介入処理

## プロジェクト構造

```
adk_tutorial/
├── README.md                    # このファイル
├── requirements.txt             # 依存関係
├── step_1/                     # Step 1: 基本的な天気エージェント
│   ├── __init__.py
│   ├── agent.py                # エージェントとツールの定義
│   └── tools/
│       └── get_weather.py      # 基本的な天気取得ツール
├── step_2_litellm/             # Step 2: マルチモデル対応
│   ├── __init__.py
│   ├── agent.py                # LiteLLM使用版
│   └── tools/
│       └── get_weather.py      # 天気取得ツール
├── step_3/                     # Step 3: エージェントチーム
│   ├── __init__.py
│   ├── agent.py                # メインエージェント
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── greeting_agent.py   # 挨拶専門エージェント
│   │   └── farewell_agent.py   # 別れ専門エージェント
│   └── tools/
│       ├── get_weather.py      # 天気取得ツール
│       ├── say_hello.py        # 挨拶ツール
│       └── say_goodbye.py      # 別れツール
├── step_4/                     # Step 4: セッション状態管理
│   ├── __init__.py
│   ├── agent.py                # ステートフルエージェント
│   ├── session.py              # セッション管理
│   ├── agents/
│   │   ├── greeting_agent.py   # 挨拶エージェント
│   │   └── farewell_agent.py   # 別れエージェント
│   └── tools/
│       ├── get_weather_stateful.py      # 状態対応天気ツール
│       ├── get_last_weather_report.py   # 履歴取得ツール
│       ├── set_temperature_unit.py      # 設定変更ツール
│       ├── say_hello.py        # 挨拶ツール
│       └── say_goodbye.py      # 別れツール
└── step_5/                     # Step 5: セーフティガードレール
    ├── __init__.py
    ├── agent.py                # ガードレール付きエージェント
    ├── session.py              # セッション管理
    ├── before_model_callback.py # LLM呼び出し前ガードレール
    ├── before_tool_callback.py  # ツール実行前ガードレール
    ├── agents/
    │   ├── greeting_agent.py   # 挨拶エージェント
    │   └── farewell_agent.py   # 別れエージェント
    └── tools/
        ├── get_weather_stateful.py      # 状態対応天気ツール
        ├── get_last_weather_report.py   # 履歴取得ツール
        ├── set_temperature_unit.py      # 設定変更ツール
        ├── say_hello.py        # 挨拶ツール
        └── say_goodbye.py      # 別れツール
```

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env`ファイルを作成し、必要なAPI キーを設定してください：

```.env
# Google AI Studio API Key (Geminiモデル用)
# https://aistudio.google.com/app/apikey からAPIキーを取得
GOOGLE_GENAI_API_KEY="your-google-ai-studio-api-key-here"

# OpenAI API Key (GPT-4o用 - Step 2以降で使用)
OPENAI_API_KEY="your-openai-api-key-here"

# Anthropic API Key (Claude用 - Step 2以降で使用)
ANTHROPIC_API_KEY="your-anthropic-api-key-here"
```

## 実行方法

### ADK標準コマンドを使用

各ステップのディレクトリで以下を実行：

```bash
# Step 1: 基本的な天気エージェント
cd step_1
adk run

# Step 2: マルチモデル対応
cd step_2_litellm
adk run

# Step 3: エージェントチーム
cd step_3
adk run

# Step 4: セッション状態管理
cd step_4
adk run

# Step 5: セーフティガードレール
cd step_5
adk run
```

### Web UIを使用

```bash
adk web .
```
Web UIで使いたいステップとモデルを選択できます。

## 各ステップの詳細機能

### Step 1: 基本的な天気エージェント
- **天気検索ツール** (`get_weather`)
  - 対応都市: New York, London, Tokyo
  - モックデータによる天気情報提供
- **基本エージェント** (`weather_agent_v1`)
  - モデル: Gemini 2.5 Flash
  - 単純な天気情報取得とエラーハンドリング

### Step 2: マルチモデル対応
- **LiteLLM統合**
  - GPT-4o、Claude Sonnet、Gemini等の選択可能
  - 環境変数による簡単なモデル切り替え
- **同一ツール・インターフェース**
  - Step 1と同じツールを異なるモデルで実行

### Step 3: エージェントチーム
- **専門エージェント**
  - `greeting_agent`: 挨拶専門（`say_hello`ツール使用）
  - `farewell_agent`: 別れ専門（`say_goodbye`ツール使用）
- **タスク委譲**
  - メインエージェントが適切なサブエージェントに処理を委譲
  - 天気情報はメインエージェントが直接処理

### Step 4: セッション状態管理
- **ステートフル天気ツール** (`get_weather_stateful`)
  - ユーザーの温度単位設定を状態から読み取り
  - 一時的な単位指定（`unit`パラメータ）サポート
  - 最後にチェックした都市を状態に保存
- **設定管理ツール** (`set_temperature_unit`)
  - Celsius/Fahrenheit設定の永続的変更
- **履歴管理** (`get_last_weather_report`)
  - 前回の天気レポートの取得
  - `output_key`による自動保存
- **セッション初期化**
  - 初期状態設定（Celsius、履歴なし）
  - 同期・非同期両対応

### Step 5: セーフティガードレール
- **入力検証ガードレール** (`before_model_callback`)
  - 「BLOCK」キーワードを含むリクエストをブロック
  - LLM呼び出し前の介入処理
  - 状態への記録機能
- **ツール実行制限** (`before_tool_callback`)
  - パリの天気検索を政策的に禁止
  - ツール実行前の介入処理
  - カスタムエラーメッセージの返却
- **コールバック統合**
  - エージェント作成時のコールバック登録
  - 複数ガードレールの同時適用

## 学習の進め方

### 推奨学習順序
1. **Step 1**: ADKの基本概念とツール作成を理解
2. **Step 2**: 複数LLMモデルの使い分けを学習
3. **Step 3**: エージェントの協調動作と専門化を体験
4. **Step 4**: セッション状態を活用した高度な機能実装
5. **Step 5**: 本番環境で重要なセーフティ機能を実装

### 各ステップで学べること
- **Step 1→2**: モデル抽象化とプロバイダー切り替え
- **Step 2→3**: エージェント設計とタスク分散
- **Step 3→4**: 状態管理とユーザー体験向上
- **Step 4→5**: セキュリティとガバナンス機能

## 応用例

このチュートリアルで学んだ技術は以下のような用途に応用できます：

- **カスタマーサポートボット**: 専門エージェントによる問い合わせ分類
- **データ分析アシスタント**: 状態管理による継続的な分析セッション
- **コンテンツ生成システム**: ガードレールによる安全なコンテンツ生成
- **教育支援ツール**: 学習進捗の状態管理と適応的応答

## トラブルシューティング

### よくある問題

1. **API キーエラー**: `GOOGLE_GENAI_API_KEY`が正しく設定されているか確認
2. **モジュールが見つからない**: `pip install -r requirements.txt`を実行
3. **非同期実行エラー**: Jupyter環境では`await`、スクリプトでは`asyncio.run()`を使用
4. **セッション状態エラー**: Step 4以降で`create_session_sync()`が正しく呼ばれているか確認
5. **ガードレール動作しない**: Step 5でコールバック関数がエージェントに正しく登録されているか確認
6. **ツール実行エラー**: ツール関数のシグネチャ（引数名・型）が正しいか確認

### サポート

- [ADK ドキュメント](https://google.github.io/adk-docs/)
- [ADK GitHub リポジトリ](https://github.com/google/adk-python)

## ライセンス

このプロジェクトは、ADK チュートリアルの一部として提供されています。