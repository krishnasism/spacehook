from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from db.detabase import put_request_in_detabase
from deta import Deta
import asyncio

router = APIRouter()
deta = Deta()
requests_collection = deta.Base("requests")
responses_collection = deta.Base("responses")


@router.get("/")
async def receive_get_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.post("/")
async def receive_post_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.patch("/")
async def receive_patch_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.delete("/")
async def receive_delete_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.put("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.head("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.options("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={"message": "success"},
        status_code=200,
    )


@router.get("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


@router.post("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


@router.patch("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


@router.delete("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


@router.put("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


@router.head("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


@router.options("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path)


async def handle_rest_of_path(request: Request, rest_of_path: str):
    response = responses_collection.fetch({"endpoint": rest_of_path})
    if response.count == 0:
        return JSONResponse(
            content={"message": "Not found"},
            status_code=404,
        )
    await put_request_in_detabase(request, endpoint=rest_of_path)
    delay = int(response.items[0].get("delay"))
    await asyncio.sleep(min(19, delay))
    return JSONResponse(
        content=response.items[0].get("response"),
        status_code=int(response.items[0].get("statuscode")),
    )
