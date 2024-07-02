from .git_command_state import GitCommandState


class PushChangesState(GitCommandState):
    def execute(self, context):
        branch_name = context.repo.get_current_branch()
        context.repo.push_changes(branch_name)
        print(f"Changes pushed to branch '{branch_name}'.")
