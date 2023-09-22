from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from deta import Deta
from utils import put_request_in_detabase

# Deps
deta = Deta()
base = deta.Base("requests")
app = FastAPI()


@app.get("/")
async def receive_get_request(request: Request):
    await put_request_in_detabase(request)
    return base.fetch().items


@app.post("/")
async def receive_post_request(request: Request):
    await put_request_in_detabase(request)
    return base.fetch().items


@app.patch("/")
async def receive_patch_request(request: Request):
    await put_request_in_detabase(request)
    return base.fetch().items


@app.delete("/")
async def receive_delete_request(request: Request):
    await put_request_in_detabase(request)
    return base.fetch().items


@app.put("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return base.fetch().items


@app.get("/all-requests")
async def get_all_requests():
    return base.fetch().items


app.mount("/public", StaticFiles(directory=".", html="true"), name="static")
app.mount("/", StaticFiles(directory=".", html="true"), name="static")
