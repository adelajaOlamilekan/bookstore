class ValueExceptionError(Exception):

  def __init__(self, message:str, error_code: int):
    self.message = message
    self.error_code = error_code
    super().__init__(self.message, self.error_code)