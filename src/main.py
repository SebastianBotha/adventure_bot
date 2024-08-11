import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_haiku(topic):
    """
    Generates a haiku about the given topic using OpenAI's GPT-4 model.

    :param topic: The topic for the haiku
    :return: Haiku as a JSON response
    """
    prompt = f"Write a haiku about {topic}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        haiku = response.choices[0].message['content'].strip()
        return json.dumps({"haiku": haiku}, indent=4)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

def main():
    topic = "tennis"
    haiku_json = get_haiku(topic)
    print(haiku_json)

if __name__ == "__main__":
    main()
