import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_data():
    data = pd.read_csv("data/assessments.csv")  # adjust path if needed
    data["embedding"] = data["description"].apply(lambda x: model.encode(x, convert_to_tensor=True))
    return data

def recommend_assessments(query, data, top_k=3):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = data["embedding"].apply(lambda x: util.pytorch_cos_sim(query_embedding, x).item())
    data = data.copy()
    data["score"] = scores
    return data.sort_values("score", ascending=False).head(top_k)