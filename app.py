from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="font-family:sans-serif; text-align:center; margin-top:100px;">
            <h1>🚀 My Automated DevOps Website</h1>
            <p>Built from scratch and deployed automatically!</p>
        </body>
    </html>
    """
