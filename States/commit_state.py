from .git_command_state import GitCommandState

class CommitState(GitCommandState):
    def execute(self, context):
        commit_message = input("Enter commit message: ").strip()
        context.repo.commit_changes(commit_message)
        print("Changes committed.")
