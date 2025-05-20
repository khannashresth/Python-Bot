import os
import logging
import sys
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AI Code Generator')

class AICodeGenerator:
    def __init__(self):
        logger.info('Initializing AI Code Generator...')
        # Add initialization logic here

    def generate_code(self, user_input):
        """
        Generate Python code based on user input.
        """
        logger.info(f'Generating code for input: {user_input}')
        
        # Example code generation logic
        if 'calculator' in user_input.lower():
            return '''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error! Division by zero.'
    return x / y

# Example usage
print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
print(multiply(5, 3))  # Output: 15
print(divide(5, 3))  # Output: 1.6666666666666667
'''
        elif 'data visualization' in user_input.lower():
            return '''
import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
'''
        elif 'web scraper' in user_input.lower():
            return '''
import requests
from bs4 import BeautifulSoup

# Example URL
url = 'https://example.com'

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract all paragraph texts
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)
'''
        elif 'file io' in user_input.lower():
            return '''
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
'''
        elif 'sorting algorithm' in user_input.lower():
            return '''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
'''
        elif 'flask app' in user_input.lower():
            return '''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
        else:
            return 'No specific code generated for this request. Please try another request.'

    def run(self):
        """
        Run the AI Code Generator interactively.
        """
        print('Welcome to the AI Code Generator!')
        print('Enter your code generation request (or type "exit" to quit):')
        
        while True:
            user_input = input('> ').strip()
            if user_input.lower() == 'exit':
                print('Exiting AI Code Generator. Goodbye!')
                break
            
            try:
                generated_code = self.generate_code(user_input)
                # Syntax highlighting
                highlighted_code = highlight(generated_code, PythonLexer(), TerminalFormatter())
                print(f'Generated code:\n{highlighted_code}\n')
                
                # Option to save the generated code
                save_option = input('Do you want to save the generated code to a file? (yes/no): ').strip().lower()
                if save_option == 'yes':
                    filename = input('Enter the filename (e.g., output.py): ').strip()
                    with open(filename, 'w') as file:
                        file.write(generated_code)
                    print(f'Code saved to {filename}')
            except Exception as e:
                logger.error(f'Error generating code: {str(e)}')
                print(f'Error: {str(e)}')

if __name__ == "__main__":
    # Initialize the AI Code Generator
    generator = AICodeGenerator()
    
    # Run the generator interactively
    generator.run() 