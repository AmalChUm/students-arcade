# AI Use Log

## Interaction 1

**Prompt/Summary:**  
I asked how I could keep my original `random.choices()` and weights while creating the Even/Odd plugin.

**AI Suggestion:**  
Select the Even or Odd category using weights first, then generate an integer that matches that category.

**Decision:** Accepted.

**Reason:**  
This matched the approach I wanted and allowed me to keep the probability values adjustable.

---

## Interaction 2

**Prompt/Summary:**  
I asked how to make the integer range adjustable.

**AI Suggestion:**  
Use additional variables and more complicated range logic to handle different minimum and maximum values.

**Decision:** Rejected.

**Reason:**  
The suggested solution was more complicated than I wanted for this assignment. I wanted to keep my code simple and similar to my original plugin.

---

## Interaction 3

**Prompt/Summary:**  
I asked for an alternative to using a `while` loop to select an integer matching the Even/Odd category.

**AI Suggestion:**  
Use `random.randrange()` with a step of 2 to directly select an even or odd integer.

**Decision:** Rejected.

**Reason:**  
I wanted to keep my implementation closer to the code I had already developed and understood.

---

## Interaction 4

**Prompt/Summary:**  
I asked whether my weighted Even/Odd approach was too complicated for a beginner assignment.

**AI Suggestion:**  
The approach was reasonable because it reused the probability and `random.choices()` concepts from my previous plugin.

**Decision:** Rejected.

**Reason:**  
I decided to use my own judgment about the complexity of the code and keep the implementation focused on the requirements of the issue.
