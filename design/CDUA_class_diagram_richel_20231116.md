#Class Diagram Solving the design of NBody simulation

@Designer: Richèl Bilderbeek

This class design was created un assisted (create time about 1h of skilled work) It presents the first iteration of a class design of the NBody problem
This design as the other implements a MVC design pattern

```plantuml
@startuml

class Simulation

abstract class SimulationView
class SimulationTerminal
class SimulationWindow

abstract class SimulationController
class SimulationTerminalController
class SimulationWindowController

class SimulationParameters
class Particles
class Particle
class Speed
class Position

SimulationController --* Simulation
SimulationController --* SimulationView

Simulation --* SimulationParameters
SimulationParameters --* InteractionParameters
SimulationParameters --* BoundaryConditions

Simulation --* Particles
Particles --* "SimulationParameters::m_n_particles" Particle

Particle --* Speed
Particle --* Position


SimulationView <|-- SimulationTerminal
SimulationView <|-- SimulationWindow

SimulationController <|-- SimulationTerminalController
SimulationController <|-- SimulationWindowController

class SimulationParameters {
  + SimulationParameters(parameter_filename)
  - m_timestep
  - m_n_particles
  - m_interaction_parameters
  - m_boundary_conditions
}

class Simulation {
  + go_to_next_state()
  - m_simulation_parameters
}

note left of Simulation::go_to_next_state
  uses SimulationParameters::m_timestep
end note


class Particles {
  + move()
  + interact(interaction_parameters)
  + respond_to_boundary_conditions(boundary_conditions)
}

note left of Particles::move
  as if each particle is alone
end note

class Particle {
  + move()
  + respond_to_boundary_conditions(boundary_conditions)

  - m_position
  - m_speed
}

note left of Particle::move
  as if alone
end note


abstract class SimulationView {
  + {abstract} show()
}

class SimulationTerminal {
  SimulationTerminal(terminal_size)
  + show()
}
note left of SimulationTerminal::show
  show as ASCII art
end note

class SimulationWindow {
  + show()
  SimulationWindow(window_size)
}

note left of SimulationWindow::show
  show as pixels
end note


abstract class SimulationController {
  + SimulationController(parameter_filename)
  + run()
  + {abstract} exit()
  - m_simulation
  - m_simulation_view
}

note left of SimulationController::m_simulation_view
  of the compatible derived class
end note


class SimulationTerminalController {
  + show_n_steps()
  + exit()
}

note left of SimulationTerminalController::show_n_steps
  shows n steps, then pauses
end note


class SimulationWindowController {
  + stop()
  + start()
  + exit()
}

note left of SimulationWindowController::start
  on key press or mouse click
end note

note left of SimulationWindowController::stop
  on key press or mouse click
end note

note left of SimulationWindowController::exit
  on ESC press
end note



@enduml
```