from gemini_api.gemini_client import GeminiClient
from github_api.github_client import get_github_code
import os

if __name__ == "__main__":
    output_path = "./documentation_output"
    os.makedirs(output_path, exist_ok=True)
    github_repo_url = "https://github.com/galang006/github_documentation_generator"

    github_repo_name = github_repo_url.split("github.com/")[1]
    code = get_github_code(github_repo_name)
    client = GeminiClient()
    prompt = fprompt = f"""
        You are an expert software documentation writer.

        I will provide you a codebase from GitHub repository {github_repo_url} as a dictionary, 
        where each key is a file path and each value is the source code of that file.

        Please write a complete, clear, and professional project documentation in Markdown format based on this codebase.

        If the dictionary keys do NOT include a file named `requirements.txt`, 
        please write the documentation **without** a Prerequisites section.

        # Project Title

        A short description of the project.

        ## Features
        - Key features of the project.

        ## Prerequisites
        - Required software and libraries.

        ## Installation
        Step-by-step instructions on how to install the project.

        ## Usage
        How to run and use the project.

        ## Code Structure
        Explanation of the main folders and important files.

        Here is the codebase (file path : code content):

        {code}

        Please generate the full Markdown documentation now.
        """
    response = client.generate_text(prompt)
    
    username = github_repo_name.split("/")[0]
    repo_name = github_repo_name.split("/")[1]
    filename = f"{username}_{repo_name}_documentation.md"

    full_path = os.path.join(output_path, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(response)
    
    print(f"Documentation generated and saved to {full_path}")