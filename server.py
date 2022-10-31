from fastapi import FastAPI
import uvicorn
from routers import pokemons, trainers, operations

app = FastAPI()

app.include_router(pokemons.router)
app.include_router(trainers.router)
app.include_router(operations.router)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
