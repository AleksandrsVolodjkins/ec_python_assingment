from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "What is recommender system in two word? Suggestion engine!.what is recommender system in five word? Personalized item recommendation system!."}