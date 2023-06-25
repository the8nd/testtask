from fastapi import FastAPI, UploadFile
import shutil
import os

app = FastAPI()


@app.post("/userupload/{directoryname}")
async def upload_file(directoryname: str, file: UploadFile):
    try:
        os.mkdir(f"users/{directoryname}")
        with open(f"users/{directoryname}/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            return {f"{file.filename} successfully uploaded"}
    except FileExistsError:
        if os.path.exists(f"users/{directoryname}/{file.filename}"):
            msg = {f"{file.filename} successfully updated"}
        else:
            msg = f"{file.filename} successfully uploaded"
        with open(f"users/{directoryname}/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return msg

