import unittest
from unittest.mock import patch, MagicMock
from main import run_creative_writer

class TestCreativeWriter(unittest.TestCase):

    @patch('main.get_creative_writer_details')
    @patch('main.get_latest_chapter')
    @patch('main.generate_chapter_outline')
    def test_run_creative_writer(self, mock_generate_outline, mock_get_chapter, mock_get_writer):
        # Mock the return values
        mock_get_writer.return_value = {
            "base_prompt": "Test prompt",
            "parameters": "Test parameters",
            "version": 1
        }
        mock_get_chapter.return_value = {
            "chapter_number": 1,
            "title": "Test Chapter",
            "content": "Test content" * 100
        }
        mock_generate_outline.return_value = "Test outline"

        # Run the function
        run_creative_writer()

        # Assert that all the mocked functions were called
        mock_get_writer.assert_called_once()
        mock_get_chapter.assert_called_once()
        mock_generate_outline.assert_called_once()

        # You can add more specific assertions here if needed

if __name__ == '__main__':
    unittest.main()