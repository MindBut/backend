from fastapi import FastAPI
from router import user, chatting

app = FastAPI()

app.include_router(user.router)
app.include_router(chatting.router)
