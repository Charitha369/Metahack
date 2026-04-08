from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from server.environment import CloudEnv
from server.app import app, main

@app.get("/",include_in_schema=False)
def homepage():
    return RedirectResponse(url='/docs')

if __name__ == "__main__":
    main()