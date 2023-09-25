from fastapi import APIRouter, Query
from deta import Deta

router = APIRouter()
deta = Deta()
requests_collection = deta.Base("requests")
responses_collection = deta.Base("responses")


@router.get("/all-requests")
async def get_all_requests():
    return requests_collection.fetch(desc=True).items


@router.get("/request")
async def get_request_by_id(request_key: str = Query()):
    return requests_collection.fetch({"key": request_key})
