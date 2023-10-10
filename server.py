import asyncio
import websockets

# Define a function to handle incoming WebSocket connections
async def handle_websocket(websocket, path):
    try:
        async for message in websocket:
            # Handle messages received from the client
            print(f"Received message: {message}")
            
            # Send a response back to the client
            response = f"Server received: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedError:
        pass

# Start the WebSocket server
start_server = websockets.serve(handle_websocket, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
