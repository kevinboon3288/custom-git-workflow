# This is a static workflow that created a new branch based on the current branch, then switch to the new branch, and 
# commit into a packages and push to the repository.

from Models.git_repository import GitRepository
from Models.git_context import GitContext
from States.add_changes_state import AddChangesState
from States.commit_state import CommitState
from States.status_check_state import StatusCheckState
from States.checkout_state import CheckoutState
from States.push_changes_state import PushChangesState
from Commons.exceptions import WorkflowException

def main():
    try:
        repo_dir = input("Enter the directory path of the git repository: ")
        repo = GitRepository(repo_dir)
        context = GitContext(repo)

        commands = {
            "add": AddChangesState(),
            "commit": CommitState(),
            "status": StatusCheckState(),
            "checkout": CheckoutState(),
            "push": PushChangesState(),
        }

        while True:
            command = input("Enter a git command (add, commit, status, checkout, push) or 'exit' to quit: ").strip().lower()
            if command == 'exit':
                break
            if command in commands:
                context.set_state(commands[command])
                context.execute_state()
            else:
                print("Invalid command")

    except ValueError as ve:
        print(ve)
    except WorkflowException as we:
        print(f"Git command error: {we}")

if __name__ == "__main__":
    main()
