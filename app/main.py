"""Tenant Python app scaffold (tenant-python-app-template)."""
import os
from fastapi import FastAPI

app = FastAPI(title="tenant-app", version="0.1.0")


@app.get("/healthz")
def healthz():
    return {"status": "ok", "app": "tenant-app"}


@app.get("/")
def root():
    return {"app": "tenant-app", "env": os.getenv("APP_ENV", "dev")}
