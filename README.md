# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number guessing game where the player tries to guess a secret number within a limited number of attempts. The player receives hints after each guess telling them to go higher or lower. The score decreases with each wrong guess and increases when the player wins.

**Bugs Found:**
1. Hints were reversed — the game was converting the secret number to a string on even attempts, causing incorrect comparisons between integers and strings
2. New game button was not resetting all state — score, status, and history were carrying over from the previous game
3. Input parsing gave a misleading error message — typing a word like "five" returned "That is not a number" when it should explain to use digits instead

**Fixes Applied:**
1. Removed the string conversion logic in app.py and always pass the integer secret directly to check_guess()
2. Updated the new game reset to clear all session state including score, status, and history
3. Improved the error message in logic_utils.py to say "Please enter a number using digits (e.g. 5, not 'five')"
4. Refactored all core logic functions out of app.py and into logic_utils.py where they belong

## 📸 Demo Walkthrough

1. User opens the game and selects Normal difficulty (range 1 to 100, 8 attempts)
2. User enters a guess of 40 — game returns "📈 Go HIGHER!" and score decreases by 5
3. User enters a guess of 80 — game returns "📉 Go LOWER!" and score decreases by 5
4. User enters a guess of 60 — game returns "📈 Go HIGHER!" and score decreases by 5
5. User enters a guess of 70 — game returns "📈 Go HIGHER!" and score decreases by 5
6. User enters a guess of 77 — game returns "🎉 Correct!" and score increases with win bonus
7. Game ends and displays final score — clicking New Game resets everything cleanly

## 🧪 Test Results

```
platform darwin -- Python 3.11.1, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/ammarmalick/Documents/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.12.1
collected 11 items

tests/test_game_logic.py ...........                    [100%]

======================================== 11 passed in 0.01s =========================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
