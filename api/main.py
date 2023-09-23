from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
from utils import put_request_in_detabase

# Deps
deta = Deta()
base = deta.Base("requests")
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4201",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def receive_get_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={'message': 'success'},
        status_code=200,
    )


@app.post("/")
async def receive_post_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={'message': 'success'},
        status_code=200,
    )


@app.patch("/")
async def receive_patch_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={'message': 'success'},
        status_code=200,
    )

@app.delete("/")
async def receive_delete_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={'message': 'success'},
        status_code=200,
    )

@app.put("/")
async def receive_put_request(request: Request):
    await put_request_in_detabase(request)
    return JSONResponse(
        content={'message': 'success'},
        status_code=200,
    )

@app.get("/all-requests")
async def get_all_requests():
    return base.fetch().items


app.mount("/public", StaticFiles(directory=".", html="true"), name="static")
app.mount("/", StaticFiles(directory=".", html="true"), name="static")
