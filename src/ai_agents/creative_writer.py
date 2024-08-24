from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_chapter_outline(previous_chapter):
    """
    Generate a basic outline for the next chapter based on the previous chapter.
    """
    prompt = f"""
    Based on the following previous chapter, generate a brief outline for the next chapter:

    Previous chapter:
    Title: {previous_chapter['title']}
    Content: {previous_chapter['content'][:500]}...

    Provide a 3-5 point outline for the next chapter, considering:
    1. Continuation of the story
    2. Character development
    3. Potential new plot elements

    Outline:
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating chapter outline: {str(e)}")
        return None

# If you want to test this file directly
if __name__ == "__main__":
    test_chapter = {
        "title": "The Journey Begins",
        "content": "As the sun rose over the misty mountains, our hero set out on their perilous journey..."
    }
    outline = generate_chapter_outline(test_chapter)
    if outline:
        print("Generated outline:")
        print(outline)
    else:
        print("Failed to generate outline.")