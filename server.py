from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, responses as rsp
from main import main

main(is_server=True)
time = datetime.now()

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
app.mount("/files", StaticFiles(directory="public"), name="public")


@app.get("/")
async def root():
    return rsp.RedirectResponse("/files/index.html")


@app.get("/json")
async def get_index():
    return rsp.RedirectResponse("/files/lock.json")


@app.get("/update")
async def update():
    global time
    now = datetime.now()
    one_hour = 3600
    if (now-time).seconds < one_hour:
        return "一小时内已更新"
    time = now
    main(is_server=True)
    return rsp.RedirectResponse("/files/index.html")
