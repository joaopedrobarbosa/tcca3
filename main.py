from parser import parser
import argparse
from fastapi import FastAPI, Request
from error_translator import ErrorTranslator
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
            raise Exception("Invalid Syntax")
        return templates.TemplateResponse(
            request=request,
            name="code-input.html",
            context={"codeOutput": output, "previousCode": code},
        )
    except Exception as e:
        print("error", e)
        error = ErrorTranslator(e).read_error()
        return templates.TemplateResponse(
            request=request, name="code-input.html", context={"codeOutput": error}
        )


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog="bahia_lang")
    arg_parser.add_argument("filename")
    args = arg_parser.parse_args()

    with open(args.filename) as program:
        lines = program.readlines()
        output = parser.parse("\n".join(lines))
        print(output)

    with open("./output.py", "w") as py_output:
        py_output.write(output)
