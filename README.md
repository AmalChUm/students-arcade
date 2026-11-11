# Students Arcade

A Python plugin launcher for student contributions. The existing launcher is `main.py`; plugin modules are stored in `plugins/`.

## Run locally

Keep `main.py` and the `plugins` folder together. Open `main.py` in Python IDLE and select **Run > Run Module**.

The launcher discovers plugin modules, calls their `run()` functions when present, and prints results. Modules without `run()` are skipped. Plugin import and runtime exceptions are printed rather than automatically failing the entire launcher.

## Continuous integration

`.github/workflows/arcade-ci.yml` validates relevant pushes and pull requests targeting `main`, and supports manual execution when available on the default branch. It uses Python 3.12, compiles Python files, and runs the launcher with a 20-second timeout.

## Continuous delivery

`.github/workflows/arcade-cd.yml` runs on pushes to `main` or manual dispatch. It validates the source, saves launcher output in `run-log.txt`, and uploads `students-arcade-release.zip` as the `students-arcade-release` Actions artifact.

The release includes the launcher, plugins, README, license, run log, and requirements file if present. Git history, virtual environments, and Python caches are not included.

Download and extract the artifact, extract the release ZIP if necessary, then open `arcade-release/main.py` in IDLE and select **Run > Run Module**.
