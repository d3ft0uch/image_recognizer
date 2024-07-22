class ApiException(Exception):
    message: str
    code: int

    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code
        self.message = message
