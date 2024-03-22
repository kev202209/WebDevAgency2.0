from agency_swarm import Agency
from ImageVideoCreatorWebDevAgency import ImageVideoCreatorWebDevAgency
from ContentWriterWebDevAgency import ContentWriterWebDevAgency
from WebDesignerWebDevAgency import WebDesignerWebDevAgency
from WebDeveloperWebDevAgency import WebDeveloperWebDevAgency
from CEOWebDevAgency import CEOWebDevAgency
import os

# load env from .env
from dotenv import load_dotenv
load_dotenv()

set_openai_key=os.environ["OPENAI_API_KEY"]

ceo = CEOWebDevAgency()
web_developer = WebDeveloperWebDevAgency()
web_designer = WebDesignerWebDevAgency()
graphic_designer = GraphicDesignerWebDevAgency()
imageandvideo_creator = ImageVideoCreatorWebDevAgency()
content_writer = ContentWriterWebDevAgency()

agency = Agency([ceo,
                 [ceo, web_designer],
                 [web_designer, web_developer],
                 [web_designer, content_writer],
                 [web_designer, imageandvideo_creator]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()