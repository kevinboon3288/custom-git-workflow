import subprocess
import os
from Commons.exceptions import WorkflowException


class GitRepository:
    def __init__(self, repo_directory):
        if not os.path.isdir(repo_directory):
            raise ValueError(f"Invalid repo directory path: {repo_directory}")
        self.repo_directory = repo_directory

    def execute_command(self, command):
        result = subprocess.run(command, cwd=self.repo_directory, text=True, capture_output=True, shell=True)
        if result.returncode != 0:
            raise WorkflowException(result.stderr.strip())
        return result.stdout.strip()

    def get_current_branch(self):
        return self.execute_command("git rev-parse --abbrev-ref HEAD")

    def switch_new_branch(self, branch_name):
        self.execute_command(f"git checkout -b {branch_name}")

    def add_all_changes(self):
        self.execute_command("git add .")

    def get_branch_status(self):
        return self.execute_command("git status")

    def commit_changes(self, message):
        self.execute_command(f'git commit -m "{message}"')

    def push_changes(self, branch_name):
        self.execute_command(f"git push -f origin {branch_name}")
