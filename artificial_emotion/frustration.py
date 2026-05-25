from collections import defaultdict, deque


class FrustrationEngine:
    def __init__(self):
        self.goal_state = {}
        self.failure_history = defaultdict(deque)

        self.frustration = 0.2
        self.escalation_rate = 0.1
        self.decay = 0.97

    def set_goal(self, goal, target):
        self.goal_state[goal] = target

    def report_failure(self, goal, error):
        self.failure_history[goal].append(error)

    def compute_error_pressure(self, goal):
        errors = self.failure_history[goal]
        if not errors:
            return 0
        return sum(errors) / len(errors)

    def update_frustration(self, goal):
        pressure = self.compute_error_pressure(goal)

        repetition_factor = len(self.failure_history[goal]) * 0.05

        self.frustration += pressure * self.escalation_rate
        self.frustration += repetition_factor

        self.frustration *= self.decay

        return max(0, min(1, self.frustration))

    def strategy_shift_signal(self):
        if self.frustration > 0.7:
            return "CHANGE STRATEGY"
        elif self.frustration > 0.4:
            return "INCREASE EFFORT"
        return "STABLE"


# Example usage
engine = FrustrationEngine()
engine.set_goal("solve_task", True)

failures = [0.2, 0.5, 0.6, 0.9, 1.0]

for err in failures:
    engine.report_failure("solve_task", err)
    level = engine.update_frustration("solve_task")

    print("Frustration:", round(level, 3), "State:", engine.strategy_shift_signal())