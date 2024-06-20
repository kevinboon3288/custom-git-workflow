# This is a static workflow that created a new branch based on the current branch, then switch to the new branch, and 
# commit into a packages and push to the repository.

import subprocess
import os

def execute_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, shell=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def create_branch(repo):
    new_branch_name = input("Enter the new branch name: ").strip()
    print("Created new branch and switching to it....")
    if ' ' in new_branch_name:
        print(f"[Error] Branch name is not allowed to have white space: {new_branch_name}\n")
        print("******** New Prompt *********\n")
        main()
    execute_command(f"git checkout -b {new_branch_name}", repo)
    print("******** Done *********\n")
    return new_branch_name

def add_all_changed_files(repo):
    print("Adding all changed files....")
    execute_command("git add .", repo) 
    print("Added all the files\n")
    print("******** Done *********\n")

def get_current_status(repo):
    print("Listed down the current status of Git:")
    execute_command("git status", repo)
    print("******** Done *********\n")

def create_commits(repo):
    proceed_commit = input("Do you want to proceed to commit? (y/n): ").strip().lower()
    if proceed_commit != 'y':
        print("[Abort] Commit aborted.")
        return
    
    commit_messages = input("Enter commit message: ").strip()
    print("Commiting the changes....\n")
    execute_command(f'git commit -m "{commit_messages}"', repo)
    print("******** Done *********\n")

def push(branch, repo):
    proceed_push = input("Do you want to push the changes? (y/n): ").strip().lower()
    if proceed_push != 'y':
        print("[Abort] Push aborted.")
        return
    
    print("Pushing the changes....")
    execute_command(f"git push -f origin {branch}", repo)
    print("******** Done *********\n")


def main():
    repo_directory = input("Enter the directory path of the git repository: ")

    if not os.path.isdir(repo_directory):
        print("[Abort] Unable to found the directory path")
        return

    new_branch_name = create_branch(repo_directory)
    add_all_changed_files(repo_directory)
    get_current_status(repo_directory)
    create_commits(repo_directory)
    get_current_status(repo_directory)
    push(new_branch_name, repo_directory)
    exit(1)

if __name__ == "__main__":
    main()
