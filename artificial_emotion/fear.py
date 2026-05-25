import math
from collections import defaultdict


class FearEngine:
    def __init__(self):
        self.threat_memory = defaultdict(list)

        self.base_fear = 0.2
        self.stress = 0.3
        self.sensitivity = 1.0

        self.avoidance_bias = 0.4
        self.decay = 0.98

    def threat_assessment(self, stimulus_threat, uncertainty):
        return stimulus_threat * (1 + uncertainty)

    def memory_bias(self, source):
        if source not in self.threat_memory:
            return 0
        return sum(self.threat_memory[source]) / len(self.threat_memory[source])

    def fear_signal(self, source, threat, uncertainty):
        learned_threat = self.memory_bias(source)

        risk = self.threat_assessment(threat, uncertainty)

        signal = (
            risk * self.sensitivity
        ) + learned_threat + self.stress

        signal -= self.avoidance_bias * 0.2

        return max(0, signal)

    def update_memory(self, source, threat):
        self.threat_memory[source].append(threat)

    def adapt(self, fear_level):
        if fear_level > 0.7:
            self.stress += 0.06
            self.sensitivity += 0.05

        self.stress *= self.decay
        self.sensitivity *= self.decay


# Example usage
engine = FearEngine()

inputs = [
    ("Unknown Shadow", 0.9, 0.8),
    ("Loud Noise", 0.6, 0.4),
    ("Familiar Object", 0.1, 0.2)
]

for source, threat, uncertainty in inputs:
    fear = engine.fear_signal(source, threat, uncertainty)

    engine.update_memory(source, threat)
    engine.adapt(fear)

    print(f"{source} -> Fear Level: {fear:.3f}")