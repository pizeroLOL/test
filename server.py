from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi import responses as rsp
from main import main

main(is_server=True)
time = datetime.now()

app = FastAPI()
app.mount("/files", StaticFiles(directory="public"), name="public")


@app.get("/")
async def root():
    return rsp.RedirectResponse("/files/index.html")


@app.get("/update")
async def update():
    global time
    now = datetime.now()
    one_hour = 3600
    if (now-time).seconds < one_hour:
        return "一小时内已更新"
    time = now
    main.main(is_server=True)
    return rsp.RedirectResponse("/files/index.html")
