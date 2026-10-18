# Random number addition contribution plan

Contributor: Andrew Haralambous (aharalam)
Original plugin author: Gaige Szy (ginishima)
Issue: https://github.com/AmalChUm/students-arcade/issues/18
Pull request: https://github.com/AmalChUm/students-arcade/pull/66
Branch: feature/issue-18-random-addition

This plan consolidates the original Lab 9 plan (kept with the course submission) and the follow-up work requested in ginishima's October 15, 2026 review. It is being added during the review follow-up, not presented as a newly discovered original artifact.

## Goal and scope

Replace the fixed 18 + 21 calculation with two random integers from 1 to 100. Display both operands and their correct sum without requiring user input. Keep AUTHOR, APP_NAME, and run(), preserve the MIT license and original credit, and leave main.py and unrelated plugins unchanged.

## Work

1. Generate two integers using the standard-library random module.
2. Return a readable equation with a completion label.
3. Rename plugins/ginishima.py to plugins/random_addition.py so the filename describes its activity.
4. Credit Gaige Szy and Andrew Haralambous in the launcher; retain the original author's credit.
5. Explain why random values avoid interactive prompts in the launcher.
6. Verify boundary sums, 100 random results, and launcher discovery without duplicate execution.
7. Keep issue #18 in In Review on the student's project board while awaiting review.

## Acceptance and verification

- Random behavior and the 1..100 inclusive range are documented in the function docstring.
- Boundary examples: 1 + 1 = 2, 100 + 100 = 200, 1 + 100 = 101.
- Every displayed sum equals the two displayed operands.
- python main.py discovers Number Addition exactly once, with both contributors credited.
- No input validation is necessary because this version does not accept user input.
- Run python -m unittest discover -s tests -v and python main.py.
- Preserve the existing launcher, license, and unrelated plugins.

## AI assistance

Codex helped implement the changes, draft this plan, and run automated checks.
