import gradio as gr
import requests

# Function to call the backend API
def get_recommendations(query):
    response = requests.post("http://localhost:5000/recommend", json={"query": query})
    if response.status_code == 200:
        return response.json()["recommendations"]
    else:
        return [{"error": "Failed to get recommendation"}]

# Create the Gradio UI
demo = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(label="Job Description or Query", lines=4, placeholder="Enter job role, skills, duration..."),
    outputs="json",
    title="SHL Assessment Recommendation System",
    description="Type a job query or paste a job description to get matching SHL assessments"
)

# Run the Gradio demo
demo.launch(share=True)