from collections import defaultdict


class ConfidenceEngine:
    def __init__(self):
        self.accuracy_memory = defaultdict(list)
        self.base_confidence = 0.5

        self.learning_rate = 0.05
        self.overconfidence_penalty = 0.1
        self.underconfidence_boost = 0.05

    def record_outcome(self, prediction, actual):
        error = abs(prediction - actual)
        self.accuracy_memory["global"].append(1 - error)

    def reliability_score(self):
        data = self.accuracy_memory["global"]
        if not data:
            return self.base_confidence
        return sum(data) / len(data)

    def confidence(self, prediction_uncertainty):
        reliability = self.reliability_score()

        confidence = reliability * (1 - prediction_uncertainty)

        if confidence > 0.8:
            confidence -= self.overconfidence_penalty
        elif confidence < 0.3:
            confidence += self.underconfidence_boost

        return max(0, min(1, confidence))

    def adapt(self, confidence_score):
        if confidence_score > 0.75:
            self.learning_rate += 0.01
        else:
            self.learning_rate *= 0.99


# Example usage
engine = ConfidenceEngine()

trials = [
    (0.9, 1.0, 0.1),
    (0.4, 0.3, 0.3),
    (0.7, 0.8, 0.2),
]

for prediction, actual, uncertainty in trials:
    engine.record_outcome(prediction, actual)

    conf = engine.confidence(uncertainty)
    engine.adapt(conf)

    print(f"Prediction: {prediction} | Confidence: {conf:.3f}")