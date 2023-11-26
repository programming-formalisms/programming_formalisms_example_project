---
name: Create a is-a-type-of relation
about: Need to create a is-a-type-of relation
title: 'A [name_of_derived_class] is-a-type-of [name_of_base_class]'
labels: ''
assignees: ''

---

In [the class design document](https://github.com/programming-formalisms/programming_formalisms_example_project/blob/main/design/class_diagram_richel.puml), the classes in the title
have a is-a-type-of relation. Create it!

# Procedure

 * [ ] Add the is-a-type-of relationship to the implementation
   of the derived class, for example:

```python
# ...

class SimulationTerminalController(SimulationController):
   # ...
```

(yes, that is all there is!)

The tests that are in place should keep working.

Use [the workflow that fits you best](https://github.com/programming-formalisms/programming_formalisms_example_project/tree/main/workflow#github-workflows), 
ideally use a topic branch for this issue 
and merge to develop using a PR with code review.
