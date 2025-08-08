# GitHub Documentation Generator

A Python application that automates the generation of comprehensive project documentation for GitHub repositories. It fetches the codebase from a specified GitHub repository and leverages the Google Gemini API to intelligently create professional Markdown documentation.

## Features

*   **Automated Codebase Retrieval**: Automatically fetches all source code files (excluding `README.md`) from a public GitHub repository.
*   **AI-Powered Documentation Generation**: Utilizes the Google Gemini API to generate detailed and well-structured project documentation in Markdown format.
*   **Configurable API Interaction**: Supports environment variables for securely managing GitHub API tokens, Gemini API keys, and model names.
*   **Organized Output**: Saves the generated documentation in a dedicated `documentation_output` directory with a clear naming convention (`username_repository-name_documentation.md`).
*   **Extensible**: Designed with a modular structure, separating GitHub and Gemini API concerns, making it easier to adapt or extend.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/galang006/github_documentation_generator.git
    cd github_documentation_generator
    ```

2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies**:
    This project uses the `google-generativeai`, `PyGithub`, and `python-dotenv` libraries.
    ```bash
    pip install google-generativeai PyGithub python-dotenv
    ```

4.  **Set up Environment Variables**:
    Create a `.env` file in the root directory of the project and add the following variables. Replace the placeholder values with your actual API keys and desired Gemini model.

    ```
    GITHUB_TOKEN=YOUR_GITHUB_PERSONAL_ACCESS_TOKEN
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    GEMINI_MODEL_NAME=gemini-pro # Or another suitable model like gemini-1.5-flash
    ```
    *   **GitHub Token**: Generate a personal access token from your GitHub settings ([Developer settings -> Personal access tokens -> Tokens (classic)](https://github.com/settings/tokens)). Ensure it has at least `repo` scope for public repositories if you need to access private ones or higher limits, otherwise public access might suffice.
    *   **Gemini API Key**: Obtain your API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage

Once installed and configured, you can run the application to generate documentation for a GitHub repository.

1.  **Run the script**:
    Execute the `main.py` file from the project's root directory:
    ```bash
    python main.py
    ```

2.  **Enter GitHub Repository URL**:
    The script will prompt you to enter the URL of the GitHub repository you wish to document:
    ```
    Enter the GitHub repository URL (https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME):
    ```
    Provide the full HTTPS URL, for example, `https://github.com/galang006/github_documentation_generator`.

3.  **Documentation Generation**:
    The script will then proceed to fetch the codebase, send it to the Gemini API for analysis, and generate the documentation. This process may take a few moments depending on the size of the repository and API response times.

    ```
    Generating documentation...
    Documentation generated and saved to ./documentation_output/galang006_github_documentation_generator_documentation.md
    ```

4.  **Output Location**:
    The generated Markdown documentation will be saved in the `documentation_output/` directory, created automatically if it doesn't exist. The filename will follow the format `username_repo_name_documentation.md`.

## Code Structure

The project is organized into logical directories to separate concerns:

```
github_documentation_generator/
├── .gitignore
├── main.py
├── gemini_api/
│   └── gemini_client.py
├── github_api/
│   └── github_client.py
└── documentation_output/ (created at runtime)
    └── <username>_<repo-name>_documentation.md
```

*   **`.gitignore`**: Specifies files and directories that Git should ignore, such as virtual environments, bytecode, and generated output.
*   **`main.py`**:
    This is the main entry point of the application. It orchestrates the entire process:
    *   Initializes the output directory.
    *   Defines the target GitHub repository URL.
    *   Calls functions from `github_api` to fetch the codebase.
    *   Initializes the `GeminiClient`.
    *   Constructs the prompt for the Gemini API, embedding the fetched codebase.
    *   Sends the prompt to Gemini and receives the generated documentation.
    *   Saves the documentation to a Markdown file in the `documentation_output` directory.
*   **`gemini_api/`**:
    This directory contains modules for interacting with the Google Gemini API.
    *   **`gemini_api/gemini_client.py`**: Encapsulates the logic for connecting to and utilizing the Gemini API. It handles API key authentication and provides a method (`generate_text`) to send prompts and receive text responses from the AI model.
*   **`github_api/`**:
    This directory contains modules for interacting with the GitHub API.
    *   **`github_api/github_client.py`**: Provides functions to interact with the GitHub API. Key functions include `get_github_repo` (which recursively fetches all files from a repository) and `get_github_code` (which initializes the GitHub client and uses `get_github_repo` to retrieve the entire codebase as a dictionary of file paths and content).
*   **`documentation_output/`**:
    This directory is automatically created by `main.py` at runtime. All generated Markdown documentation files are stored here.