import os
import yaml
from notion_client import Client
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Load config
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize the Notion client
notion = Client(auth=os.environ["NOTION_API_KEY"])

# Constants
STEPS_LOGGER_DATABASE_ID = config['notion']['steps_logger_database_id']

def get_last_step():
    """
    Retrieve the last step from the Steps Logger table.
    """
    try:
        results = notion.databases.query(
            database_id=STEPS_LOGGER_DATABASE_ID,
            sorts=[{"property": "Step Number", "direction": "descending"}],
            page_size=1
        ).get("results")
        
        if results:
            step = results[0]
            properties = step.get("properties", {})
            step_number = int(properties.get("Step Number", {}).get("title", [{}])[0].get("plain_text", "0"))
            foot = properties.get("Foot", {}).get("select", {}).get("name", "N/A")
            return step_number, foot
        return 0, "N/A"
    except Exception as e:
        print(f"Error querying Notion database: {str(e)}")
        return 0, "N/A"

def add_new_step(step_number, foot):
    """
    Add a new step to the Steps Logger table.
    """
    try:
        notion.pages.create(
            parent={"database_id": STEPS_LOGGER_DATABASE_ID},
            properties={
                "Step Number": {
                    "title": [{"text": {"content": str(step_number)}}]
                },
                "Foot": {
                    "select": {"name": foot}
                }
            }
        )
        print(f"Added step {step_number} with {foot} foot.")
    except Exception as e:
        print(f"Error adding new step to Notion database: {str(e)}")

def increment_step():
    """
    Increment the step and alternate the foot.
    """
    last_step, last_foot = get_last_step()
    new_step = last_step + 1
    new_foot = "Left" if last_foot == "Right" else "Right"
    add_new_step(new_step, new_foot)
    return new_step, new_foot

def update_steps_logger():
    """
    Main function to update the Steps Logger.
    """
    new_step, new_foot = increment_step()
    print(f"Updated Steps Logger: Step {new_step}, Foot: {new_foot}")

# If you want to test this file directly
if __name__ == "__main__":
    update_steps_logger()