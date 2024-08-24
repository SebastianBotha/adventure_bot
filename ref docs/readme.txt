<OBJECTIVE>
The objective is to create an automated story telling agent that works within Notion and built on API integration with LLM's and supported by Python code 
</OBJECTIVE>

<STRUCTURE>
1. Main coding platform on MacOS
2. Server on Raspberry PI 4 that handles automated execution of the code 
3. Coding language in Python
</STRUCTURE> 

<WAYS OF WORKING>
When starting session: 
Always start with reading the key files in this order: 
1) readme for project overview 
2) changelog for latest updates 
3) todo for current areas of focus 
4) Q&A for relevant past problems faced and solution implemented 
5) main.py for current overview of code 
6) other python files to get full overview of project
</WAYS OF WORKING>

When ending session: 
Individually update all of the key files in order: 
1) readme - update code structure to latest 
2) changelog - to summarise what was done in the session 
3) todo - any open or closed tasks status 
4) Q&A - update if any specifc big challanges were solved that should be noted 
5) requirements - if any new dependencies should be noted 

<CODE STRUCTURE>
ADVENTURE_BOT/
│
├── ref docs/
│   ├── changelog.txt
│   ├── todo.txt
│   ├── Q&A.txt
│   ├── notion-database-structure.md
│   └── readme.txt
│ 
├── src/
│   ├── notion_api/
│   │   ├── __init__.py
│   │   ├── story_db.py
│   │   ├── characters_db.py
│   │   ├── world_db.py
│   │   ├── writers_db.py
│   │   └── outline_db.py
│   ├── ai_agents/
│   │   ├── __init__.py
│   │   ├── creative_writer.py
│   │   ├── expander.py
│   │   ├── creative_critique.py
│   │   ├── audience_optimizer.py
│   │   ├── style_tone_adjuster.py
│   │   └── final_editor.py
│   ├── utils/
│   │   ├── config_loader.py
│   │   └── logger.py
│   ├── notion_api.py
│   ├── openai_api.py
│   └── main.py
│
├── tests/
│   ├── test_notion_api.py
│   └── test_openai_api.py
│
├── config.yml
├── logs/
│
├── requirements.txt
├── .gitignore
├── .env
└── environment.yml

</CODE STRUCTURE>

<SETUP INSTRUCTIONS>
To set up the development environment, follow these steps:
**Create the Conda Environment**: Navigate to the project directory and create the Conda environment using the `environment.yml` file:
   ```sh
   cd /path/to/ADVENTURE_BOT
   conda env create -f environment.yml