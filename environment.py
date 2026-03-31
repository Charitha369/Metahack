import random

class CloudEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.active_servers = 1
        self.current_traffic = 10.0
        self.done = False
        return self._get_state()

    def _get_state(self):
        # CPU usage increases if traffic is high and servers are low
        cpu = (self.current_traffic / (self.active_servers * 50)) * 100
        return {"active_servers": self.active_servers, "current_traffic": self.current_traffic, "cpu_usage": min(cpu, 100.0)}

    def step(self, action):
        # logic for action
        if action == 1: # Add
            self.active_servers += 1
        elif action == 2 and self.active_servers > 1: # Remove
            self.active_servers -= 1
        
        # Simulate traffic change
        self.current_traffic = max(10.0, self.current_traffic + random.uniform(-20, 50))
        
        state = self._get_state()
        reward = self._calculate_reward(state)
        
        return state, reward, self.done

    def _calculate_reward(self, state):
        cpu = state["cpu_usage"]
        # REWARD LOGIC:
        if 40 <= cpu <= 80:
            return 1.0  # Perfect balance!
        elif cpu > 90:
            return -1.0 # Website is crashing! (Penalty)
        else:
            return 0.2  # Too many servers, wasting money (Low reward)