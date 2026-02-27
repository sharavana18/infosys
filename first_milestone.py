from fastapi import FastAPI, WebSocket
import uvicorn
app = FastAPI()
@app.get("/")
async def home():
    return {"message": "WebSocket Chat Server Running"}
@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome to the WebSocket server!")
    try:
        while True:
            message = await websocket.receive_text()
            if message.lower() == "bye":
                await websocket.send_text("Goodbye!")
                break
            reply = f"Server received: {message}"
            await websocket.send_text(reply)
    except Exception:
        print("Client disconnected")
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)