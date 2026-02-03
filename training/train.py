import os
import pandas as pd
import joblib
import kagglehub

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# --------------------------------------------------
# Download dataset using kagglehub
# --------------------------------------------------
dataset_path = kagglehub.dataset_download("davidshinn/github-issues")

csv_path = os.path.join(dataset_path, "github_issues.csv")
print("Loading dataset from:", csv_path)


# --------------------------------------------------
# Load dataset
# --------------------------------------------------
df = pd.read_csv(csv_path)

df["ticket_text"] = (
    df["issue_title"].fillna("") + " " +
    df["body"].fillna("")
)


# --------------------------------------------------
# Weak supervision (label generation)
# --------------------------------------------------
def derive_priority_label(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["crash", "error", "failure", "urgent", "broken"]):
        return "High"
    elif any(word in text for word in ["slow", "performance", "latency", "timeout"]):
        return "Medium"
    elif any(word in text for word in ["feature", "enhancement", "request"]):
        return "Low"
    else:
        return "Medium"


df["priority"] = df["ticket_text"].apply(derive_priority_label)

X = df["ticket_text"]
y = df["priority"]


# --------------------------------------------------
# Train / validation split
# --------------------------------------------------
X_train, _, y_train, _ = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# Vectorization
# --------------------------------------------------
vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    stop_words="english"
)

X_train_vec = vectorizer.fit_transform(X_train)


# --------------------------------------------------
# Model training
# --------------------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)


# --------------------------------------------------
# Save artifacts
# --------------------------------------------------
MODEL_DIR = "../ml_service/model"
os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_DIR, "ticket_priority_model.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))

print("Model and vectorizer saved successfully.")
