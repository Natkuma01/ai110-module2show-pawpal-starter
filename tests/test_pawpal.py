from datetime import date
from pawpal_system import Task, Pet, Owner


def test_mark_complete_changes_status():
    task = Task(
        task_id="task-001",
        description="Morning walk",
        date=date.today(),
        time="07:00",
        frequency="daily",
        priority="high"
    )

    assert task.is_completed is False

    task.mark_complete()

    assert task.is_completed is True


def test_add_task_increases_pet_task_count():
    owner = Owner(
        owner_id="owner-001",
        name="Natalie",
        email="natalie@email.com",
        phone="555-1234"
    )
    pet = Pet(
        pet_id="pet-001",
        name="Buddy",
        age=3,
        species="Dog",
        breed="Labrador",
        insurance_provider="PetFirst"
    )
    owner.add_pet(pet)

    assert len(pet.tasks) == 0

    owner.add_task("pet-001", Task(
        task_id="task-001",
        description="Morning walk",
        date=date.today(),
        time="07:00",
        frequency="daily",
        priority="high"
    ))

    assert len(pet.tasks) == 1
