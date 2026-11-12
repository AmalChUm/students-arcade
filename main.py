
import importlib
import pkgutil
import pathlib

PLUGIN_DIR = pathlib.Path(__file__).parent / "plugins"


def discover_plugins():
    """Yield imported modules found in the plugins package."""
    if not PLUGIN_DIR.is_dir():
        return

    for module_info in pkgutil.iter_modules([str(PLUGIN_DIR)]):
        if module_info.name.startswith("_"):
            continue
        try:
            yield importlib.import_module(f"plugins.{module_info.name}")
        except Exception as exc:
            print(f"  [skipped] plugins/{module_info.name}.py failed to import: {exc}")


def main():
    print("=" * 50)
    print("PLUGIN RUNNER")
    print("=" * 50)

    count = 0
    for module in discover_plugins():
        author = getattr(module, "AUTHOR", "Unknown author")
        app_name = getattr(module, "APP_NAME", module.__name__)

        if not hasattr(module, "run"):
            print(f"\n{app_name} by {author}")
            print("  [skipped] no run() function defined")
            continue

        print(f"\n{app_name} by {author}")
        try:
            print(f"  {module.run()}")
            count += 1
        except Exception as exc:
            print(f"  [error] run() raised: {exc}")

    print("\n" + "=" * 50)
    print(f"Ran {count} plugin(s).")


if __name__ == "__main__":
    main()