import math
import random
import time
from collections import deque


class ScentStimulus:
    def __init__(
        self,
        source,
        intensity,
        toxicity,
        familiarity,
        volatility,
        distance,
        airflow
    ):
        self.source = source
        self.intensity = intensity
        self.toxicity = toxicity
        self.familiarity = familiarity
        self.volatility = volatility
        self.distance = distance
        self.airflow = airflow


class OlfactoryMemory:
    def __init__(self):
        self.scent_database = {}

    def remember(self, source, threat_score):
        if source not in self.scent_database:
            self.scent_database[source] = []

        self.scent_database[source].append(
            threat_score
        )

    def average_threat(self, source):
        if source not in self.scent_database:
            return 0

        records = self.scent_database[source]

        return sum(records) / len(records)


class ArtificialSmellSystem:
    def __init__(self):
        self.sensitivity = 1.0

        self.stress_level = 0.2
        self.fatigue = 0.1

        self.environmental_humidity = 0.5
        self.air_density = 1.0

        self.focus_scent = None

        self.scent_history = deque(maxlen=25)

        self.memory = OlfactoryMemory()

    def scent_decay(self, stimulus):
        decay = math.exp(
            -stimulus.distance / 25
        )

        return decay

    def airflow_modifier(self, stimulus):
        return 1 + (
            stimulus.airflow * 0.5
        )

    def volatility_modifier(self, stimulus):
        return stimulus.volatility * 1.2

    def toxicity_analysis(self, stimulus):
        learned_threat = self.memory.average_threat(
            stimulus.source
        )

        return (
            stimulus.toxicity +
            learned_threat +
            self.stress_level
        ) / 3

    def familiarity_filter(self, stimulus):
        return stimulus.familiarity * 0.2

    def environmental_modifier(self):
        humidity_effect = (
            1 - self.environmental_humidity * 0.3
        )

        density_effect = self.air_density

        return humidity_effect * density_effect

    def calculate_scent_priority(self, stimulus):
        decay = self.scent_decay(stimulus)

        airflow = self.airflow_modifier(
            stimulus
        )

        volatility = self.volatility_modifier(
            stimulus
        )

        toxicity = self.toxicity_analysis(
            stimulus
        )

        familiarity_penalty = self.familiarity_filter(
            stimulus
        )

        environmental = self.environmental_modifier()

        signal_strength = (
            stimulus.intensity *
            self.sensitivity *
            decay *
            airflow *
            volatility *
            environmental
        )

        score = (
            signal_strength +
            toxicity
        )

        score -= familiarity_penalty
        score -= self.fatigue * 0.1

        return max(0, score)

    def prioritize_scents(self, stimuli):
        scored = []

        for stimulus in stimuli:
            score = self.calculate_scent_priority(
                stimulus
            )

            scored.append((stimulus, score))

        scored.sort(
            key=lambda x: x[1],
            reverse=True
        )

        if scored:
            self.focus_scent = scored[0][0]

            self.memory.remember(
                self.focus_scent.source,
                self.focus_scent.toxicity
            )

            self.scent_history.append(
                self.focus_scent.source
            )

    def adaptive_response(self):
        if not self.focus_scent:
            return

        if self.focus_scent.toxicity > 0.7:
            self.stress_level += 0.06
            self.sensitivity += 0.04

        if self.focus_scent.intensity > 0.9:
            self.fatigue += 0.01

        self.sensitivity = min(
            self.sensitivity,
            3.0
        )

    def sensory_decay(self):
        self.stress_level *= 0.99
        self.sensitivity *= 0.996
        self.fatigue *= 0.998

    def process_environment(self, stimuli):
        self.prioritize_scents(stimuli)

        self.adaptive_response()

        self.sensory_decay()

        self.debug_state()

    def debug_state(self):
        if not self.focus_scent:
            return

        print(
            f"FOCUS SCENT: "
            f"{self.focus_scent.source}"
        )

        print(
            f"Toxicity: "
            f"{self.focus_scent.toxicity}"
        )

        print(
            f"Distance: "
            f"{self.focus_scent.distance}"
        )

        print(
            f"Sensitivity: "
            f"{self.sensitivity:.2f}"
        )

        print(
            f"Stress Level: "
            f"{self.stress_level:.2f}"
        )

        print("-" * 40)


environmental_scents = [
    ScentStimulus(
        "Smoke",
        intensity=0.9,
        toxicity=0.8,
        familiarity=0.3,
        volatility=0.9,
        distance=10,
        airflow=0.7
    ),

    ScentStimulus(
        "Fresh Grass",
        intensity=0.5,
        toxicity=0.0,
        familiarity=0.9,
        volatility=0.4,
        distance=5,
        airflow=0.3
    ),

    ScentStimulus(
        "Chemical Leak",
        intensity=1.0,
        toxicity=1.0,
        familiarity=0.1,
        volatility=1.0,
        distance=20,
        airflow=0.8
    )
]

smell_system = ArtificialSmellSystem()

for _ in range(5):
    smell_system.process_environment(
        environmental_scents
    )

    time.sleep(1)