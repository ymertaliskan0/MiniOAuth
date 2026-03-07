from fastapi import FastAPI

app = FastAPI(title="Authorization Server")

@app.get("/")
async def read_root():
    return {"message": "Authorization Server Running"}

