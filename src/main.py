from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from notion_api import update_steps_logger
from notion_apis.story_db import get_latest_chapter
from ai_agents.creative_writer import generate_chapter_outline

def main():
    # Update Steps Logger in Notion
    update_steps_logger()

    # Get the latest chapter from the Story database
    latest_chapter = get_latest_chapter()
    if latest_chapter:
        print(f"Latest chapter: {latest_chapter['chapter_number']} - {latest_chapter['title']}")
        print(f"Content preview: {latest_chapter['content'][:100]}...")

        # Generate outline for the next chapter
        new_outline = generate_chapter_outline(latest_chapter)
        if new_outline:
            print("\nGenerated outline for the next chapter:")
            print(new_outline)
        else:
            print("Failed to generate new chapter outline.")
    else:
        print("No chapters found or an error occurred.")

if __name__ == "__main__":
    main()