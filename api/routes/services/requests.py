from fastapi import APIRouter, Query
from deta import Deta

router = APIRouter()
deta = Deta()
requests_collection = deta.Base("requests")
responses_collection = deta.Base("responses")


@router.get("/all-requests")
async def get_all_requests():
    all_requests = requests_collection.fetch(desc=True).items
    sorted_requests = sorted(all_requests, key=lambda x: x["timestamp"], reverse=True)
    return sorted_requests


@router.get("/request")
async def get_request_by_id(request_key: str = Query()):
    return requests_collection.fetch({"key": request_key})
