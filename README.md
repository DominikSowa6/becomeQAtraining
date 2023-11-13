# Automation QA Training
This project is a training framework for testing GitHub API and UI

## Framework structure
### Config module
Config module contain framework's and env's configuration. The parameters used will be stored in the _**config.py**_ file

### Application module
Application module contain directories for tested applications

How to add application:
1. Create a folder in applications/<application_name>
2. Create a subfolders in applications/<application_name>/<sub_folder>
3. Create a file inside tests/<application_name>/<test_module>/<file_name>
4. Create a file inside tests/<application_name>/<test_module>/<file_name>
5. Use the same coding standards to create a code

### Helpers module
This module contains helper functions stored in helper.py
### Tests module
The module contains tests divided into testing areas: 
* **API folder** contains API tests
* **UI folder** contains UI tests.
