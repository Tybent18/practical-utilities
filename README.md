# Practical Utilities & Cognitive Experiments

A mixed programming laboratory containing everyday command-line utilities alongside early experiments in artificial perception and emotion modeling.

The repository is divided into three tracks so practical software and cognitive prototypes can evolve without pretending they are the same kind of project.

## Project clusters

### 1. Everyday utilities

Small C and Java programs focused on input handling, calculations, validation, and string manipulation.

| Area | Examples |
| --- | --- |
| Finance | [`interest_calculator.java`](interest_calculator.java), [`sale_price_calculator.c`](sale_price_calculator.c), [`tax_calculator.c`](tax_calculator.c) |
| Money handling | [`money_counter.c`](money_counter.c) |
| Text and validation | [`string_reversal.java`](string_reversal.java), [`codeword_checker.java`](codeword_checker.java) |
| Low-level operations | [`bit.c`](bit.c) |

### 2. Artificial sensory systems

The [`senses/`](senses/) directory separates perception-inspired modules into vision, hearing, touch, smell, taste, and spatial awareness (“sixth sense”).

These are educational abstractions for experimenting with signal interpretation and environmental state—not claims of human-equivalent perception.

### 3. Artificial emotion models

The [`artificial_emotion/`](artificial_emotion/) directory contains focused Python modules for curiosity, trust, confidence, stress, grief, boredom, empathy, fear, attachment, anticipation, jealousy, loneliness, frustration, and awe.

These modules model variables and behavioral weighting. They do not attempt to reproduce consciousness or clinical human emotion.

## Design principles

- readable logic before premature optimization;
- minimal dependencies and portable examples;
- explicit state and understandable behavior;
- modular experiments that can later be composed;
- honest separation between implemented behavior and future research ideas.

## Run examples

```bash
python artificial_emotion/curiosity.py
python senses/vision.py
gcc -Wall -Wextra -pedantic money_counter.c -o money_counter
./money_counter
javac string_reversal.java
java string_reversal
```

## Suggested evolution

The utility collection can remain here while mature cognitive work moves into focused repositories for adaptive memory, multisensory integration, decision policy, and human–AI interaction.

That preserves this repository as the experimental nursery without forcing every sapling into the same flowerpot.

## Foundation portfolio

This repository is part of a five-repository learning path:

1. [Foundations & Algorithms](https://github.com/Tybent18/foundations-algorithms)
2. [Data Structures Practice](https://github.com/Tybent18/data-structures-practice)
3. [OOP Concepts](https://github.com/Tybent18/oop-concepts)
4. [Math for Computing](https://github.com/Tybent18/math-for-computing)
5. [Practical Utilities](https://github.com/Tybent18/practical-utilities)

## Status

Active exploratory collection. Everyday utilities are foundational exercises; sensory and emotion modules are early prototypes requiring formal interfaces, tests, and measured evaluation before research claims.

## License

[MIT](LICENSE)
