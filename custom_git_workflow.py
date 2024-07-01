# This is a static workflow that created a new branch based on the current branch, then switch to the new branch, and 
# commit into a packages and push to the repository.

import subprocess
import os

class WorkflowException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.log_Error(message)

    @staticmethod
    def log_Error(message):
        with open('git_errors.log', 'a') as log_file:
            log_file.write(f"{message}\n")
        print(f"[ERR] {message}")

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


def main():
    try:
        repo_dir = input("Enter the directory path of the git repository: ")
        repo = GitRepository(repo_dir)

        option = input("Do you want to create a new branch? (y/n): ").strip().lower()
        if option == 'y':
            new_branch_name = input("Enter the new branch name: ").strip()
            repo.switch_new_branch(new_branch_name)
            print(f"Switched to a new branch '{new_branch_name}'.")
        else:
            new_branch_name = repo.get_current_branch()

        repo.add_all_changes()

        print(repo.get_branch_status())

        proceed_commit = input("Do you want to proceed to commit? (y/n): ").strip().lower()
        if proceed_commit != 'y':
            print("Commit aborted.")
            return

        commit_message = input("Enter commit message: ").strip()
        print(commit_message)
        repo.commit_changes(commit_message)

        print(repo.get_branch_status())

        proceed_push = input("Do you want to push the changes? (y/n): ").strip().lower()
        if proceed_push != 'y':
            print("Push aborted.")
            return

        repo.push_changes(new_branch_name)
        print(f"Changes pushed to branch '{new_branch_name}'.")
        exit(1)

    except ValueError as ve:
        print(ve)
    except WorkflowException as wfex:
        print(f"Git command error: {wfex}")

if __name__ == "__main__":
    main()
