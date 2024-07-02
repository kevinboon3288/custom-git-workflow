from .git_command_state import GitCommandState

class AddChangesState(GitCommandState):
    def execute(self, context):
        context.repo.add_all_changes()
        print("Changes added to staging area.")
