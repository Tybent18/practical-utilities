from collections import defaultdict, deque


class BoredomEngine:
    def __init__(self):
        self.experience_log = defaultdict(int)
        self.attention_trace = deque(maxlen=20)

        self.boredom_level = 0.2
        self.novelty_threshold = 0.5

        self.exploration_drive = 0.4
        self.decay = 0.97

    def novelty(self, item):
        # more repetition = less novelty
        visits = self.experience_log[item]
        return 1 / (1 + visits)

    def entropy_deficit(self, recent_items):
        if not recent_items:
            return 1.0

        unique = len(set(recent_items))
        total = len(recent_items)

        diversity = unique / total
        return 1 - diversity

    def compute_boredom(self, item, recent_items):
        self.attention_trace.append(item)

        n = self.novelty(item)
        e = self.entropy_deficit(recent_items)

        self.boredom_level += (1 - n) * 0.3
        self.boredom_level += e * 0.5

        self.boredom_level *= self.decay

        return max(0, min(1, self.boredom_level))

    def adapt_behavior(self):
        if self.boredom_level > 0.7:
            self.exploration_drive += 0.05
            return "FORCE EXPLORATION"
        elif self.boredom_level > 0.4:
            return "SHIFT CONTEXT"
        return "STABLE"


# Example usage
engine = BoredomEngine()

stream = [
    "Task_A", "Task_A", "Task_A",
    "Task_B", "Task_A", "Task_A"
]

for i in range(len(stream)):
    recent = stream[max(0, i-5):i]

    level = engine.compute_boredom(stream[i], recent)

    print(stream[i], "Boredom:", round(level, 3), engine.adapt_behavior())