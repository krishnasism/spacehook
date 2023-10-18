from pydantic import BaseModel
from typing import Optional
from utils.enums import AuthType


class ResponseRequest(BaseModel):
    endpoint: str
    statuscode: int
    category: str
    response: str
    delay: int
    responsetype: str
    authtype: Optional[str] = AuthType.public.value
    basic_auth_username: Optional[str] = ""
    basic_auth_password: Optional[str] = ""
    access_token: Optional[str] = ""
    hook_id: Optional[str] = ""
    custom_response: Optional[bool] = True


class SettingsRequest(BaseModel):
    default_endpoints_enabled: bool
    unset_endpoints_enabled: bool


class SwaggerIngestRequest(BaseModel):
    swagger_yaml: str
