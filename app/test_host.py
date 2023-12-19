#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-


from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def start():
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
