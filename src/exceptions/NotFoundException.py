class NotFoundException(Exception):

    message:str

    def __init__(self: Exception, message: str):
        self.message=message