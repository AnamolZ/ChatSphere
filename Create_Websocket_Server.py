import asyncio
import websockets

async def handle(websocket, path):
    message = await websocket.recv()
    print(f"Received message: {message}")

start_server = websockets.serve(handle, "172.17.112.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
