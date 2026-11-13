12. How does the launcher find Python files in plugins/?
 - It uses the defined function "discover_plugins". The function first looks to ensure it is in the correct directory when searching for plugins. Then the function checks to ensure the module name starts with an underscore "_". Then the function attempts to return all modules following these conditions.
13. What happens when a plugin does not define run()?
 - The module returns "no run() function defined" along with identifying information about the plugin missing the run() function.
14. What happens when a plugin raises an exception?
 - The infromation "print(f"  [error] run() raised: {exc}")" is printed to the terminal, describing the error that occurred from exception.
15. Why could an interactive plugin cause an automated workflow to hang?
 - It could block further execution of the workflow -- like if I had kept my rockpaperscissors.py active, it could cause the execution to hang because it requires an input from the user, which an automated workflow does not do.
16. Why is it useful to run the launcher automatically in a pull request?
 - To get an execution status message in the workflow upon pull request!