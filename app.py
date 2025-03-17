from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# Configure Google Gemini AI Client
client = genai.Client(
    vertexai=True,
    project="tt-sandbox-001",  # Replace with your GCP Project ID
    location="us-central1",
)

# Define AI Model
model = "gemini-2.0-flash-001"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form.get('user_input')

    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        max_output_tokens=8192,
        response_modalities=["TEXT"],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    ai_output = response.candidates[0].content.parts[0].text

    return jsonify({'output': ai_output})

if __name__ == '__main__':
    app.run(debug=True)
