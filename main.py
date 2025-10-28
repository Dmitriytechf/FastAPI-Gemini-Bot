from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google_request import get_quick_response, get_chat_response
from fastapi.responses import JSONResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="base.html")


@app.post("/process-message")
async def process_message(request: Request):
    data = await request.form()
    message = data["user-input"]
    response = get_quick_response(message)

    return response


@app.post("/process-chat")
async def process_message(request: Request):
    data = await request.form()
    message = data["input-chat"]
    response = get_chat_response(message)

    return response
