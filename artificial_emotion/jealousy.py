from collections import defaultdict


class JealousyEngine:
    def __init__(self):
        self.value_map = defaultdict(float)
        self.attention_allocation = defaultdict(float)
        self.attachment_strength = defaultdict(float)

        self.sensitivity = 0.6
        self.decay = 0.98

    def set_value(self, entity, value):
        self.value_map[entity] = value

    def update_attachment(self, entity, interaction_quality):
        self.attachment_strength[entity] += interaction_quality * 0.1
        self.attachment_strength[entity] *= self.decay

    def competitive_pressure(self, entity, competitor):
        base = self.value_map[entity]
        rival = self.value_map[competitor]

        return max(0, rival - base)

    def jealousy_score(self, entity, competitor):
        attachment = self.attachment_strength[entity]
        pressure = self.competitive_pressure(entity, competitor)

        score = (
            attachment * pressure * self.sensitivity
        )

        return max(0, min(1, score))

    def update_attention(self, entity, competitor):
        score = self.jealousy_score(entity, competitor)

        self.attention_allocation[entity] += score

        return score


# Example usage
engine = JealousyEngine()

engine.set_value("Agent_A", 0.8)
engine.set_value("Agent_B", 0.9)

engine.update_attachment("Agent_A", 0.7)
engine.update_attachment("Agent_A", 0.9)
engine.update_attachment("Agent_B", 0.6)

score = engine.update_attention("Agent_A", "Agent_B")

print("Jealousy Score (A vs B):", score)