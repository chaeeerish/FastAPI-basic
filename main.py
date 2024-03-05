from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def 작명():
    return 'hello'

@app.get("/data")
def 작명():
    return {'hello' : 'data'}

from fastapi.responses import FileResponse

@app.get("/file")
def 작명():
    return FileResponse('index.html')

from pydantic import BaseModel
class Model(BaseModel):
    name :str
    phone :int

@app.post("/send")
async def 작명(data : Model):
    print(data)
    return '전송완료'