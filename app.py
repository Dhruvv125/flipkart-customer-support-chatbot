from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


# ===========================
# Home Page
# ===========================

@app.route("/")
def home():

    return render_template("index.html")


# ===========================
# Chat API
# ===========================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "")

    reply = get_response(message)

    return jsonify({

        "reply": reply

    })


# ===========================
# Run Flask Server
# ===========================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
    