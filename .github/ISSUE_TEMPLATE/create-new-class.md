---
name: Create new class
about: Need to create a new class
title: 'Create [name_of_class]'
labels: ''
assignees: ''

---

In the design document, the class in the title
is mentioned. Create it!

# Procedure

 * [ ] Create a file for the class implementation
   with name `src/pf_example/[class_name].py`,
   e.g. `src/pf_example/simulation_parameters.py`
 * [ ] Create a file for the class tests,
   with name `tests/test-[class_name].py`,
   e.g. `tests/test-simulation_parameters.py`
 * [ ] Create a minimal class implementation,
   for example:

```python
"""Simulation parameters."""

class SimulationParameters:

    """SimulationParameters holds the simulation's parameters."""
```

 * [ ] Create a minimal class test,
   for example:

```python
"""Tests all function in src.pf_example.simulation_parameters."""
import unittest

from src.pf_example.simulation_parameters import (
    SimulationParameters,
)


class TestSimulationParameters(unittest.TestCase):

    """Class to test the code in src.pf_example.simulation_parameters."""

    def test_can_create_params(self):
        """#14: Can construct a SimulationParameters."""
        SimulationParameters()
```

The test is that it works, not that it does anything useful.

Use [the workflow that fits you best](https://github.com/programming-formalisms/programming_formalisms_example_project/tree/main/workflow#github-workflows), 
ideally use a topic branch for this issue 
and merge to develop using a PR with code review.

