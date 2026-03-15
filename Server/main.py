from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import uuid
import database
# http://127.0.0.1:8000
app = FastAPI(title="Authorization Server")

templates = Jinja2Templates(directory="templates")

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, client_id: str = ""):
    # Serve the HTML page and pass the client_id to it
    return templates.TemplateResponse("login.html", {"request": request, "client_id": client_id})
@app.get("/")
async def read_root():
    return {"message": "Authorization Server Running"}

@app.post("/login")
async def process_login(username: str = Form(...), password: str = Form(...), client_id: str = Form(...)):
    if database.users.get(username) != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if client_id not in database.clients:
        raise HTTPException(status_code=400, detail="Unknown Client")

    auth_code = str(uuid.uuid4())
    database.auth_codes[auth_code] = username

    _, redirect_url = database.clients[client_id]

    return RedirectResponse(url=f"{redirect_url}?code={auth_code}", status_code=302)

