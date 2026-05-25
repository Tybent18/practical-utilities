from collections import defaultdict
import math


class AweEngine:
    def __init__(self):
        self.experience_memory = defaultdict(list)

        self.base_sensitivity = 0.6
        self.expansion_drive = 0.5
        self.cognitive_capacity = 1.0

    def complexity_score(self, novelty, structure, scale):
        return (novelty + structure + scale) / 3

    def vastness(self, scale, unfamiliarity):
        return scale * (1 + unfamiliarity)

    def uncertainty_load(self, prediction_error):
        return math.sqrt(max(0, prediction_error))

    def awe_intensity(self, novelty, structure, scale, uncertainty):
        comp = self.complexity_score(novelty, structure, scale)
        vast = self.vastness(scale, novelty)
        uncertainty_pressure = self.uncertainty_load(uncertainty)

        intensity = (
            comp * self.base_sensitivity +
            vast +
            uncertainty_pressure
        )

        intensity *= self.expansion_drive

        return max(0, min(1, intensity))

    def adapt_model(self, intensity):
        # awe expands capacity instead of only reinforcing
        if intensity > 0.7:
            self.cognitive_capacity += 0.05
            self.expansion_drive += 0.03
        else:
            self.expansion_drive *= 0.99

        self.cognitive_capacity = min(3.0, self.cognitive_capacity)


# Example usage
engine = AweEngine()

inputs = [
    (0.9, 0.8, 0.95, 0.4),
    (0.3, 0.4, 0.2, 0.1),
    (1.0, 0.9, 1.0, 0.8)
]

for novelty, structure, scale, uncertainty in inputs:
    score = engine.awe_intensity(novelty, structure, scale, uncertainty)

    engine.adapt_model(score)

    print(f"Awe Intensity: {score:.3f} | Capacity: {engine.cognitive_capacity:.2f}")