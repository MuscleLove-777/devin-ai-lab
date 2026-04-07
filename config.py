"""Devin AIエージェント研究所 - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Devin AIエージェント研究所"
BLOG_DESCRIPTION = "AIソフトウェアエンジニアDevinの使い方・最新情報・料金・活用術を毎日更新。自律型AIエージェント開発の最前線を初心者にもわかりやすく解説。"
BLOG_URL = "https://musclelove-777.github.io/devin-ai-lab"
BLOG_TAGLINE = "AI開発者エージェントDevinの全てがわかる日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/devin-ai-lab"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Devin 使い方",
    "Devin 料金・プラン",
    "Devin vs 人間エンジニア",
    "Devin 最新ニュース",
    "AIエージェント開発",
    "Devin 活用事例",
    "Devin API・統合",
    "AIエージェント比較",
]

THEME = {
    "primary": "#7c3aed",
    "accent": "#c084fc",
    "gradient_start": "#7c3aed",
    "gradient_end": "#4f46e5",
    "dark_bg": "#0a0a1a",
    "dark_surface": "#1a1033",
    "light_bg": "#faf5ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [12]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Devin": [
        {"service": "Devin", "url": "https://devin.ai", "description": "月額$20からAI開発者エージェントが使える"},
    ],
    "AI開発ツール": [
        {"service": "GitHub Copilot", "url": "https://github.com/features/copilot", "description": "GitHub Copilot（比較用）"},
        {"service": "Cursor", "url": "https://cursor.sh", "description": "Cursor（比較用）"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI開発講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAIエージェント関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8087

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
