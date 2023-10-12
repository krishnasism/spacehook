from deta import Deta
from datetime import datetime
deta = Deta()

requests_collection = deta.Base("requests")


async def put_request_in_detabase(request_data: dict, endpoint="/"):
    request_data["timestamp"] = str(datetime.utcnow())
    request_data["endpoint"] = endpoint
    requests_collection.put(request_data)
