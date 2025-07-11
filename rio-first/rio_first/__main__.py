
# Make sure the project is in the Python path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).absolute().parent.parent))


# Import the main module
import rio_first

# Run the app
rio_first.app.run_in_window()
