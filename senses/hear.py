import math
import random
import time
from collections import deque


class AudioStimulus:
    def __init__(
        self,
        source,
        volume,
        frequency,
        direction,
        motion,
        threat,
        repetition
    ):
        self.source = source
        self.volume = volume
        self.frequency = frequency
        self.direction = direction
        self.motion = motion
        self.threat = threat
        self.repetition = repetition


class AuditoryMemory:
    def __init__(self):
        self.sound_history = {}

    def remember(self, source):
        self.sound_history[source] = (
            self.sound_history.get(source, 0) + 1
        )

    def familiarity(self, source):
        return self.sound_history.get(source, 0)


class ArtificialHearingSystem:
    def __init__(self):
        self.attention_focus = None

        self.sensitivity = 1.0
        self.stress_level = 0.2
        self.fatigue = 0.1

        self.noise_tolerance = 0.5

        self.audio_memory = AuditoryMemory()

        self.directional_focus = {
            "front": 1.0,
            "left": 0.8,
            "right": 0.8,
            "rear": 0.6
        }

        self.recent_sounds = deque(maxlen=20)

    def directional_modifier(self, direction):
        return self.directional_focus.get(direction, 0.5)

    def frequency_analysis(self, frequency):
        if 200 <= frequency <= 4000:
            return 1.0

        return 0.5

    def motion_tracking(self, stimulus):
        return stimulus.motion * 1.5

    def familiarity_filter(self, stimulus):
        familiarity = self.audio_memory.familiarity(
            stimulus.source
        )

        return familiarity * 0.05

    def threat_analysis(self, stimulus):
        return stimulus.threat * (
            1 + self.stress_level
        )

    def repetition_decay(self, stimulus):
        return stimulus.repetition * 0.1

    def calculate_attention_score(self, stimulus):
        direction_weight = self.directional_modifier(
            stimulus.direction
        )

        frequency_weight = self.frequency_analysis(
            stimulus.frequency
        )

        motion_weight = self.motion_tracking(
            stimulus
        )

        threat_weight = self.threat_analysis(
            stimulus
        )

        familiarity_penalty = self.familiarity_filter(
            stimulus
        )

        repetition_penalty = self.repetition_decay(
            stimulus
        )

        signal_strength = (
            stimulus.volume *
            self.sensitivity *
            direction_weight *
            frequency_weight
        )

        score = (
            signal_strength +
            motion_weight +
            threat_weight
        )

        score -= familiarity_penalty
        score -= repetition_penalty
        score -= self.fatigue * 0.2

        return max(0, score)

    def isolate_priority_sound(self, stimuli):
        scored = []

        for stimulus in stimuli:
            score = self.calculate_attention_score(
                stimulus
            )

            scored.append((stimulus, score))

        scored.sort(
            key=lambda x: x[1],
            reverse=True
        )

        if scored:
            self.attention_focus = scored[0][0]

            self.audio_memory.remember(
                self.attention_focus.source
            )

            self.recent_sounds.append(
                self.attention_focus.source
            )

    def adaptive_sensitivity(self):
        if not self.attention_focus:
            return

        if self.attention_focus.threat > 0.7:
            self.stress_level += 0.05
            self.sensitivity += 0.03

        if self.attention_focus.volume > 0.9:
            self.fatigue += 0.02

        self.sensitivity = min(
            self.sensitivity,
            3.0
        )

    def sensory_decay(self):
        self.stress_level *= 0.99
        self.sensitivity *= 0.995
        self.fatigue *= 0.998

    def process_audio_environment(self, stimuli):
        self.isolate_priority_sound(stimuli)

        self.adaptive_sensitivity()

        self.sensory_decay()

        self.debug_state()

    def debug_state(self):
        if not self.attention_focus:
            return

        print(
            f"FOCUS SOUND: "
            f"{self.attention_focus.source}"
        )

        print(
            f"Direction: "
            f"{self.attention_focus.direction}"
        )

        print(
            f"Threat Level: "
            f"{self.attention_focus.threat}"
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


audio_environment = [
    AudioStimulus(
        "Footsteps",
        volume=0.6,
        frequency=900,
        direction="rear",
        motion=0.8,
        threat=0.7,
        repetition=2
    ),

    AudioStimulus(
        "Wind",
        volume=0.4,
        frequency=300,
        direction="left",
        motion=0.1,
        threat=0.0,
        repetition=10
    ),

    AudioStimulus(
        "Metal Impact",
        volume=1.0,
        frequency=2500,
        direction="front",
        motion=0.9,
        threat=1.0,
        repetition=1
    )
]

hearing_system = ArtificialHearingSystem()

for _ in range(5):
    hearing_system.process_audio_environment(
        audio_environment
    )

    time.sleep(1)