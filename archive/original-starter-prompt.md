> **Historical artifact, not current guidance.** Preserved from the supplied earlier handoff. Some claims, links, and defaults were not revalidated and may be superseded. Read [the archive guide](README.md) and [source corrections](../research/source-corrections.md).

---

# Coding Session Starter Prompt

**Mission:** Help me build a reusable, agent-friendly TypeScript software-factory project template using NestJS and Next.js. Read the attached `AI_Software_Factory_Blueprint.md` as our design brief. The purpose is maintainable software under repeated AI-driven changes, not maximal initial code volume.

**Start with Phase 0 only. Do not scaffold the whole repository yet.** Interview me on the truly consequential unknown choices: exact third stack/tool if any, pnpm/Turborepo/Nx, Node version, database/ORM/migrations, auth provider, deploy target, testing stack, tenancy and first trial product. Offer sound defaults but never treat them as approved. Record decisions and disagreements in a short draft ADR and `docs/template-decisions.md`.

Then show me a proposed repository tree, module ownership rule, dependency matrix, typed authorization strategy (compile/build + runtime deny-by-default), database ownership model, contracts strategy, representative golden vertical slice, CI gates and a phased implementation plan. Distinguish executable hard constraints from advisory architecture metrics. Highlight where my approval is required. Optimize for **deep modules, narrow public interfaces and low future change cost**. Build one working phase at a time, prove it with real commands, and pause for approval at architecture-changing decisions.

**Definition of done:** new projects can start with product/persona/use-case templates, agents can follow a golden path, prohibited dependencies fail CI, undocumented endpoint security fails CI or defaults to deny, runtime auth policies are tested, and one reference vertical slice works across Next → typed contract → Nest → domain → DB. We also exercise sequential future-change scenarios before calling the factory successful.
