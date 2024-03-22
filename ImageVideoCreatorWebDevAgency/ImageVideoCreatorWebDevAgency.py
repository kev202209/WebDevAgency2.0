from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class ImageVideoCreatorWebDevAgency(Agent):
    def __init__(self):
        super().__init__(
            name="ImageVideoCreatorWebDevAgency",
            description="This agent uses AI tools to produce high-quality images and videos that complement the website's content.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
