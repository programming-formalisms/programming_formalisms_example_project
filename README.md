# programming_formalisms_example_project

The Programming Formalisms example project.

## Goal

N-body simulation, e.g. galaxy sim or predator-prey

### 1. Client Project Brief

> The Client Project Brief is the start of a design document.
> From the Brief, the more formal design documents follow.

The program should visually display a number of particles on a field. 
Particles are initialised with a certain position and speed. 
Each particle interacts with all the other particles in a simple way, 
e.g. gravitational attraction, Lennard-Jones potential, 
direction alignment (implementing a flocking behaviour), 
or something else, the group chooses which. 
Decide on a boundary condition (e.g. bounce or wrap or eliminate the particle). 
The simulation is then stepped forward, drawing each step, until stopped. 
The goal is to create a stable simulation capable 
of the maximum number of particles at an acceptable framerate.

## Design documents

Number|Document                                                              |Description
------|----------------------------------------------------------------------|------------------------------------------------
1     |[Client Project Brief](client_project_brief.md)                       |The start of a design, written by the client
2     |[Project documentation](Example_project_designProcessDocumentation.md)|General exercise for `3a` and `3b`
3a    |[DPD unassisted](DPD_unassisted.md)                                   |The exercise to create the formal design
3b    |[DPUA requirements specification](DPUA_requirementspecification.md)   |The requirements specification, the result of `3a`
4a    |[DPD assisted](DPD_assisted.md)                                       |The exercise to create DPAI. It is part of the course
4b    |[DPAI requirements](DPAI_requirements.md)                             |The result of `4a`. This is tailored to the example project

## Abbreviations

Abbreviation|Full
------------|------------------------------------
DPAI        |Design Process Artifical Inteligence 
DPD         |Design Process Document
DPUA        |Design Process Un Assisted
