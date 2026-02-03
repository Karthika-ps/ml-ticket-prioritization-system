# ML Ticket Prioritization System

This repository contains an applied machine learning system for
automatically prioritizing support tickets based on textual content.

The system is designed using a **multi-service architecture** and
demonstrates how machine learning models can be deployed as independent
services and orchestrated using Docker.

---

## Project Overview

The system classifies incoming support tickets into priority levels
(Low, Medium, High) using a trained machine learning model and provides
human-readable explanations for the predictions.

The project is implemented in two phases:

- **Phase 1 (Kaggle):**
  - Data preparation
  - Model training and evaluation
  - Prototype-level integration

- **Phase 2 (This Repository):**
  - Multi-service architecture
  - ML inference service
  - LLM-based explanation service
  - API gateway
  - Docker-based deployment

---

## Architecture (Phase 2)

The system consists of three services:

1. **ML Inference Service**
   - Hosts the trained ML model
   - Provides prediction and confidence scores

2. **LLM Explanation Service**
   - Generates human-readable explanations for predictions

3. **API Gateway**
   - Serves as the single public entry point
   - Orchestrates communication between services

---

## Status

🚧 **Under active development**  
Currently implementing **ML Inference Service (Step 2.1)**.
