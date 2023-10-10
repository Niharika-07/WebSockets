import asyncio
import websockets

async def main():
    uri = "ws://localhost:8765"  # WebSocket server address
    
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        message = "Hello, WebSocket Server!"
        await websocket.send(message)
        print(f"Sent message: {message}")
        
        # Receive and print the response from the server
        response = await websocket.recv()
        print(f"Received response: {response}")

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(main())
