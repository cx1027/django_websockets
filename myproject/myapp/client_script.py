import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = "Django User"  # You can modify this as needed
        await websocket.send(name)
        print(f"Sent: {name}")

        greeting = await websocket.recv()
        print(f"Received: {greeting}")

# This function is no longer needed for Django integration
# asyncio.get_event_loop().run_until_complete(hello())
