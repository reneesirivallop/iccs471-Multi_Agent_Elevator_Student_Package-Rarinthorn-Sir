"""Builder 2 implements a readable scenario display here."""
from dispatcher import choose_elevator
from scenarios import SCENARIOS
from models import Decision

def run_scenarios(scenarios, output_fn=print) -> list[Decision]:
    """Show each snapshot, call the dispatcher once, display and return decisions."""
    decisions: list[Decision] = []

    for scenario in scenarios:
        decision = choose_elevator(scenario.elevators, scenario.request)
        decisions.append(decision)

        output_fn(f"Scenario: {scenario.name}")
        for elevator in scenario.elevators:
            output_fn(
                f"Elevator {elevator.id}: floor={elevator.floor}, "
                f"direction={elevator.direction}, load_kg={elevator.load_kg}, "
                f"stops={elevator.stops}"
            )
        output_fn(
            f"Request: floor={scenario.request.floor}, "
            f"direction={scenario.request.direction}"
        )
        selected = decision.elevator_id if decision.elevator_id is not None else "WAIT"
        output_fn(f"Selected: {selected}")
        output_fn(f"Reason: {decision.reason}")

    return decisions

if __name__ == "__main__":
    run_scenarios(SCENARIOS)
