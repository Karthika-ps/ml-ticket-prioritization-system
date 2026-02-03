from flask import Flask, request, jsonify
import joblib
import os

# --------------------------------------------------
# App initialization
# --------------------------------------------------
app = Flask(__name__)

# --------------------------------------------------
# Load ML artifacts
# --------------------------------------------------
MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")

model_path = os.path.join(MODEL_DIR, "ticket_priority_model.pkl")
vectorizer_path = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")

priority_model = joblib.load(model_path)
tfidf_vectorizer = joblib.load(vectorizer_path)

# --------------------------------------------------
# Health check endpoint
# --------------------------------------------------
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ML service is running"}), 200

# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict_priority():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in request"}), 400

    ticket_text = data["text"]

    # Vectorize input text
    vectorized_text = tfidf_vectorizer.transform([ticket_text])

    # Predict priority
    predicted_priority = priority_model.predict(vectorized_text)[0]

    # Predict confidence scores
    probabilities = priority_model.predict_proba(vectorized_text)[0]

    confidence = {
        label: float(prob)
        for label, prob in zip(priority_model.classes_, probabilities)
    }

    response = {
        "priority": predicted_priority,
        "confidence": confidence
    }

    return jsonify(response), 200

# --------------------------------------------------
# Run locally (for development only)
# --------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
