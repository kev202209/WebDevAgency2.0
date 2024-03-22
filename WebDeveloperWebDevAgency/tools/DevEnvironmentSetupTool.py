from agency_swarm.tools import BaseTool
from pydantic import Field
import subprocess
import os
from typing import Optional
import importlib
import time

class DevEnvironmentSetupTool(BaseTool):
    """
    this will be the first tool to run
    Initializes development environments for web development projects.
    Supported stacks include WordPress, JavaScript frameworks, and plain HTML, CSS, and JavaScript.
    """

    project_name: str = Field(
        ..., description="Name of the project to set up the environment for."
    )
    stack: str = Field(
        ..., description="The technology stack to initialize (WordPress, JavaScript, HTML/CSS/JS).")
    file_name: str = Field(
        ..., description="Name of the file in camel case", examples=["index"]
    )
    chain_of_thought: str = Field(
        ..., description="Think step by step to determine how to best implement this tool.", exclude=True
    )
    file_code: str = Field(
        ..., description="Correct code for the file. Must include all the import statements, "
                         "as shown to the client",
        example="Example HTML/CSS/JavaScript/PHP code"
    )
    file_extension: str = Field(
        ..., description="File extension for the tool code. They are 'html', 'css', 'js', 'php'."
    )

    def run(self):
        project_path = f'./{self.project_name}'
        os.makedirs(project_path, exist_ok=True)
        current_directory = os.getcwd()
        time.sleep(1)
        os.chdir(project_path)

        with open(f"{self.file_name}.{self.file_extension}", "w") as f:
            f.write(self.file_code)
            f.close()

        os.chdir(os.path.dirname(current_directory))

        return f"Development environment for {self.project_name} initialized using {self.stack} stack in {project_path}"



