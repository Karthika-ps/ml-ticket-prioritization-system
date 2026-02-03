from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "LLM service running"}), 200


@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()

    text = data.get("text", "")
    priority = data.get("priority", "")
    confidence = data.get("confidence", {})

    explanation = (
        f"This ticket was classified as '{priority}' priority "
        f"because the language indicates system impact or urgency. "
        f"The model assigned high confidence based on similar historical issues."
    )

    return jsonify({
        "explanation": explanation
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
