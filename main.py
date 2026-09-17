import importlib
import pkgutil
import plugins

print("==========================================")
print("     WELCOME TO THE CLASSROOM ARCADE      ")
print("==========================================\n")

# Dynamically find and import all Python files inside the /plugins folder
for _, module_name, is_pkg in pkgutil.iter_modules(plugins.__path__):
    if is_pkg or module_name.startswith("__"):
        continue

    # Load module dynamically
    module = importlib.import_module(f"plugins.{module_name}")

    # Check for required properties and execution function
    if hasattr(module, "run"):
        author = getattr(module, "AUTHOR", "Unknown Student")
        app_name = getattr(module, "APP_NAME", module_name)
        
        print(f"Running '{app_name}' by {author}:")
        try:
            result = module.run()
            print(f"  ↳ {result}\n")
        except Exception as e:
            print(f"  ↳ ❌ Error executing script! {e}\n")