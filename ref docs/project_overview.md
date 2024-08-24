# Adventure Bot Project Overview (Updated)

## Project Goal
The goal of the Adventure Bot project is to create an automated system that generates a cohesive, high-quality fantasy story using Notion for data management and AI agents for content creation. The system will:

1. Generate a new chapter daily
2. Maintain consistency with previously generated content
3. Utilize multiple AI agents for different aspects of the writing process
4. Store and manage all story-related data in Notion databases
5. Produce engaging, readable content of at least 10 minutes reading time per chapter
6. Continuously improve based on feedback

## File Structure and Components

### src/

#### notion_api/
- __init__.py
- story_db.py: CRUD operations for Story database
- characters_db.py: CRUD operations for Characters database
- world_db.py: CRUD operations for World-building database
- storyarcs_db.py: CRUD operations for StoryArcs database
- storyrules_db.py: CRUD operations for StoryRules database
- feedback_db.py: CRUD operations for Feedback database

#### ai_agents/
- __init__.py
- creative_writer.py: Generates story outlines
- expander.py: Expands outlines into full chapters
- creative_critique.py: Analyzes and critiques the draft
- audience_optimizer.py: Optimizes content for target audience
- style_tone_adjuster.py: Adjusts style and tone of the draft
- final_editor.py: Performs final editing and polishing

#### utils/
- config_loader.py: Loads and parses configuration
- logger.py: Handles logging

#### notion_api.py: Initializes Notion client, provides high-level Notion operations
#### openai_api.py: Handles interactions with OpenAI API
#### quality_check.py: Implements quality check criteria
#### main.py: Orchestrates the entire story generation process

### tests/
(Test files for each module)

### config.yml: Project configuration
### requirements.txt: Project dependencies

## Workflow

1. **Initialization**:
   - Load configuration
   - Initialize Notion API
   - Initialize OpenAI API

2. **Database Queries**:
   - Query all relevant Notion databases (Story, Characters, World, StoryArcs, StoryRules, Feedback)
   - Compile context from queried data

3. **Feedback Analysis and AI Prompt Updates**:
   - Analyze user feedback from Feedback database
   - Update prompts for all AI agents based on feedback

4. **Content Generation**:
   - Generate story outline (Creative Writer)
   - Check alignment with current story arcs
   - Apply story rules for consistency
   - Expand outline to full chapter (Expander)
   - Perform creative critique (Creative Critique)
   - Optimize for target audience (Audience Optimizer)
   - Adjust style and tone (Style Tone Adjuster)
   - Final editing (Final Editor)

5. **Quality Check**:
   - Evaluate chapter based on criteria:
     - Coherence with story arcs
     - Adherence to story rules
     - Character consistency
     - Engagement factor
     - Writing quality
     - Length (10 min read)
   - If fails, return to outline generation
   - If passes, proceed to storage

6. **Database Updates**:
   - Store new chapter in Story database
   - Update Characters database with any new information
   - Update World database with new elements
   - Update StoryArcs database to reflect progress

7. **Process Logging**:
   - Log the entire process for tracking and debugging

8. **Cycle Completion**:
   - End daily run
   - Prepare for next day's cycle

This workflow repeats daily, continuously generating new chapters while improving based on feedback and maintaining consistency with the overall narrative.

