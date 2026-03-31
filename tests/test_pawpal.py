from datetime import date, datetime
from pawpal_system import Task, Pet, Owner, Scheduler


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


def test_generate_schedule_sorts_tasks_chronologically():
    target_date = date(2026, 4, 1)
    tasks = [
        Task(task_id="t3", description="Evening meds", date=target_date, time="18:00", frequency="daily", priority="high"),
        Task(task_id="t1", description="Morning walk", date=target_date, time="07:00", frequency="daily", priority="medium"),
        Task(task_id="t2", description="Midday feeding", date=target_date, time="12:00", frequency="daily", priority="low"),
    ]
    scheduler = Scheduler(
        plan_id="sched-001",
        scheduled_date=target_date,
        generated_at=datetime(2026, 4, 1, 6, 0),
    )

    scheduler.generate_schedule(tasks)

    times = [t.time for t in scheduler.tasks]
    assert times == sorted(times)


def test_completing_daily_task_generates_next_day_task():
    from datetime import timedelta

    today = date(2026, 4, 1)
    task = Task(
        task_id="task-daily-001",
        description="Evening meds",
        date=today,
        time="20:00",
        frequency="daily",
        priority="medium",
    )

    task.mark_complete()
    repeats = task.generate_repeats("daily")

    assert task.is_completed is True
    assert len(repeats) == 1
    assert repeats[0].date == today + timedelta(days=1)
    assert repeats[0].description == task.description
    assert repeats[0].time == task.time


def test_completing_daily_task_generates_next_day_task():
    from datetime import timedelta

    today = date(2026, 4, 1)
    task = Task(
        task_id="task-daily-001",
        description="Evening meds",
        date=today,
        time="20:00",
        frequency="daily",
        priority="medium",
    )

    task.mark_complete()
    repeats = task.generate_repeats("daily")

    assert task.is_completed is True
    assert len(repeats) > 0
    assert repeats[0].date == today + timedelta(days=1)
    assert repeats[0].description == task.description
    assert repeats[0].time == task.time
