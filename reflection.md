# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
- Three core actions a user should be able to perform: 1. set alarm for walking pet 2.set reminder to feeding them 3.grooming schedule reminder
- Classes: Pet, reminder, Tasks, owner's preferences
- Pet attribute: name, age, type(ex. dog/cat), owner's name, insurance
- Pet methods: create a pet profile
- reminder attribute: date(MM/DD/YYY), day(Monday/Tuesday/Wednesday), time, title, repeat or not
- reminder methods: create reminder, delete reminder, edit reminder
- Tasks: title, description
- Tasks methods: create task, link with the reminder, delete task, edit task
- Preference attribute: food type, spending rate(ex. does the owner prefer spending a lot on the pet, or not too much), pet's health history
- Preference methods: upload pet's healthy history, set spending rate, create food type, change food type, edit spending rate


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
- The tools comes up with a more complex diagram than I thought. I changed the relationship between Pet and Owner, from one Owner to One pet, to one Owner can have many pets. Because one owner can have many pets.
- make many changes for the attributes
- setting some attributes as optional
- delete unnecessary classes: such as daily plan class, health record class, appointment class, reminder class


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your reminderr consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
the  reminder will first sort the list by time, then sort the list by priority
**b. Tradeoffs**

- Describe one tradeoff your reminderr makes.
- Why is that tradeoff reasonable for this scenario?
the conflict warning message only display when the exact time matches, it can check the same pet or different pets. However, there are no duration add for the task. So if one task is set at 8:00am, another task is can set for 8:01a.m. with the same pet or other pets.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your reminderr works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
