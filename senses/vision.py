import math

import random

import time

from collections import deque



class VisualStimulus:

    def __init__(self, name, x, y, intensity, motion, threat, novelty):

        self.name = name

        self.x = x

        self.y = y

        self.intensity = intensity

        self.motion = motion

        self.threat = threat

        self.novelty = novelty



class VisionMemory:

    def __init__(self):

        self.memory = {}


    def remember(self, stimulus_name):

        self.memory[stimulus_name] = self.memory.get(stimulus_name, 0) + 1


    def familiarity(self, stimulus_name):

        return self.memory.get(stimulus_name, 0)



class ArtificialVisionSystem:

    def __init__(self):

        self.focus_target = None

        self.focus_strength = 1.0

        self.peripheral_decay = 0.4


        self.attention_span = 10

        self.attention_history = deque(maxlen=20)


        self.stress_level = 0.2

        self.fatigue = 0.1

        self.visibility = 1.0


        self.memory = VisionMemory()


        self.fov_radius = 100

        self.center_x = 0

        self.center_y = 0


    def distance(self, stimulus):

        return math.sqrt(

            (stimulus.x - self.center_x) ** 2 +

            (stimulus.y - self.center_y) ** 2

        )


    def peripheral_modifier(self, distance):

        return max(0.1, 1 - (distance / self.fov_radius))


    def calculate_attention_score(self, stimulus):

        distance = self.distance(stimulus)


        if distance > self.fov_radius:

            return 0


        peripheral_weight = self.peripheral_modifier(distance)


        familiarity = self.memory.familiarity(stimulus.name)

        familiarity_penalty = familiarity * 0.03


        motion_priority = stimulus.motion * 1.8

        threat_priority = stimulus.threat * (2 + self.stress_level)

        novelty_priority = stimulus.novelty * 1.5


        environmental_visibility = self.visibility * stimulus.intensity


        fatigue_penalty = self.fatigue * 0.5


        attention_score = (

            environmental_visibility +

            motion_priority +

            threat_priority +

            novelty_priority

        )


        attention_score *= peripheral_weight

        attention_score -= familiarity_penalty

        attention_score -= fatigue_penalty


        return max(0, attention_score)


    def select_focus_target(self, stimuli):

        scored = []


        for stimulus in stimuli:

            score = self.calculate_attention_score(stimulus)

            scored.append((stimulus, score))


        scored.sort(key=lambda x: x[1], reverse=True)


        if scored:

            self.focus_target = scored[0][0]

            self.attention_history.append(self.focus_target.name)

            self.memory.remember(self.focus_target.name)


    def adaptive_focus(self):

        if not self.focus_target:

            return


        if self.focus_target.threat > 0.7:

            self.focus_strength += 0.1

            self.stress_level += 0.05


        if self.focus_target.motion > 0.8:

            self.focus_strength += 0.05


        self.focus_strength = min(3.0, self.focus_strength)

        self.stress_level = min(1.0, self.stress_level)


    def sensory_decay(self):

        self.focus_strength *= 0.98

        self.stress_level *= 0.99

        self.fatigue += 0.001


    def process_scene(self, stimuli):

        self.select_focus_target(stimuli)

        self.adaptive_focus()

        self.sensory_decay()


    def debug_state(self):

        if self.focus_target:

            print(f"FOCUS: {self.focus_target.name}")

            print(f"Threat: {self.focus_target.threat}")

            print(f"Motion: {self.focus_target.motion}")

            print(f"Focus Strength: {self.focus_strength:.2f}")

            print(f"Stress Level: {self.stress_level:.2f}")

            print("-" * 40)



stimuli = [

    VisualStimulus("Moving Shadow", 10, 15, 0.6, 0.9, 0.8, 0.7),

    VisualStimulus("Tree", 40, 20, 0.5, 0.0, 0.0, 0.1),

    VisualStimulus("Flashing Light", 25, 5, 1.0, 0.6, 0.3, 0.9),

    VisualStimulus("Unknown Entity", 5, 8, 0.7, 0.5, 1.0, 1.0)

]


vision = ArtificialVisionSystem()


for _ in range(10):

    vision.process_scene(stimuli)

    vision.debug_state()

    time.sleep(0.5)