# AI-use log

## Interaction 1
Date: October 4, 2026
Assistant: ChatGPT
Purpose: Understand how GitHub Desktop and Python work together.
Prompt or summary: I asked whether I could create Python code using GitHub Desktop.

### Suggestion accepted
What did the AI suggest?
The AI explained that GitHub Desktop is used to manage the Git repository, while a code editor such as VS Code is used to write Python code and Python is used to run it.

Why did I accept it?
This explained how the different programs work together and helped me set up my Python project.

What evidence supported the decision?
I was able to create and run my Python plugin using the repository.

## Interaction 2
Date: October 4, 2026
Assistant: ChatGPT
Purpose: Fix my plugin not being detected by the plugin runner.
Prompt or summary: I explained that my plugin was in the `plugins` folder but the program was not finding it.

### Suggestion revised
What did the AI suggest?
The AI suggested naming the plugin `yes_no_plugin.py` instead of `yes-no-plugin`.

What did I change?
I changed the filename so that it had the `.py` extension and used underscores.

Why did I change it?
My original file did not have the `.py` extension. After adding `.py`, the plugin was successfully detected and ran.

## Interaction 3
Date: October 4, 2026
Assistant: ChatGPT
Purpose: Add random Yes/No responses with adjustable probability.
Prompt or summary: I asked how to make the plugin randomly choose Yes or No and later wanted multiple statements for each result.

### Suggestion rejected
What did the AI suggest?
The AI suggested using four separate lists: Yes words, Yes statements, No words, and No statements.

Why did it not fit the repository or issue?
I thought this was unnecessarily complicated. I wanted the plugin to be easier to edit, so I chose to use only two lists: one for complete Yes responses and one for complete No responses.

Related issue: Yes/No plugin response design
Related branch or pull request: Not specified


## Interaction 4 
Date: October 4, 2026
Assistant: ChatGPT
Purpose: Understand and implement weights and the `k` parameter in Python's random.choices().
Prompt or summary: I asked how to use weights with Yes/No options and what `k=1` meant.

### Suggestion accepted
What did the AI suggest?
The AI showed me how to use `random.choices()` with weights to control the probability of each option. It also explained that `k=1` tells Python to select one result.

Why did I accept it?
I accepted the suggestion because it allowed me to control the probability of each option and helped me understand how the `k` parameter works.

What evidence supported the decision?
I was able to use separate variables for the options and their weights, and I understood that `k=1` means the program selects one result.

Related issue:
Related branch or pull request:
