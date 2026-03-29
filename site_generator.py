"""Devin AIエージェント研究所 - サイト生成ラッパー

blog_engineのSiteGeneratorを利用し、Devin特化のSEO強化（JSON-LD、OGP、robots.txt）を追加する。
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.site_generator import SiteGenerator as BaseSiteGenerator


class SiteGenerator(BaseSiteGenerator):
    """Devin特化のサイト生成クラス"""

    def __init__(self, config):
        super().__init__(config)

    def build_site(self):
        """サイトビルドを実行し、追加SEOファイルを生成する"""
        super().build_site()
        self._generate_robots_txt()
        self._generate_og_meta()
        print("  robots.txt 生成完了")
        print("  OGP/構造化データ準備完了")

    def _generate_robots_txt(self):
        """robots.txtを生成する"""
        blog_url = self.config.BLOG_URL
        content = (
            "User-agent: *\n"
            "Allow: /\n"
            f"Sitemap: {blog_url}/sitemap.xml\n"
            f"\n"
            "User-agent: Googlebot\n"
            "Allow: /\n"
            f"\n"
            "User-agent: Bingbot\n"
            "Allow: /\n"
        )
        (self.output_dir / "robots.txt").write_text(content, encoding="utf-8")

    def _generate_og_meta(self):
        """OGPメタタグ用のJSONファイルを生成する（テンプレートで利用）"""
        og_data = {
            "site_name": self.config.BLOG_NAME,
            "description": self.config.BLOG_DESCRIPTION,
            "url": self.config.BLOG_URL,
            "type": "website",
            "locale": "ja_JP",
        }
        og_path = self.output_dir / "og_meta.json"
        with open(og_path, "w", encoding="utf-8") as f:
            json.dump(og_data, f, ensure_ascii=False, indent=2)

    def _get_common_context(self) -> dict:
        """共通コンテキストにOGP・構造化データ情報を追加する"""
        context = super()._get_common_context()
        context.update({
            "blog_tagline": getattr(self.config, "BLOG_TAGLINE", ""),
            "canonical_url": self.config.BLOG_URL,
            "og_type": "website",
            "og_locale": "ja_JP",
        })
        return context


__all__ = ["SiteGenerator"]
