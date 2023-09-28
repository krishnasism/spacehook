from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse
from db.detabase import put_request_in_detabase
from deta import Deta
import asyncio
from utils.enums import ResponseType

router = APIRouter()
deta = Deta()
requests_collection = deta.Base("requests")
responses_collection = deta.Base("responses")


@router.get("/")
async def receive_get_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.post("/")
async def receive_post_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.patch("/")
async def receive_patch_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.delete("/")
async def receive_delete_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.put("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.head("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.options("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return PlainTextResponse(
        content="OK",
        status_code=200,
    )


@router.get("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "get")


@router.post("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "post")


@router.patch("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "patch")


@router.delete("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "delete")


@router.put("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "put")


@router.head("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "head")


@router.options("/{rest_of_path:path}")
async def serve_my_app(request: Request, rest_of_path: str):
    return await handle_rest_of_path(request, rest_of_path, "options")


async def handle_rest_of_path(request: Request, rest_of_path: str, category: str):
    response = responses_collection.fetch(
        {"endpoint": rest_of_path, "category": category}
    )
    if response.count == 0:
        return PlainTextResponse(
            content="NOT FOUND",
            status_code=404,
        )
    await put_request_in_detabase(request, endpoint=rest_of_path)
    delay = int(response.items[0].get("delay"))
    await asyncio.sleep(min(19, delay))
    response_type = response.items[0].get("responsetype")
    response_body = response.items[0].get("response")
    response_code = int(response.items[0].get("statuscode"))

    if response_type == ResponseType.plaintext.value:
        return PlainTextResponse(
            content=response_body,
            status_code=response_code,
        )
    elif response_type == ResponseType.json.value:
        return JSONResponse(
            content=response_body,
            status_code=response_code,
        )
    elif response_type == ResponseType.html.value:
        return HTMLResponse(
            content=response_body,
            status_code=response_code,
        )

    # Default
    return PlainTextResponse(
        content=response_body,
        status_code=response_code,
    )
