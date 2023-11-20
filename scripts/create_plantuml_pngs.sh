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

plantuml -t png -output design/class_diagram_richel.png design/class_diagram_richel.puml
