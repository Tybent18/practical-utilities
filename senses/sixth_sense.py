import random
import math
import time
from collections import deque


class EnvironmentalSignal:
    def __init__(
        self,
        source,
        anomaly,
        uncertainty,
        threat_probability,
        sensory_conflict,
        motion_variance,
        familiarity
    ):
        self.source = source

        self.anomaly = anomaly
        self.uncertainty = uncertainty

        self.threat_probability = (
            threat_probability
        )

        self.sensory_conflict = (
            sensory_conflict
        )

        self.motion_variance = (
            motion_variance
        )

        self.familiarity = familiarity


class IntuitionMemory:
    def __init__(self):
        self.prediction_history = {}

    def remember(self, source, outcome):
        if source not in self.prediction_history:
            self.prediction_history[source] = []

        self.prediction_history[source].append(
            outcome
        )

    def predictive_bias(self, source):
        if source not in self.prediction_history:
            return 0

        history = self.prediction_history[source]

        return sum(history) / len(history)


class ArtificialSixthSense:
    def __init__(self):
        self.intuition_level = 1.0

        self.stress_level = 0.2
        self.fatigue = 0.1

        self.environmental_paranoia = 0.3

        self.focus_signal = None

        self.recent_predictions = deque(
            maxlen=25
        )

        self.memory = IntuitionMemory()

    def anomaly_detection(self, signal):
        return signal.anomaly * 1.5

    def uncertainty_processing(self, signal):
        return (
            signal.uncertainty *
            self.environmental_paranoia
        )

    def conflict_analysis(self, signal):
        return (
            signal.sensory_conflict *
            1.3
        )

    def motion_prediction(self, signal):
        return (
            signal.motion_variance *
            1.2
        )

    def familiarity_penalty(self, signal):
        return signal.familiarity * 0.2

    def predictive_memory_bias(self, signal):
        return self.memory.predictive_bias(
            signal.source
        )

    def calculate_instinct_score(self, signal):
        anomaly = self.anomaly_detection(
            signal
        )

        uncertainty = self.uncertainty_processing(
            signal
        )

        conflict = self.conflict_analysis(
            signal
        )

        motion = self.motion_prediction(
            signal
        )

        threat = (
            signal.threat_probability *
            (1 + self.stress_level)
        )

        memory_bias = (
            self.predictive_memory_bias(
                signal
            )
        )

        familiarity_penalty = (
            self.familiarity_penalty(
                signal
            )
        )

        instinct_score = (
            anomaly +
            uncertainty +
            conflict +
            motion +
            threat +
            memory_bias
        )

        instinct_score *= self.intuition_level

        instinct_score -= familiarity_penalty
        instinct_score -= self.fatigue * 0.1

        return max(0, instinct_score)

    def prioritize_signal(self, signals):
        scored = []

        for signal in signals:
            score = self.calculate_instinct_score(
                signal
            )

            scored.append((signal, score))

        scored.sort(
            key=lambda x: x[1],
            reverse=True
        )

        if scored:
            self.focus_signal = scored[0][0]

            self.recent_predictions.append(
                self.focus_signal.source
            )

            self.memory.remember(
                self.focus_signal.source,
                self.focus_signal.threat_probability
            )

    def adaptive_instinct(self):
        if not self.focus_signal:
            return

        if self.focus_signal.anomaly > 0.7:
            self.stress_level += 0.04
            self.intuition_level += 0.03

        if self.focus_signal.uncertainty > 0.8:
            self.environmental_paranoia += 0.02

        self.intuition_level = min(
            self.intuition_level,
            3.0
        )

    def cognitive_decay(self):
        self.stress_level *= 0.99
        self.intuition_level *= 0.995
        self.fatigue += 0.002

    def process_environment(self, signals):
        self.prioritize_signal(signals)

        self.adaptive_instinct()

        self.cognitive_decay()

        self.debug_state()

    def debug_state(self):
        if not self.focus_signal:
            return

        print(
            f"INTUITIVE FOCUS: "
            f"{self.focus_signal.source}"
        )

        print(
            f"Threat Probability: "
            f"{self.focus_signal.threat_probability}"
        )

        print(
            f"Uncertainty: "
            f"{self.focus_signal.uncertainty}"
        )

        print(
            f"Intuition Level: "
            f"{self.intuition_level:.2f}"
        )

        print(
            f"Stress Level: "
            f"{self.stress_level:.2f}"
        )

        print("-" * 40)


environmental_signals = [
    EnvironmentalSignal(
        "Unusual Footsteps",
        anomaly=0.8,
        uncertainty=0.7,
        threat_probability=0.9,
        sensory_conflict=0.6,
        motion_variance=0.8,
        familiarity=0.2
    ),

    EnvironmentalSignal(
        "Normal Wind",
        anomaly=0.1,
        uncertainty=0.1,
        threat_probability=0.0,
        sensory_conflict=0.0,
        motion_variance=0.2,
        familiarity=0.9
    ),

    EnvironmentalSignal(
        "Shadow Movement",
        anomaly=1.0,
        uncertainty=0.9,
        threat_probability=0.95,
        sensory_conflict=0.8,
        motion_variance=0.9,
        familiarity=0.1
    )
]

sixth_sense = ArtificialSixthSense()

for _ in range(5):
    sixth_sense.process_environment(
        environmental_signals
    )

    time.sleep(1)