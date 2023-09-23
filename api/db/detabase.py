from fastapi import Request
from deta import Deta
from datetime import datetime

deta = Deta()

requests_collection = deta.Base("requests")

async def put_request_in_detabase(request: Request, endpoint='/'):
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
        "timestamp": str(datetime.utcnow()),
        "endpoint": endpoint,
    }
    requests_collection.put(request_data)

