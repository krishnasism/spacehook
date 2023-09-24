from fastapi import APIRouter, Query, Form
from fastapi.responses import JSONResponse
from rrequests.models import ResponseRequest

from deta import Deta

router = APIRouter()
deta = Deta()
requests_collection = deta.Base("requests")
responses_collection = deta.Base("responses")


@router.get("/")
async def get_settings():
    return responses_collection.fetch(desc=True).items

@router.delete("/hook")
async def delete_hook(hook_id: str):
    responses_collection.delete(hook_id)
    return JSONResponse(
        content={
            "success": True,
        },
        status_code=200
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
        status_code=200
    )

@router.post("/request")
async def post_new_request(item: ResponseRequest):
    updated = False
    endpoint = item.endpoint.strip("/")
    data = responses_collection.fetch({"endpoint": endpoint})
    if data.count > 1:
        updated = True
        for existing_item in data.items:
            responses_collection.delete(existing_item.get("key"))
    responses_collection.put(
        {
            "endpoint": endpoint,
            "statuscode": item.statuscode,
            "category": item.category,
            "response": item.response,
        }
    )
    return JSONResponse(
        content={"success": True, "updated": updated},
        status_code=200,
    )
