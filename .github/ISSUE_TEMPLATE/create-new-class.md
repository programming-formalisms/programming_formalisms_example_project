---
name: Create new class
about: Need to create a new class
title: 'Create [name_of_class]'
labels: ''
assignees: ''

---

In the [the class design document](https://github.com/programming-formalisms/programming_formalisms_example_project/blob/main/design/class_diagram_richel.puml), 
a class is composed ('has-a') of at least one other class.
Create that relationship!

# Procedure

 * [ ] Add the smaller class to the bigger class
   in the implementation, for example:

```python
# ...

class Particle:
   # ...

   def __init__(self):
       self._speed = Speed()

   # ...
```

 * [ ] Create a minimal class test,
   for example:

```python
# ...

class TestParticle(unittest.TestCase):

    # ...

    def test_a_particle_has_a_speed(self):
        """#[number]: a Particle has a Speed."""
        p = Particle()
        p._speed()
```

The test is that it works, not that it does anything useful.

Use [the workflow that fits you best](https://github.com/programming-formalisms/programming_formalisms_example_project/tree/main/workflow#github-workflows), 
ideally use a topic branch for this issue 
and merge to develop using a PR with code review.
