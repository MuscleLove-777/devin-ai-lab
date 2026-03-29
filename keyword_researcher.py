"""Devin AIエージェント研究所 - キーワードリサーチラッパー

blog_engineのKeywordResearcherを利用する。
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.keyword_researcher import KeywordResearcher

__all__ = ["KeywordResearcher"]
