#Class Diagram example NBodyProblem

@Designer: Lars Eklund, ChatGPT

This is an example of how one could generate and build a class diagram for the NBody simulation. 
The process started with prompting the Ai to generate a class diagram of the  
UseCase diagram previously created. Then ChatGPT created a rough draft,
 which was manually changed to correct mistakes that the AI (ChatGPT) had generated and to added missing parts like the package(module)and changed an interface to an abstract class. This Design uses a strict MVC design pattern and a Factory Method Design Pattern to create the simulation, this is a rather complicated design for such a small project and implementation from this track might not be recommended for this project but is included for educational purposes.

classes.
```plantuml
@startuml SimulationFactory
!theme spacelab

package simulation{

class SimulationController {
  +runSimulation(components: List<SimulationComponent>) : void
  +main():void
}

package simulation.model #CCDDDD{

Abstract SimulationComponent {
  +configure() : void
  +initialize() : void
  +update():SimulationComponent
  
}

class ParticleField {
  +configure() : void
  +initialize() : void
  +update() : ParticleField
}

class GravitationalInteraction {
  +configure() : void
  +initialize() : void
  +update() : GravitationalInteraction
}

class BoundaryCondition {
  +configure() : void
  +initialize() : void
  +update() : BoundaryCondition
}

class SimulationFactory {
  +createComponent(type: String) : SimulationComponent
}

class SettingsModule {
  +configureComponents(factory: SimulationFactory) : void
  +initializeComponents() : void
}
class Particle {
  -mass:number
  -position:Coordinate
  -speed:vector(number)
  +update()
}
Class Coordinate{
 ~x:number
 ~y:number
}
}

package simulation.views #FFFFDD {
class SettingsView {
  +DisplaySettings(controler: SettingsModule) : void
  +UpdateSettings() : void
}

class SimulationView{
 +DisplaySimulation(component:: List<SimulationComponent>):void
 +StartSimulation(SimulationController:runSimulation()):void
 +UpdateSimulation():void
}
}

SimulationFactory ..> SimulationComponent: createComponent()
SimulationComponent <|-- ParticleField
SimulationComponent <|-- GravitationalInteraction
SimulationComponent <|-- BoundaryCondition
SimulationComponent <|-- Particle
Particle --* Coordinate


SimulationController ..> SettingsModule : Uses
SimulationController ..> SimulationComponent : Uses

SettingsView ..> SimulationController: Uses
SettingsModule ..> SimulationFactory : configureComponents()
SimulationView ..>SimulationController:Uses
SimulationView-->SettingsView: Associate

@enduml
```