# Simple WebSocket Chat App with FastAPI

This is a simple demonstration chat application built using FastAPI and WebSockets. It allows clients to connect via WebSocket and exchange messages in real-time.

## Setup

### Requirements
- Python 3.8 or later

### Installation
1. Clone this repository.
2. Navigate to the project directory.
3. Install the dependencies by running:
    ```
    pip install -r requirements.txt
    ```

## Running the App
From a main.app folder use the following command to start the FastAPI server:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The server will be accessible at `http://localhost:8000`.

## Usage
- Open your browser and navigate to `http://localhost:8000`.
- Once connected, you can send messages in the chat input field.
- Messages will be displayed in the chat area, and other connected clients will see them in real-time.

## Dependencies
- fastapi
- uvicorn
- websockets


## File Structure
- `main.py`: Contains the FastAPI application setup and WebSocket endpoints.
- `templates/index.html`: HTML template for the chat interface.
- `services.py`: Contains the ConnectionManager class responsible for managing WebSocket connections.

## Docker Setup (Optional)
You can also run the app using Docker. Ensure Docker is installed on your system.

Run docker-compose from the fastapichatwebsockets folder:
    ```
    docker build -t fastapi-websocket-chat .
    ```

The app will be accessible at `http://localhost:8000`.

Feel free to modify and extend the code as needed for your own projects!