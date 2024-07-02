from .git_command_state import GitCommandState

class CheckoutState(GitCommandState):
    def execute(self, context):
        new_branch_name = input("Enter the new branch name: ").strip()
        context.repo.switch_new_branch(new_branch_name)
        print(f"Switched to a new branch '{new_branch_name}'.")
