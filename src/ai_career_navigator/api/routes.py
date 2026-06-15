from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EchoRequest(BaseModel):
    message: str


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}


@router.post("/echo")
async def echo(payload: EchoRequest) -> EchoRequest:
    return payload
