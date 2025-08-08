from gemini_api.gemini_client import GeminiClient
from github_api.github_client import get_github_code

if __name__ == "__main__":
    code = get_github_code("galang006/youtube_download")
    client = GeminiClient()
    prompt = fprompt = f"""
        You are an expert software documentation writer.

        I will provide you a codebase from GitHub as a dictionary, where each key is a file path and each value is the source code of that file.

        Please write a complete, clear, and professional project documentation in Markdown format based on this codebase.

        The documentation should include the following sections:

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
    print(response)