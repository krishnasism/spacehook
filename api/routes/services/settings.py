from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from rrequests.models import ResponseRequest, SettingsRequest
from utils.variables import DEFAULT_USER_SETTINGS

from deta import Deta

router = APIRouter()
deta = Deta()
requests_collection = deta.Base("requests")
responses_collection = deta.Base("responses")
user_settings = deta.Base("usersettings")


@router.get("/")
async def get_settings():
    responses = []
    for item in responses_collection.fetch(desc=True).items:
        item["response"] = item["response"][0 : min(len(item["response"]), 100)] + (
            "..." if len(item["response"]) > 100 else ""
        )
        responses.append(item)
    return responses


@router.get("/hook")
async def get_hook(hook_id: str):
    hook = responses_collection.get(hook_id)
    return JSONResponse(
        content=hook,
        status_code=200,
    )


@router.delete("/hook")
async def delete_hook(hook_id: str):
    responses_collection.delete(hook_id)
    return JSONResponse(
        content={
            "success": True,
        },
        status_code=200,
    )


@router.get("/request")
async def get_request(request_id: str = Query()):
    _request = requests_collection.get(request_id)
    return _request


@router.delete("/request")
async def delete_request(request_id: str = Query()):
    requests_collection.delete(request_id)
    return JSONResponse(
        content={
            "success": True,
        },
        status_code=200,
    )


@router.post("/request")
async def post_new_request(item: ResponseRequest):
    updated = False
    endpoint = item.endpoint.strip("/")
    if item.hook_id:
        responses_collection.delete(item.hook_id)
    data = responses_collection.fetch({"endpoint": endpoint, "category": item.category})
    if data.count > 0:
        updated = True
        for existing_item in data.items:
            responses_collection.delete(existing_item.get("key"))
    responses_collection.put(
        {
            "endpoint": endpoint,
            "statuscode": item.statuscode,
            "category": item.category,
            "response": item.response,
            "delay": item.delay,
            "responsetype": item.responsetype,
            "authtype": item.authtype,
            "basic_auth_username": item.basic_auth_username,
            "basic_auth_password": item.basic_auth_password,
            "access_token": item.access_token,
        }
    )
    return JSONResponse(
        content={"success": True, "updated": updated},
        status_code=200,
    )


@router.post("/user-settings")
async def update_settings(settings: SettingsRequest):
    _settings = user_settings.fetch()
    if _settings.count > 0:
        for existing_item in _settings.items:
            user_settings.delete(existing_item.get("key"))
    user_settings.put(
        {
            "default_endpoints_enabled": settings.default_endpoints_enabled,
            "unset_endpoints_enabled": settings.unset_endpoints_enabled,
        }
    )
    return JSONResponse(
        content={
            "success": True,
        },
        status_code=200,
    )


@router.get("/user-settings")
async def get_user_settings():
    _settings = user_settings.fetch()
    settings = DEFAULT_USER_SETTINGS
    if _settings.count > 0:
        settings = _settings.items[0]
    print(settings)
    return JSONResponse(
        content=settings,
        status_code=200,
    )
