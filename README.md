# Students Arcade

Students Arcade runs Python activities from the `plugins/` folder using the existing `main.py` launcher.

## Run locally

From the project folder, run:

```bash
python main.py
```

Plugins provide `AUTHOR`, `APP_NAME`, and a non-interactive `run()` function. The launcher skips modules without `run()` and reports caught plugin exceptions.

## GitHub Actions

- `.github/workflows/arcade-ci.yml` checks Python syntax and runs the launcher with a 20-second timeout.
- `.github/workflows/arcade-cd.yml` checks and runs the project, saves output in `run-log.txt`, and uploads `students-arcade-release.zip` as an Actions artifact.

To run the downloaded package, extract it, open the `arcade-release` folder, and run `python main.py`.
