import logging
from notion_apis.writers_db import get_creative_writer_details
from ai_agents.creative_writer import generate_chapter_outline
from notion_apis.story_db import get_latest_chapter
from utils.config_loader import config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def run_creative_writer():
    try:
        logging.info("Fetching Creative Writer details")
        logging.debug(f"Using AI Writers Database ID: {config['notion']['ai_writers_database_id']}")
        agent_details = get_creative_writer_details()
        logging.debug(f"Agent details: {agent_details}")
        
        logging.info("Fetching latest chapter for context")
        latest_chapter = get_latest_chapter()
        story_context = f"Latest chapter: {latest_chapter['chapter_number']} - {latest_chapter['title']}\n{latest_chapter['content'][:500]}..."
        logging.debug(f"Story context: {story_context[:100]}...")
        
        logging.info("Generating new chapter outline")
        outline = generate_chapter_outline(story_context, agent_details)
        
        logging.info("Chapter outline generated successfully")
        print("Generated Chapter Outline:")
        print(outline)
        
        # TODO: Save outline to Notion
        logging.info("Outline saved to Notion (Not implemented yet)")
        
    except ValueError as ve:
        logging.error(f"Configuration error: {str(ve)}")
    except Exception as e:
        logging.error(f"Error in running Creative Writer: {str(e)}", exc_info=True)

if __name__ == "__main__":
    run_creative_writer()