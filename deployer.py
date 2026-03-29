"""Devin AIエージェント研究所 - デプロイラッパー

blog_engineのGitHubPagesDeployerを利用する。
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.deployer import GitHubPagesDeployer

__all__ = ["GitHubPagesDeployer"]
