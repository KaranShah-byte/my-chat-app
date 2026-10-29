from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

app = FastAPI()

# NEW: This route serves your HTML page when someone visits the URL
@app.get("/")
async def get():
    return FileResponse("index.html")


# This dictionary stores all our active chat rooms
# Example: {"General": [user1, user2], "DSA-Study": [user3]}
rooms: dict[str, list[WebSocket]] = {}

@app.websocket("/ws/{room_name}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, username: str):
    # Accept the incoming connection
    await websocket.accept()
    
    # 1. If this is a new room, create it in our dictionary
    if room_name not in rooms:
        rooms[room_name] = []
    
    # 2. Add the user's WebSocket connection to this specific room
    rooms[room_name].append(websocket)
    
    try:
        # Announce to the room that a new user joined
        join_msg = f"🟢 {username} joined {room_name}."
        for client in rooms[room_name]:
            await client.send_text(join_msg)

        # Keep listening for new messages from this user
        while True:
            data = await websocket.receive_text()
            formatted_message = f"{username}: {data}"
            
            # 3. Broadcast the message ONLY to people in this exact room
            for client in rooms[room_name]:
                await client.send_text(formatted_message)
                
    except WebSocketDisconnect:
        # 4. If the user closes the tab, remove them from the room
        if websocket in rooms[room_name]:
            rooms[room_name].remove(websocket)
        
        # If the room is now empty, delete it to save server memory
        if not rooms[room_name]:  
            del rooms[room_name]
        else:
            # Otherwise, tell the remaining users that someone left
            leave_msg = f"🔴 {username} left {room_name}."
            for client in rooms[room_name]:
                await client.send_text(leave_msg)