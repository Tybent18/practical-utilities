from collections import defaultdict


class GriefEngine:
    def __init__(self):
        self.memory_strength = defaultdict(float)
        self.loss_flags = set()

        self.grief_level = 0.2
        self.decay = 0.97
        self.reorganization_rate = 0.1

    def bond(self, entity, strength):
        self.memory_strength[entity] += strength

    def remove(self, entity):
        self.loss_flags.add(entity)

    def grief_response(self, entity):
        if entity not in self.loss_flags:
            return 0

        loss_weight = self.memory_strength[entity]

        self.grief_level += loss_weight * self.reorganization_rate
        self.grief_level *= self.decay

        return max(0, min(1, self.grief_level))

    def memory_reweight(self):
        for entity in list(self.memory_strength.keys()):
            if entity in self.loss_flags:
                self.memory_strength[entity] *= 0.5
            else:
                self.memory_strength[entity] *= 0.99


# Example usage
engine = GriefEngine()

engine.bond("Agent_A", 0.9)
engine.bond("Agent_B", 0.6)

engine.remove("Agent_A")

print("Grief A:", engine.grief_response("Agent_A"))
print("Grief B:", engine.grief_response("Agent_B"))