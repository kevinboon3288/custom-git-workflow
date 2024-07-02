from .git_command_state import GitCommandState


class StatusCheckState(GitCommandState):
    def execute(self, context):
        status = context.repo.get_branch_status()
        print(status)
