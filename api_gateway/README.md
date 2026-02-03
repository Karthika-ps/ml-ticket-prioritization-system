## API Gateway & UI

The API Gateway serves as the entry point for users and orchestrates
communication between the ML inference service and the LLM explanation service.

### UI Access

Once the API Gateway is running, open:

http://127.0.0.1:5000

### UI Features

- Text input for support tickets
- Automatic priority classification using ML
- Explanation generation using LLM logic
- Security-aware priority escalation for sensitive issues

### API Endpoints

- `GET /` – Web UI
- `POST /analyze` – JSON API for ticket analysis
- `GET /health` – Health check
