import uvicorn
import asyncio

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import Database
from pydantic import BaseModel


class Auth(BaseModel):
    email: str
    password: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), "static")
templates = Jinja2Templates(directory="templates")
db = Database()


@app.get("/login", response_class=HTMLResponse)
async def login_html(request: Request):
    return templates.TemplateResponse(request, "login.html")


@app.post("/login")
async def login(auth: Auth):
    print(auth.email, auth.password)


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(request, "register.html")


async def main():
    server = uvicorn.Server(uvicorn.Config(app))
    await server.serve()


if __name__ == "__main__":
    db.init_tables()
    asyncio.run(main())
