# Contribution Plan

**Issue:** Add an even-or-odd checker plugin  
**Forked Issue URL:** https://github.com/moeshaw/students-arcade/issues/1  
**Original Issue URL:** https://github.com/AmalChUm/students-arcade/issues/61  
**Selected Difficulty:** Beginner  
**Proposed Branch:** `feature/even-or-odd-plugin`  
**Expected Files:** `plugins/even_odd_plugin.py`

## My Interpretation of the Task

Create a plugin that selects an integer and determines whether the number is even or odd.

The plugin should define a `run()` function that selects an integer, checks its classification, and displays the selected integer along with whether it is **even** or **odd**.

The existing `main.py` should discover and run the plugin automatically. `main.py` should not be modified.

## Acceptance Criteria

- [ ] The new file is placed in `plugins/` with a unique descriptive filename.
- [ ] The module defines `AUTHOR`, `APP_NAME`, and `run()`.
- [ ] The module uses only the Python standard library.
- [ ] `python main.py` discovers and runs the plugin.
- [ ] The output displays the selected integer and whether it is even or odd.
- [ ] The output is readable.
- [ ] The pull request explains the verification.

## Possible Risks or Questions

- Should the plugin select the integer randomly, or is any valid integer acceptable?
- What range should be used when selecting the integer?
- Should the output follow the formatting conventions used by the existing plugins?
- I will review the existing plugins before implementing the new one so the plugin follows the project's expected structure.

# Contribution Plan

**Issue:** Add an even-or-odd checker plugin  
**Forked Issue URL:** https://github.com/moeshaw/students-arcade/issues/1  
**Original Issue URL:** https://github.com/AmalChUm/students-arcade/issues/61  
**Selected Difficulty:** Beginner  
**Proposed Branch:** `feature/even-odd-plugin`  
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

