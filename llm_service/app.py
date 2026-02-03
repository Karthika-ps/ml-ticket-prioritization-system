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

    override = data.get("override", False)

    if override:
        explanation = (
            f"This ticket was escalated to '{priority}' priority due to potential "
            f"security or unauthorized access concerns, which require immediate attention."
        )
    else:
        explanation = (
            f"This ticket was classified as '{priority}' priority "
            f"based on patterns learned from historical support tickets."
        )


    return jsonify({
        "explanation": explanation
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
