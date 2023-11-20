#!/bin/bash
#
# Create the PNGs of the PlantUML files
#
# Usage:
#
#   ./scripts/create_plantuml_pngs.sh
# 
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/create_plantuml_pngs.sh"
    exit 42
fi

# Output file is relative to the input file
# plantuml -t png -output class_diagram_richel.png design/class_diagram_richel.puml

echo "Does not work, use https://planttext.com instead"
