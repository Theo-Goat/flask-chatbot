from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure this is set!

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"response": response["choices"][0]["message"]["content"]})

    except Exception as e:
        print("🔥 Flask Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
