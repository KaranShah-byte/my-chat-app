# Deployment & Debugging Log

## Bug 1: Render Build Failure (Missing Dependencies)
*   **Symptom:** Build failed on Render with `[Errno 2] No such file or directory: 'requirements.txt'`.
*   **Root Cause:** The `requirements.txt` file was not successfully pushed to the `main` branch.
*   **Resolution:** Generated file via `pip freeze > requirements.txt` and executed a forced git push.

## Bug 2: Cross-Platform Distribution Error
*   **Symptom:** `No matching distribution found for pywin32==306`.
*   **Root Cause:** `pip freeze` captured Windows-specific local packages. Render provisions Linux environments, causing the build to crash.
*   **Resolution:** Sanitized `requirements.txt` to strictly include production dependencies: `fastapi`, `uvicorn`, `websockets`.

## Bug 3: Mixed Content Protocol Rejection
*   **Symptom:** Silent failure on the frontend; F12 Console showed WebSocket connection blocked.
*   **Root Cause:** Hardcoded `ws://` protocol in JavaScript was rejected by the browser when served via Render's HTTPS.
*   **Resolution:** Implemented dynamic protocol assignment:
    `var wsProtocol = window.location.protocol === "https:" ? "wss://" : "ws://";`

## Bug 4: 404 Not Found on Root URL
*   **Symptom:** Returning `{"detail":"Not Found"}` when visiting the base URL.
*   **Root Cause:** Refactoring the WebSocket state manager accidentally removed the base HTTP route.
*   **Resolution:** Restored `@app.get("/")` utilizing `FileResponse("index.html")`.
