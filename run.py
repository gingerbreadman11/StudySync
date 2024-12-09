
import sys
from subprocess import call

# Change directory to the app folder

# Run the Streamlit app
call(['streamlit', 'run', 'app.py'] + sys.argv[1:])
