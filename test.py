from google import genai
from google.genai import types

def generate():
    client = genai.Client(
        vertexai=True,
        project="tt-sandbox-001",
        location="us-central1",
    )

    model = "gemini-2.0-flash-001"

    # Add a prompt inside contents
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text="Write a short story about a brave astronaut.")]
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        max_output_tokens=8192,
        response_modalities=["TEXT"],
    )

    # Stream response
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

generate()
