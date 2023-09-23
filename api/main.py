from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = get_application()

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


app.mount("/public", StaticFiles(directory=".", html="true"), name="static")
app.mount("/", StaticFiles(directory=".", html="true"), name="static")
