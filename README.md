# AI Code Generator

This project is an AI-powered system that can generate Python code for various tasks. It uses advanced machine learning models to understand user requirements and produce efficient, well-documented code.

## Features

- **Code Generation**: Automatically generates Python code based on user input.
- **Multiple Use Cases**: Supports a wide range of applications, from simple scripts to complex applications.
- **Extensible**: Designed to be easily extended with new capabilities.

## Setup Instructions

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

## Usage

### Interactive Mode

When you run the AI Code Generator, it will prompt you to enter your code generation request. For example:

```
Welcome to the AI Code Generator!
Enter your code generation request (or type "exit" to quit):
> Create a simple calculator
Generated code: Generated code will appear here
```

### Example Requests

- **Create a simple calculator**: Generates a basic calculator script.
- **Generate a data visualization**: Creates a script for data visualization using libraries like `matplotlib`.
- **Build a web scraper**: Produces a script to scrape data from a specified website.
- **File I/O**: Generates code for reading and writing files.
- **Sorting Algorithm**: Produces a bubble sort implementation.
- **Flask App**: Creates a basic Flask web application.

## Testing

To ensure the AI Code Generator works as expected, you can run the test suite:

```bash
python test_main.py
```

### Test Cases

- **Calculator Code Generation**: Checks if the generated code for a calculator request includes the expected functions (`add`, `subtract`, `multiply`, `divide`).
- **Data Visualization Code Generation**: Verifies that the generated code for data visualization includes the necessary imports (`matplotlib`, `numpy`).
- **Web Scraper Code Generation**: Ensures that the generated code for a web scraper includes the required imports (`requests`, `BeautifulSoup`).
- **Invalid Input Handling**: Confirms that the generator returns an appropriate message for invalid requests.

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating your feature branch
3. Committing your changes
4. Pushing to the branch
5. Creating a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 