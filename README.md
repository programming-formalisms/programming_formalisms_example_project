# programming_formalisms_example_project

![](images/programming_formalisms_teacher_team_logo_116x116.png)

The Programming Formalisms example project

## Goal

N-body simulation, e.g. galaxy sim or predator-prey

## Usage

The simulation can be started in two ways:

 * Console application: a text-only version
 * GUI application: using graphical windows

Additionally, the simulation can be benchmarked.

### Console application

#### From the command line

In the project root, from a terminal, do:

```
./scripts/run_console.sh
```

Or, which are the equivalent two steps:

```
# Install the package from the local code
python3 -m pip install .

# Run the code
python3 main.py
```

### GUI application

The GUI application uses [Pygame](https://www.pygame.org),
as was decided by voting.

#### From the command line

In the project root, from a terminal, do:

```
./scripts/run_gui_application.sh
```

Or, which are the equivalent two steps:

```
# Install the package from the local code
python3 -m pip install .

# Run the code
python3 main.py --gui
```

### Benchmarking

#### From the command line

In the project root, from a terminal, do:

```
./scripts/run_benchmarks.sh
```

Or, which are the equivalent two steps:

```
# Install the package from the local code
python3 -m pip install .

# Run the code
python3 -O main.py --benchmark
```

## Documentation

 * [Design](design/README.md)
 * [Workflow](workflow/README.md)
