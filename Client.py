import asyncio
import websockets

async def main():
    while True:
        try:
            async with websockets.connect("ws://localhost:8765") as websocket:
                message = input("You: ")
                await websocket.send(message)
                await websocket.close()
                break
        except:
            pass

asyncio.run(main())