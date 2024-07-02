from .git_command_state import GitCommandState


class GetLogsState(GitCommandState):
    def execute(self, context):
        logs = context.repo.get_logs()
        print(logs)