"""Builder 1 implements the student's policy here."""
from models import Elevator, Request, Decision
from rules import eligible_ids

def choose_elevator(elevators: tuple[Elevator, Elevator], request: Request) -> Decision:
    """Choose one eligible elevator according to POLICY.md; never mutate inputs."""
    eligible = eligible_ids(elevators, request)
    if not eligible:
        return Decision(None, "No elevator is eligible to serve this caller, so the assignment is deferred.")

    by_id = {elevator.id: elevator for elevator in elevators}
    candidates = [by_id[elevator_id] for elevator_id in eligible if elevator_id in by_id]

    def serves_caller_on_route(elevator: Elevator) -> bool:
        if elevator.direction == "up" and elevator.stops:
            return elevator.floor <= request.floor <= max(elevator.stops)
        if elevator.direction == "down" and elevator.stops:
            return min(elevator.stops) <= request.floor <= elevator.floor
        return False

    def ranked(elevator: Elevator) -> tuple[int, int, int, int, int]:
        route_priority = 0 if serves_caller_on_route(elevator) else 1
        stop_priority = 0 if request.floor in elevator.stops else 1
        distance = abs(elevator.floor - request.floor)
        id_priority = 0 if elevator.id == "A" else 1
        return route_priority, stop_priority, distance, elevator.load_kg, id_priority

    selected = min(candidates, key=ranked)
    route_match = serves_caller_on_route(selected)
    scheduled_stop = request.floor in selected.stops

    if route_match:
        if scheduled_stop:
            reason = (
                f"Elevator {selected.id} selected: it is eligible and already moving on a "
                f"route that serves floor {request.floor}, with floor {request.floor} scheduled as a stop."
            )
        else:
            reason = (
                f"Elevator {selected.id} selected: it is eligible and already moving on a "
                f"route that serves floor {request.floor}."
            )
    elif scheduled_stop:
        reason = (
            f"Elevator {selected.id} selected: it is eligible and has "
            f"floor {request.floor} scheduled as a stop."
        )
    else:
        distance = abs(selected.floor - request.floor)
        reason = (
            f"Elevator {selected.id} selected: it is eligible and is nearest at "
            f"{distance} floor(s) away"
        )
        tied_by_distance = [
            elevator for elevator in candidates
            if abs(elevator.floor - request.floor) == distance
        ]
        if len(tied_by_distance) > 1:
            lowest_load = min(elevator.load_kg for elevator in tied_by_distance)
            if selected.load_kg == lowest_load:
                tied_by_load = [
                    elevator for elevator in tied_by_distance
                    if elevator.load_kg == lowest_load
                ]
                if len(tied_by_load) > 1:
                    reason += ", and elevator-A is the deterministic tie-break after distance and load tie"
                else:
                    reason += ", and it has the lowest load among equal-distance candidates"
            else:
                reason += ", after applying the lower-load tie-break"
        reason += "."

    return Decision(selected.id, reason)
