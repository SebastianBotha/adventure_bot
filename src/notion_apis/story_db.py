import os
import yaml
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load config
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize the Notion client
notion = Client(auth=os.environ["NOTION_API_KEY"])

# Constants
STORY_DATABASE_ID = config['notion']['story_database_id']

def get_latest_chapter():
    """
    Retrieve the latest chapter from the Story database.
    """
    try:
        results = notion.databases.query(
            database_id=STORY_DATABASE_ID,
            sorts=[{"property": "Chapter Number", "direction": "descending"}],
            page_size=1
        ).get("results")
        
        if results:
            chapter = results[0]
            properties = chapter.get("properties", {})
            chapter_number = properties.get("Chapter Number", {}).get("number", 0)
            title = properties.get("Title", {}).get("title", [{}])[0].get("plain_text", "Untitled")
            content = properties.get("Content", {}).get("rich_text", [{}])[0].get("plain_text", "")
            
            return {
                "chapter_number": chapter_number,
                "title": title,
                "content": content
            }
        return None
    except Exception as e:
        print(f"Error querying Story database: {str(e)}")
        return None

# If you want to test this file directly
if __name__ == "__main__":
    latest_chapter = get_latest_chapter()
    if latest_chapter:
        print(f"Latest chapter: {latest_chapter['chapter_number']} - {latest_chapter['title']}")
        print(f"Content preview: {latest_chapter['content'][:100]}...")
    else:
        print("No chapters found or an error occurred.")