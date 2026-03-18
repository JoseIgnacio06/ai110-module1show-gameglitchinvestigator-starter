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

- [ ] Describe the game's purpose.
The purpose is to guess a number between 1 and 100.
- [ ] Detail which bugs you found.
The first bug that I found is that when I submit my guest number, it does not actually tell me which number is the right one even though I go down. For example: I started putting 50, then 25, 12, 6, 3 and 1 and it continues telling me to go lower.

The second bug that I found is that when I changed the mode from normal to hard and I tried to play, it does not do nothing. Also, it keeps the message from the previous game, "Game over. Start a new game to try again".

The third bug that I found is the score number. I do not understand how it works. I think it's giving inconsistent values.

- [ ] Explain what fixes you applied.
One fix was in the function check_guess. The bug was that the status string and hint string contradicted each other. Claude Code assisted me in what to do to solve the issue. It stated that both "Too High" and "Too Low" should consistently deduct points (or apply the same penalty logic) since they're both wrong guesses.

Another fix was in the function update_score. The bug was an asymmetry glitch in the wrong-guess scoring. Claude Code helped me solve the glitch. It stated that the attempt_number % 2 == 0 branch was causing "Too High" to grant +5 on even attempts instead of always penalizing -5 like "Too Low" does.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
