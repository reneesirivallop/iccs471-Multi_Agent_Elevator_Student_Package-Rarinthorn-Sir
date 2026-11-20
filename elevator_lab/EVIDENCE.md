# My experiment results

Fill in this template with actual observations. Short bullets are sufficient.

Name / student ID: Rarinthorn Sirivallop 6580229

Tool, visible software version and model(s): Copilot SDK in VS Code; Python 3.11.5; worker model versions unknown

Route: automatic workers with separate dispatcher, display, and read-only review executions

## Agent outputs

| Role | What it delivered | Brief excerpt or screenshot link |
|---|---|---|
| Dispatcher builder | Implemented `choose_elevator` using `eligible_ids`, the written priority order, deterministic tie-breaking, and non-empty reasons. | Worker report: `python3 -m unittest -v`: 6 tests passed; `python3 app.py` produced the expected selections. |
| Display builder | Implemented `run_scenarios`, including state/request display, one dispatcher call per scenario, WAIT formatting, and ordered decision results. | Worker report: `AppContract`: 2 tests passed; importing `app` did not run scenarios. |
| Reviewer | Found no implementation defects or policy inconsistencies. Identified route reuse versus shorter pickup distance as an accepted policy tradeoff. | Read-only reviewer report: `python3 -m unittest -v`: 6 tests passed; scenario results matched predictions. |

## Compare with my predictions

Run `python app.py` after adding S6. Compare with the predictions you wrote in POLICY.md before implementation.

| Scenario | Expected selection | Actual selection and reason | Matches my policy? |
|---|---|---|---|
| S1 | A | A — eligible moving elevator A already serves floor 5 on its route. | Yes |
| S2 or S3 | A | A — S2: A remains eligible at 325 kg and already serves floor 5. | Yes |
| S6 | B | B — both idle cars are one floor away; B has the lower load. | Yes |

- Supplied suite command and actual result: `cd elevator_lab && python3 -m unittest -v` all 6 tests passed.
- One review finding or concern I checked: The reviewer checked the route-priority rule in `dispatcher.py` against S1 and S2. A is farther from the caller than B, but selecting A follows my policy because A is already travelling through floor 5.
- Change made, if needed: No correction was needed after review. The implementation and observed choices match the policy and predictions.
- Does my policy serve my stated priority? Yes. In S1, using A reuses an existing trip and avoids starting an idle car. The limitation is that passengers already aboard A may experience an additional stop.
- What did I have to coordinate between the agents? I kept ownership separate: the dispatcher worker edited only `dispatcher.py`, the display worker edited only `app.py`, and the reviewer inspected the integrated files without editing them.
