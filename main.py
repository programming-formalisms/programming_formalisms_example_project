"""The Programming Formalisms Example Project.

Project used in the UPPMAX Programming Formalisms course.
"""

import sys

from pf_example.simulation_terminal_controller import (
    SimulationTerminalController,
)
from pf_example.simulation_window_controller import (
    SimulationWindowController,
)

"""
TODO

import cProfile

from pf_example.testing import (
    get_datas,
    get_sorting_functions,
    get_speed_measurements,
    save_speed_measurements,
)
"""

if __name__ == "__main__":

    if "--gui" in sys.argv:
        print("GUI application") # noqa: T201 print is used as a stub
        c = SimulationWindowController()
        c.run()
    else:
        print("Console application") # noqa: T201 print is used as a stub
        c = SimulationTerminalController()


"""
TODO
    speed_measurements = get_speed_measurements(
        datas = get_datas(data_lengths = [2, 4, 6, 8, 10]),
        functions = get_sorting_functions(),
    )
    save_speed_measurements(speed_measurements, "speeds.csv")

    cProfile.run(
        "get_speed_measurements("
        "datas = get_datas(data_lengths = [2, 4, 6, 8, 10]), "
        "functions = get_sorting_functions())",
    )

"""
