from fastapi import FastAPI
from models import State, Action, StepResponse
from environment import CloudEnv

app = FastAPI()
env = CloudEnv()

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