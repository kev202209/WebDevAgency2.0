import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from pydantic import Field
from agency_swarm.tools import BaseTool
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

class AIBasedCreationSoftwareTool(BaseTool):
    """
    Utilizes AI to generate high-quality images and videos for website content.
    Supports a variety of styles, themes, and formats, allowing for creative customization.
    """

    project_name: str = Field(
        ..., description="Name of the project to create visual content for.")
    text: str = Field(
        ..., description="The user specifications for the image"
    )

    def run(self):
        API_KEY = os.getenv("OPENAI_API_KEY")
        if not API_KEY:
            raise ValueError("OpenAI API key not found in environment variables.")

        try:
            client = OpenAI(api_key=API_KEY)
            response = client.images.generate(
                model="dall-e-3",
                prompt=self.text,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            
            # Download the image file
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                # Determine the path to save the image
                project_folder = f"./{self.project_name}"
                os.makedirs(project_folder, exist_ok=True)
                
                # Generate a unique filename with a timestamp
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                image_filename = f"image_{timestamp}.jpg"
                image_path = os.path.join(project_folder, image_filename)

                # Save the image to the project's folder
                with open(image_path, "wb") as image_file:
                    image_file.write(image_response.content)
                
                return f"Visual content created for project {self.project_name}. Image saved at: {image_path}"
            else:
                return "Failed to download image."
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
