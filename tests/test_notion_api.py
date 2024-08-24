import pytest
from notion_client import Client
from dotenv import load_dotenv
import os
import yaml

##===============================================
## TEST IF CAN ACCESS ALL NOTION DATABASES 
##===============================================

# Load environment variables
load_dotenv()

# Load config
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))

# Get all database IDs from config
DATABASE_IDS = {
    key: value for key, value in config['notion'].items() if key.endswith('_database_id')
}

@pytest.mark.parametrize("db_name, db_id", DATABASE_IDS.items())
def test_database_connection(db_name, db_id):
    """Test if each database can be accessed."""
    try:
        result = notion.databases.query(database_id=db_id)
        print(f"Successfully accessed the {db_name}")
    except Exception as e:
        pytest.fail(f"Failed to access {db_name}: {str(e)}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])