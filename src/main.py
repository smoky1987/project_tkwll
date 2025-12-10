import uvicorn
from fastapi import FastAPI
from src.config import  settings
from src.database import create_tables

app = FastAPI(title = "PRJ_TKWLL",version="0.0.1")

print(settings.DATABASE_URL)

@app.on_event("startup")
async def startup():
    await create_tables()


@app.get("/")
def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)