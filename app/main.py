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
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api")
app.include_router(page.router, prefix="/api")
