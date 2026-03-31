from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
import uuid


@dataclass
class Preference:
    feeding_schedule: str
    spending_rate: str
    preferred_walk_time: str
    walk_duration_minutes: int

    """Sets the spending rate for budget tracking."""
    def set_spending_rate(self, rate: str) -> None:
        self.spending_rate = rate

    """Updates the preferred walk time and duration in minutes."""
    def set_walk_preferences(self, time: str, duration: int) -> None:
        self.preferred_walk_time = time
        self.walk_duration_minutes = duration


@dataclass
class Task:
    task_id: str
    description: str
    date: date          # the day this task is scheduled for
    time: str           # scheduled time for the activity, e.g. "08:00"
    frequency: str      # how often the task recurs, e.g. "daily", "weekly"
    priority: str       # e.g. "high", "medium", "low"
    is_completed: bool = False

    """Validates that required fields are present for the task."""
    def create_task(self) -> None:
        if not self.task_id or not self.description:
            raise ValueError("task_id and description are required")

    """Updates task attributes by keyword arguments."""
    def edit_task(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Task has no attribute '{key}'")

    """Clears the task description and resets completion status."""
    def delete_task(self) -> None:
        self.description = ""
        self.is_completed = False

    """Marks the task as completed."""
    def mark_complete(self) -> None:
        self.is_completed = True

    """Generates the next occurrence of this task based on repeat_type."""
    def generate_repeats(self, repeat_type: str) -> list[Task]:
        from datetime import timedelta
        repeats = []
        if repeat_type == "daily":
            repeats.append(Task(
                task_id=str(uuid.uuid4()),
                description=self.description,
                date=self.date + timedelta(days=1),
                time=self.time,
                frequency=self.frequency,
                priority=self.priority,
            ))
        elif repeat_type == "weekly":
            repeats.append(Task(
                task_id=str(uuid.uuid4()),
                description=self.description,
                date=self.date + timedelta(weeks=1),
                time=self.time,
                frequency=self.frequency,
                priority=self.priority,
            ))
        return repeats


@dataclass
class Scheduler:
    plan_id: str
    scheduled_date: date
    generated_at: datetime
    tasks: list[Task] = field(default_factory=list)
    preference: Optional[Preference] = None

    """Filters and sorts tasks for the scheduled date by time and priority."""
    def generate_schedule(self, all_tasks: list[Task]) -> None:
        # Gather only tasks that belong to scheduled_date, then sort by time → priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        day_tasks = [t for t in all_tasks if t.date == self.scheduled_date]
        day_tasks.sort(key=lambda t: (t.time, priority_order.get(t.priority, 3)))
        self.tasks = day_tasks

    """Removes a task from the schedule by task ID."""
    def delete_schedule(self, task_id: str) -> None:
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    """Prints a formatted summary of the schedule and its tasks."""
    def display(self) -> None:
        print(f"\n{'=' * 40}")
        print(f"  Schedule for {self.scheduled_date}")
        print(f"  Generated: {self.generated_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"{'=' * 40}")
        if not self.tasks:
            print("  No tasks scheduled for this day.")
        else:
            for task in self.tasks:
                status = "✓" if task.is_completed else "○"
                print(f"  [{status}] {task.time}  [{task.priority.upper()}]  {task.description}")
        print(f"{'=' * 40}\n")


@dataclass
class Pet:
    pet_id: str
    name: str
    age: int
    species: str
    breed: str
    insurance_provider: str
    avatar: str = "🐾"
    tasks: list[Task] = field(default_factory=list)
    preference: Optional[Preference] = None

    """Sets the preference for this pet."""
    def set_preference(self, pref: Preference) -> None:
        self.preference = pref

    """Returns a dictionary of the pet's profile information."""
    def create_profile(self) -> dict:
        return {
            "pet_id": self.pet_id,
            "name": self.name,
            "age": self.age,
            "species": self.species,
            "breed": self.breed,
            "insurance_provider": self.insurance_provider,
        }

    """Updates pet profile attributes by keyword arguments."""
    def update_profile(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Pet has no attribute '{key}'")


@dataclass
class Owner:
    owner_id: str
    name: str
    email: str
    phone: str
    pets: list[Pet] = field(default_factory=list)
    preference: Optional[Preference] = None
    daily_plans: list[Scheduler] = field(default_factory=list)

    """Returns the total number of tasks across all pets."""
    @property
    def total_tasks(self) -> int:
        return sum(len(pet.tasks) for pet in self.pets)

    """Finds and returns a pet by ID, raising ValueError if not found."""
    def _find_pet(self, pet_id: str) -> Pet:
        for pet in self.pets:
            if pet.pet_id == pet_id:
                return pet
        raise ValueError(f"Pet '{pet_id}' not found")

    """Iterates all pets and their tasks, comparing each task's date and time to the new task; returns (pet, task) pairs where both match."""
    def find_conflicts(self, new_task: Task) -> list[tuple[Pet, Task]]:
        conflicts = []
        new_date = str(new_task.date)
        new_time = new_task.time.strip()
        for pet in self.pets:
            for task in pet.tasks:
                if str(task.date) == new_date and task.time.strip() == new_time:
                    conflicts.append((pet, task))
        return conflicts

    # --- Pet management ---
    """Adds a pet to the owner's pet list."""
    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    """Removes a pet from the owner's pet list by pet ID."""
    def remove_pet(self, pet_id: str) -> None:
        self.pets = [p for p in self.pets if p.pet_id != pet_id]

    # --- Task management ---
    """Adds a task to the specified pet's task list."""
    def add_task(self, pet_id: str, task: Task) -> None:
        pet = self._find_pet(pet_id)
        pet.tasks.append(task)

    """Removes a task from the specified pet's task list by task ID."""
    def remove_task(self, pet_id: str, task_id: str) -> None:
        pet = self._find_pet(pet_id)
        pet.tasks = [t for t in pet.tasks if t.task_id != task_id]

    # --- Plan & preferences ---
    """Updates the owner's preference settings."""
    def update_preferences(self, pref: Preference) -> None:
        self.preference = pref

    """Generates and stores a daily schedule for the owner's pets starting from start_date."""
    def generate_daily_plan(self, start_date: date, end_date: date) -> Scheduler:
        all_tasks = [task for pet in self.pets for task in pet.tasks]
        scheduler = Scheduler(
            plan_id=str(uuid.uuid4()),
            scheduled_date=start_date,
            generated_at=datetime.now(),
            preference=self.preference,
        )
        scheduler.generate_schedule(all_tasks)
        self.daily_plans.append(scheduler)
        return scheduler
