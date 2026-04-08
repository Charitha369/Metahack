from fastapi import FastAPI
from server.environment import CloudEnv
from server.models import Action, StepResponse

app = FastAPI(title="Meta OpenEnv Cloud Environment")
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
    return env.state