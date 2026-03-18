# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
What I saw was a simple game.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first bug that I found is that when I submit my guest number, it does not actually tell me which number is the right one even though I go down. For example: I started putting 50, then 25, 12, 6, 3 and 1 and it continues telling me to go lower.

The second bug that I found is that when I changed the mode from normal to hard and I tried to play, it does not do nothing. Also, it keeps the message from the previous game, "Game over. Start a new game to try again".

The third bug that I found is the score number. I do not understand how it works. I think it's giving inconsistent values.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I was solving for the function check_guess, it suggested me that if guess was too high, then it goes lower same as if guess was too low, it goes higher.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At one point, the AI suggested a pytest for update_score that used parameters my function didn’t actually accept. It assumed the function signature included guess_relation="low" and guess_relation="high", which wasn’t true in my code.
I verified the mistake by: checking my actual function definition, running the suggested test, which immediately failed with a TypeError and rewriting the test to match the real parameters.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
When I ran a pytest, it gave me the right output.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a pytest for the function check_guess and it showed that has both the status string and the hint string fully correct.
- Did AI help you design or understand any tests? How?
Yes. When I asked Claude to do a pytest, it provided me suggestions that I could understand and were correct.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the entire script from top to bottom every time the user interacts with the page. Since the original code generated the secret number at the top of the file, it created a new number on every rerun. That made the game impossible to win.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain it like this: Streamlit behaves like a “live notebook.” Every time you click a button or type something, Streamlit restarts the script from the beginning. To keep values from disappearing during these reruns, Streamlit gives you a special dictionary called st.session_state where you can store things that should persist—like a secret number in a guessing game.
- What change did you make that finally gave the game a stable secret number?
I fixed the issue by storing the secret number inside st.session_state and only generating it if it didn’t already exist.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to keep using the habit of writing targeted pytest cases immediately after fixing a bug. It forced me to understand the bug deeply, and it gave me confidence that the fix actually worked. It also prevented regressions when I made later changes.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will verify AI-generated code more carefully before trusting it. I learned that AI can produce convincing but incorrect suggestions, so I want to treat it as a collaborator, not an authority.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI is great for brainstorming, debugging, and speeding up repetitive tasks, but it still requires human judgment. AI can accelerate development, but it can’t replace understanding the code yourself.
