class NegativeBalanceError(Exception):
    def __int__(self, message):
        self.message = message


class ValidNum(Exception):
    def __int__(self, message):
        self.message = message
