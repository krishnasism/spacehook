from fastapi import Request
from deta import Deta
deta = Deta()

base = deta.Base("requests")

async def put_request_in_detabase(request: Request):
    request_data = {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": str(request.client),
        "cookies": dict(request.cookies),
        "query_params": dict(request.query_params),
        "path_params": request.path_params,
        "user_agent": request.headers.get("user-agent"),
        "remote_address": request.client.host,
        "body": str(await request.body()),
    }
    base.put(request_data)