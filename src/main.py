from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from notion_api import update_steps_logger

def main():
    
    # Update Steps Logger in Notion
    update_steps_logger()

if __name__ == "__main__":
    main()