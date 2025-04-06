from flask import Flask, request, jsonify
from utils.recommender import load_data, recommend_assessments

app = Flask(__name__)
data = load_data()

@app.route('/')
def home():
    return "SHL Recommender API is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    content = request.get_json()
    query = content.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    results = recommend_assessments(query, data)
    response = []

    for _, row in results.iterrows():
        response.append({
            "assessment_name": row["assessment_name"],
            "description": row["description"],
            "skills": row["skills"],
            "test_type": row["test_type"],
            "duration": row["duration"],
            "recommended_roles": row["recommended_roles"],
            "job_level": row["job_level"]
        })

    return jsonify({
        "query": query,
        "recommendations": response
    })

if __name__ == "__main__":
    app.run(debug=True)