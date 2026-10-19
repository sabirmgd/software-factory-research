# One feature, all the way through

**Status: fictional worked example.** The product decisions below are illustrative, not client approvals. A narrow in-memory model is executable; the complete web/API/database product is not implemented here.

The request is to let a team coordinator assign a task to a workspace member. The important question is not how to update an `assignee_id`, but who may do it, which targets are valid, what assignment means for access, and what evidence establishes the result.

Read [the use case](use-case.md), [research brief](research.md), [PRD](prd.md), [technical design](technical-design.md), [implementation outline](implementation-outline.md), and [Make Clear review](make-clear-review.md) in order. [Verification](verification-plan.md) links the acceptance claims to checks. [The next change](next-change.md) challenges the initial design instead of stopping after its first success.

## What to notice

The PRD owns the user-facing promise. The technical design owns the proposed system and code shape. The outline orders demonstrable behavior. The delegation contract limits authority. The review view explains consequences. The evidence record reports actual local checks separately from unimplemented integration work.

The same terms and decisions persist across artifacts; each document should not invent a new permission or repeat every upstream paragraph. Stable IDs connect the claims.

## Run the limited model

From the repository root, with Node 22 and TypeScript 5.8.3 available:

```bash
tsc -p examples/task-assignment/runnable/tsconfig.json
node --test examples/task-assignment/runnable/assignment.test.mjs
```

The model demonstrates typed policy declarations and synchronous in-memory assignment behavior. It does not authenticate a real request, run NestJS or Next.js, access a database, simulate concurrent transactions, or measure customer value. [Read its exact scope](runnable/README.md) before interpreting the results.
