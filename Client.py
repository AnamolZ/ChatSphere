import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://192.168.1.65:8765") as websocket:
        message = input("You: ")
        await websocket.send(message)
        print(f"{message}")

asyncio.get_event_loop().run_until_complete(send_message())


