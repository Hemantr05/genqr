import traceback
from uuid import UUID, uuid4
from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from starlette.responses import StreamingResponse

# from utils import create_qr, img2bytes, decode_qr
from database_ops import firestore_delete, firestore_read, firestore_write
from utils import create_qr, img2bytes

app = FastAPI()

@app.get('/')
async def root():
    content = {"status": "Ok"}
    return JSONResponse(content=content)

@app.post('/api/v1/qr/create')
async def create(content: str):
    resp = {"id": None}
    try:
        image = create_qr(content)
        img_bytes = img2bytes(image)
        resp["id"] = firestore_write(img_bytes)
        return JSONResponse(content=resp, status_code=201)
    except Exception as e:
        print(traceback.print_exc(), flush=True)
        return JSONResponse(content={"error message": str(e)}, status_code=500)

@app.get('/api/v1/qr/fetch')
async def retrieve_qr(id: Optional[UUID] = str(id)):
    try:
        image = firestore_read(id)
        return StreamingResponse(content=image, status_code=200, media="image/png")
    except Exception as e:
        print(traceback.print_exc(), flush=True)
        return JSONResponse(content={"error message": str(e)}, status_code=500)

@app.delete("/api/v1/qr/delete")
async def delete_qr(id: Optional[UUID] = str(id)):
    resp = {"id": None}
    try:
        firestore_delete(id)
        resp["id"] = f'{id} deleted!'
        return JSONResponse(content=resp, status_code=204)
    except Exception as e:
        print(traceback.print_exc(), flush=True)
        return JSONResponse(content={"error message": str(e)}, status_code=500)

# @app.get('/api/v1/decode')
# async def decode(image: UploadFile = File(...)):
#     resp = {"message": None}
#     try:
#         message = decode_qr(image)
#         if message:
#             resp["message"] = message
#             return JSONResponse(content=resp, status_code=200)
#         return JSONResponse(content=resp, status_code=404)
#     except Exception as e:
#         print(traceback.print_exc(), flush=True)
#         return JSONResponse(content={"error message": str(e)}, status_code=500)    