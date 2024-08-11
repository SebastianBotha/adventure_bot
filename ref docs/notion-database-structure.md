# Notion Database Structure for Adventure Bot

## 1. Story Database
Purpose: Store each chapter/entry of the ongoing story.

Properties:
- Title (Title): Chapter title
- Content (Rich Text): The full text of the chapter
- Date Created (Date): Automatically set
- Last Edited (Last Edited Time): Automatically updated
- Status (Select): Draft, In Review, Final
- Chapter Number (Number): Sequential chapter number
- Word Count (Number): Total words in the chapter
- Main Characters (Multi-select): Links to characters featured in this chapter
- Location (Select): Main setting of the chapter
- Story Arc (Select): Which major story arc this chapter belongs to

## 2. Characters Database
Purpose: Keep track of all characters in the story.

Properties:
- Name (Title): Character's full name
- Description (Rich Text): Brief character description
- Role (Select): Protagonist, Antagonist, Supporting, etc.
- Status (Select): Active, Inactive, Deceased
- First Appearance (Relation): Link to their first chapter appearance
- Traits (Multi-select): Personality traits
- Skills (Multi-select): Special abilities or skills
- Relationships (Relation): Links to other characters
- Background (Rich Text): Detailed character history
- Development Arc (Rich Text): Character's growth throughout the story

## 3. World-building Database
Purpose: Store details about the fantasy world.

Properties:
- Name (Title): Location or concept name
- Type (Select): City, Country, Magic System, Religion, etc.
- Description (Rich Text): Detailed information
- Importance (Select): Major, Minor, Background
- Related Characters (Relation): Links to associated characters
- Related Events (Relation): Links to relevant story events
- History (Rich Text): Background information
- Cultural Notes (Rich Text): Specific cultural details
- Map/Image (Files & Media): Visual representations

## 4. AI Writers Database
Purpose: Store prompts and instructions for different AI roles.

Properties:
- Name (Title): Name of the AI role (e.g., "Creative Writer", "Expander")
- Role Description (Rich Text): Detailed description of the AI's purpose
- Base Prompt (Rich Text): The foundational prompt for this AI role
- Parameters (Rich Text): Any specific parameters or instructions
- Example Output (Rich Text): Sample of expected output
- Last Updated (Date): When the prompt was last modified
- Version (Number): Version number of the prompt
- Notes (Rich Text): Any additional notes or considerations

## 5. Story Outline Database
Purpose: Track the overall plot and story arcs.

Properties:
- Event Title (Title): Name of the plot point or event
- Description (Rich Text): Detailed description of the event
- Order (Number): Sequence in the overall story
- Status (Select): Planned, In Progress, Completed
- Related Chapters (Relation): Links to relevant chapters
- Involved Characters (Relation): Links to characters involved
- Story Arc (Select): Which major story arc this event belongs to
- Importance (Select): Major, Minor, Background
- Notes (Rich Text): Additional planning notes

## 6. Theme and Motifs Database
Purpose: Track recurring themes and motifs in the story.

Properties:
- Name (Title): Name of the theme or motif
- Type (Select): Theme, Motif, Symbol
- Description (Rich Text): Explanation of the theme/motif
- Occurrences (Relation): Links to chapters where it appears
- Related Characters (Relation): Characters associated with this theme/motif
- Notes (Rich Text): Additional analysis or planning notes

## 7. Reader Feedback Database
Purpose: Store and analyze reader feedback for story improvement.

Properties:
- Feedback Type (Select): Praise, Criticism, Suggestion
- Content (Rich Text): The actual feedback
- Source (Select): Website, Email, Social Media, etc.
- Related Chapter (Relation): Link to the relevant chapter
- Date Received (Date): When the feedback was given
- Addressed (Checkbox): Whether the feedback has been addressed
- Action Taken (Rich Text): Description of how the feedback was handled
- Impact (Select): None, Minor, Major (how it affected the story)

## 8. User Feedback Database
Purpose: Collect and organize user/community feedback to influence story direction and improvements.
Properties:
Feedback ID (Title): Unique identifier for each piece of feedback
Content (Rich Text): The actual feedback or suggestion
Type (Select): Plot Suggestion, Character Development, World Building, Writing Style, General Comment
Related Chapter (Relation): Link to the relevant chapter(s)
Related Character (Relation): Link to the relevant character(s), if applicable
Status (Select): New, Under Review, Accepted, Implemented, Rejected
Impact Level (Select): Low, Medium, High
User/Community Member (Text): Name or identifier of the feedback provider
Date Received (Date): When the feedback was submitted
Date Processed (Date): When the feedback was reviewed/acted upon
AI Writer Notes (Rich Text): Notes from AI agents about how to incorporate the feedback
Implementation Details (Rich Text): Description of how the feedback was implemented in the story