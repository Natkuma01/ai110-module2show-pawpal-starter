from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional


@dataclass
class Preference:
    feeding_schedule: str
    spending_rate: str
    preferred_walk_time: str
    walk_duration_minutes: int

    def set_spending_rate(self, rate: str) -> None:
        pass

    def set_walk_preferences(self, time: str, duration: int) -> None:
        pass


@dataclass
class Reminder:
    reminder_id: str
    title: str
    date: date
    day_of_week: str
    time: str
    is_recurring: bool
    recurrence_pattern: str

    def create_reminder(self) -> None:
        pass

    def edit_reminder(self) -> None:
        pass

    def delete_reminder(self) -> None:
        pass

    def trigger(self) -> None:
        pass


@dataclass
class Task:
    task_id: str
    title: str
    description: str
    task_type: str
    duration_minutes: int
    priority: str
    reminder: Optional[Reminder] = None

    def create_task(self) -> None:
        pass

    def edit_task(self) -> None:
        pass

    def delete_task(self) -> None:
        pass

    def link_reminder(self, reminder: Reminder) -> None:
        pass


@dataclass
class Appointment:
    appointment_id: str
    type: str
    location: str
    provider_name: str
    date: date
    time: str
    notes: str
    reminder: Optional[Reminder] = None

    def schedule_appointment(self) -> None:
        pass

    def cancel_appointment(self) -> None:
        pass

    def reschedule_appointment(self) -> None:
        pass


@dataclass
class HealthRecord:
    record_id: str
    condition: str
    medications: str
    last_checkup: date
    next_checkup: date

    def add_record(self) -> None:
        pass

    def update_record(self) -> None:
        pass


@dataclass
class DailyPlan:
    plan_id: str
    date: date
    generated_at: datetime
    explanation: str
    tasks: list[Task] = field(default_factory=list)
    preference: Optional[Preference] = None

    def generate_plan(self) -> None:
        pass

    def explain_plan(self) -> None:
        pass

    def adjust_plan(self) -> None:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    age: int
    species: str
    breed: str
    insurance_provider: str
    health_records: list[HealthRecord] = field(default_factory=list)
    appointments: list[Appointment] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)

    def create_profile(self) -> None:
        pass

    def update_profile(self) -> None:
        pass


@dataclass
class Owner:
    owner_id: str
    name: str
    email: str
    phone: str
    pets: list[Pet] = field(default_factory=list)
    preference: Optional[Preference] = None
    daily_plans: list[DailyPlan] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: str) -> None:
        pass

    def update_preferences(self, pref: Preference) -> None:
        pass

    def generate_daily_plan(self, date: str) -> DailyPlan:
        pass
