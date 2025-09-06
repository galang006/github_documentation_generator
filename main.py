from gemini_api.gemini_client import GeminiClient
from github_api.github_client import get_github_code
import os

if __name__ == "__main__":
    output_path = "./documentation_output"
    os.makedirs(output_path, exist_ok=True)
    github_repo_url = input("Enter the GitHub repository URL (https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME): ")

    github_repo_name = github_repo_url.split("github.com/")[1]
    code = get_github_code(github_repo_name)
    client = GeminiClient()
    
    print("Generating documentation...")
    response = client.generate_text(github_repo_url, code)
    
    username = github_repo_name.split("/")[0]
    repo_name = github_repo_name.split("/")[1]
    filename = f"{username}_{repo_name}_documentation.md"

    full_path = os.path.join(output_path, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(response)
    
    print(f"Documentation generated and saved to {full_path}")