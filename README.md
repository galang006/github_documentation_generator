# AI-Powered GitHub Documentation Generator

This project provides an automated solution for generating comprehensive project documentation in Markdown format by leveraging the Google Gemini AI model and the GitHub API. It fetches a given GitHub repository's codebase, processes it, and then uses a Large Language Model (LLM) to create a detailed documentation file, making it easier for developers to quickly understand and onboard new projects.

## Features
-   **Automated Code Fetching**: Connects to the GitHub API to recursively retrieve all source code files from a specified public repository.
-   **AI-Powered Documentation Generation**: Utilizes the `gemini-2.5-flash` model via `langchain-google-genai` to intelligently analyze the codebase and generate structured documentation.
-   **Markdown Output**: Produces clean, readable documentation in Markdown format, ready for integration into project READMEs or other documentation platforms.
-   **Structured Output**: Organizes generated documentation into a dedicated `documentation_output` directory with clear naming conventions.
-   **Configurable LLM Prompt**: The project uses a predefined prompt template within its `GeminiClient` to guide the AI in generating high-quality, relevant documentation sections (Features, Installation, Usage, Code Structure).

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the Repository (or create the files locally):**
    First, you would typically clone the repository. As this is a hypothetical scenario for documentation generation, assume you have access to the project files.

2.  **Install Dependencies:**
    
    ```bash
    pip install python-dotenv PyGithub langchain-google-genai langchain
    ```

3.  **Set Up Environment Variables:**
    The project requires API keys for both GitHub and Google Gemini.
    Create a `.env` file in the root directory of the project and add the following:

    ```
    GITHUB_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    -   **GitHub Token**: Generate a Personal Access Token from your GitHub developer settings. Ensure it has at least `repo` scope to access private repositories or no specific scope for public ones.
    -   **Gemini API Key**: Obtain a Google API Key from the Google AI Studio or Google Cloud Console.

## Usage

To generate documentation for a GitHub repository:

1.  **Run the `main.py` script:**

    ```bash
    python main.py
    ```

2.  **Enter GitHub Repository URL:**
    The script will prompt you to enter the full URL of the GitHub repository you wish to document:

    ```
    Enter the GitHub repository URL (https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME):
    ```
    Provide the URL, for example: `https://github.com/galang006/github_documentation_generator`

3.  **View Generated Documentation:**
    The script will then fetch the code, send it to the Gemini API, and save the generated documentation. You will see a confirmation message indicating where the documentation file has been saved:

    ```
    Generating documentation...
    Documentation generated and saved to ./documentation_output/YOUR_USERNAME_YOUR_REPOSITORY_NAME_documentation.md
    ```
    The generated Markdown file will be located in the `documentation_output/` directory, named after the GitHub username and repository.

## Code Structure

The project is organized into logical modules to separate concerns between GitHub API interaction, Gemini API interaction, and the main application logic.

```
.
├── .gitignore
├── main.py
├── gemini_api/
│   └── gemini_client.py
├── github_api/
│   └── github_client.py
└── documentation_output/ (created at runtime)
    └── [username]_[repo_name]_documentation.md (generated output)
```

### Main Files and Directories:

-   **`.gitignore`**:
    A standard Git ignore file for Python projects, specifying files and directories that should not be tracked by Git (e.g., `__pycache__`, virtual environments, API keys, and the `documentation_output` directory).

-   **`main.py`**:
    This is the entry point of the application. It orchestrates the entire process:
    -   Prompts the user for a GitHub repository URL.
    -   Calls `github_api.github_client` to fetch the repository's codebase.
    -   Initializes `gemini_api.gemini_client` to interact with the Gemini LLM.
    -   Sends the fetched code and repository URL to the Gemini client for documentation generation.
    -   Saves the resulting Markdown documentation to a file within the `documentation_output/` directory.

-   **`gemini_api/`**:
    This directory contains modules related to interacting with the Google Gemini API.
    -   **`gemini_api/gemini_client.py`**:
        Defines the `GeminiClient` class responsible for:
        -   Loading environment variables (e.g., `GOOGLE_API_KEY`).
        -   Initializing the `ChatGoogleGenerativeAI` model (`gemini-2.5-flash`).
        -   Defining the `prompt_template` that guides the LLM in generating the project documentation with specific sections (Project Title, Features, Installation, Usage, Code Structure).
        -   Creating an `LLMChain` for structured interaction with the LLM.
        -   The `generate_text` method takes the GitHub repository URL and the codebase dictionary as input, invokes the LLM chain, and returns the generated documentation text.

-   **`github_api/`**:
    This directory contains modules for interacting with the GitHub API.
    -   **`github_api/github_client.py`**:
        Provides functions to fetch repository content:
        -   `get_github_repo(repo, path="")`: A recursive function that traverses a GitHub repository, fetches the content of each file, and stores it in a dictionary where keys are file paths and values are file contents. It explicitly ignores `README.md` files.
        -   `get_github_code(repo_name)`: Initializes the `PyGithub` client using a `GITHUB_TOKEN` from environment variables and then calls `get_github_repo` to retrieve the entire codebase for the specified repository.

-   **`documentation_output/`**:
    This directory is created automatically by `main.py` if it doesn't exist. It serves as the storage location for all generated Markdown documentation files. Each generated file is named using the format `YOUR_USERNAME_YOUR_REPOSITORY_NAME_documentation.md`.