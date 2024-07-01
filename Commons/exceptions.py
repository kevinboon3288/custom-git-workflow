class WorkflowException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.log_Error(message)

    @staticmethod
    def log_Error(message):
        with open('git_errors.log', 'a') as log_file:
            log_file.write(f"{message}\n")
        print(f"[ERR] {message}")