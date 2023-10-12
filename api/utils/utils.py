from fastapi import Request
from datetime import datetime

async def get_request_dict(request: Request):
    return {
        "method": request.method,
        "url": str(request.url).replace("api/hook/", "/api/hook/"),
        "headers": dict(request.headers),
        "client": str(request.client),
        "cookies": dict(request.cookies),
        "query_params": dict(request.query_params),
        "path_params": request.path_params,
        "user_agent": request.headers.get("user-agent"),
        "remote_address": request.client.host,
        "body": str(await request.body()),
    }
