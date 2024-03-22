import os
import subprocess
from typing import Literal
from pydantic import Field
from agency_swarm.tools import BaseTool

class RunCommand(BaseTool):
    """Enables you to execute terminal commands related to JavaScript frameworks."""
    framework: Literal['nextjs', 'react', 'angular', 'vuejs'] = Field(...,
        description='The JavaScript framework to work with.'
    )
    command: Literal['build', 'create', 'install'] = Field(...,
        description='The action to perform. Options include `build`, `create` (for file creation), or `install`.'
    )
    options: str = Field(
        default='',
        description='Additional options to pass to the command.'
    )

    def run(self):
        try:
            if self.command == 'create':
                # Creating a new file
                file_name = self.options.strip()
                if not file_name:
                    return 'Please provide a file name.'
                file_path = os.path.join(self.shared_state.get('app_directory'), file_name)
                with open(file_path, 'w') as f:
                    f.write('')
                return f'File "{file_name}" created successfully.'

            elif self.command == 'build' or self.command == 'install':
                # Command execution
                if not self.shared_state.get('app_directory'):
                    return 'Please create a project directory first.'

                current_directory = os.getcwd()
                os.chdir(self.shared_state.get('app_directory'))

                cmd = []
                if self.framework == 'nextjs':
                    if self.command == 'build':
                        cmd = ['npm', 'run', 'build']
                    elif self.command == 'install':
                        cmd = ['npm', 'install']
                    else:
                        return 'Invalid command.'
                elif self.framework == 'react':
                    # Define commands for React
                    pass
                elif self.framework == 'angular':
                    # Define commands for Angular
                    pass
                elif self.framework == 'vuejs':
                    # Define commands for Vue.js
                    pass
                else:
                    return 'Invalid framework.'

                cmd += self.options.split()
                process = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                os.chdir(current_directory)  # Ensure the directory is switched back

                if process.returncode == 0:
                    return f'Command executed successfully. Output:\n{process.stdout}'
                else:
                    return f'Error executing command: {process.stderr}'

            else:
                return 'Invalid command. Please use either `build`, `create`, or `install`.'

        except subprocess.CalledProcessError as e:
            return f'Error executing command: {e.stderr}'
