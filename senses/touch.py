import random
import time
from collections import deque


class TouchStimulus:
    def __init__(
        self,
        source,
        pressure,
        temperature,
        texture,
        vibration,
        pain_risk,
        duration
    ):
        self.source = source
        self.pressure = pressure
        self.temperature = temperature
        self.texture = texture
        self.vibration = vibration
        self.pain_risk = pain_risk
        self.duration = duration


class TouchMemory:
    def __init__(self):
        self.experiences = {}

    def remember(self, source, pain_level):
        if source not in self.experiences:
            self.experiences[source] = []

        self.experiences[source].append(pain_level)

    def average_pain(self, source):
        if source not in self.experiences:
            return 0

        data = self.experiences[source]
        return sum(data) / len(data)


class ArtificialTouchSystem:
    def __init__(self):
        self.sensitivity = 1.0
        self.pain_threshold = 0.75

        self.stress_level = 0.2
        self.fatigue = 0.1

        self.reflex_triggered = False

        self.contact_history = deque(maxlen=20)

        self.memory = TouchMemory()

    def pressure_response(self, stimulus):
        return stimulus.pressure * self.sensitivity

    def thermal_response(self, stimulus):
        optimal_temp = 22

        deviation = abs(stimulus.temperature - optimal_temp)

        return deviation / 50

    def texture_response(self, stimulus):
        texture_weights = {
            "smooth": 0.1,
            "rough": 0.5,
            "sharp": 1.0,
            "soft": 0.05,
            "metallic": 0.4
        }

        return texture_weights.get(stimulus.texture, 0.3)

    def vibration_response(self, stimulus):
        return stimulus.vibration * 0.8

    def predictive_threat(self, stimulus):
        memory_pain = self.memory.average_pain(stimulus.source)

        prediction = (
            stimulus.pain_risk +
            memory_pain +
            self.stress_level
        )

        return prediction / 3

    def calculate_touch_state(self, stimulus):
        pressure = self.pressure_response(stimulus)

        thermal = self.thermal_response(stimulus)

        texture = self.texture_response(stimulus)

        vibration = self.vibration_response(stimulus)

        predicted_threat = self.predictive_threat(stimulus)

        combined_signal = (
            pressure +
            thermal +
            texture +
            vibration +
            predicted_threat
        )

        combined_signal *= (1 + self.stress_level)

        combined_signal -= self.fatigue * 0.2

        return max(0, combined_signal)

    def reflex_system(self, signal_strength):
        if signal_strength >= self.pain_threshold:
            self.reflex_triggered = True
            print("REFLEX ACTIVATED")
        else:
            self.reflex_triggered = False

    def sensory_adaptation(self):
        self.sensitivity *= 0.995
        self.stress_level *= 0.99
        self.fatigue += 0.002

        self.sensitivity = max(0.5, self.sensitivity)

    def process_touch(self, stimulus):
        signal = self.calculate_touch_state(stimulus)

        self.memory.remember(stimulus.source, signal)

        self.contact_history.append(stimulus.source)

        self.reflex_system(signal)

        self.sensory_adaptation()

        self.debug_state(stimulus, signal)

    def debug_state(self, stimulus, signal):
        print(f"CONTACT: {stimulus.source}")
        print(f"Signal Strength: {signal:.2f}")
        print(f"Texture: {stimulus.texture}")
        print(f"Temperature: {stimulus.temperature}")
        print(f"Stress Level: {self.stress_level:.2f}")
        print(f"Sensitivity: {self.sensitivity:.2f}")
        print("-" * 40)


touch_inputs = [
    TouchStimulus(
        "Hot Surface",
        pressure=0.7,
        temperature=85,
        texture="metallic",
        vibration=0.1,
        pain_risk=0.9,
        duration=2
    ),

    TouchStimulus(
        "Soft Fabric",
        pressure=0.2,
        temperature=24,
        texture="soft",
        vibration=0.0,
        pain_risk=0.0,
        duration=5
    ),

    TouchStimulus(
        "Sharp Object",
        pressure=0.9,
        temperature=20,
        texture="sharp",
        vibration=0.2,
        pain_risk=1.0,
        duration=1
    )
]

touch_system = ArtificialTouchSystem()

for stimulus in touch_inputs:
    touch_system.process_touch(stimulus)
    time.sleep(1)