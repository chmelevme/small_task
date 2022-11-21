from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/url_name/")
async def read_items(name: str = 'Rekruto', message: str = 'Давай дружить'):
    html_content = f"""
    <html>
        <head>
            <title>Rekruto small test task</title>
        </head>
        <body>
            Hello {name}! {message}!
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)