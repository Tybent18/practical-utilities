from collections import defaultdict


class EmpathyEngine:
    def __init__(self):
        self.agent_models = defaultdict(lambda: {
            "perceived_stress": 0.0,
            "perceived_reward": 0.0,
            "alignment": 0.5
        })

        self.empathy_sensitivity = 0.6
        self.mirroring_rate = 0.1

    def observe(self, agent, stress_signal, reward_signal):
        model = self.agent_models[agent]

        # update perceived internal state
        model["perceived_stress"] += stress_signal * self.mirroring_rate
        model["perceived_reward"] += reward_signal * self.mirroring_rate

        # normalize bounds
        model["perceived_stress"] = min(1.0, model["perceived_stress"])
        model["perceived_reward"] = min(1.0, model["perceived_reward"])

    def infer_state(self, agent):
        model = self.agent_models[agent]

        # simple emotional reconstruction
        distress = model["perceived_stress"]
        satisfaction = model["perceived_reward"]

        empathy_score = (
            distress * (1 - satisfaction) * self.empathy_sensitivity
        )

        return {
            "distress": distress,
            "satisfaction": satisfaction,
            "empathy_score": empathy_score
        }

    def align_response(self, agent):
        state = self.infer_state(agent)

        if state["distress"] > 0.7:
            return "INTERVENE / SUPPORT"
        elif state["empathy_score"] > 0.4:
            return "ACKNOWLEDGE STATE"
        return "NO ACTION"


# Example usage
engine = EmpathyEngine()

observations = [
    ("Agent_A", 0.8, 0.2),
    ("Agent_A", 0.6, 0.3),
    ("Agent_B", 0.2, 0.9),
    ("Agent_C", 0.9, 0.1)
]

for agent, stress, reward in observations:
    engine.observe(agent, stress, reward)
    print(agent, engine.align_response(agent), engine.infer_state(agent))