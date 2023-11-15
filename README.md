# programming_formalisms_example_project

The Programming Formalisms example project.

## Goal

N-body simulation, e.g. galaxy sim or predator-prey

## Design documents

Number|Document                                                              |Description
------|----------------------------------------------------------------------|------------------------------------------------
1     |[Client Project Brief](client_project_brief.md)                       |The start of a design, written by the client
2     |[Project documentation](Example_project_designProcessDocumentation.md)|General exercise for `3a` and `4a`
3a    |[DPD unassisted](DPD_unassisted.md)                                   |The exercise to create the formal design
3b    |[DPUA requirements specification](DPUA_requirementspecification.md)   |The requirements specification, the result of `3a`
4a    |[DPD assisted](DPD_assisted.md)                                       |The exercise to create DPAI. It is part of the course
4b    |**[DPAI requirements](DPAI_requirements.md)**                         |The requirements specification, the result of `4a`

We use both console application (written by humans) and a GUI application 
(written by AI). The GUI package is PyGame.

## Abbreviations

Abbreviation|Full
------------|--------------------------------------
CDAI        |Class Design assisted by Artificial Intelligence 
DPAI        |Design Process Artificial Intelligence 
DPD         |Design Process Document
DPUA        |Design Process UnAssisted

## git branching model

![](git_branches.png)

Our `git` branching model:

 * `master`/`main`: a working version
 * `develop`: merging topic branches
 * topic branches: where work is done,
   for example, Issue `x` is done on 
   a branch called `issue_x`

Videos:

 * [Overview of the git branches](https://youtu.be/trLafZpD1Tg?si=ZliLdIQ8KXDW7xjq)
 * [Working with this git branching model](https://youtu.be/pM520_JLR6w?si=1pvh5uUjXFJPPqGZ)

## GitHub workflows

  1. [Modify README on main branch using GitHub web interface](https://youtu.be/xBH2xZoKof4?si=ohdG6-y8lzarSqIa)
  2. [Modify README on topic branch using GitHub web interface](https://youtu.be/vPyHWsnbXw8?si=XjD6a3WDY44I97Se)
  3. [Modify README on main branch using git](https://youtu.be/A85wZTiCMTc?si=oUyrg_53gVlqEanb)
  4. [Modify README on topic branch using git](https://youtu.be/ZkfjAfu9Wo4?si=myBTkJ179n9fXHrS)
  5. [Merge topic branch to develop yourself](https://youtu.be/1fKdU1m3Uug?si=qox0K-EdZ-tDpcRY)
  6. [Merge topic branch to develop with a code review](https://youtu.be/VexyXysb-BM?si=uCOuqCVuZ_ylsUtI)

## Project workflows

 * [From design to feature](https://youtu.be/f-rzfZtsPKU)
 * [Splitting up an Issues to smaller Issues](https://youtu.be/mhIBXfxVxIU)
