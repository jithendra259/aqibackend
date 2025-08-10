import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from app.gemini.geminiclient import get_gemini_client

# Load environment variables from .env file
load_dotenv()  # Ensure this is called early to load variables

# Debugging: Check if GEMINI_API_KEY is loaded
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Gemini Client
client = get_gemini_client()

@app.route("/generate", methods=["POST"])
def generate():
    """
    Endpoint to generate content using Gemini's model.
    """
    data = request.get_json()
    user_input = data.get("prompt", "")
    
    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        # Call the Gemini API
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
