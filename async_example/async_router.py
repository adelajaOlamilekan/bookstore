from fastapi import APIRouter
import time
import asyncio

router = APIRouter()

@router.get("/sync")
def read_sync():
  time.sleep(2)

  return {
    "message": "Synchronous blocking endpoint"
  }

@router.get("/async")
async def read_async():
  await asyncio.sleep(2)
  return {
    "message": "Asynchronous non-blocking ednpoint"
  }