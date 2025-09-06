import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import os

load_dotenv()

class GeminiClient:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
        )
        
        self.prompt_template = """
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

        Use English language only
        """

        self.prompt = PromptTemplate(
            template= self.prompt_template,
            input_variables=["github_repo_url", "code"]
        )

        self.chain = self.prompt | self.llm

    def generate_text(self, github_repo_url, code): 
        response = self.chain.invoke({ 
            "github_repo_url": github_repo_url, 
            "code": code 
        }) 
        return response.content