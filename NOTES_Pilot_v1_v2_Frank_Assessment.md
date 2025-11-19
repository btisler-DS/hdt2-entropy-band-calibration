HDT² Pilot v1–v2: Frank Technical Assessment of Scope, Boundaries, and Completeness
1. Purpose of the Pilot Program

The HDT² pilot was intentionally designed as a feasibility and boundary-finding study, not a full method or final system.
Its goal was simple:

Determine whether the entropy field of a large language model contains stable, measurable geometric structure that can be used as a control signal.

Everything in Pilot v1 was subordinate to that goal.

2. What Pilot v1 Was Designed to Test (and What It Was Not)
Pilot v1 was designed to test:

Whether entropy per token is structured, not noise

Whether regimes (stable, ambiguous, underdetermined) appear consistently

Whether bands can be aligned across models

Whether correctness correlates with these regimes (sanity check only)

Whether the measurement pipeline works end-to-end

Pilot v1 was not designed to test:

Universality across all model types

Large-scale statistical claims

Causal mechanisms

Explanatory theory behind correctness

Hallucination detection

Task-general generalization

Production deployment

This distinction is crucial for reviewers.

3. What Pilot v1 Demonstrated Successfully

Pilot v1 produced clear, reproducible results:

Entropy forms structured geometric patterns across reasoning sequences.

These patterns can be partitioned into epistemic regimes.

These regimes are stable within compatible models.

Cross-model alignment is conditional, not universal — a critical empirical finding.

Entropy bands correlate directionally with correctness (sanity check).

The calibration and measurement pipeline is viable and falsifiable.

This is exactly what a pilot should do.

4. Known Limitations — and Why They Are Acceptable for a Pilot

A pilot is meant to expose constraints, not solve them.

Here are the explicit, intentional limitations:

Small prompt set → enough to test structure, not statistics

Few models → sufficient to identify compatibility boundaries

Affine alignment only → chosen as the simplest falsifiable first step

Minimal baselines → comparison comes after feasibility

No mechanistic explanations → outside pilot scope

Implementation bugs → caught by the gate system and fixed

These are not flaws; they represent a completed pilot scope.

5. What Pilot v2 Addresses Directly

Pilot v2 exists specifically to explore everything Pilot v1 exposed as open questions:

Detailed characterization of epistemic regimes

Cross-model comparability

Task dependence

Non-affine alignment methods

Sampling sensitivity

Control policies (abstention, escalation, hedging, tool routing)

Conditions under which regime geometry collapses or changes

Pilot v2 is the natural continuation — taking the “structure exists” result and exploring it.

6. What HDT² Is Not Claiming

To pre-empt misreadings:

Not a hallucination detector

Not a correctness classifier

Not a calibration replacement

Not a universal model alignment framework

Not a theory of internal LLM cognition

Not a final method

This should appear in every review-facing document.

7. What HDT² Is Claiming

A clear, defendable claim:

Entropy geometry exposes the epistemic regime a model is currently in.
This regime signal can be used as a practical control surface for adaptive behavior.

This is novel, falsifiable, and useful.

8. Open Questions (Intentionally Unanswered)

These are left open for Pilot v2 and collaborator exploration:

What internal model states underlie regime transitions?

How do tasks shape entropy geometry?

When do two models share compatible uncertainty manifolds?

How stable are regimes under sampling or perturbation?

What policies best attach to each regime?

Leaving these open shows honesty and scientific maturity.

9. Minimal Reproduction Notes (For Researchers)

A minimal reproduction path:

Choose one open model (Mistral, Llama, etc.).

Run a set of prompts (≥ 20).

Record token-level entropy for each decoding step.

Bucket entropies into quantiles (bands).

Plot accuracy vs band (sanity check).

Plot band transitions across reasoning sequences.

Attempt affine alignment to a second model.

Observe whether alignment succeeds or fails.

This is all that is needed to validate the pilot.

10. Closing Statement: The Value of a Bounded Pilot

Pilot v1 is complete because it answered the only question it set out to ask:
Does structured entropy geometry exist, and can it be measured?
The answer is yes.

Pilot v2 now investigates what that structure means.

This note exists to clarify the scope, boundaries, and intent of the pilot program so researchers can enter the work with the correct expectations and collaborate effectively.