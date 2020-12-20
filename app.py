import os
import shutil
import shortuuid

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from predict import predict_height_weight_BMI

isprod = os.environ.get('prod', False)


if (isprod):
    app = FastAPI(docs_url=None, redoc_url=None)
    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["POST"],
        allow_headers=["*"],
    )

else:
    app = FastAPI()
    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["POST"],
        allow_headers=["*"],
    )


@app.post("/getbmi/")
async def create_upload_file(file: UploadFile = File(...)):

    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if (allowed_file(file.filename)):

        file_loc = "{}/{}_{}". \
            format("uploads", shortuuid.uuid(), file.filename)

        with open(file_loc, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        predicted = predict_height_weight_BMI(file_loc)
        return {"prediction": predicted}
    else:
        return {"error": "jpeg image only"}
