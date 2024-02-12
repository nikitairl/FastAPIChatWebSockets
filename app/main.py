from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates

from services import ConnectionManager

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


con_manager = ConnectionManager()


@app.get("/")
async def get():
    return templates.TemplateResponse("index.html", {"request": {}})


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await con_manager.connect(websocket)
    try:
        async for data in websocket.iter_text():
            await con_manager.send_personal_message(
                f"+++ You wrote: {data}",
                websocket
            )
            print(websocket)
            await con_manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        con_manager.disconnect(websocket)
        await con_manager.broadcast(f"Client #{client_id} has left the chat")
