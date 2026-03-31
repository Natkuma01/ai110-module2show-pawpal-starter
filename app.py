import streamlit as st
import uuid
import time
from datetime import date
from pawpal_system import Owner, Pet, Task, Preference

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.markdown("""
<style>
/* ── Bubbly global styles ───────────────────────────────────────────── */

/* Rounded, pill-style buttons */
.stButton > button {
    border-radius: 999px !important;
    font-weight: 700 !important;
    padding: 0.4rem 1.4rem !important;
    background: linear-gradient(135deg, #a855f7, #ec4899) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 4px 14px rgba(168,85,247,0.45) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 6px 20px rgba(168,85,247,0.6) !important;
}

/* Bubbly expander panels */
[data-testid="stExpander"] {
    border-radius: 20px !important;
    border: 2px solid #7c3aed !important;
    overflow: hidden !important;
    box-shadow: 0 4px 18px rgba(124,58,237,0.3) !important;
}

/* Rounded input boxes */
input, textarea, select, [data-baseweb="select"] {
    border-radius: 14px !important;
}

/* Pill-style info / warning / success boxes */
[data-testid="stAlert"] {
    border-radius: 18px !important;
}

/* Rounded metric cards */
[data-testid="stMetric"] {
    border-radius: 18px !important;
    background: #2d0060 !important;
    padding: 0.8rem 1rem !important;
    box-shadow: 0 4px 14px rgba(168,85,247,0.25) !important;
}

/* Bubbly title */
h1 {
    background: linear-gradient(90deg, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.6rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.5px;
}

/* Section subheaders */
h2, h3 {
    color: #d8b4fe !important;
    font-weight: 800 !important;
}
</style>
""", unsafe_allow_html=True)

def pink_info(msg: str) -> None:
    st.markdown(
        f'<div style="background:#fdf0f8; border-left:4px solid #f0abfc; border-radius:18px;'
        f' padding:0.75rem 1.1rem; color:#7e22ce; font-size:0.95rem;">{msg}</div>',
        unsafe_allow_html=True,
    )

# ── Session state init ──────────────────────────────────────────────────────
if "owner" not in st.session_state:
    st.session_state.owner = None

owner: Owner | None = st.session_state.owner

# ── Header ──────────────────────────────────────────────────────────────────
st.title("🐾 PawPal+")
st.caption("A pet care planning assistant.")
st.divider()

# ════════════════════════════════════════════════════════════════════════════
# SECTION 1 — Owner profile
# Displays a form for the user to create an owner profile with name, email, and phone.
# Once created, the profile is stored in session state and shown as a summary with a reset option.
# ════════════════════════════════════════════════════════════════════════════
st.subheader("Owner Profile")

if owner is None:
    with st.form("owner_form"):
        name  = st.text_input("Your name", value="Jordan")
        email = st.text_input("Email", value="jordan@example.com")
        phone = st.text_input("Phone", value="555-0100")
        submitted = st.form_submit_button("Create profile")

    if submitted:
        st.session_state.owner = Owner(
            owner_id=str(uuid.uuid4()),
            name=name,
            email=email,
            phone=phone,
        )
        st.rerun()
else:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**Name:** {owner.name}  |  **Email:** {owner.email}  |  **Phone:** {owner.phone}")
    with col2:
        if st.button("Reset profile"):
            st.session_state.owner = None
            st.rerun()

st.divider()

# Only show the rest of the app once an owner exists
if st.session_state.owner is None:
    pink_info("Create an owner profile above to get started.")
    st.stop()

owner = st.session_state.owner  # refresh local reference after potential rerun

# ════════════════════════════════════════════════════════════════════════════
# SECTION 2 — Pets
# Lets the owner add pets with basic info (name, age, species, breed, insurance).
# Lists all existing pets with a remove button next to each one.
# ════════════════════════════════════════════════════════════════════════════
st.subheader("Pets")

AVATAR_OPTIONS = ["🐶", "🐱", "🐰", "🐹", "🐦", "🐠", "🐢", "🐍", "🦜", "🐾"]

with st.expander("Add a pet", expanded=len(owner.pets) == 0):
    with st.form("pet_form"):
        p_avatar   = st.selectbox("Avatar", AVATAR_OPTIONS, format_func=lambda e: e)
        p_name     = st.text_input("Pet name", value="Mochi")
        p_age      = st.number_input("Age (years)", min_value=0, max_value=30, value=2)
        p_species  = st.selectbox("Species", ["dog", "cat", "other"])
        p_breed    = st.text_input("Breed", value="Mixed")
        p_insurer  = st.text_input("Insurance provider", value="PetFirst")
        add_pet    = st.form_submit_button("Add pet")

    if add_pet:
        pet = Pet(
            pet_id=str(uuid.uuid4()),
            name=p_name,
            age=int(p_age),
            species=p_species,
            breed=p_breed,
            insurance_provider=p_insurer,
            avatar=p_avatar,
        )
        owner.add_pet(pet)
        st.success(f"{p_avatar} {p_name} added!")
        st.rerun()

if owner.pets:
    for pet in owner.pets:
        cols = st.columns([3, 1])
        with cols[0]:
            st.markdown(
                f"{pet.avatar} **{pet.name}** — {pet.species}, {pet.breed}, age {pet.age} | "
                f"Insurance: {pet.insurance_provider} | Tasks: {len(pet.tasks)}"
            )
        with cols[1]:
            if st.button("Remove", key=f"remove_pet_{pet.pet_id}"):
                owner.remove_pet(pet.pet_id)
                st.rerun()
else:
    pink_info("No pets yet. Add one above.")

st.divider()

# ════════════════════════════════════════════════════════════════════════════
# SECTION 3 — Tasks
# Allows the owner to add tasks to a specific pet, with conflict detection to prevent double-booking.
# Displays all tasks filtered by a dropdown (all, completed, incomplete, or per pet) with done and delete actions.
# ════════════════════════════════════════════════════════════════════════════
st.subheader("Tasks")

if not owner.pets:
    pink_info("Add a pet first before creating tasks.")
else:
    with st.expander("Add a task"):
        with st.form("task_form"):
            t_pet     = st.selectbox("Assign to pet", options=owner.pets, format_func=lambda p: p.name)
            t_desc    = st.text_input("Description", value="Morning walk")
            t_date    = st.date_input("Date", value=date.today())
            t_time    = st.text_input("Time (HH:MM)", value="08:00")
            t_freq    = st.selectbox("Frequency", ["daily", "weekly", "monthly", "once"])
            t_prio    = st.selectbox("Priority", ["low", "medium", "high"], index=2)
            t_repeat  = st.selectbox(
                "Repeat",
                ["No repeat", "Every day for the next week", "Every week (same day)"],
                help="Automatically create copies of this task going forward.",
            )
            add_task  = st.form_submit_button("Add task")

        if add_task:
            task = Task(
                task_id=str(uuid.uuid4()),
                description=t_desc,
                date=t_date,
                time=t_time,
                frequency=t_freq,
                priority=t_prio,
            )

            selected_pet_id = t_pet.pet_id
            conflicts = owner.find_conflicts(task)
            if conflicts:
                for conflict_pet, conflict_task in conflicts:
                    if conflict_pet.pet_id == selected_pet_id:
                        label = f"same pet ({conflict_pet.name})"
                    else:
                        label = f"different pet ({conflict_pet.name})"
                    st.warning(
                        f"⚠️ Time conflict [{label}]: '{conflict_task.description}' is already "
                        f"scheduled at {conflict_task.time} on {conflict_task.date}."
                    )
            else:
                owner.add_task(t_pet.pet_id, task)
                repeat_map = {
                    "Every day for the next week": "daily",
                    "Every week (same day)": "weekly",
                }
                if t_repeat in repeat_map:
                    repeats = task.generate_repeats(repeat_map[t_repeat])
                    for repeated_task in repeats:
                        owner.add_task(t_pet.pet_id, repeated_task)
                    st.success(f"Task '{t_desc}' added to {t_pet.name} ({1 + len(repeats)} occurrences)!")
                else:
                    st.success(f"Task '{t_desc}' added to {t_pet.name}!")
                st.rerun()

    # ── Task filter dropdown ─────────────────────────────────────────────────
    filter_options = ["All tasks", "Completed tasks", "Incomplete tasks"] + [
        f"{pet.name}'s tasks" for pet in owner.pets
    ]
    task_filter = st.selectbox("View", filter_options, key="task_filter")

    # Build (pet, task) pairs based on selected filter
    filtered: list[tuple] = []
    for pet in owner.pets:
        for task in pet.tasks:
            if task_filter == "All tasks":
                filtered.append((pet, task))
            elif task_filter == "Completed tasks" and task.is_completed:
                filtered.append((pet, task))
            elif task_filter == "Incomplete tasks" and not task.is_completed:
                filtered.append((pet, task))
            elif task_filter == f"{pet.name}'s tasks":
                filtered.append((pet, task))

    if filtered:
        for pet, task in filtered:
            status = "✅" if task.is_completed else "⬜"
            cols = st.columns([4, 1, 1])
            with cols[0]:
                st.markdown(
                    f"{status} **{pet.name}** — `{task.time}` [{task.priority.upper()}] "
                    f"{task.description} — {task.date} ({task.frequency})"
                )
            with cols[1]:
                if not task.is_completed and st.button("Done", key=f"done_{task.task_id}"):
                    task.mark_complete()
                    st.rerun()
            with cols[2]:
                if st.button("Delete", key=f"del_{task.task_id}"):
                    owner.remove_task(pet.pet_id, task.task_id)
                    st.rerun()
    else:
        pink_info("No tasks match this filter.")

st.divider()

# ════════════════════════════════════════════════════════════════════════════
# SECTION 4 — Preferences
# Lets the owner set care preferences including feeding schedule, spending rate, and walk time/duration.
# Saved preferences are displayed as a summary below the form.
# ════════════════════════════════════════════════════════════════════════════
st.subheader("Preferences")

if not owner.pets:
    pink_info("Add a pet first before setting preferences.")
else:
    with st.expander("Set preferences"):
        with st.form("pref_form"):
            pref_pet      = st.selectbox("Select pet", options=owner.pets, format_func=lambda p: p.name)
            pref_feeding  = st.text_input("Feeding schedule", value="twice daily")
            pref_spending = st.selectbox("Spending rate", ["low", "medium", "high"], index=1)
            pref_walk_time = st.text_input("Preferred walk time", value="07:00")
            pref_walk_dur  = st.number_input("Walk duration (minutes)", min_value=5, max_value=120, value=30)
            save_pref = st.form_submit_button("Save preferences")

        if save_pref:
            pref_pet.set_preference(
                Preference(
                    feeding_schedule=pref_feeding,
                    spending_rate=pref_spending,
                    preferred_walk_time=pref_walk_time,
                    walk_duration_minutes=int(pref_walk_dur),
                )
            )
            msg = st.empty()
            msg.success(f"Preferences saved for {pref_pet.name}!")
            time.sleep(3)
            msg.empty()
            st.rerun()

    for pet in owner.pets:
        if pet.preference:
            p = pet.preference
            st.markdown(
                f"**{pet.name}** — Feeding: {p.feeding_schedule} | Spending: {p.spending_rate} | "
                f"Walk at {p.preferred_walk_time} for {p.walk_duration_minutes} min"
            )

st.divider()

# ════════════════════════════════════════════════════════════════════════════
# SECTION 5 — Schedule
# Generates a daily schedule for a selected date by sorting all pets' tasks by time and priority.
# Displays the result and keeps a collapsible history of all previously generated schedules.
# ════════════════════════════════════════════════════════════════════════════
st.subheader("Generate Schedule")

sched_date = st.date_input("Schedule date", value=date.today(), key="sched_date")

if st.button("Generate schedule"):
    if not owner.pets:
        st.warning("Add at least one pet before generating a schedule.")
    else:
        scheduler = owner.generate_daily_plan(sched_date, sched_date)
        if not scheduler.tasks:
            pink_info(f"No tasks found for {sched_date}.")
        else:
            st.success(f"Schedule for {sched_date} — {len(scheduler.tasks)} task(s)")
            for task in scheduler.tasks:
                status = "✅" if task.is_completed else "⬜"
                st.markdown(
                    f"{status} `{task.time}` [{task.priority.upper()}] {task.description}"
                )

if owner.daily_plans:
    with st.expander(f"Past schedules ({len(owner.daily_plans)})"):
        for sched in reversed(owner.daily_plans):
            st.markdown(
                f"**{sched.scheduled_date}** — generated at "
                f"{sched.generated_at.strftime('%H:%M')} | {len(sched.tasks)} task(s)"
            )
