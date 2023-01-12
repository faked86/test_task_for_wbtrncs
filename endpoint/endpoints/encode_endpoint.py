from urllib.parse import quote

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from pydantic import AnyUrl, BaseModel


class Body(BaseModel):
    link: AnyUrl


encode_router = APIRouter()


@encode_router.post("/encode", response_class=PlainTextResponse)
def encode_view(body: Body):
    return quote(body.link.encode("utf8"), safe=":/")
