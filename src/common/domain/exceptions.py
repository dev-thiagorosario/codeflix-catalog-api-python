class InvalidUuidException(Exception):
    def __init__(self, message: str = "ID deve ser um UUID válido."):
        self.message = message
        super().__init__(self.message)
