from fastapi import FastAPI

from endpoints.encode_endpoint import encode_router


app = FastAPI()
app.include_router(encode_router)
