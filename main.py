#!/usr/bin/env python3
"""Devin AIエージェント研究所 - CLIエントリポイント

blog_engineのmain.pyに処理を委譲する。

使い方:
    python main.py generate --keyword "Devin 使い方" --category "Devin 使い方"
    python main.py build
    python main.py deploy
    python main.py schedule
    python main.py dashboard
"""
import sys
import os
from llm import get_llm_client

# blog_engineへのパスを追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# 自身のconfigとpromptsを--configとして自動設定
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "config.py")
    prompts_path = os.path.join(os.path.dirname(__file__), "prompts.py")

    # --configが指定されていなければ自動追加
    if "--config" not in sys.argv:
        sys.argv.insert(1, "--config")
        sys.argv.insert(2, config_path)

    from blog_engine.main import main
    main()
