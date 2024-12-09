import os
import sys
from subprocess import call

# Change directory to the app folder
os.chdir('Version_3/')

# Run the Streamlit app
call(['streamlit', 'run', 'app.py'] + sys.argv[1:])
