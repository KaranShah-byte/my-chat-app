# Architecture & State Management

## Tech Stack
*   **Backend:** Python, FastAPI, Uvicorn
*   **Frontend:** HTML5, CSS3, Vanilla JS
*   **Infrastructure:** Render (PaaS)
*   **Authentication:** Firebase Phone Auth (OTP)

## Room Partitioning Logic (Dictionary-Based State)
To transition from a global broadcast to isolated chat rooms, the backend utilizes a hash map implementation. The state manager maps string room names to arrays of active WebSocket client connections.

```python
# Dictionary maps room names to active client lists
# Time Complexity for room lookup: O(1)
rooms: dict[str, list[WebSocket]] = {}

@app.websocket("/ws/{room_name}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, username: str):
    await websocket.accept()
    if room_name not in rooms:
        rooms[room_name] = []
    rooms[room_name].append(websocket)
```

## Security & Routing
*   **Mixed Content Handling:** Implemented environment-aware JavaScript routing to enforce `wss://` (secure WebSockets) when served over Render's automatic HTTPS.
*   **Identity Verification:** Replaced anonymous entry with Firebase Phone Auth, passing the verified telecom number to the FastAPI backend as the `{username}` parameter.
