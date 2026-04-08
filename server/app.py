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

def main():
    import uvicorn
    # MUST be 0.0.0.0 to be visible outside the container
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()