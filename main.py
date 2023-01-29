from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "What is recommender syster in two word? Suggestion engine."}