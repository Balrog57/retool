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

# Now we can mock the environment and use Retool's native update function
try:
    from modules.config.config import Config
    from modules.clone_lists.update_clone_list_metadata import update_clonelists_metadata
    
    # Mock UserInput if needed, but Config(None) seems to handle "no GUI"
    print("Initializing Config...")
    config = Config(None)
    
    print("Starting full asset download...")
    # Run the update with no_exit=True so we don't kill the script
    update_clonelists_metadata(config, None, no_exit=True)
    
    print("Asset download complete.")
    
except Exception as e:
    print(f"Failed to run update: {e}")
    # Print traceback
    import traceback
    traceback.print_exc()
    sys.exit(1)
