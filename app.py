from fastapi import FastAPI
from pydantic import BaseModel
from model import AssessmentRecommender
from utils import load_assessments

app = FastAPI()

df = load_assessments()
recommender = AssessmentRecommender(df)

class QueryRequest(BaseModel):
    text: str

@app.post("/recommend")
def get_recommendations(request: QueryRequest):
    results = recommender.recommend(request.text)
    return results.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
