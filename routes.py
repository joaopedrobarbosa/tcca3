from fastapi import FastAPI, Request
from parser import parser
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="code-input.html", context={}
    )

@app.post("/", response_class=HTMLResponse)
async def compile(request: Request):
    code = await request.form()
    code = code["codeInput"]
    try:
        output = parser.parse(code)
        if not output:
            raise Exception('Invalid Syntax')
        print('output', output)
        return templates.TemplateResponse(
        request=request, name="code-input.html", context={"codeOutput": output, "previousCode": code}
    )
    except Exception as e:
        print('error', e)
        return templates.TemplateResponse(
            request=request, name="code-input.html", context={"codeOutput": 'Invalid Syntax'}
        )
