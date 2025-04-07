import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user, page

load_dotenv(override=True)

allowed_origins = (
    ["https://onboarcerer.app"]
    if os.getenv("ENV") == "production"
    else ["http://localhost:5173"]
)


app = FastAPI(
    title="Onboarding Flow API",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Service is up."}


app.include_router(
    user.router,
)
app.include_router(
    page.router,
)
