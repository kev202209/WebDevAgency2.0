from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class ContentWriterWebDevAgency(Agent):
    def __init__(self):
        super().__init__(
            name="ContentWriterWebDevAgency",
            description="This agent focuses on producing tailored written content for websites, blogs, and other content areas, ensuring engagement and relevance.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
