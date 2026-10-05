# Contribution Plan

**Issue:** Create a Yes-or-No plugin  
**Forked Issue URL:** https://github.com/moeshaw/students-arcade/issues/1  
**Original Issue URL:** https://github.com/AmalChUm/students-arcade/issues/61 
**Selected Difficulty:** Beginner  
**Proposed Branch:** `feature/issue-61-yes-no-plugin`  
**Expected Files:** `plugins/yes_no_plugin.py`

## My Interpretation of the Task

Create a plugin that randomly returns either **Yes** or **No** with a short explanatory phrase.

The plugin should define a `run()` function that randomly selects Yes or No and displays the result along with a short explanation.

The existing `main.py` should discover and run the plugin automatically. `main.py` should not be modified.

## Acceptance Criteria

- [ ] The new file is placed in `plugins/` with a unique descriptive filename.
- [ ] The module defines `AUTHOR`, `APP_NAME`, and `run()`.
- [ ] The module uses only the Python standard library.
- [ ] `python main.py` discovers and runs the plugin.
- [ ] The output clearly displays either Yes or No.
- [ ] The result includes a short explanatory phrase.
- [ ] The output is readable.
- [ ] The pull request explains the verification.


## Possible Risks or Questions

- Should Yes and No have an equal 50/50 probability?
- Should the explanatory phrase be randomly selected from multiple phrases?
- Should there be a different explanation for Yes and No?
- I will review the existing plugins before implementing the new one so the plugin follows the project's expected structure.

# Contribution Plan

**Issue:** Add an even-or-odd checker plugin  
**Forked Issue URL:** https://github.com/moeshaw/students-arcade/issues/2  
**Original Issue URL:** https://github.com/AmalChUm/students-arcade/issues/45  
**Selected Difficulty:** Beginner  
**Proposed Branch:** `feature/issue-45-even-odd-plugin`  
**Expected Files:** `plugins/even_odd_plugin.py`

## My Interpretation of the Task

Create a plugin that selects an integer and reports whether it is **even** or **odd**.

The plugin will use a `run()` function to select an integer, determine its classification, and display the integer along with whether it is even or odd.

The plugin should work with the existing `main.py` discovery system without modifying `main.py`.

## Acceptance Criteria

The new file is placed in `plugins/` with a unique descriptive filename.

The module defines `AUTHOR`, `APP_NAME`, and `run()`.

The module uses only the Python standard library.

`python main.py` discovers and runs the plugin.

The output displays the selected integer and its classification.

The output is readable and the pull request explains the verification.

## Possible Risks or Questions

- Should the integer be selected randomly?
- What range of integers should be used?
- Should the plugin include negative numbers and zero?
- How do i take the user input if i cant modify the main.py?

