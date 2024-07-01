# This is a static workflow that created a new branch based on the current branch, then switch to the new branch, and 
# commit into a packages and push to the repository.

from Commons.exceptions import WorkflowException
from Modules.git_repository import GitRepository


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
    except WorkflowException as workflow_ex:
        print(f"Git command error: {workflow_ex}")


if __name__ == "__main__":
    main()
