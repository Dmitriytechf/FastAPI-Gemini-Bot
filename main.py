from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google_request import get_quick_response, get_chat_response
from fastapi.responses import PlainTextResponse


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

    return PlainTextResponse(content=f'''
    <div class="space-y-4">
        <div class="flex justify-end">
            <div class="bg-blue-500 text-white rounded-2xl rounded-br-none px-4 py-3 max-w-[80%]">
                <p class="text-sm">{message}</p>
            </div>
        </div>

        <div class="flex justify-start">
            <div class="bg-blue-100 border border-blue-200 rounded-2xl rounded-bl-none px-4 py-3 max-w-[80%]">
                <p class="text-gray-800 text-sm">{response}</p>
            </div>
        </div>
    </div>
    ''')


@app.post("/process-chat")
async def process_message(request: Request):
    data = await request.form()
    message = data["input-chat"]
    response = get_chat_response(message)

    return PlainTextResponse(content=f'''
    <div class="space-y-4">
        <div class="flex justify-end">
            <div class="bg-green-500 text-white rounded-2xl rounded-br-none px-4 py-3 max-w-[80%]">
                <p class="text-sm">{message}</p>
            </div>
        </div>
        
        <div class="flex justify-start">
            <div class="bg-green-100 border border-green-200 rounded-2xl rounded-bl-none px-4 py-3 max-w-[80%]">
                <p class="text-gray-800 text-sm">{response}</p>
            </div>
        </div>
    </div>
    ''')
