class GitContext:
    def __init__(self, repo):
        self.repo = repo
        self.state = None

    def set_state(self, state):
        self.state = state

    def execute_state(self):
        if self.state:
            self.state.execute(self)
        else:
            print("No state set")
