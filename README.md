# Date Range Extraction with FSM
This project automatically converts a large dataset of varied date expressions—including different formats, notes, Roman numerals, and period markers—into standardized year ranges using a logical finite state machine.

## What Is a Finite State Machine (FSM)?
A finite state machine (FSM) is a model of computation based on **states** and **transitions** between them triggered by incoming **events** or inputs.

At any given moment, the system is in a specific state and uses the current input to decide which state to move to next and what action to take. This makes it easier to structure pattern recognition and context handling without relying on deeply nested conditional logic.