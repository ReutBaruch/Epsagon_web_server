import json
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/spans")
async def get_spans():
    with open('./spans.json') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)