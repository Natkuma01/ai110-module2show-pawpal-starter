# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

### Smart Schediling 
- Add conflict warning message when same pet or different pets try to add a task same time as an existed tasks
- Tasks are listed by incompleted, completed, pet's name
- Tasks can set to repeat daily or weekly

### Testing PawPal+
- **Mark complete changes status** — creates a task and calls `mark_complete()`, then verifies `is_completed` flips from `False` to `True`
- **Add task increases pet task count** — adds a task to a pet via the owner and confirms the pet's task list grows from 0 to 1
- **Schedule sorts tasks chronologically** — gives the scheduler three tasks in random time order and verifies they come out sorted earliest to latest
- **Completing a daily task generates the next day's task** — marks a daily task complete, calls `generate_repeats("daily")`, and confirms exactly one new task is created for the following day with the same description and time
- In terminal, run `python -m pytest`

### Confidence Level
⭐️⭐️⭐️⭐️⭐️

### Features
- create a profile with name, email, and phone to get started; reset at any time
- add multiple pets with name, age, species, breed, insurance provider, and a custom emoji avatar; remove pets as needed
- set individual care preferences for each pet independently
- assign tasks to a specific pet with a description, date, scheduled time, priority (low / medium / high), and frequency (once / daily / weekly / monthly)
- warns when a new task's date and time clash with an existing task
- view tasks by all, completed, incomplete, or filtered by individual pet name
- generate a daily plan for any date; tasks are sorted first by time, then by priority (high → medium → low)

### Demo
<img width="1176" height="880" alt="Screenshot 2026-03-30 at 9 46 25 PM" src="https://github.com/user-attachments/assets/fefc3a63-0454-4af3-94f0-6d0b6cca3a6b" />

