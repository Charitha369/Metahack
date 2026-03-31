from pydantic import BaseModel
from typing import List

class State(BaseModel):
    active_servers: int
    current_traffic: float
    cpu_usage: float

class Action(BaseModel):
    change: int  # 0: Stay, 1: Add Server, 2: Remove Server

class StepResponse(BaseModel):
    observation: State
    reward: float
    done: bool