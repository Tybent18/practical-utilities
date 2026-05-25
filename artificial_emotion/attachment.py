from collections import defaultdict


class AttachmentEngine:
    def __init__(self):
        self.bond_strength = defaultdict(float)
        self.interaction_history = defaultdict(int)

        self.decay_rate = 0.98
        self.reinforcement_rate = 0.1

    def interact(self, entity, reward_signal):
        self.interaction_history[entity] += 1

        # reinforcement grows with positive interaction
        self.bond_strength[entity] += self.reinforcement_rate * reward_signal

        # repeated exposure strengthens baseline bond
        self.bond_strength[entity] += 0.01 * self.interaction_history[entity]

        # decay prevents infinite accumulation
        self.bond_strength[entity] *= self.decay_rate

    def separation_response(self, entity):
        """Simulates distress when interaction is missing"""
        base = self.bond_strength[entity]

        if base > 0.7:
            return "HIGH DISTRESS"
        elif base > 0.4:
            return "MODERATE DISTRESS"
        return "STABLE"

    def preference_score(self, entity):
        return self.bond_strength[entity]


# Example usage
engine = AttachmentEngine()

sessions = [
    ("Agent_A", 0.8),
    ("Agent_A", 0.9),
    ("Agent_B", 0.3),
    ("Agent_A", 1.0),
    ("Agent_C", 0.5)
]

for entity, reward in sessions:
    engine.interact(entity, reward)

print("A:", engine.preference_score("Agent_A"))
print("B:", engine.preference_score("Agent_B"))
print("A separation state:", engine.separation_response("Agent_A"))