# Adventure Bot Project Overview

## Project Goal
The goal of the Adventure Bot project is to create an automated system that generates a cohesive, high-quality fantasy story in Notion. The system should:

1. Generate a new chapter daily
2. Maintain consistency with previously generated content
3. Utilize multiple AI agents for different aspects of the writing process
4. Store and manage all story-related data in Notion databases
5. Produce engaging, readable content of at least 10 minutes reading time per chapter

## File Structure and Components

### ref docs/
Contains reference documents for the project.

#### changelog.txt
- Input: Project updates
- Process: Manual entry of significant changes
- Output: Chronological list of project changes

#### todo.txt
- Input: Pending tasks and features
- Process: Manual entry and update of tasks
- Output: Current list of todo items

#### Q&A.txt
- Input: Questions and their answers about the project
- Process: Manual entry of Q&A
- Output: Searchable Q&A document

#### notion-database-structure.md
- Input: Notion database designs
- Process: Manual entry and update of database structures
- Output: Detailed description of Notion databases

#### readme.txt
- Input: Project overview and setup instructions
- Process: Manual creation and updates
- Output: Quick start guide for the project

#### project_overview.md (this file)
- Input: Comprehensive project details
- Process: Manual creation and updates
- Output: Detailed project structure and component descriptions

### src/

#### notion_api/

##### __init__.py
- Input: N/A
- Process: Import and initialize Notion API modules
- Output: Exposed Notion API functions

##### story_db.py
- Input: Story data, Notion credentials
- Process: CRUD operations for Story database
- Output: Updated Story database in Notion

##### characters_db.py
- Input: Character data, Notion credentials
- Process: CRUD operations for Characters database
- Output: Updated Characters database in Notion

##### world_db.py
- Input: World-building data, Notion credentials
- Process: CRUD operations for World-building database
- Output: Updated World-building database in Notion

##### writers_db.py
- Input: AI writer prompts, Notion credentials
- Process: CRUD operations for AI Writers database
- Output: Updated AI Writers database in Notion

##### outline_db.py
- Input: Story outline data, Notion credentials
- Process: CRUD operations for Story Outline database
- Output: Updated Story Outline database in Notion

#### feedback_db.py
Input: User feedback data, Notion credentials
Process: CRUD operations for User Feedback database
Output: Updated User Feedback database in Notion

#### ai_agents/

##### __init__.py
- Input: N/A
- Process: Import and initialize AI agent modules
- Output: Exposed AI agent functions

##### creative_writer.py
- Input: Story context, AI prompt
- Process: Generate story outline
- Output: Initial story outline

##### expander.py
- Input: Story outline, AI prompt
- Process: Expand outline into full draft
- Output: Expanded story draft

##### creative_critique.py
- Input: Story draft, AI prompt
- Process: Analyze and critique the draft
- Output: Feedback and suggestions

##### audience_optimizer.py
- Input: Story draft, target audience info, AI prompt
- Process: Optimize content for target audience
- Output: Audience-optimized draft

##### style_tone_adjuster.py
- Input: Optimized draft, style/tone guidelines, AI prompt
- Process: Adjust style and tone of the draft
- Output: Style and tone adjusted draft

##### final_editor.py
- Input: Adjusted draft, editing guidelines, AI prompt
- Process: Final editing and polishing
- Output: Final version of the chapter

#### feedback_analyzer.py
Input: User feedback, story context, AI prompt
Process: Analyze feedback and generate suggestions for story adjustments
Output: Actionable suggestions based on user feedback

#### utils/

##### config_loader.py
- Input: config.yml file
- Process: Load and parse configuration
- Output: Configuration object

##### logger.py
- Input: Logging configuration, log messages
- Process: Format and write log messages
- Output: Log files

#### notion_api.py
- Input: Notion credentials, database IDs
- Process: Initialize Notion client, provide high-level Notion operations
- Output: Notion API wrapper functions

#### claude_api.py
- Input: Claude API credentials, prompts
- Process: Interact with Claude API
- Output: Claude API responses

#### openai_api.py
- Input: OpenAI API credentials, prompts
- Process: Interact with OpenAI API
- Output: OpenAI API responses

#### main.py
- Input: Configuration, Notion data, AI responses, User feedback
- Process: Orchestrate the entire story generation process, including feedback incorporation
- Output: Generated story chapter, updated Notion databases, processed feedback

### tests/

#### test_notion_api.py
- Input: Test data, Notion API mock
- Process: Run unit tests for Notion API functions
- Output: Test results

#### test_claude_api.py
- Input: Test data, Claude API mock
- Process: Run unit tests for Claude API functions
- Output: Test results

#### test_openai_api.py
- Input: Test data, OpenAI API mock
- Process: Run unit tests for OpenAI API functions
- Output: Test results

### config.yml
- Input: Manual configuration entries
- Process: Store project configuration
- Output: Configuration data for the project

### logs/
- Input: Log messages from logger.py
- Process: Store log files
- Output: Chronological log files

### requirements.txt
- Input: Project dependencies
- Process: List required Python packages
- Output: Installable list of dependencies

### .gitignore
- Input: File patterns to ignore
- Process: Specify files for Git to ignore
- Output: Git-ignored files and directories

### .env
- Input: Environment variables
- Process: Store sensitive configuration
- Output: Environment variables for the project

### environment.yml
- Input: Conda environment specification
- Process: Define Conda environment
- Output: Reproducible Conda environment

## Workflow

1. main.py initiates the story generation process
2. Notion databases are queried for context (story_db.py, characters_db.py, world_db.py, outline_db.py, feedback_db.py)
3. feedback_analyzer.py processes recent user feedback to generate suggestions
4. AI agents are called sequentially, now incorporating feedback suggestions: (feedback_analyzer.py → creative_writer.py → expander.py → creative_critique.py → audience_optimizer.py → style_tone_adjuster.py → final_editor.py)
5. The final output is stored back in Notion (story_db.py)
6. Any new characters or world elements are updated in their respective databases
7. Feedback status is updated in the feedback database (feedback_db.py)
8. The process repeats daily to generate new chapters, continuously incorporating new feedback
