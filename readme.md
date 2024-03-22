# Agency Swarm Lab
Welcome to the Web development agency repository! This is a AI project of custom AI agent teams developed using the [Agency Swarm](https://github.com/VRSEN/agency-swarm) framework.

## Getting Started

To get started with the webdevagency, follow these detailed steps:

1. **Clone the Repository**: First, clone the Agency Swarm Lab repository to your local machine to access the framework and the example agencies.

    ```bash
    git clone https://github.com/kev202209/webdevagency.git
    ```

2. **Install Global Requirements**: Navigate to the root directory of the cloned repository and install the global requirements using the `requirements.txt` file. This will set up the necessary environment for running the Agency Swarm framework.

    ```bash
    cd agency-swarm-lab
    pip install -r requirements.txt
    ```



3. **Set Up the `.env` File**: The project utilize OpenAI's API for their operations. To enable this functionality, you must provide your OpenAI API key.

    - Create a `.env` file in the chosen agency's folder.
    - Add your OpenAI API key to this file as follows:

        ```
        OPENAI_API_KEY='your_openai_api_key_here'
        ```

    Dropping this `.env` file into the agency folder allows the system to authenticate with OpenAI's services seamlessly.

5. **Run Your Agency**: With the environment properly set up, you are now ready to activate your agency. Execute the following command within the agency's directory:

    ```bash
    python agency.py
    ```

    This command starts the operation of your custom AI agency, demonstrating the collaborative power of AI agents in accomplishing complex tasks.

# Contributing
We encourage contributions to the WebDevAgency! If you have an improvement of the project and would like to share it, please submit a pull request with your project.