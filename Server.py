import asyncio
import websockets

async def start_server():
    global message_received
    async def handle(websocket, path):
        message_received = await websocket.recv()
        print(f"{message_received}")
        asyncio.get_event_loop().stop()

    server = await websockets.serve(handle, "localhost", 8765)
    await server.wait_closed()

    return "Server has stopped."

try:
    message_received = asyncio.run(start_server())
    print(f"Message received: {message_received}")
except:
    pass
