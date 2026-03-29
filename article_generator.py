"""Devin AIエージェント研究所 - 記事生成ラッパー

blog_engineのArticleGeneratorを利用し、Devin特化の記事を生成する。
"""

import sys
import os

# blog_engineへのパスを追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.article_generator import ArticleGenerator

__all__ = ["ArticleGenerator"]
