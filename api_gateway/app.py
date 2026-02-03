from flask import Flask, request, jsonify, render_template

import requests

app = Flask(__name__)

ML_SERVICE_URL = "http://127.0.0.1:8000/predict"
LLM_SERVICE_URL = "http://127.0.0.1:7000/explain"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/ui-analyze", methods=["POST"])
def ui_analyze():
    ticket_text = request.form.get("text")

    # Call ML service
    ml_response = requests.post(
        ML_SERVICE_URL,
        json={"text": ticket_text},
        timeout=5
    )
    ml_result = ml_response.json()

    # Call LLM service
    llm_response = requests.post(
        LLM_SERVICE_URL,
        json={
            "text": ticket_text,
            "priority": ml_result["priority"],
            "confidence": ml_result["confidence"]
        },
        timeout=5
    )
    explanation = llm_response.json()["explanation"]

    result = {
        "priority": ml_result["priority"],
        "confidence": ml_result["confidence"],
        "explanation": explanation
    }

    return render_template("index.html", result=result)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "API gateway running"}), 200


@app.route("/analyze", methods=["POST"])
def analyze_ticket():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    ticket_text = data["text"]

    # --------------------------------------------------
    # Call ML service
    # --------------------------------------------------
    ml_response = requests.post(
        ML_SERVICE_URL,
        json={"text": ticket_text},
        timeout=5
    )

    ml_result = ml_response.json()

    # --------------------------------------------------
    # Call LLM service
    # --------------------------------------------------
    llm_response = requests.post(
        LLM_SERVICE_URL,
        json={
            "text": ticket_text,
            "priority": ml_result["priority"],
            "confidence": ml_result["confidence"]
        },
        timeout=5
    )

    explanation = llm_response.json()["explanation"]

    # --------------------------------------------------
    # Final response
    # --------------------------------------------------
    return jsonify({
        "priority": ml_result["priority"],
        "confidence": ml_result["confidence"],
        "explanation": explanation
    }), 200

def security_override(text: str) -> bool:
    security_keywords = [
        "admin",
        "unauthorized",
        "access",
        "security",
        "vulnerability",
        "exposed",
        "private",
        "leak",
        "breach"
    ]

    text_lower = text.lower()
    return any(keyword in text_lower for keyword in security_keywords)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
