from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from schemas import STask, STaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print('Ready to work')
    yield
    print('Turn OFF')

app = FastAPI(lifespan=lifespan)

tasks = []


