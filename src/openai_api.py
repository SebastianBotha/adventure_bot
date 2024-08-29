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

