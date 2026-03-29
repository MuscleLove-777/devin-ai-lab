"""Devin AIエージェント研究所 - ダッシュボードラッパー

blog_engineのダッシュボードを利用する。
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.dashboard import create_app

__all__ = ["create_app"]
