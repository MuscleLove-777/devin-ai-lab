"""Devin AIエージェント研究所 - トピック収集モジュール

topics.jsonからトピックを読み込み、未使用のトピックを選定する。
Gemini APIを使ってトレンドに基づく新規トピック提案も行う。
"""

import json
import logging
import random
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class TopicCollector:
    """トピックの収集・管理を行うクラス"""

    def __init__(self, config, prompts=None):
        self.config = config
        self.prompts = prompts
        self.topics_file = Path(config.BASE_DIR) / "topics.json"
        self.used_topics_file = Path(config.BASE_DIR) / "output" / "topics" / "used_topics.json"
        self.used_topics_file.parent.mkdir(parents=True, exist_ok=True)
        logger.info("TopicCollector を初期化しました")

    def load_topics(self) -> dict:
        """topics.jsonからトピック一覧を読み込む"""
        if not self.topics_file.exists():
            logger.warning("topics.json が見つかりません: %s", self.topics_file)
            return {"categories": {}}

        with open(self.topics_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_used_topics(self) -> list:
        """使用済みトピックのリストを読み込む"""
        if not self.used_topics_file.exists():
            return []
        with open(self.used_topics_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_used_topic(self, keyword: str, category: str):
        """使用済みトピックを記録する"""
        used = self.load_used_topics()
        used.append({
            "keyword": keyword,
            "category": category,
            "used_at": datetime.now().isoformat(),
        })
        with open(self.used_topics_file, "w", encoding="utf-8") as f:
            json.dump(used, f, ensure_ascii=False, indent=2)
        logger.info("使用済みトピックを記録: %s", keyword)

    def get_next_topic(self) -> dict | None:
        """未使用の優先度の高いトピックを1つ選定する"""
        topics_data = self.load_topics()
        used = self.load_used_topics()
        used_keywords = {t["keyword"] for t in used}

        # 優先度順にソートして未使用を選択
        candidates = []
        for category, topics in topics_data.get("categories", {}).items():
            for topic in topics:
                if topic["keyword"] not in used_keywords:
                    candidates.append({
                        "keyword": topic["keyword"],
                        "category": category,
                        "title": topic.get("title", ""),
                        "description": topic.get("description", ""),
                        "priority": topic.get("priority", "medium"),
                    })

        if not candidates:
            logger.info("未使用のトピックがありません。AIで新規トピックを生成します。")
            return None

        # 優先度でソート（high > medium > low）
        priority_order = {"high": 0, "medium": 1, "low": 2}
        candidates.sort(key=lambda x: priority_order.get(x["priority"], 1))

        # 同じ優先度内でランダム選択
        top_priority = candidates[0]["priority"]
        top_candidates = [c for c in candidates if c["priority"] == top_priority]
        selected = random.choice(top_candidates)

        logger.info(
            "トピック選定: カテゴリ=%s, キーワード=%s, 優先度=%s",
            selected["category"], selected["keyword"], selected["priority"],
        )
        return selected

    def get_topics_by_category(self, category: str) -> list:
        """指定カテゴリのトピック一覧を取得する"""
        topics_data = self.load_topics()
        return topics_data.get("categories", {}).get(category, [])

    def get_unused_count(self) -> int:
        """未使用トピック数を返す"""
        topics_data = self.load_topics()
        used = self.load_used_topics()
        used_keywords = {t["keyword"] for t in used}

        count = 0
        for topics in topics_data.get("categories", {}).values():
            for topic in topics:
                if topic["keyword"] not in used_keywords:
                    count += 1
        return count

    def add_topic(self, category: str, title: str, keyword: str,
                  description: str = "", priority: str = "medium"):
        """新しいトピックをtopics.jsonに追加する"""
        topics_data = self.load_topics()

        if category not in topics_data.get("categories", {}):
            topics_data.setdefault("categories", {})[category] = []

        topics_data["categories"][category].append({
            "title": title,
            "keyword": keyword,
            "description": description,
            "priority": priority,
        })

        topics_data.setdefault("metadata", {})["last_updated"] = datetime.now().strftime("%Y-%m-%d")

        with open(self.topics_file, "w", encoding="utf-8") as f:
            json.dump(topics_data, f, ensure_ascii=False, indent=2)

        logger.info("トピックを追加: カテゴリ=%s, キーワード=%s", category, keyword)
