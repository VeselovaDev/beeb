from src.exceptions import BeebError


class UserNotFound(BeebError):
    pass


class WrongPassword(BeebError):
    pass
