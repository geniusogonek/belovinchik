import uvicorn
import asyncio

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models import LoginData, RegisterData
from database import Database
from jwt_utils import decode_jwt, generate_jwt


db = Database()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), "static")
templates = Jinja2Templates(directory="templates")


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/login", response_class=HTMLResponse)
async def login_html(request: Request):
    return templates.TemplateResponse(request, "login.html")


@app.post("/login", response_class=JSONResponse)
async def login(login_data: LoginData):
    if db.log_user(login_data):
        jwt = {"jwt": generate_jwt(login_data.email, login_data.password)}
        return JSONResponse(jwt)
    return False


@app.get("/register", response_class=HTMLResponse)
async def register_html(request: Request):
    return templates.TemplateResponse(request, "register.html")


@app.post("/register")
async def register(register_data: RegisterData):
    if db.reg_user(register_data):
        return generate_jwt(register_data.email, register_data.password)
    return False


@app.get("/check")
async def check(request: Request):
    return HTMLResponse(f"<h1>{'YES' if validate(request.cookies) else 'NO'}</h1>")


def validate(cookies):
    print(cookies)
    data = decode_jwt(cookies.get("Authorization"))
    if data:
        email, password = data["email"], data["password"]
        return db.log_user(LoginData(email=email, password=password))
    return False

async def main():
    server = uvicorn.Server(uvicorn.Config(app))
    await server.serve()


if __name__ == "__main__":
    db.init_tables()
    asyncio.run(main())
