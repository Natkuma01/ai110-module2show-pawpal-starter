# PawPal+ Class Diagram

```mermaid
classDiagram
    class Owner {
        +String owner_id
        +String name
        +String email
        +String phone
        +list~Pet~ pets
        +Preference preference
        +list~Scheduler~ daily_plans
        +total_tasks() int
        +add_pet(pet: Pet)
        +remove_pet(pet_id: String)
        +add_task(pet_id: String, task: Task)
        +remove_task(pet_id: String, task_id: String)
        +find_conflicts(new_task: Task) list
        +update_preferences(pref: Preference)
        +generate_daily_plan(start_date: Date, end_date: Date) Scheduler
    }

    class Pet {
        +String pet_id
        +String name
        +int age
        +String species
        +String breed
        +String insurance_provider
        +String avatar
        +list~Task~ tasks
        +Preference preference
        +set_preference(pref: Preference)
        +create_profile() dict
        +update_profile(**kwargs)
    }

    class Task {
        +String task_id
        +String description
        +Date date
        +String time
        +String frequency
        +String priority
        +bool is_completed
        +create_task()
        +edit_task(**kwargs)
        +delete_task()
        +mark_complete()
        +generate_repeats(repeat_type: String) list
    }

    class Scheduler {
        +String plan_id
        +Date scheduled_date
        +DateTime generated_at
        +list~Task~ tasks
        +Preference preference
        +generate_schedule(all_tasks: list)
        +delete_schedule(task_id: String)
        +display()
    }

    class Preference {
        +String feeding_schedule
        +String spending_rate
        +String preferred_walk_time
        +int walk_duration_minutes
        +set_spending_rate(rate: String)
        +set_walk_preferences(time: String, duration: int)
    }

    Owner "1" --> "0..*" Pet : owns
    Owner "1" --> "0..1" Preference : has
    Owner "1" --> "0..*" Scheduler : generates

    Pet "1" --> "0..*" Task : has
    Pet "1" --> "0..1" Preference : has

    Scheduler "1" --> "0..*" Task : schedules
    Scheduler "1" --> "0..1" Preference : references
```

## Class Responsibilities

| Class | Responsibility |
|---|---|
| **Owner** | Central actor — owns pets, manages tasks across all pets, detects scheduling conflicts, triggers daily plan generation |
| **Pet** | Pet profile (name, species, breed, insurance, avatar); holds its own task list and care preferences |
| **Task** | A single care activity with date, time, priority, frequency, and completion status; can generate the next occurrence |
| **Scheduler** | Filters and sorts all pet tasks for a given date by time and priority; stores the generated daily plan |
| **Preference** | Per-pet care preferences (feeding, spending, walk timing) set independently for each pet |

## Relationship Legend

- `-->` Association — navigable reference between classes
- `"1" --> "0..*"` One-to-many (e.g. one Owner has zero or more Pets)
- `"1" --> "0..1"` One-to-optional (e.g. a Pet may or may not have a Preference set)
