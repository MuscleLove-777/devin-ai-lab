"""Devin AIエージェント研究所 - アフィリエイトリンク管理ラッパー

blog_engineのAffiliateManagerを利用する。
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.affiliate import AffiliateManager

__all__ = ["AffiliateManager"]
