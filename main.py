"""The Programming Formalisms Example Project.

Project used in the UPPMAX Programming Formalisms course.
"""

import cProfile

import sys


from pf_example.simulation import (
    run_profile_simulation,
)
from pf_example.simulation_terminal_controller import (
    SimulationTerminalController,
)
from pf_example.simulation_window_controller import (
    SimulationWindowController,
)

"""
TODO


from pf_example.testing import (
    get_datas,
    get_sorting_functions,
    get_speed_measurements,
    save_speed_measurements,
)
"""

def do_benchmark():
    """Benchmark this project."""

    cProfile.run(
        "run_profile_simulation()"
    )
"""
TODO
    speed_measurements = get_speed_measurements(
        datas = get_datas(data_lengths = [2, 4, 6, 8, 10]),
        functions = get_sorting_functions(),
    )
    save_speed_measurements(speed_measurements, "speeds.csv")


"""

if __name__ == "__main__":

    if "--gui" in sys.argv:
        print("GUI application") # noqa: T201 print is used as a stub
        c = SimulationWindowController()
        c.run()
    elif "--benchmark" in sys.argv:
        print("Benchmarking application") # noqa: T201 print is used as a stub
        if __debug__:
            e = RuntimeError("Do not benchmark in debug mode")
            raise e
        do_benchmark()
    else:
        print("Console application") # noqa: T201 print is used as a stub
        c = SimulationTerminalController()
