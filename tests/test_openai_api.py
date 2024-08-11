import sys
import os

# Adjust the Python path to include the src directory
# This allows us to import modules from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from openai_api import send_prompt

class TestOpenAIApi(unittest.TestCase):
    """
    Unit tests for the OpenAI API integration.
    """

    def test_send_prompt(self):
        """
        Test sending a simple prompt to the OpenAI API.
        This test checks if the response is a non-empty string.
        """
        prompt = "Once upon a time"
        response = send_prompt(prompt)
        
        # Check if the response is a string
        self.assertIsInstance(response, str)
        
        # Check if the response is non-empty
        self.assertGreater(len(response), 0)
    
    def test_send_prompt_with_specific_model(self):
        """
        Test sending a prompt to the OpenAI API with a specific model.
        This test checks if the response is a non-empty string.
        """
        prompt = "Tell me a joke"
        response = send_prompt(prompt, model="text-curie-001")
        
        # Check if the response is a string
        self.assertIsInstance(response, str)
        
        # Check if the response is non-empty
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
