from datetime import date
from pawpal_system import Task, Pet, Owner

# --- Setup Owner ---
owner = Owner(
    owner_id="owner-001",
    name="Natalie",
    email="natalie@email.com",
    phone="555-1234"
)

# --- Create two pets ---
buddy = Pet(
    pet_id="pet-001",
    name="Buddy",
    age=3,
    species="Dog",
    breed="Labrador",
    insurance_provider="PetFirst"
)

luna = Pet(
    pet_id="pet-002",
    name="Luna",
    age=2,
    species="Cat",
    breed="Siamese",
    insurance_provider="PetFirst"
)

owner.add_pet(buddy)
owner.add_pet(luna)

# --- Add tasks for Buddy ---
today = date.today()

owner.add_task("pet-001", Task(
    task_id="task-001",
    description="Morning walk with Buddy",
    date=today,
    time="07:00",
    frequency="daily",
    priority="high"
))

owner.add_task("pet-001", Task(
    task_id="task-002",
    description="Feed Buddy breakfast",
    date=today,
    time="08:00",
    frequency="daily",
    priority="medium"
))

owner.add_task("pet-001", Task(
    task_id="task-003",
    description="Evening walk with Buddy",
    date=today,
    time="18:00",
    frequency="daily",
    priority="high"
))

# --- Add tasks for Luna ---
owner.add_task("pet-002", Task(
    task_id="task-004",
    description="Feed Luna breakfast",
    date=today,
    time="08:30",
    frequency="daily",
    priority="medium"
))

owner.add_task("pet-002", Task(
    task_id="task-005",
    description="Playtime with Luna",
    date=today,
    time="17:00",
    frequency="daily",
    priority="low"
))

# --- Generate and display today's schedule ---
schedule = owner.generate_daily_plan(start_date=today, end_date=today)
schedule.display()
