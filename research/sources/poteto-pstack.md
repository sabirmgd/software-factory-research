# Poteto / PStack

## Inspected scope

This note refers to the architect skill, its design-red-flags reference, and the correct skill in `cursor/plugins/pstack`. It does not infer the behavior of every PStack workflow from those files. [S08–S10](index.md#s08)

## Architect

The workflow grounds the existing system, explores structurally distinct candidates, synthesizes a sketch, implements against it, and revisits the sketch when repeated friction exposes a pattern. Caller usage comes before the derived type shape. Human approval is opt-in in the inspected source.

The review prompts include shallow interfaces, information leakage, organization by execution stage instead of owned knowledge, forwarding layers, split ownership, duplicate supported paths, reachable internals, and manually synchronized lists. Their purpose is to expose costly design choices, not to create a score whose minimum proves quality.

## Correct

Recurring mistake classes are addressed through architecture, types, checks, and behavior tests before adding more prose. New checks must be demonstrated against an actual prior failure. The emphasis is on improving the environment the next contributor sees, not merely increasing instructions.

## Our adaptation

We reserve multi-design exploration for consequential decisions and add explicit authority requirements for changing client-facing contracts, access boundaries, or external commitments. We treat repeated friction as a review trigger, not automatic permission to scrap a system. A small implementation mistake and a mistaken architecture need different interventions.

## What not to infer

The presence of model identifiers in a source does not make those models available in this environment. This publication does not reproduce the orchestration runtime, claim benchmark superiority, or verify the author's current employment from a repository path.
