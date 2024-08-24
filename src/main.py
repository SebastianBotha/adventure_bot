from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from notion_api import update_steps_logger
from notion_apis.story_db import get_latest_chapter

def main():
    # Update Steps Logger in Notion
    update_steps_logger()

    # Get the latest chapter from the Story database
    latest_chapter = get_latest_chapter()
    if latest_chapter:
        print(f"Latest chapter: {latest_chapter['chapter_number']} - {latest_chapter['title']}")
        print(f"Content preview: {latest_chapter['content'][:100]}...")
    else:
        print("No chapters found or an error occurred.")

if __name__ == "__main__":
    main()