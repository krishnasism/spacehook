from pydantic import BaseModel


class ResponseRequest(BaseModel):
    endpoint: str
    statuscode: int
    category: str
    response: str
    delay: int
    responsetype: str
