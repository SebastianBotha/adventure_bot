import pytest
from notion_client import Client
from dotenv import load_dotenv
import os
import yaml
##===============================================
## TEST IF ALL DATABASES HAVE RIGHT STRUCTURE
##===============================================

# Load environment variables
load_dotenv()

# Load config
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))

# Expected structures for all databases
EXPECTED_STRUCTURES = {
    "story_database_id": {
        "Title": "title",
        "Content": "rich_text",
        "Date Created": "created_time",
        "Last Edited": "last_edited_time",
        "Chapter Number": "number",
        "Word Count": "number",
        "Main Characters": "multi_select",
        "Location": "select",
        "Story Arc": "select",
        "Quality Rating": "number",
        "Status": "select"
    },
    "characters_database_id": {
        "Name": "title",
        "Description": "rich_text",
        "Role": "select",
        "Status": "select",
        "Traits": "multi_select",
        "Skills": "multi_select",
        "Relationships": "rich_text",
        "Background": "rich_text",
        "Development Arc": "rich_text"
    },
    "world_database_id": {
        "Name": "title",
        "Type": "select",
        "Description": "rich_text",
        "Importance": "select",
        "Related Characters": "relation",
        "Related Events": "relation",
        "History": "rich_text",
        "Cultural Notes": "rich_text"
    },
    "story_arcs_database_id": {
        "Arc Name": "title",
        "Description": "rich_text",
        "Related Chapter": "relation",
        "Status": "select",
        "Key Events": "multi_select",
        "Related Characters": "relation",
        "Importance": "select"
    },
    "story_rules_database_id": {
        "Rule Name": "title",
        "Description": "rich_text",
        "Type": "select",
        "Priority": "number",
        "Examples": "rich_text",
        "Exceptions": "rich_text"
    },
    "feedback_database_id": {
        "Feedback ID": "title",
        "Related Chapter": "relation",
        "Feedback Summary": "rich_text",
        "Impact Areas": "multi_select",
        "Status": "select",
        "AI Analysis": "rich_text",
        "Implementation Notes": "rich_text"
    },
    "ai_writers_database_id": {
        "Name": "title",
        "Role Description": "rich_text",
        "Base Prompt": "rich_text",
        "Parameters": "rich_text",
        "Example Output": "rich_text",
        "Last Updated": "last_edited_time",
        "Version": "number",
        "Notes": "rich_text"
    },
    "steps_logger_database_id": {
        "Step Number": "title",
        "Foot": "select"
    }
}

@pytest.mark.parametrize("db_key, expected_structure", EXPECTED_STRUCTURES.items())
def test_database_structure(db_key, expected_structure):
    """Test if each database has the expected structure."""
    db_id = config['notion'][db_key]
    try:
        database = notion.databases.retrieve(database_id=db_id)
        properties = database["properties"]
        
        for field, expected_type in expected_structure.items():
            assert field in properties, f"Field '{field}' not found in {db_key}"
            assert properties[field]["type"] == expected_type, f"Field '{field}' in {db_key} has type '{properties[field]['type']}', expected '{expected_type}'"
        
        print(f"All expected fields are present with correct types in {db_key}")
    except Exception as e:
        pytest.fail(f"Failed to verify structure of {db_key}: {str(e)}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])