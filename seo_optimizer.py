"""Devin AIエージェント研究所 - SEO最適化ラッパー

blog_engineのSEOOptimizerを利用し、JSON-LD構造化データ生成を追加する。
"""

import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from blog_engine.seo_optimizer import SEOOptimizer as BaseSEOOptimizer


class SEOOptimizer(BaseSEOOptimizer):
    """Devin特化のSEO最適化クラス"""

    def __init__(self, config):
        super().__init__(config)

    def generate_faq_schema(self, faq_list: list) -> str:
        """FAQPage JSON-LDを生成する"""
        if not faq_list:
            return ""

        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [],
        }

        for item in faq_list:
            schema["mainEntity"].append({
                "@type": "Question",
                "name": item.get("question", ""),
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item.get("answer", ""),
                },
            })

        return json.dumps(schema, ensure_ascii=False, indent=2)

    def generate_article_schema(self, article: dict, config) -> str:
        """Article JSON-LDを生成する"""
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": article.get("title", ""),
            "description": article.get("meta_description", ""),
            "author": {
                "@type": "Organization",
                "name": config.BLOG_NAME,
            },
            "publisher": {
                "@type": "Organization",
                "name": config.BLOG_NAME,
            },
            "datePublished": article.get("generated_at", "")[:10],
            "dateModified": article.get("generated_at", "")[:10],
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": f"{config.BLOG_URL}/articles/{article.get('slug', '')}.html",
            },
        }

        return json.dumps(schema, ensure_ascii=False, indent=2)

    def generate_breadcrumb_schema(self, article: dict, config) -> str:
        """BreadcrumbList JSON-LDを生成する"""
        schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "ホーム",
                    "item": config.BLOG_URL,
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": article.get("category", "未分類"),
                    "item": f"{config.BLOG_URL}/category/{article.get('category', '')}",
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": article.get("title", ""),
                    "item": f"{config.BLOG_URL}/articles/{article.get('slug', '')}.html",
                },
            ],
        }

        return json.dumps(schema, ensure_ascii=False, indent=2)


__all__ = ["SEOOptimizer"]
