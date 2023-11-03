# programming_formalisms_example_project

The Programming Formalisms example project.

## Goal

N-body simulation, e.g. galaxy sim or predator-prey

### Client Project Brief

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

 * [DPAI requirements](DPAI_requirements.md)
 * [DPD assisted](DPD_assisted.md)
 * [DPD unassisted](DPD_unassisted.md)
 * [DPUA requirements specification](DPUA_requirementspecification.md)
 * [Project documentation](Example_project_designProcessDocumentation.md)

## Abbreviations

Abbreviation|Full
------------|------------------------------------
DPAI        |Design Process Artifical Inteligence 
DPD         |Design Process Document
DPUA        |Design Process Un Assisted
