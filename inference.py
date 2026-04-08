from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from server.environment import CloudEnv
from server.app import app

@app.get("/",include_in_schema=False)
def homepage():
    return RedirectResponse(url='/docs')

if __name__ == "__main__":
    import uvicorn
    # MUST be 0.0.0.0 to be visible outside the container
    uvicorn.run(app, host="0.0.0.0", port=7860)