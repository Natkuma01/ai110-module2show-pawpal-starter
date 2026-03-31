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
on writing code, debugging, explaining the code
- What kinds of prompts or questions were most helpful?
The most helpful prompt is "How could this algorithm be simplified for better readability or performance?" in Phase 4 step 5. Sometimes AI use complicated stratergy, using this prompt can check if there are a simple way to implement the code.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
I did not accept the AI suggestion for using the list comprehension to find any tasks that are the same time. It is less code, and less space complexity. Using regulare loop need extra space complexity for variable. However, I think it makes the code easier to read. That one extra space is affordable.
- How did you evaluate or verify what the AI suggested?
I will make sure if the suggestion make sense or not. For instance when creating the class diagram at the beginning. The AI suggest to have one to one relationship between the Owner class and the Pet class. When think about it, an owner can have more than one pet. I evaluate the suggestion with real-world cases, to make sure the project is practical.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- add task
- properly sort all tasks by time then by priority
- able to set daily task for the next following day
- ensure task status changed after marked as completed

- Why were these tests important?
these tests are important because they are the essential functions of the app,
if these functions are not working, the app fail

**b. Confidence**

- How confident are you that your reminderr works correctly?
I'm confidence the reminder works correctly but it still can cause time conflicts.
Right now there are no duration for each task. Therefore, two tasks can be only have one minute gap, this cause time conflict. It do not allow add task at the same time.

- What edge cases would you test next if you had more time?
First I will add the duration for each task. Then I will test on - if I can add task during the task. For example if task A is 6:00a.m. to 7:00a.m. , I will try to add a task at 6:16a.m. see if the system let me to add that.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
small features such as displaying warning message, add avatar in create pet form, AI get it done quickly
Most satisfied with the list of tasks that can display either completed, incompleted, and pet's name

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I will list more details on requirements. Add duration for each task so make sure it does not overlapping. Also if for specific task such as walking dog - it should be ok to overlap because one person can walk more than one dog. If I have more time, I would like to make this more practical, more peronsalize for pets owners

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
clear instruction
use simple and direct prompt
observate(or read) what the AI is trying to do after type in the prompt
