"""The Programming Formalisms Example Project.

Project used in the UPPMAX Programming Formalisms course.
"""

from pf_example.simulation_controller import (
    SimulationTerminalController,
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
    c = SimulationTerminalController()
    print("Cannor measure speed yet") # noqa: T201 print is used as a stub


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
