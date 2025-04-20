# Reapy-next, reapy package lives on

This is a project to continue the legacy of https://github.com/RomeoDespres/reapy since 2025. 

- The goal is to keep Reapy living on and make the fun automation happened in the current Python and Reaper versions.
- The original Reapy package hasn't been updated in a long time. 
I attempted to submit a bug fixes causing fx methods not working after reconnect long ago, but has not been handled. I assume the contributors have moved on.
- It is a cool project, so let's keep it aflow. And instead of keeping it a fork, this will be on its own.
- Unfortunately I have very little time to figure the documentations, helps appreciated!!!

## Official Reascript documentation

https://www.reaper.fm/sdk/reascript/reascript.php

## How to setup Reapy / Reascript

The guide is MacOS only currently, tested on Reaper v7.36

### Part 1 Reaper Setup

#### Enable Reascript

- Open Reaper Preferences (Settings), under `Plug-ins` -- `Reascript`, select **Enable Python for use with ReaScript**. 
- The next field is: **Custom path to Python dll directory**
    - On Apple Silicon with Python installed using `homebrew`, you can find the `libpython$PYTHON_VERSION.dylib` in `/opt/homebrew/opt/python@$PYTHON_VERSION/Frameworks/Python.framework/Versions/$PYTHON_VERSION/lib`, relace $PYTHON_VERSION with the version you intend to use, e.g. 3.12.
    - If you are unsure how to find it you can run: `python3.12 -c "import sys; print(sys.prefix)"` to get the folder before `lib`, the the dylib file in like in `./lib` or `./lib/python3.12/config-3.12-darwin/`
- In the dylib file, type in the name of the dylib file, e.g `libpython3.12.dylib`
- Restart Reaper

### Part 2 Python package

- `pip install reapy`
- For local dev:
    - Under your virtual environment, navigate to the root folder of this project
    - `pip install -e .`
- Run `python -c "import reapy; reapy.configure_reaper()"`
    - You may see this message:
    ```
    DisabledDistAPIWarning: Can't reach distant API. Please start REAPER, or call reapy.config.enable_dist_api() from inside REAPER to enable distant API.
  warnings.warn(errors.DisabledDistAPIWarning())
    ```
    - Don't worry just restart Reapy and Python that is it!
- Test the installation with: `python -c "import reapy; reapy.print('a message')"`
- Check Reaper there should be a console log message.

### Optional: For uninterrupted automation

This part is not conpulsory for Reapy/Reascript to work, but it disabled certain features to make automation more repreducible. 

Open Preferences on Reaper

    - In `General`, uncheck automatic update version check in Startup Settings. (Better for CI automation)

    - General --> Open project(s) on startup to -- New project (ignore default template)

    - Project --> Project loading uncheck prompt when files are not found on project load (This can break automation)

    - Audio --> Recording uncheck all options in Prompt to save/delete/rename new files

    - Audio --> Rendering check Automatically close render window when render has finished

## Quick guide:

Refer to `examples` folder.

### Using ReaScript API directly

Not all API are implemented in reapy currently. You can find available API in:
https://www.reaper.fm/sdk/reascript/reascripthelp.html

```python
from reapy import reascript_api as RPR

print(RPR.GetProjectName())
```

### Interact with UI with Perform Action

Action list can be found in: https://raw.githubusercontent.com/Ultraschall/ultraschall-lua-api-for-reaper/Ultraschall-API-4.6/ultraschall_api/misc/misc_docs/Reaper-ActionList.txt



### Use Action ID:

You can find available action ID in:

https://raw.githubusercontent.com/Ultraschall/ultraschall-lua-api-for-reaper/Ultraschall-API-4.6/ultraschall_api/misc/misc_docs/Reaper-ActionList.txt

```python
import reapy
project = reapy.Project()
track = project.tracks[0].select()
project.perform_action(40701)
```