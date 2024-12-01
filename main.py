from parser import parser
import os
import subprocess
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

        with open("./interface_output.py", "w") as python_output:
            python_output.write(output)

        result = subprocess.run(
            ["python", "interface_output.py"], capture_output=True, text=True
        )
        os.remove("interface_output.py")
        std_out_lines = [str(line) for line in result.stdout.splitlines()]

        return templates.TemplateResponse(
            request=request,
            name="code-input.html",
            context={
                "code_output": output,
                "previous_code": code,
                "std_out": std_out_lines,
            },
        )
    except Exception as e:
        print("error", e)
        error = ErrorTranslator(e).read_error()
        return templates.TemplateResponse(
            request=request,
            name="code-input.html",
            context={
                "code_output": error,
                "previous_code": code,
            },
        )


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog="bahia_lang")
    arg_parser.add_argument("filename")
    args = arg_parser.parse_args()

    with open(args.filename) as program:
        lines = program.readlines()
        output = parser.parse("\n".join(lines))

    print("Python output:")
    print(output)

    with open("./output.py", "w") as python_output:
        python_output.write(output)

    print("Stdout:")
    subprocess.run(["python", "output.py"])
