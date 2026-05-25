from collections import defaultdict, deque


class LonelinessEngine:
    def __init__(self):
        self.connection_map = defaultdict(int)
        self.feedback_history = deque(maxlen=20)

        self.loneliness = 0.2
        self.resonance_threshold = 0.5
        self.decay = 0.95

    def update_feedback(self, source, response_strength):
        self.connection_map[source] += 1 if response_strength > 0 else 0
        self.feedback_history.append(response_strength)

    def resonance(self):
        if not self.feedback_history:
            return 0
        return sum(self.feedback_history) / len(self.feedback_history)

    def compute_loneliness(self):
        avg_resonance = self.resonance()
        connection_density = sum(self.connection_map.values())

        deficit = 1 - avg_resonance
        isolation = 1 / (1 + connection_density)

        self.loneliness += deficit * isolation
        self.loneliness *= self.decay

        return max(0, min(1, self.loneliness))

    def behavior_state(self):
        if self.loneliness > 0.7:
            return "SEEK CONNECTION"
        elif self.loneliness > 0.4:
            return "LOW RESONANCE"
        return "STABLE"


# Example usage
engine = LonelinessEngine()

inputs = [
    ("Agent_A", 0.0),
    ("Agent_A", 0.1),
    ("Agent_B", 0.8),
    ("Agent_C", 0.0),
]

for source, response in inputs:
    engine.update_feedback(source, response)
    level = engine.compute_loneliness()

    print(source, "Loneliness:", round(level, 3), "State:", engine.behavior_state())