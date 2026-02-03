# ML Ticket Prioritization System

This repository contains an **applied machine learning system** for
automatically prioritizing support tickets based on textual content.

The project demonstrates how a trained ML model can be deployed as an
independent service, combined with an explanation layer, and exposed
through a user-facing web interface using a **multi-service architecture**.

---

## Problem Statement

Support teams often receive large volumes of tickets with varying levels
of urgency. Manual prioritization is time-consuming and error-prone.

This system aims to:
- Automatically classify ticket priority (Low / Medium / High)
- Provide confidence scores for predictions
- Generate human-readable explanations
- Escalate security-sensitive issues using rule-based safeguards

---

## Project Phases

### Phase 1 – Model Development (Kaggle)

Performed in Kaggle due to dataset size and memory requirements.

Includes:
- Dataset exploration and preprocessing
- Weakly supervised label generation
- Model training and evaluation
- Export of trained model artifacts

> Training is **not** performed locally.

---

### Phase 2 – System Implementation (This Repository)

Focuses on **deployment and system design**, not training.

Includes:
- ML inference service
- LLM-based explanation service
- API gateway with web UI
- Security-aware priority escalation
- (Upcoming) Docker-based deployment

---

## System Architecture

The system consists of three decoupled services:

1. **ML Inference Service**
   - Loads a pre-trained ML model
   - Returns priority predictions and confidence scores

2. **LLM Explanation Service**
   - Generates human-readable explanations
   - Explains both ML predictions and rule-based overrides

3. **API Gateway**
   - Single entry point for users
   - Hosts a web UI
   - Orchestrates calls to ML and LLM services

---

## Running the Application (Local)

Each service runs independently and communicates over HTTP.

### 1. Start ML Inference Service
```bash
cd ml_service
pip install -r requirements.txt
python app.py
```

### 2. Start LLM Explanation Service
```bash
cd llm_service
pip install -r requirements.txt
python app.py
```

### 3. Start API Gateway (UI)
```bash
cd api_gateway
pip install -r requirements.txt
python app.py
```

Once all services are running, open a browser and visit:

http://127.0.0.1:5000
