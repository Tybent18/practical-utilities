import random
import time
from collections import deque


class TasteStimulus:
    def __init__(
        self,
        source,
        sweetness,
        bitterness,
        saltiness,
        sourness,
        umami,
        toxicity,
        nutrition,
        temperature,
        texture
    ):
        self.source = source

        self.sweetness = sweetness
        self.bitterness = bitterness
        self.saltiness = saltiness
        self.sourness = sourness
        self.umami = umami

        self.toxicity = toxicity
        self.nutrition = nutrition

        self.temperature = temperature
        self.texture = texture


class TasteMemory:
    def __init__(self):
        self.memory = {}

    def remember(self, source, reward):
        if source not in self.memory:
            self.memory[source] = []

        self.memory[source].append(reward)

    def preference_score(self, source):
        if source not in self.memory:
            return 0

        values = self.memory[source]

        return sum(values) / len(values)


class ArtificialTasteSystem:
    def __init__(self):
        self.sensitivity = 1.0

        self.hunger = 0.7
        self.stress_level = 0.2
        self.fatigue = 0.1

        self.preference_bias = 0.5

        self.recent_tastes = deque(maxlen=20)

        self.memory = TasteMemory()

    def flavor_complexity(self, stimulus):
        return (
            stimulus.sweetness +
            stimulus.bitterness +
            stimulus.saltiness +
            stimulus.sourness +
            stimulus.umami
        ) / 5

    def toxicity_response(self, stimulus):
        return stimulus.toxicity * (
            1 + self.stress_level
        )

    def nutritional_reward(self, stimulus):
        return stimulus.nutrition * (
            1 + self.hunger
        )

    def temperature_response(self, stimulus):
        optimal_temp = 35

        deviation = abs(
            stimulus.temperature - optimal_temp
        )

        return max(
            0,
            1 - (deviation / 50)
        )

    def texture_modifier(self, stimulus):
        texture_map = {
            "smooth": 1.0,
            "crunchy": 0.9,
            "soft": 0.8,
            "slimy": 0.2,
            "dry": 0.5
        }

        return texture_map.get(
            stimulus.texture,
            0.5
        )

    def memory_bias(self, stimulus):
        return self.memory.preference_score(
            stimulus.source
        )

    def calculate_taste_score(self, stimulus):
        flavor = self.flavor_complexity(
            stimulus
        )

        nutrition = self.nutritional_reward(
            stimulus
        )

        toxicity = self.toxicity_response(
            stimulus
        )

        temperature = self.temperature_response(
            stimulus
        )

        texture = self.texture_modifier(
            stimulus
        )

        memory = self.memory_bias(
            stimulus
        )

        score = (
            flavor +
            nutrition +
            temperature +
            texture +
            memory
        )

        score -= toxicity
        score -= self.fatigue * 0.1

        return max(0, score)

    def adaptive_preference(self, stimulus, score):
        reward = (
            stimulus.nutrition -
            stimulus.toxicity
        )

        self.memory.remember(
            stimulus.source,
            reward
        )

        if reward > 0:
            self.preference_bias += 0.02
        else:
            self.preference_bias -= 0.03

        self.preference_bias = max(
            0,
            min(self.preference_bias, 1)
        )

    def survival_response(self, stimulus):
        if stimulus.toxicity > 0.8:
            print("REJECTION REFLEX ACTIVATED")

            self.stress_level += 0.08

    def sensory_decay(self):
        self.hunger *= 0.995
        self.stress_level *= 0.99
        self.fatigue += 0.002

    def process_taste(self, stimulus):
        score = self.calculate_taste_score(
            stimulus
        )

        self.adaptive_preference(
            stimulus,
            score
        )

        self.survival_response(
            stimulus
        )

        self.recent_tastes.append(
            stimulus.source
        )

        self.sensory_decay()

        self.debug_state(
            stimulus,
            score
        )

    def debug_state(self, stimulus, score):
        print(
            f"TASTING: {stimulus.source}"
        )

        print(
            f"Taste Score: {score:.2f}"
        )

        print(
            f"Toxicity: {stimulus.toxicity}"
        )

        print(
            f"Nutrition: {stimulus.nutrition}"
        )

        print(
            f"Hunger: {self.hunger:.2f}"
        )

        print(
            f"Stress Level: "
            f"{self.stress_level:.2f}"
        )

        print("-" * 40)


taste_inputs = [
    TasteStimulus(
        "Sweet Fruit",
        sweetness=0.9,
        bitterness=0.1,
        saltiness=0.0,
        sourness=0.3,
        umami=0.1,
        toxicity=0.0,
        nutrition=0.8,
        temperature=24,
        texture="soft"
    ),

    TasteStimulus(
        "Spoiled Meat",
        sweetness=0.0,
        bitterness=0.8,
        saltiness=0.5,
        sourness=0.9,
        umami=0.6,
        toxicity=1.0,
        nutrition=0.1,
        temperature=30,
        texture="slimy"
    ),

    TasteStimulus(
        "Salted Nuts",
        sweetness=0.2,
        bitterness=0.1,
        saltiness=0.8,
        sourness=0.0,
        umami=0.4,
        toxicity=0.0,
        nutrition=0.7,
        temperature=22,
        texture="crunchy"
    )
]

taste_system = ArtificialTasteSystem()

for stimulus in taste_inputs:
    taste_system.process_taste(
        stimulus
    )

    time.sleep(1)