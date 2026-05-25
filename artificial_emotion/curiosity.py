import math
from collections import defaultdict


class CuriosityEngine:
    def __init__(self):
        self.memory = defaultdict(int)
        self.prediction_history = {}

        self.curiosity_drive = 1.0
        self.uncertainty_bias = 0.5
        self.exploration_pressure = 0.3

        self.decay_rate = 0.99

    def novelty_score(self, item):
        visits = self.memory[item]
        return 1 / (1 + visits)

    def prediction_error(self, item, expected, actual):
        error = abs(expected - actual)
        return error

    def information_gain(self, novelty, error, uncertainty):
        return (novelty * 1.5) + error + uncertainty

    def curiosity_signal(self, item, expected, actual, uncertainty):
        novelty = self.novelty_score(item)
        error = self.prediction_error(item, expected, actual)

        gain = self.information_gain(
            novelty,
            error,
            uncertainty
        )

        drive = (
            gain * self.curiosity_drive
        )

        drive -= self.exploration_pressure * 0.2

        return max(0, drive)

    def update_memory(self, item):
        self.memory[item] += 1

    def adapt(self, signal_strength):
        if signal_strength > 0.7:
            self.curiosity_drive += 0.05
            self.exploration_pressure += 0.03

        self.curiosity_drive *= self.decay_rate
        self.exploration_pressure *= self.decay_rate


# Example usage
engine = CuriosityEngine()

experiences = [
    ("Unknown Pattern", 0.2, 0.9, 0.8),
    ("Familiar Object", 0.8, 0.85, 0.1),
    ("Anomaly", 0.3, 0.95, 0.9)
]

for item, expected, actual, uncertainty in experiences:
    score = engine.curiosity_signal(
        item,
        expected,
        actual,
        uncertainty
    )

    engine.update_memory(item)
    engine.adapt(score)

    print(f"{item} -> Curiosity Score: {score:.3f}")