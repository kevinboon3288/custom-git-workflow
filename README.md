# PyGitAutomator
Welcome to PyGitAutomator Repository! This Python script helps to create a custom workflow with a set of git commands.

[![License](https://img.shields.io/github/license/kevinboon3288/custom-git-workflow)](https://github.com/kevinboon3288/version-controller/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/kevinboon3288/custom-git-workflow)](https://github.com/kevinboon3288/version-controller/issues)
[![GitHub stars](https://img.shields.io/github/stars/kevinboon3288/custom-git-workflow)](https://github.com/kevinboon3288/version-controller/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kevinboon3288/custom-git-workflow)](https://github.com/kevinboon3288/version-controller/network)
[![GitHub contributors](https://img.shields.io/github/contributors/kevinboon3288/custom-git-workflow)](https://github.com/kevinboon3288/version-controller/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/kevinboon3288/custom-git-workflow)](https://github.com/kevinboon3288/version-controller/commits/main)

## Built With

- **Language:** Python

## Git Commands Supported

These are supported git commands can be used in the workflow:
- Add all files changes
  ```python
    AddChangeState
  ```
- Checkout to a new branch
  ```python
    CheckoutState
  ```
- Commit the changes
  ```python
    CommitState
  ```
- Get the commit log histroies
  ```python
    GetLogsState
  ```
- Push the commits
  ```python
    PushChangesState
  ```
- Check current branch status
  ```python
    CheckoutState
  ```

## Execution

To run the script:
1. Clone this repository:
   ```bash
    git clone https://github.com/kevinboon3288/custom-git-workflow.git
   ```
2. Please install the latest version of [Python3](https://www.python.org/downloads/) and set the PATH into your environment.
3. Open Command Prompt (CMD) and switch to the repo directory.
   ```bash
    cd custom-git-workflow
   ```
5. Run this command:
   ```bash
    python custom_git_workflow.py
   ```

## Customize the Git Commands

1. Open Command Prompt (CND) and switch to the repo directory
2. Open the Visual Studio Code with this command:
   ```bash
    code .
   ```
3. Open custom_git_workflow.py
4. Update the the contents in the dictionary based on your options:
   ```python
    commands = {
        "add": AddChangesState(),
        "commit": CommitState(),
        "status": StatusCheckState(),
        "checkout": CheckoutState(),
        "push": PushChangesState(),
        "log": GetLogsState()
    }
   ```

## License
This project is licensed under the MIT License.

## Contact
Have any questions or suggestions? Feel free to open an issue or contact the author directly at kevintan7227@gmail.com.
