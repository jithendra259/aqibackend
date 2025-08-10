
from flask import Flask, request, jsonify
from flask_cors import CORS
from app.gemini.geminiclient import get_gemini_client

app = Flask(__name__)
CORS(app)  # Enable CORS

client = get_gemini_client()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_input = data.get("prompt", "")

    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
