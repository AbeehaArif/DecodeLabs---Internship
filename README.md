# Project 1: Rule-Based AI Bot

## Project Description
This is a deterministic, rule-based AI assistant developed as part of my internship at **DecodeLabs**. The bot utilizes efficient string sanitization and Python dictionary mapping to act as a robust conversational guardrail. It guarantees 100% hallucination-free, safe, and accurate responses based on predefined organizational knowledge and interactive intents.

## Key Features
- **Deterministic Guardrails:** Hard-coded logic ensures safe and secure interactions.
- **Input Sanitization:** Automatically handles trailing spaces and case insensitivity (`.strip().lower()`).
- **Graceful Fallback:** Uses `.get()` methodology to provide an intuitive fallback message when an unknown query is entered.
- **Interactive Loop:** Includes a continuous conversation loop with clear exit strategies (`exit`, `quit`, `bye`).

## Tools & Technologies
- **Language:** Python 3.x
- **Core Concepts:** Dictionaries, Infinite Loops, Conditional Flow, Data Sanitization

## How to Run
1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt in the directory containing this project.
3. Run the script using the following command:
   ```bash
   python main.py
   ```
