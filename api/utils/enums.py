from enum import Enum


class ResponseType(Enum):
    json = "json"
    html = "html"
    plaintext = "plaintext"


class AuthType(Enum):
    public = "public"
    basic_auth = "basic"
    bearer_token = "bearer"
