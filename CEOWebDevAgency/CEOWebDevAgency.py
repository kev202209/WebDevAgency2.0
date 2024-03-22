from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class CEOWebDevAgency(Agent):
    def __init__(self):
        super().__init__(
            name="CEOWebDevAgency",
            description="This agent oversees agency operations, client liaisons, and coordination among different specialized agents within a web development agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
