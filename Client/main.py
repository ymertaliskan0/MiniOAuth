from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Client App")

# The URL of your Authorization Server
AUTH_SERVER_URL = "http://localhost:8000/login"
CLIENT_ID = "Test_client"

@app.get("/", response_class=HTMLResponse)
async def home():
    # A simple page with a link that sends the user to the Auth Server
    return f"""
    <html>
        <body>
            <h2>Client Application</h2>
            <p>Click below to authenticate via MiniOAuth.</p>
            <a href="{AUTH_SERVER_URL}?client_id={CLIENT_ID}">
                <button>Login with MiniOAuth</button>
            </a>
        </body>
    </html>
    """

@app.get("/callback")
async def callback(code: str):
    # The server redirects here after a successful login
    return {"message": "Success!", "authorization_code": code}