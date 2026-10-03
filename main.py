import importlib
import pkgutil
import plugins


def discover_plugins():
    """Return a list of plugin modules that are importable and define run()."""
    modules = []
    for _, module_name, is_pkg in pkgutil.iter_modules(plugins.__path__):
        if is_pkg or module_name.startswith("__"):
            continue
        module = importlib.import_module(f"plugins.{module_name}")
        if hasattr(module, "run"):
            modules.append(module)
    return modules


def run_plugin(module):
    """Run a single plugin module and print its result."""
    author = getattr(module, "AUTHOR", "Unknown Student")
    app_name = getattr(module, "APP_NAME", module.__name__)

    print(f"Running '{app_name}' by {author}:")
    try:
        result = module.run()
        print(f"  \u21b3 {result}\n")
    except Exception as e:
        print(f"  \u21b3 \u274c Error executing script! {e}\n")


def run_all(modules):
    for module in modules:
        run_plugin(module)


def run_one(modules):
    if not modules:
        print("No plugins available to run.\n")
        return

    print()
    for i, module in enumerate(modules, start=1):
        app_name = getattr(module, "APP_NAME", module.__name__)
        print(f"  {i}. {app_name}")

    while True:
        choice = input("\nSelect a plugin number (or 'b' to go back): ").strip()
        if choice.lower() == "b":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(modules):
            print()
            run_plugin(modules[int(choice) - 1])
            return
        print("Invalid selection. Please enter a valid number or 'b'.")


# Presents the run-all / run-one / exit menu and dispatches to the right handler.
def prompt_run_mode(modules):
    while True:
        print("1. Run all plugins")
        print("2. Run one plugin")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            print()
            run_all(modules)
            return
        elif choice == "2":
            run_one(modules)
            return
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


def main():
    print("==========================================")
    print("     WELCOME TO THE CLASSROOM ARCADE      ")
    print("==========================================\n")

    modules = discover_plugins()
    prompt_run_mode(modules)


if __name__ == "__main__":
    main()