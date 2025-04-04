from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user, page


app = FastAPI(
    title="Onboarding Flow API",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api")
app.include_router(page.router, prefix="/api")
