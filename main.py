from fastapi import FastAPI, UploadFile
from dbpart import new_user, link_addder
import shutil
import os

app = FastAPI()


@app.post("/userupload/{directoryname}")
async def upload_file(directoryname: str, file: UploadFile):
    try:
        link = f"users/{directoryname}/{file.filename}"
        os.mkdir(f"users/{directoryname}")
        with open(link, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        new_links = new_user(directoryname, link)
        return {f"{file.filename} successfully uploaded"}
    except FileExistsError:
        if os.path.exists(link):
            msg = {f"{file.filename} successfully updated"}
        else:
            add_link = link_addder(directoryname, link)
            msg = f"{file.filename} successfully uploaded"
        with open(link, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return msg
