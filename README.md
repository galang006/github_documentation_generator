# GitHub Documentation Generator

This project is a Python application designed to automate the generation of comprehensive project documentation for GitHub repositories. It leverages Google's Gemini Large Language Model (LLM) to analyze a given codebase and produce clear, professional documentation in Markdown format.

## Features
-   **Automated Documentation Generation**: Automatically fetches all relevant source code files from a specified GitHub repository.
-   **AI-Powered Content Creation**: Utilizes the Gemini 2.5 Flash LLM via the LangChain framework to generate detailed and structured documentation.
-   **Recursive Code Fetching**: Efficiently navigates and retrieves files from nested directories within a GitHub repository.
-   **Markdown Output**: Generates documentation in a universally readable Markdown format, suitable for `README.md` files or project wikis.
-   **Customizable Prompt**: The LLM interaction is guided by a predefined, structured prompt to ensure consistent and high-quality documentation output.
-   **Environment Variable Management**: Securely handles API tokens using environment variables.

## Installation

To set up the project locally, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/galang006/github_documentation_generator.git
    cd github_documentation_generator
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    The project relies on several Python libraries. Install them using pip:
    ```bash
    pip install python-dotenv langchain langchain-google-genai PyGithub
    ```

4.  **Set Up Environment Variables**:
    Create a `.env` file in the root directory of the project and add your GitHub Personal Access Token and Google Gemini API Key:
    ```
    GITHUB_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    -   **GitHub Token**: Generate a personal access token from your GitHub settings with `repo` scope.
    -   **Gemini API Key**: Obtain an API key from Google AI Studio.

## Usage

To generate documentation for a GitHub repository:

1.  **Run the Main Script**:
    Execute the `main.py` file from your terminal:
    ```bash
    python main.py
    ```

2.  **Enter GitHub Repository URL**:
    The script will prompt you to enter the full URL of the GitHub repository you wish to document. For example:
    ```
    Enter the GitHub repository URL (https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME): https://github.com/galang006/github_documentation_generator
    ```

3.  **View Generated Documentation**:
    Once the process is complete, the documentation will be saved as a Markdown file in the `documentation_output/` directory within your project. The filename will be in the format `username_reponame_documentation.md`.

    Example output message:
    ```
    Documentation generated and saved to ./documentation_output/galang006_github_documentation_generator_documentation.md
    ```

## Code Structure

The project is organized into logical modules to separate concerns and enhance maintainability:

```
github_documentation_generator/
├── .gitignore
├── main.py
├── gemini_api/
│   └── gemini_client.py
├── github_api/
│   └── github_client.py
└── documentation_output/
    └── <generated_documentation_files>.md
```

-   **`.gitignore`**: Specifies intentionally untracked files that Git should ignore, such as virtual environment folders, compiled Python files, and generated documentation output.
-   **`main.py`**:
    -   This is the entry point of the application.
    -   It orchestrates the entire documentation generation process: prompts for the GitHub URL, fetches code, calls the Gemini LLM, and saves the output.
-   **`gemini_api/`**:
    -   **`gemini_client.py`**: Contains the `GeminiClient` class responsible for interacting with the Google Gemini LLM. It loads environment variables for authentication, defines the prompt template used for documentation generation, and manages the LangChain integration.
-   **`github_api/`**:
    -   **`github_client.py`**: Houses functions for interacting with the GitHub API. It uses the `PyGithub` library to authenticate with a GitHub token, recursively fetches all source code files from a specified repository (excluding `README.md`), and returns them as a dictionary.
-   **`documentation_output/`**:
    -   This directory is created by `main.py` and serves as the destination for all generated Markdown documentation files.