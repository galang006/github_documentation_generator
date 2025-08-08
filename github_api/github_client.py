from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

def get_github_repo(repo, path=""):  
    file_dict = {}

    contents = repo.get_contents(path)
    for content_file in contents:
        if content_file.type == "file":
            if content_file.path == "README.md":
                continue
            file_data = repo.get_contents(content_file.path)

            file_dict[content_file.path] = file_data.decoded_content.decode()
        elif content_file.type == "dir":
            nested_files = get_github_repo(repo, content_file.path)
            file_dict.update(nested_files)
    
    return file_dict

def get_github_code(repo_name):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)  # tanpa token
    repo = g.get_repo(repo_name)
    return get_github_repo(repo)

