# PawPal+ Class Diagram

```mermaid
classDiagram
    class Owner {
        +String ownerId
        +String name
        +String email
        +String phone
        +addPet(pet: Pet)
        +removePet(petId: String)
        +updatePreferences(pref: Preference)
        +generateDailyPlan(date: String) DailyPlan
    }

    class Pet {
        +String petId
        +String name
        +int age
        +String species
        +String breed
        +String insuranceProvider
        +createProfile()
        +updateProfile()
    }

    class HealthRecord {
        +String recordId
        +String condition
        +String medications
        +Date lastCheckup
        +Date nextCheckup
        +addRecord()
        +updateRecord()
    }

    class Preference {
        +String feedingSchedule
        +String spendingRate
        +String preferredWalkTime
        +int walkDurationMinutes
        +setSpendingRate(rate: String)
        +setWalkPreferences(time: String, duration: int)
    }

    class Task {
        +String taskId
        +String title
        +String description
        +String taskType
        +int durationMinutes
        +String priority
        +createTask()
        +editTask()
        +deleteTask()
        +linkReminder(reminder: Reminder)
    }

    class Reminder {
        +String reminderId
        +String title
        +Date date
        +String dayOfWeek
        +String time
        +Boolean isRecurring
        +String recurrencePattern
        +createReminder()
        +editReminder()
        +deleteReminder()
        +trigger()
    }

    class Appointment {
        +String appointmentId
        +String type
        +String location
        +String providerName
        +Date date
        +String time
        +String notes
        +scheduleAppointment()
        +cancelAppointment()
        +rescheduleAppointment()
    }

    class DailyPlan {
        +String planId
        +Date date
        +DateTime generatedAt
        +String explanation
        +generatePlan()
        +explainPlan()
        +adjustPlan()
    }

    Owner "1" --> "0..*" Pet : owns
    Owner "1" --> "1" Preference : has
    Owner "1" --> "0..*" DailyPlan : generates

    Pet "1" *-- "0..*" HealthRecord : has
    Pet "1" --> "0..*" Appointment : scheduled for
    Pet "1" --> "0..*" Task : associated with

    Task "1" --> "0..1" Reminder : linked to
    Appointment "1" --> "0..1" Reminder : notified by

    DailyPlan "1" o-- "1..*" Task : schedules
    DailyPlan "1" --> "1" Preference : references to explain plan
```

## Class Responsibilities

| Class | Responsibility |
|---|---|
| **Owner** | Central actor — owns pets, holds preferences, triggers daily plan generation |
| **Pet** | Pet profile (species, breed, insurance); links to health records and appointments |
| **HealthRecord** | Stores medical conditions, medications, and checkup history (composition of Pet) |
| **Preference** | Owner's care preferences (food, spending, walk timing) used by the AI planner to justify its choices |
| **Task** | A single care activity (walk / feed / groom / vet visit) with duration and priority; links to a Reminder |
| **Reminder** | Date/time alert for a Task or Appointment; supports one-off and recurring schedules |
| **Appointment** | Vet or grooming bookings with their own Reminder for notifications |
| **DailyPlan** | AI-generated schedule for a day; selects and orders Tasks based on Preferences and explains why |

## Relationship Legend

- `*--` Composition — HealthRecord cannot exist without Pet
- `o--` Aggregation — DailyPlan contains Tasks but Tasks exist independently
- `-->` Association — navigable reference between classes
