"""Devin AIエージェント研究所 - プロンプト定義

Devin（Cognition AI）特化ブログ用のプロンプトを一元管理する。
"""

# ペルソナ設定
PERSONA = (
    "あなたはAIエージェント開発の専門家です。"
    "Cognition AIが開発した自律型AIソフトウェアエンジニア「Devin」を実際に開発プロジェクトで使い込んでいます。"
    "Devinの機能、限界、実用的な活用法を熟知しており、初心者にもわかりやすく解説できます。"
    "競合製品（Cursor Agent、Claude Code、GitHub Copilot Agent等）との違いも把握しています。"
)

# 記事構成テンプレート
ARTICLE_FORMAT = """
## この記事でわかること
- ポイント1
- ポイント2
- ポイント3

## 結論（先に知りたい人向け）
（3行で結論を述べる）

## 本題の詳細解説
（メインコンテンツ）

## Devinの使い方・設定方法
（該当する場合のセットアップ手順）

## 人間エンジニアとの比較
（Devinに任せるべきタスク vs 人間がやるべきタスク）

## 他ツールとの比較
（Cursor Agent、Claude Code、GitHub Copilot Agent等との違い）

## よくある質問（FAQ）
Q1. ...
A1. ...

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別プロンプト追加指示
CATEGORY_PROMPTS = {
    "Devin 使い方": (
        "Devinのセットアップ手順、タスク依頼方法、Slackからの使い方を具体的に解説してください。"
        "ターゲットキーワード例: 「Devin 使い方」「Devin AI 始め方」「Devin セットアップ」"
        "初心者がつまずきやすいポイントも含めてください。"
    ),
    "Devin 料金・プラン": (
        "Devinの料金プラン（$20/月のCoreプラン）の詳細、以前の$500/月からの値下げ経緯、"
        "ACU（Agent Compute Unit）の仕組みを解説してください。"
        "ターゲットキーワード例: 「Devin 料金」「Devin 無料」「Devin 価格」"
        "コストパフォーマンスの分析も含めてください。"
    ),
    "Devin vs 人間エンジニア": (
        "Devinがエンジニアの仕事をどこまで代替できるか、客観的に分析してください。"
        "ターゲットキーワード例: 「Devin エンジニア 不要」「AI 仕事 奪う」「Devin 限界」"
        "煽りではなく、現実的な棲み分けを解説してください。"
    ),
    "Devin 最新ニュース": (
        "Cognition AIとDevinの最新動向を解説してください。"
        "注目トピック: DevinがDevinを管理する自律オーケストレーション機能、"
        "スケジュール自動実行（Devin Triggers）、料金値下げ、新機能リリース。"
        "ターゲットキーワード例: 「Devin 最新」「Devin アップデート」「Cognition AI」"
    ),
    "AIエージェント開発": (
        "広義のAIエージェント技術について解説してください。"
        "ターゲットキーワード例: 「AIエージェント とは」「AIエージェント 開発」「自律型AI」"
        "Devinを含むAIエージェントの技術的背景・アーキテクチャにも触れてください。"
    ),
    "Devin 活用事例": (
        "Devinを実際の開発プロジェクトでどう活用するか、具体例を交えて解説してください。"
        "コードレビュー自動化、バグ修正、リファクタリング、テスト作成などの実例。"
        "ターゲットキーワード例: 「Devin 活用」「Devin 事例」「Devin コードレビュー」"
    ),
    "Devin API・統合": (
        "DevinのAPI利用方法、Slack統合、GitHub統合、Devin Triggersの設定方法を解説してください。"
        "ターゲットキーワード例: 「Devin API」「Devin Slack連携」「Devin GitHub統合」"
        "実際のコード例や設定手順を含めてください。"
    ),
    "AIエージェント比較": (
        "Devinと他のAI開発ツールを客観的に比較してください。"
        "比較対象: Cursor Agent、Claude Code、GitHub Copilot Agent、Windsurf等。"
        "ターゲットキーワード例: 「Devin vs Cursor」「AIエージェント 比較」「Devin Copilot 違い」"
        "料金・機能・使いやすさ・得意分野で比較してください。"
    ),
}

# ニュースソース
NEWS_SOURCES = [
    "Cognition AI Blog (https://cognition.ai/blog)",
    "TechCrunch",
    "The Verge",
    "Hacker News",
    "X (Twitter) #Devin #CognitionAI",
]

# FAQ構造化データ有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "Devin（Cognition AI）に関連するキーワードを選定してください。\n"
    "以下のトレンドトピックを参考にしてください:\n"
    "- Devinの$20/月への値下げとCoreプラン\n"
    "- DevinがDevinを管理する自律オーケストレーション\n"
    "- Devin Triggers（スケジュール自動実行）\n"
    "- Devin vs Cursor Agent vs Claude Code\n"
    "- AIエージェントによるコード自動生成の進化\n"
    "- Cognition AIの資金調達と評価額\n"
    "日本語で検索されやすいキーワードを意識してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        "Devin AIエージェント研究所用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        "以下のカテゴリから1つ選び、そのカテゴリで今注目されている"
        "Devin関連のトピック・キーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        "日本のエンジニアやテック系ビジネスマンが検索しそうなキーワードを意識してください。\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Devin特化記事生成プロンプトを構築する"""
    category_extra = CATEGORY_PROMPTS.get(category, "")

    faq_instruction = ""
    if FAQ_SCHEMA_ENABLED:
        faq_instruction = (
            "\n\n【FAQ要件】\n"
            "記事内に「## よくある質問（FAQ）」セクションを必ず含め、"
            "3〜5個のQ&Aを記載してください。"
            "このFAQはJSON-LD（FAQPage）構造化データとしてサイトに埋め込まれます。"
        )

    return f"""{PERSONA}

以下のキーワードに関する記事を、{config.BLOG_NAME}の読者向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

【カテゴリ固有の指示】
{category_extra}

【記事フォーマット】
{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）
{faq_instruction}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 専門用語には必ず簡単な補足説明を付ける（カッコ書きで）
- 具体的な数字やデータを含める（料金、性能、導入事例数など）
- 「Devin」というキーワードを自然に記事全体に散りばめる
- Cognition AIの公式情報に基づく正確な記述を心がける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3〜5個のQ&Aペアを含めること
- 読者にとって実用的で具体的な内容を心がけること
- Devinの最新情報（$20/月プラン、自律オーケストレーション等）を含めること"""
