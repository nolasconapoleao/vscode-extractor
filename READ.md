# Service extractor

Given a folder structure use vscode to extract the folder that contain a specific file.
For example root.cmake

Given visual studio's limited environemnt variables, this provides a way to extract a new customizable environment variable that can be updated by running a command.

## Usage
- While selecting a file from any service
- Start command palette in visual studio Ctrl+Shift+P
- Run task "Extract Service"
- Run task "Print Service"

## Explanation
The task under "Extract Service" calls the python script that evaluates the service.
The path containing the CMakeLists.txt will be stored to an environment variable under ${config:service}
