from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List
import sqlite3  # NEW: Python's built-in database library

app = FastAPI()

# --- DATABASE SYSTEM DESIGN ---
def init_db():
    # This creates a file named chat.db in your folder
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    # SQL to create our table if it doesn't exist yet
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Run database setup when the file is loaded
init_db()

def save_message(message: str):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (content) VALUES (?)", (message,))
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    # Fetch all past messages to show newly connected users
    cursor.execute("SELECT content FROM messages ORDER BY id ASC")
    messages = cursor.fetchall()
    conn.close()
    return [msg[0] for msg in messages]
# ------------------------------

@app.get("/")
async def get():
    with open("index.html", "r") as f:
        return HTMLResponse(f.read())

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        
        # NEW: When someone connects, send them the chat history!
        history = get_chat_history()
        for msg in history:
            await websocket.send_text(msg)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            formatted_message = f"User says: {data}"
            
            # NEW: Save to disk before sending to other users
            save_message(formatted_message)
            
            await manager.broadcast(formatted_message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        leave_msg = "A user left the chat."
        save_message(leave_msg)
        await manager.broadcast(leave_msg)