# My dispatch policy

Fill in this template yourself before asking the builders to implement it. Short bullets and a small table are enough. You may discuss ideas or ask AI to challenge them, but make and explain your own choices.

## Priorities

- What I prioritise: Reduce the distruption to the passengers that already aboard by using another eligible elevator through the caller’s floor.
- My exact selection rule: 
1. Use only elevators returned by eligible_ids(...)
2. Prefer a moving elevator whose existing route serves the caller’s floor.
3. Prefer an elevator with the caller’s floor already scheduled as a stop.
4. Otherwise, choose the eligible elevator with the smallest floor distance to pickup.
5. If still tied, choose the lower load_kg.
- My deterministic tie-breaker: if candidates remain equal, chooose elevator A.
- A tradeoff I accept: Passengers in the selected moving elevator may experience an additional stop, but this avoids assigning an idle car and starting another journey. Route matching is only a proxy for lower disruption, not a measured waiting-time or energy guarantee.

## Predictions before implementation

Use S1, one of S2/S3, and one valid scenario you create in scenarios.py. For your own case, change something meaningful: location, direction, load or scheduled stops. Name it S6.

| Scenario | My expected selection | Why it follows my policy | Benefit and cost / who is affected |
|---|---|---|---|
| S1 | A | A is already moving down, and its route from floor 8 to floor 1 passes floor 5 | Reuses A’s existing journey; passengers aboard may experience an added stop. |
| S2 | A | A remains eligible because 325 + 65 = 390 kg, and it is already travelling through floor 5. | Avoids starting B. As A’s passengers may experience extra delay, and A has a heavier load. |
| S6: Equal-distance idle cars | B | A is idle at floor 1 with 455 kg. B is idle at floor 3 with 0 kg. For a floor-2 up request, both are one floor away. The lower-load tie-break selects B. | Preserves more capacity in A and uses B; B may require slightly more future loading capacity management. |

S6 scenario : A idle at floor 1 with load_kg=455; B idle at floor 3 with load_kg=0; request from floor 2 going up.


## Another defensible policy

- An alternative priority: Always choose the eligible elevator with the shortest floor distance to the caller, regardless of whether it is already travelling along the caller’s route.

- A scenario where it could choose differently, and why: In S1, this policy would choose B because B is one floor from floor 5, while A is three floors away. It may reduce pickup distance but could create a new trip and leave A’s existing journey unused.

If your predicted choices contradict your general rule, resolve that before implementation. If review later changes your mind, note the revision in EVIDENCE.md and update the policy and code together.
