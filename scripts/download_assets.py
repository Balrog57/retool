import os
import sys
import pathlib
import urllib.request

# Add current directory to path so imports work
sys.path.append(os.getcwd())

# Manually download internal-config.json first to bootstrap Config
config_dir = pathlib.Path('config')
config_dir.mkdir(exist_ok=True)
config_file = config_dir / 'internal-config.json'

url = 'https://raw.githubusercontent.com/Balrog57/retool-clonelists-metadata/main/config/internal-config.json'

print(f"Bootstrapping: Downloading {url} to {config_file}")
try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        with open(config_file, 'wb') as f:
            f.write(data)
    print("Bootstrap successful.")
except Exception as e:
    print(f"Bootstrap failed: {e}")
    sys.exit(1)

# Fake sys.argv[0] so Config uses the project root as base directory
# Config.retool_location uses pathlib.Path(sys.argv[0]).resolve().parent
# We want it to be the current working directory (project root)
sys.argv[0] = str(pathlib.Path(os.getcwd()) / 'retool.py')

# Now we can mock the environment and use Retool's native update function
# Now we can mock the environment and use Retool's native update function
try:
    from modules.config.config import Config
    import modules.constants as const
    from modules.clone_lists.update_clone_list_metadata import update_clonelists_metadata
    
    # Use real UserInput class to avoid missing attributes
    from modules.input import UserInput

    user_input = UserInput(update=True)

    print("Initializing Config...")
    
    # Instantiate Config with all required constants, matching retool.py
    config = Config(
        const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION,
        const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION_KEY,
        const.PROGRAM_DOWNLOAD_LOCATION,
        const.PROGRAM_DOWNLOAD_LOCATION_KEY,
        const.CONFIG_FILE,
        const.DAT_FILE_TAGS_KEY,
        const.IGNORE_TAGS_KEY,
        const.DISC_RENAME_KEY,
        const.VERSION_IGNORE_KEY,
        const.BUDGET_EDITIONS_KEY,
        const.PROMOTE_EDITIONS_KEY,
        const.DEMOTE_EDITIONS_KEY,
        const.MODERN_EDITIONS_KEY,
        const.LANGUAGES_KEY,
        const.REGION_ORDER_KEY,
        const.VIDEO_ORDER_KEY,
        const.CLONE_LISTS_KEY,
        const.METADATA_KEY,
        const.MIAS_KEY,
        const.RA_KEY,
        const.USER_CONFIG_KEY,
        const.USER_LANGUAGE_ORDER_KEY,
        const.USER_REGION_ORDER_KEY,
        const.USER_LOCALIZATION_ORDER_KEY,
        const.USER_VIDEO_ORDER_KEY,
        const.USER_LIST_PREFIX_KEY,
        const.USER_LIST_SUFFIX_KEY,
        const.USER_OVERRIDE_EXCLUDE_KEY,
        const.USER_OVERRIDE_INCLUDE_KEY,
        const.USER_FILTER_KEY,
        const.USER_GUI_SETTINGS_KEY,
        const.SYSTEM_SETTINGS_PATH,
        const.SANITIZED_CHARACTERS,
        const.RESERVED_FILENAMES,
        user_input
    )
    
    print(f"DEBUG: Config.retool_location = {config.retool_location}")
    print(f"DEBUG: Config.path_clone_list = {config.path_clone_list}")
    
    print("Starting full asset download...")
    # Run the update with no_exit=True so we don't kill the script
    # Pass None as gui_input, config handles logic based on it
    update_clonelists_metadata(config, None, no_exit=True)
    
    print("Asset download complete.")
    
except Exception as e:
    print(f"Failed to run update: {e}")
    # Print traceback
    import traceback
    traceback.print_exc()
    sys.exit(1)
