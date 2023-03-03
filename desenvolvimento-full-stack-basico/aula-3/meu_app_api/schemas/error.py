from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de eero será representada
    """
    mesage: str
