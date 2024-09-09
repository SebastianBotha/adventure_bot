from notion_client import Client
from dotenv import load_dotenv
import os
from utils.config_loader import config

load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))

AI_WRITERS_DATABASE_ID = config['notion']['ai_writers_database_id']

def get_creative_writer_details():
    if not AI_WRITERS_DATABASE_ID:
        raise ValueError("AI_WRITERS_DATABASE_ID is not set in the config file")
    
    query = notion.databases.query(
        database_id=AI_WRITERS_DATABASE_ID,
        filter={
            "property": "Name",
            "title": {
                "equals": "Creative Writer"
            }
        }
    )
    
    if not query["results"]:
        raise Exception("Creative Writer not found in the database")
    
    writer = query["results"][0]
    return {
        "base_prompt": writer["properties"]["Base Prompt"]["rich_text"][0]["plain_text"],
        "parameters": writer["properties"]["Parameters"]["rich_text"][0]["plain_text"],
        "version": writer["properties"]["Version"]["number"]
    }