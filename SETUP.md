# Setup
## Environment Setup Guide
Before using this repo, make sure you’ve completed the [environment setup guide](https://github.com/UofT-DSI/onboarding/blob/main/environment_setup/README.md), which installs the core tools you’ll need for this module, such as:

- Git  
- Git Bash (for Windows)  
- Visual Studio Code
- UV

## Necessary Packages
This project uses its own isolated environment called `ds4-env` so that packages don’t conflict with other projects. 
We use UV to create this environment, activate it, and install the required packages listed in the module’s `pyproject.toml`.  
This setup only needs to be done **once per module**, after that, you just activate the environment whenever you want to work in this repo.  


Open a terminal (macOS/Linux) or Git Bash (Windows) in this repo, and run the following commands in order:

1. Create a virtual environment called `ds4-env`:
    ```
    uv venv ds4-env --python 3.11
    ```

2. Activate the environment:
    - for macOS/Linux:
        ```
        source ds4-env/bin/activate
        ```
        
    - for windows (git bash):    
        ```
        source ds4-env/Scripts/activate
        ```

3. Install all required packages from the [pyproject.toml](./pyproject.toml)
    ```bash
    uv sync --active
    ```

## Environment Usage
In order to run any code in this repo, you must first activate its environment.
- for macOS/Linux:
    ```
    source ds4-env/bin/activate
    ```
    
- for windows (git bash):    
    ```
    source ds4-env/Scripts/activate
    ```

When the environment is active, your terminal prompt will change to show:  
```
(ds4-env) $
```
This is your **visual cue** that you’re working inside the right environment.  

When you’re finished, you can deactivate it with:  
```bash
deactivate
```

## Modules installed at a later date
We may need other modules down the line. We could update the list here so everyone on the team could run to get their code working. After running any of the following commands, you may need to run `uv sync --active` and restart your notebook to pick up the changes.
List of commands for adding modules that are installed at a later date:
```
uv add statsmodels
uv add prince
uv add graphviz
uv add dtreeviz
uv add kmodes
uv add xgboost 
```

> **👉 Remember**   
> Only one environment can be active at a time. If you switch to a different repo, first deactivate this one (or just close the terminal) and then activate the new repo’s environment.

---

