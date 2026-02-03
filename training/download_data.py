import os
from kaggle.api.kaggle_api_extended import KaggleApi

DATA_DIR = "../data"
DATASET = "github-issues/github_issues"

os.makedirs(DATA_DIR, exist_ok=True)

def download_dataset():
    api = KaggleApi()
    api.authenticate()   # uses KAGGLE_API_TOKEN env var

    print("Downloading dataset from Kaggle...")
    api.dataset_download_files(
        DATASET,
        path=DATA_DIR,
        unzip=True
    )
    print("Download complete.")

if __name__ == "__main__":
    download_dataset()
