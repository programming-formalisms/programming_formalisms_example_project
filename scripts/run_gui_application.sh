#!/bin/bash
#
# Start a GUI application, by running 'main.py'
#
# Usage:
#
#   ./scripts/run_gui_application.sh
#
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/run_gui_application.sh"
    exit 42
fi

# Install the package from the local code
python3 -m pip install .

# Run the code
python3 main.py --gui
