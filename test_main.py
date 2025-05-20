import unittest
from main import AICodeGenerator

class TestAICodeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AICodeGenerator()

    def test_generate_code_calculator(self):
        user_input = 'Create a simple calculator'
        generated_code = self.generator.generate_code(user_input)
        self.assertIn('def add', generated_code)
        self.assertIn('def subtract', generated_code)
        self.assertIn('def multiply', generated_code)
        self.assertIn('def divide', generated_code)

    def test_generate_code_data_visualization(self):
        user_input = 'Generate a data visualization'
        generated_code = self.generator.generate_code(user_input)
        self.assertIn('import matplotlib.pyplot as plt', generated_code)
        self.assertIn('import numpy as np', generated_code)

    def test_generate_code_web_scraper(self):
        user_input = 'Build a web scraper'
        generated_code = self.generator.generate_code(user_input)
        self.assertIn('import requests', generated_code)
        self.assertIn('from bs4 import BeautifulSoup', generated_code)

    def test_generate_code_invalid_input(self):
        user_input = 'Invalid request'
        generated_code = self.generator.generate_code(user_input)
        self.assertEqual(generated_code, 'No specific code generated for this request. Please try another request.')

if __name__ == '__main__':
    unittest.main() 