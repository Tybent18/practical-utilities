from collections import defaultdict, deque


class TrustEngine:
    def __init__(self):
        self.trust_scores = defaultdict(lambda: 0.5)
        self.history = defaultdict(lambda: deque(maxlen=20))

        self.learning_rate = 0.1
        self.decay = 0.02

    def update_trust(self, source, outcome_match):
        """
        outcome_match: 1 if correct / reliable, 0 if wrong
        """
        self.history[source].append(outcome_match)

        avg = sum(self.history[source]) / len(self.history[source])

        # reinforce or punish based on consistency
        self.trust_scores[source] += self.learning_rate * (avg - 0.5)

        # natural decay toward uncertainty
        self.trust_scores[source] -= self.decay * (self.trust_scores[source] - 0.5)

        self.trust_scores[source] = max(0, min(1, self.trust_scores[source]))

    def get_trust(self, source):
        return self.trust_scores[source]

    def weighted_influence(self, source, signal_strength):
        return signal_strength * self.get_trust(source)


# Example usage
engine = TrustEngine()

inputs = [
    ("Sensor_A", 1),
    ("Sensor_A", 1),
    ("Sensor_A", 0),
    ("Sensor_B", 0),
    ("Sensor_B", 1),
]

for source, outcome in inputs:
    engine.update_trust(source, outcome)

print("Trust Sensor_A:", engine.get_trust("Sensor_A"))
print("Trust Sensor_B:", engine.get_trust("Sensor_B"))