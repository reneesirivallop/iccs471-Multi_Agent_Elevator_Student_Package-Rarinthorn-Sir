# My agent plan

Fill in the brackets before delegation. This is a template, not a completed plan.

- Dispatcher builder owns dispatcher.py: Implement choose_elevator(...) using rules.eligible_ids(...). The policy is to prefer eligible moving cars already serving the caller’s floor, then an existing scheduled stop, then shortest pickup distance, then lower load, with A as the final deterministic tie-breaker.
- Display builder owns app.py: Implement run_scenarios(...) using the supplied decision interface. Display each scenario, both elevator states, the request, the selected elevator or wait, and the dispatcher’s reason. Do not duplicate dispatch logic.
- Reviewer is read-only after both outputs are integrated: Check the combined implementation against SPEC.md, POLICY.md, the interface requirements, and the S1/S2/S6 predictions. Report up to three findings, distinguishing code defects, policy inconsistencies, and accepted tradeoffs.
- Handoff steps: First add S6 and provide each worker with AGENTS.md, SPEC.md, POLICY.md, PLAN.md, and all Python files. Delegate two separate builder tasks with ownership restricted to their respective files. Inspect the actual files after both workers finish; integrate only their owned files if necessary. Then run the tests and application before starting the read-only reviewer.
- Final check: Run python -m unittest -v and python app.py. Compare the actual selections and reasons for S1, S2, and S6 with my predictions. Investigate any mismatch rather than changing predictions without justification.
