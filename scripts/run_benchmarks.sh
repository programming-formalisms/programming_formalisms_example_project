#!/bin/bash
#
# Benchmark the project, by running 'main.py'
#
# Usage:
#
#   ./scripts/run_benchmarks.sh
#
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/run_benchmarks.sh"
    exit 42
fi

echo "======================================="
echo "Install the package from the local code"
echo "======================================="

python3 -m pip install .

echo "======================================="
echo "Run the code in debug mode, should fail"
echo "======================================="
python3 main.py --benchmark || true

echo "======================================="
echo "Run the code in release mode           "
echo "======================================="
python3 -O main.py --benchmark
