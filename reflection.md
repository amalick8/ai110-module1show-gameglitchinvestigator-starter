# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|------------|-------------------|-----------------|---------------|
| Guess of 50 (secret: 77) | "Too Low" | "Too High" | none |
| Correct guess after reset | "You Win!" | "Go Higher" | none |
| Typed "five" | "Use digits not words" | "That is not a number" | none |
---

## 2. How did you use AI as a teammate?

I used Claude (claude.ai) as my AI assistant throughout this project.

**Correct AI suggestion:** Claude correctly identified that the core bug was caused by 
the secret number being converted to a string on every even attempt using 
`str(st.session_state.secret)`. This caused Python to compare an integer guess against 
a string secret, which broke the hints completely. I verified this was correct by opening 
the Developer Debug Info expander in the game, noting the secret number, then guessing 
numbers above and below it and confirming the hints were now accurate after removing 
the string conversion.

**Incorrect/misleading AI suggestion:** Claude initially told me to place the fix line 
`outcome, message = check_guess(guess_int, st.session_state.secret)` at the very top 
of app.py right after the imports. This was wrong because `guess_int` does not exist 
at that point in the code — it only gets created later inside the `if submit:` block. 
I caught this by running the app and seeing an error, then realized the fix needed to 
go inside the submit block where `guess_int` is actually defined.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed by doing two things: first testing it manually in the 
live game by using the Developer Debug Info expander to see the secret number and then 
guessing around it to confirm the hints were correct, and second by running pytest to 
confirm all 11 automated tests passed.

One specific test that was helpful was `test_guess_too_low()` which calls 
`check_guess(30, 77)` and asserts the outcome equals "Too Low". Before the fix this 
would have failed because the string conversion bug was making comparisons unreliable. 
After the fix it passed cleanly, which gave me confidence the logic was correct.

Claude helped me understand what each test was checking and why — for example explaining 
that `assert` is like a guarantee statement that makes the test fail loudly if the code 
behaves unexpectedly, which is exactly what you want in automated testing.

---

## 4. What did you learn about Streamlit and state?

Streamlit is unusual because every time you click a button or type something, the entire 
Python script reruns from the very top. This means any regular variable you create would 
reset to its starting value on every single click, which would make a game impossible 
to build since your score and attempts would disappear instantly.

Session state solves this by acting like a sticky notepad that survives every rerun. 
You store things like the secret number, attempt count, and score inside 
`st.session_state` and they stay saved between reruns. I would explain it to a friend 
like this: imagine if every time you blinked your eyes, your memory wiped clean — 
session state is like writing things down on a notepad so you still know what happened 
after you blink.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is adding a `# FIXME:` comment directly 
in the code at the exact line where I suspect the bug is before I start fixing anything. 
It forces me to actually understand where the problem is rather than just randomly 
changing things and hoping it works. It also gives AI tools a precise location to focus 
on rather than guessing.

Next time I work with AI on a coding task I would read the suggested changes more 
carefully before applying them, especially checking that any new lines of code are placed 
in the right location and that variables being referenced actually exist at that point 
in the program.

This project changed how I think about AI generated code because I used to assume that 
if AI wrote it or suggested it, it was probably correct — but this project showed me 
that AI can introduce subtle bugs like the string conversion issue that look reasonable 
at first glance but completely break the logic, which means a human always needs to 
verify and test everything the AI produces.
