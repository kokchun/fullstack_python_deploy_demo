from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def show_data():
    return {"data": "cool fake data"}