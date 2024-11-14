# Turing Machine Implementation

## Project Overview
This project is based on the theoretical foundations presented in *Introduction to the Theory of Computation* by Michael Sipser. It focuses on implementing a **Turing Machine (TM)**, the abstract model of computation defined by Alan Turing, which is essential for understanding decidability, computability, and the limits of algorithmic processes.

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Theoretical Background](#theoretical-background)
- [Implementation Details](#implementation-details)
- [Usage Instructions](#usage-instructions)
- [Testing and Results](#testing-and-results)
- [Conclusion](#conclusion)

## Introduction
In Michael Sipser’s text, the Turing Machine is introduced as a core model for understanding computation. This project aims to implement a simulator for a Turing Machine that adheres to the formal definitions, capturing the machine’s components—states, tape, and transitions—and demonstrating how they work together to perform computations.

## Objectives
- **Implement** a Turing Machine simulator inspired by Sipser’s definitions, capable of performing basic computational tasks.
- **Simulate** operations such as reading, writing, and transitioning between states on an infinite tape.
- **Test** the machine on various inputs to validate its correctness.

## Theoretical Background
In Sipser’s work, a Turing Machine consists of:
- **Tape**: Infinite in both directions and used for storing symbols from a finite alphabet.
- **Head**: Reads and writes symbols on the tape and moves left or right as per the machine's rules.
- **States**: Define the current condition of the machine, which influences its actions.
- **Transition Function**: Dictates the machine’s behavior based on the current state and the symbol read, specifying the new state, symbol to write, and direction of head movement.

This project closely follows these definitions to ensure the simulator reflects a proper Turing Machine model.

## Implementation Details
### Language and Libraries
This implementation is written in **Python**. The simplicity of Python allows for a clear representation of the theoretical concepts introduced by Sipser.

### Code Structure
1. **TuringMachine Class**: Manages tape, head position, and state transitions.
2. **Transition Function**: Encodes rules for state transitions, matching the formal definition provided by Sipser.
3. **Tape Management**: Allows infinite expansion, a fundamental feature of Turing Machines.
