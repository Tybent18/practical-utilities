from collections import deque


class StressEngine:
    def __init__(self):
        self.stress_level = 0.2
        self.load_history = deque(maxlen=20)

        self.capacity = 1.0
        self.recovery_rate = 0.03

    def compute_load(self, inputs):
        return sum(inputs) / max(1, len(inputs))

    def update_stress(self, loads):
        load = self.compute_load(loads)
        self.load_history.append(load)

        self.stress_level += load * 0.1

        if self.stress_level > self.capacity:
            self.stress_level += 0.05  # overload spike

        return self.stress_level

    def recover(self):
        self.stress_level -= self.recovery_rate
        self.stress_level = max(0, self.stress_level)

    def stress_response(self):
        if self.stress_level > 0.7:
            return "PRIORITY MODE"
        elif self.stress_level > 0.4:
            return "FOCUSED MODE"
        return "STABLE MODE"


# Example usage
engine = StressEngine()

scenarios = [
    [0.2, 0.3, 0.4],
    [0.6, 0.7, 0.8],
    [0.9, 1.0, 0.9],
]

for loads in scenarios:
    level = engine.update_stress(loads)
    state = engine.stress_response()

    engine.recover()

    print(f"Stress: {level:.2f} | State: {state}")