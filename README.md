# ML Ticket Prioritization System

This repository contains an **applied machine learning system** for automatically prioritizing support tickets based on textual content.

The project demonstrates how a trained ML model can be deployed as an **independent inference service**, combined with an **LLM-based explanation layer**, and exposed through a **user-facing web interface** using a **multi-service, Dockerized architecture**.

The focus of this project is **applied AI / ML engineering**, system design, and service orchestration — not model research.

---

## Problem Statement

Support and IT teams often receive large volumes of tickets with varying urgency levels.  
Manual prioritization is time-consuming, inconsistent, and prone to missing critical or security-sensitive issues.

This system aims to:

- Automatically classify ticket priority (**Low / Medium / High**)
- Provide confidence scores for predictions
- Generate human-readable explanations
- Escalate security-sensitive issues using rule-based safeguards
- Demonstrate production-style ML service deployment

---

## Project Phases

### Phase 1 – Model Development (Kaggle)

Model development was performed in **Kaggle** due to dataset size and memory constraints.

This phase includes:

- Dataset exploration and preprocessing
- Weakly supervised label generation
- Model training and evaluation
- Export of trained model artifacts

> **Note:**  
> Training is intentionally **not performed locally** and is not part of the runtime system.

---

### Phase 2 – System Implementation (This Repository)

This repository focuses on **deployment and system design**, not training.

It includes:

- ML inference service
- LLM-based explanation service
- API gateway with a web-based UI
- Security-aware priority escalation logic
- Docker-based multi-service orchestration

---

## System Architecture

The system is composed of **three decoupled services**:

### 1. ML Inference Service
- Loads a pre-trained machine learning model
- Accepts ticket text as input
- Returns:
  - predicted priority
  - confidence scores per class

### 2. LLM Explanation Service
- Generates human-readable explanations
- Explains:
  - ML predictions
  - rule-based overrides (e.g., security escalation)

### 3. API Gateway
- Single public entry point
- Hosts a simple web UI
- Orchestrates communication between ML and LLM services
- Applies additional safety and escalation rules

Only the **API Gateway** is externally exposed.  
ML and LLM services remain **internal-only**.

---

## Running the Application (Docker – Recommended)

The system is designed to be run using **Docker Compose**.

### Prerequisites
- Docker
- Docker Compose

### Start the system

From the project root:

```bash
docker compose up --build
```

Once all services are running, open a browser and visit:
http://127.0.0.1:5000

You can then enter a support ticket description and receive:
- priority classification
- confidence scores
- a natural-language explanation

## Running Without Docker (Development Only)

Each service can be run independently for development or debugging purposes.

### 1. ML Inference Service
```bash
cd ml_service
pip install -r requirements.txt
python app.py
```
### 2. LLM Explanation Service
```bash
cd llm_service
pip install -r requirements.txt
python app.py
```
### 3. API Gateway (UI)
```bash
cd api_gateway
pip install -r requirements.txt
python app.py
```

Then open:
http://127.0.0.1:5000

Note:
The Docker-based approach is the intended and recommended way to run the system.

## Repository Structure
```text
ml-ticket-prioritization-system/
│
├── api_gateway/        # UI + orchestration layer
├── ml_service/         # ML inference service
├── llm_service/        # LLM explanation service
├── training/           # Kaggle-only training scripts
├── data/               # (Optional) local data utilities
├── docker-compose.yml  # Multi-service orchestration
└── README.md
```
## Key Takeaways

- Demonstrates applied ML engineering, not research modeling
- Clean separation between training and inference
- Multi-service architecture with clear service boundaries
- Dockerized deployment suitable for real-world systems
- Combines ML predictions with LLM explanations
- Includes security-aware escalation logic

## Future Improvements

- Authentication and role-based access control
- Streaming or async ticket ingestion
- Monitoring and logging integration
- Model versioning and rollout strategies
- CI/CD pipeline for automated builds
