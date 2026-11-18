from fastapi import FastAPI
from app.routers import movies



app = FastAPI()

# bring in all routes from movies router file
app.include_router(movies.router)



@app.get("/")
def health_check():

    return "I'm healthy mister"