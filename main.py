from scrapper import scrapper_function

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

@app.post("/scrape")
async def scrape(fbpage_name: str, posts_count: int, browser: str, host_name: str, user_name: str, password_db: str, db_name: str):
    try:
        scrapper_function(fbpage_name, posts_count, browser, host_name, user_name, password_db, db_name)
        return {"message": "Scraping complete."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

