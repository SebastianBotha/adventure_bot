from openai_api import send_prompt

def generate_chapter_outline(story_context, agent_details):
    full_prompt = f"{agent_details['base_prompt']}\n\nStory Context:\n{story_context}\n\nParameters:\n{agent_details['parameters']}"
    
    try:
        response = send_prompt(full_prompt, model="gpt-4", max_tokens=1000)
        return response
    except Exception as e:
        raise Exception(f"Error generating chapter outline: {str(e)}")