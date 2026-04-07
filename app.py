from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from models import State, Action, StepResponse
from environment import CloudEnv

app = FastAPI()
env = CloudEnv()

@app.get("/")
def homepage():
    return RedirectResponse(url='/docs')

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step", response_model=StepResponse)
def step(action: Action):
    obs, reward, done = env.step(action.change)
    return {"observation": obs, "reward": reward, "done": done}

@app.get("/state")
def get_state():
    return env._get_state()

if __name__ == "__main__":
    import uvicorn
    # MUST be 0.0.0.0 to be visible outside the container
    uvicorn.run(app, host="0.0.0.0", port=7860)