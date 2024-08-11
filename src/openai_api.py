import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_prompt(prompt, model="gpt-4-mini", max_tokens=50):
    """
    Sends a prompt to the OpenAI API and returns the response.

    :param prompt: The prompt to send to the API
    :param model: The model to use (default is "gpt-4-mini")
    :param max_tokens: The maximum number of tokens to generate (default is 50)
    :return: The response from the API
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

"""Example for Haiku

from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_haiku(topic):
    
    Generates a haiku about the given topic using OpenAI's GPT-4 model.

    :param topic: The topic for the haiku
    :return: Haiku as a JSON response
    
    prompt = f"Write a haiku about {topic}."
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        haiku = response.choices[0].message.content.strip()
        return json.dumps({"haiku": haiku}, indent=4)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

def main():
    topic = "tennis"
    haiku_json = get_haiku(topic)
    print(haiku_json)

if __name__ == "__main__":
    main()

"""