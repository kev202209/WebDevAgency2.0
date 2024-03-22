from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class WebDesignerWebDevAgency(Agent):
    def __init__(self):
        super().__init__(
            name="WebDesignerWebDevAgency",
            description="This agent focuses on creating appealing layouts and themes, installing WordPress plugins, and ensuring a user-friendly experience.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
