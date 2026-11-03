# Declaration of AI & External Tools

## AI Assistance
This project was developed with the assistance of an AI thought partner (Google Gemini). The AI was utilized for:
* **System Architecture:** Planning the transition from a global broadcast model to a dictionary-based partitioned room structure.
* **Debugging:** Identifying and resolving Render build errors, cross-platform dependency issues (pywin32), and WebSocket mixed-content protocol mismatches (ws:// vs wss://).
* **Code Scaffolding:** Drafting the FastAPI WebSocket backend, designing the Discord-inspired CSS/UI, and integrating Firebase Phone Auth logic.

## External Libraries & Cloud Services
* **FastAPI & Uvicorn:** Utilized for building the asynchronous backend and serving WebSocket connections.
* **Google Firebase:** Employed for the Phone Authentication API to handle SMS OTPs securely.
* **Render:** Used as the Platform-as-a-Service (PaaS) for deploying the application with automated SSL/TLS certificates.
* **Vanilla JavaScript:** Used for the frontend client logic without reliance on heavy external frameworks.
