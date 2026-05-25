from collections import defaultdict
import random


class AnticipationEngine:
    def __init__(self):
        self.outcome_memory = defaultdict(list)
        self.expectation_bias = 0.5

        self.prediction_strength = 0.6
        self.uncertainty_weight = 0.4

    def record_outcome(self, event, outcome_value):
        self.outcome_memory[event].append(outcome_value)

    def expected_value(self, event):
        data = self.outcome_memory[event]
        if not data:
            return 0.5
        return sum(data) / len(data)

    def anticipation_score(self, event, predicted_outcome, uncertainty):
        historical_expectation = self.expected_value(event)

        prediction_error = abs(predicted_outcome - historical_expectation)

        anticipation = (
            predicted_outcome * self.prediction_strength
        ) + (uncertainty * self.uncertainty_weight)

        anticipation += historical_expectation * 0.5
        anticipation -= prediction_error * 0.3

        return max(0, min(1, anticipation))

    def adjust_bias(self, score):
        if score > 0.7:
            self.expectation_bias += 0.05
        else:
            self.expectation_bias *= 0.99

        self.expectation_bias = max(0, min(1, self.expectation_bias))


# Example usage
engine = AnticipationEngine()

scenarios = [
    ("Event_A", 0.8, 0.2),
    ("Event_B", 0.4, 0.6),
    ("Event_A", 0.9, 0.3),
    ("Event_C", 0.7, 0.5)
]

for event, predicted, uncertainty in scenarios:
    score = engine.anticipation_score(event, predicted, uncertainty)

    engine.record_outcome(event, predicted)
    engine.adjust_bias(score)

    print(f"{event} -> Anticipation Score: {score:.3f}")