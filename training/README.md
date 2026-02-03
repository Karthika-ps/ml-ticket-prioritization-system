## Training

Model training is performed in Kaggle due to dataset size and memory requirements.

Dataset:
https://www.kaggle.com/datasets/davidshinn/github-issues

The dataset is mounted automatically by Kaggle and is not downloaded programmatically.

The training script outputs:
- ticket_priority_model.pkl
- tfidf_vectorizer.pkl

These artifacts are used by the ML inference service.
