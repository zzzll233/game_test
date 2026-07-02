# Copilot Instructions for this Repository

This repository is a small Python learning project with standalone script files. There is no package manager, test framework, or CI configuration in the repo.

## Key files
- `hello.py` - simple startup/test script that prints environment status.
- `lesson2_variable.py` - standalone variable-check script with Chinese comments and direct print output.
- `lesson3_login_test.py` - currently empty placeholder for a login test example.

## What to do
- Keep changes simple and script-oriented. New functionality should fit the existing pattern of standalone `.py` files.
- Use direct `print(...)` output and simple control flow instead of introducing frameworks unless the user explicitly requests them.
- Preserve the repository style: file-based lessons, Chinese comments/strings when appropriate, and no hidden dependency assumptions.
- If extending the project, follow naming like `lessonX_description.py`.

## Workflow
- Run scripts from the repo root with Python: `python hello.py`, `python lesson2_variable.py`, or `python lesson3_login_test.py`.
- Do not assume `pytest`, `pipenv`, `requirements.txt`, or similar build/test tooling exists unless added explicitly.

## What to avoid
- Do not invent external dependencies or a build system that is not present in the repository.
- Do not refactor the project into a package/module layout unless the user asks for a larger architectural change.
- Avoid adding CI/automation config files unless the user requests repository automation.

## Agent-specific guidance
- The codebase is a learning/demo repo, not a production application. Prioritize clarity and simple examples.
- When asked to implement tests or new lessons, keep them self-contained in new or existing lesson scripts.
- If a file is currently empty, like `lesson3_login_test.py`, treat it as a placeholder and ask the user if they want a specific test scenario implemented.

## Feedback requested
If any of the workflow assumptions are unclear or if you want the instructions to include information on future test tooling or automation, tell me and I will refine this file.