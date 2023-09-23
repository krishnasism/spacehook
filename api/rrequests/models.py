from pydantic import BaseModel

class ResponseRequest(BaseModel):
    endpoint: str
    statuscode: str
    category: str
    response: str