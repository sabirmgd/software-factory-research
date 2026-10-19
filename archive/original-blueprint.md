> **Historical artifact, not current guidance.** Preserved from the supplied earlier handoff. Some claims, links, and defaults were not revalidated and may be superseded. Read [the archive guide](README.md) and [source corrections](../research/source-corrections.md).

---

# The AI Software Factory: Engineering Blueprint and Implementation Handoff

**Version:** 1.0 · **Prepared:** October 15, 2026  
**Intended use:** Give this document to a coding agent as the governing design brief for building a reusable project starter, then validate it on one real product.  
**Default known stack:** TypeScript, NestJS API, Next.js web app. Other preferences (ORM, database, deployment, test runner, monorepo tooling, exact third technology mentioned verbally) **remain decisions to confirm** rather than facts to invent.

---

## 0. Executive summary

We want to create a reusable **agent-friendly software engineering operating system**, not merely a boilerplate starter or a collection of prompts. The system must make the right engineering decisions *easy, visible, reproducible, and testable*.

Core hypothesis: **Spend a focused period making high-leverage decisions once; encode them into repository structure, public contracts, types, generators, examples, policies, and deterministic tests; then allow AI agents to work quickly inside those boundaries.** The goal is not zero human involvement. Humans make consequential product and architectural decisions, agents do research and execution, and automated checks keep implementation within an approved envelope.

The system has two modes:

1. **Project bootstrap (infrequent):** Define vision, personas, use cases, uncertain behavior, module boundaries, cross-cutting foundations, tech choices, golden paths, and invariant checks. Build a reference vertical slice and validate the factory.
2. **Feature delivery / maintenance (repeatable):** Start with the changed use case, research relevant current code, prototype if uncertainty merits it, adjust architecture only if necessary, approve program design, implement and test small vertical slices, run automated gates, review the resulting code and evolution pressure, then update living docs.

**Important nuance:** foundational rules should be stable, but not frozen forever. Changes to them require a conscious Architecture Decision Record (ADR) and explicit approval rather than accidental drift.

### Design lineage / attribution

- **Dex Horthy / HumanLayer:** product design → system architecture → program design → vertical slices; intentional context management; review small increments; maintainability cannot be captured by a simple passing test. Primary: [Why Software Factories Fail](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md) and [Advanced Context Engineering](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md).
- **Robert C. Martin (Uncle Bob):** use-case-centered systems, dependency inversion, keep business rules independent of delivery and persistence mechanisms. We are adopting the principle, not claiming to reproduce an unverified interview transcript.
- **John Ousterhout / A Philosophy of Software Design:** favor **deep modules** — a simple, stable interface hiding meaningful implementation complexity — rather than excessive shallow layers and wrappers.
- **Matt Pocock:** uncertainty-driven, disposable logic or UI prototypes, with learnings transferred into proper implementation. Primary: [prototype skill](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype).
- **SlopCodeBench:** iterative changes reveal quality erosion that single-shot tests cannot; offers a *benchmark and measurement ideas*, not a ready-made drop-in TS CI rule set. Primary: [benchmark repository](https://github.com/SprocketLab/slop-code-bench), [paper](https://arxiv.org/abs/2603.24755), and [Dex's examination](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md).

Everything below is a **proposed synthesis for our stack**, not a statement that those authors prescribe the exact repo structure, schemas, or code.

---

## 1. End-to-end flow and approval gates

```text
PROJECT INITIALIZATION (typically once, then refined as needed)
  1. Product intent, outcomes, non-goals
  2. Personas, actors, use cases, acceptance scenarios
  3. Disposable logic/UI prototypes where uncertainty exists
  4. Domain and module design; system and data architecture
  5. Foundation decisions: contracts, authn/authz, errors, observability,
     API standards, TS config, persistence and package boundaries
  6. Executable rules, scaffolds, CI, first reference vertical slice
                       |
                       v
EVERY SUBSTANTIVE FEATURE / CHANGE
  A. Identify use case and definition of done
  B. Investigate current code and relevant existing decisions
  C. Prototype uncertainties (optional)
  D. Architecture impact check; ADR only when necessary
  E. Program design: file tree, types, signatures, call path, test plan
  F. Human approval of consequential choices
  G. Implement one thin vertical slice, verify, review
  H. Repeat slices until complete; run all release gates
  I. Record decisions, update docs, track future-change cost
```

**Four progressively specific contracts:**

| Level | Question | Primary artifact | Human sign-off? |
| --- | --- | --- | --- |
| Product | Why, for whom, what outcome? | Vision, personas, use cases and examples | Yes for core behavior |
| System architecture | Who owns responsibilities and data? | Module map, dependency matrix, data map, API policies, ADRs | Yes for new boundaries |
| Program design | What types/functions/files/call flows will implement it? | Proposed file-tree diff, type signatures, call-tree, test plan | Yes for nontrivial features |
| Implementation | Does working code satisfy contracts without violating design? | Small PRs, tests, CI report, human review | Yes before production for consequential changes |

**Graduated rigor:** do not demand four separate documents for every typo. A small safe change may go directly to implementation and checks. A medium feature may combine product and architecture in one spec; a large new workflow gets all gates. This is aligned with Dex's explicitly proportional approach.

---

## 2. Product-first foundation

### 2.1 Product vision (`docs/product/vision.md`)

Fill in:

- Problem, target customer, desired measurable business outcome.
- What the product is **not** trying to do.
- Primary capabilities and the first thin release boundary.
- Business risks, privacy/security expectations, key constraints.
- **Open questions**, visibly marked `UNDECIDED`, not silently filled by an agent.

### 2.2 Personas versus security roles

**Product persona ≠ security role.** A persona is a human motivation and user journey (e.g., "project manager tracking team progress"). A security role is a system authorization concept (e.g., `workspace_admin`). Mapping between the two is explicit and may not be one-to-one. Do not let agents invent permission roles merely from marketing personas.

Example personas:

- Team owner — sets up a workspace and manages access.
- Member — creates, updates and completes assigned tasks.
- External collaborator — can view explicitly shared items only.

Keep a separate actor/authorization registry for service accounts and anonymous visitors where relevant.

### 2.3 Use cases (`docs/product/use-cases/UC-001-create-task.md`)

Template:

```markdown
# UC-001: Create Task
Actor: Workspace member
Trigger: User chooses "New task"
Preconditions: Authenticated; active workspace membership
Success outcome: Task is created and visible to authorized members
Happy path:
  1. Actor enters title and optional assignee
  2. System validates workspace membership and permissions
  3. System creates task under the correct workspace
  4. System returns task reference and reflects it in UI
Alternatives: Assignee absent, duplicate request, invalid title
Failures: No permission, workspace missing, assignee outside workspace
Invariants: No cross-workspace creation; no partial write
Acceptance examples (Given/When/Then): ...
Open questions: ...
Observability: Record failure category without leaking private data
```

Use cases are business behaviors, **not CRUD endpoint inventories**. One use case may require multiple API calls, UI states, or domain transitions. Begin from an actor's goal, then derive screens/endpoints and underlying modules.

Define acceptance criteria in user-observable terms, including negative cases, authorization failures, retries, and accessibility where relevant. Link each implemented feature and test back to its use case ID.

---

## 3. Prototype only to reduce uncertainty

After initial use cases, ask: "What would be costly to discover was wrong after architecture or coding?"

**Logic prototypes:** disposable simulations of state machines, permissions, transitions, or tricky business policies. Visualize actions and full resulting state; test edge cases interactively. Example: can a task be reassigned after its project is archived, and what happens to its audit history?

**UI prototypes:** radically different flows or layouts to compare, with realistic states (loading, empty, error, permission denied), ideally quickly switchable.

Discipline:

1. State one learning question in advance.
2. Keep the experiment small; don't build production authentication, persistence, or needless abstractions.
3. Decide and record the **verdict** — accepted, rejected, inconclusive — and changes to use cases/architecture.
4. Keep disposable code off the production mainline; a temporary branch/reference is fine.
5. Only migrate validated *ideas* and selectively useful logic into production with proper tests.

**Prototype is optional.** A well-understood task should not spend days prototyping for ritual compliance.

---

## 4. Architecture for change: choose modules from business capabilities

### 4.1 Default architecture: modular monolith

For an early NestJS + Next.js product, prefer a **modular monolith** unless there is a compelling deployment/scale/team constraint. One deployable backend, clear domain ownership, narrow module interfaces, explicit boundaries, and usually a single physical relational database. This minimizes infrastructure complexity without surrendering modularity.

**Candidate domains are discovered from use cases**, not preconceived folders named `utils`, `services`, `database`, `controllers`. Example: `workspaces`, `memberships`, `tasks`, `notifications`, `billing` — only create modules the current business needs. Separate stable business capabilities from cross-cutting platforms.

### 4.2 Domain module ownership contract

Each meaningful business module receives a short contract (`docs/architecture/modules/tasks.md`):

- **Purpose / responsibilities:** one high-cohesion business capability.
- **Owns:** domain concepts, state transitions, tables, operations, business invariants.
- **Public interface:** minimal operations and events other modules may rely on.
- **Dependencies:** what other public interfaces it can call, and why.
- **Forbidden knowledge:** database tables/internal services of other modules; unrelated framework details.
- **Permissions:** required capabilities per operation, tenant-scoping rules.
- **Change scenarios:** examples of likely future extensions that should remain local.
- **Failure semantics:** idempotency, transactions, retry behavior, error contract.
- **Contract tests / fitness functions:** which checks protect the module.

An illustrative **deep Tasks module** exposes meaningful operations:

```ts
export interface TasksPort {
  create(input: CreateTask, actor: ActorContext): Promise<TaskId>;
  reassign(input: ReassignTask, actor: ActorContext): Promise<void>;
  complete(input: CompleteTask, actor: ActorContext): Promise<void>;
  getVisibleTask(id: TaskId, actor: ActorContext): Promise<TaskView>;
}
```

Internally it can own policy decisions, validation, state transitions, persistence, audit events, conflict detection and eventual notification integration. External callers should **not** need to know the internal repositories, transaction details, validation pipeline, or provider SDK. Avoid an API like `getRepository()`, `saveRaw()`, `executeRule()`, which leaks decisions to the caller and makes the module shallow.

### 4.3 Clean Architecture inside a module, not ceremonial layering

Organize responsibilities (not necessarily every tiny file) so dependencies generally point inward:

```text
transport (Nest controllers, DTO mapping, HTTP mechanics)
        -> application (use cases, orchestration)
            -> domain (invariants, entities, pure policy)
            <- infrastructure (DB, gateways, providers implement ports)
```

Domain and application logic must not import Nest controllers, Prisma/ORM clients, Next components, or vendor SDKs. Ports are defined on the inside, adapters on the outside. A composition root wires implementations into Nest dependency injection.

**Avoid shallow-module theater:** do not create a controller/service/repository/facade/manager/processor chain unless each layer owns a meaningful abstraction. The number of layers is not the score. The quality of hidden complexity and locality of change is the objective.

### 4.4 Shared code, types, and clients: strict rules

Create shared packages only for deliberately stable cross-cutting contracts:

- `packages/contracts`: public wire DTOs/schemas, shared identifiers, API error envelope. Never export ORM entities or internal domain models.
- `packages/authz`: typed permissions, role/grant policy primitives, policy-test helpers.
- `packages/config`: configuration schemas and validated environment names (secrets never stored).
- `packages/tooling` / `packages/testing`: configs and test utilities when there is demonstrated reuse.

Prefer **per-module public entrypoints** to a global dumping ground of `shared/types.ts`. Shared abstractions should be created because multiple consumers need the *same concept with the same semantics*, not because two structures look similar. Resist adding ubiquitous `BaseService`, `BaseRepository`, or huge `CommonModule` abstractions.

**Clients:** generate or hand-maintain one typed API client from an explicit API contract. Next.js consumes this client, not Nest internals or backend ORM packages. Third-party service clients live behind adapters owned by the appropriate module.

### 4.5 Database and schema ownership

Recommended baseline: PostgreSQL (confirm preference) with an agreed ORM/migration tool. A single physical DB is compatible with module ownership. Each table has an owning module; writes to it go through that module's application logic or controlled repository. Cross-module writes via direct SQL are disallowed without an explicit exception.

- Choose naming conventions, migration review process, unique constraints, foreign keys, tenant isolation and index policy once.
- Database constraints complement application checks; database design itself is part of the architecture.
- Enforce the feasible aspects via CI: migration lint/validation, test migrations from scratch, metadata ownership checks, explicit transaction boundaries, tests for workspace/tenant isolation.
- Do not pretend TS compiler types validate SQL policy, row-level security, or runtime user access.
- For cross-module reporting, prefer read models/public queries; direct reporting joins may be an ADR-approved exception when necessary.

### 4.6 API contract and error semantics

Define a consistent contract: routes, methods, versioning policy, request/response schemas, pagination, filtering, idempotency, error envelope, and generated OpenAPI (or other chosen contract), with contract/compatibility tests. External clients should not know internal module layout.

Nest controllers should stay thin: validate/parse, obtain authenticated context, run authorization, delegate to application use case, map output/error. No business policy scattered in controllers or UI route handlers.

---

## 5. Make security hard to forget: personas, authn, authz

This was a key design insight: **some engineering decisions can become mandatory inputs to code creation, so missing policies fail compilation or builds instead of slipping through agent memory**.

### 5.1 Separate three concepts

1. **Authentication:** who the actor is and the legitimacy of the session/token.
2. **Authorization:** whether the actor can perform a capability *on this resource in this tenant and context*.
3. **Product persona:** why a human uses the product; this is documentation and UX, not the permission system.

### 5.2 Typed permission registry (TypeScript example)

```ts
export const ROLES = ['owner', 'admin', 'member'] as const;
export type Role = (typeof ROLES)[number];

export const PERMISSIONS = [
  'tasks:create',
  'tasks:read',
  'tasks:reassign',
  'tasks:complete',
] as const;
export type Permission = (typeof PERMISSIONS)[number];

export const roleGrants = {
  owner: ['tasks:create', 'tasks:read', 'tasks:reassign', 'tasks:complete'],
  admin: ['tasks:create', 'tasks:read', 'tasks:reassign', 'tasks:complete'],
  member: ['tasks:create', 'tasks:read', 'tasks:complete'],
} as const satisfies Record<Role, readonly Permission[]>;
```

This catches misspelled permissions and missing declared roles at compile time **in this registry**. Add a typed, centralized endpoint policy manifest referencing `Permission`, for example:

```ts
type EndpointId = 'tasks.create' | 'tasks.list';
type EndpointPolicy =
  | { access: 'public' }
  | { access: 'authenticated'; permission: Permission };

export const endpointPolicies = {
  'tasks.create': { access: 'authenticated', permission: 'tasks:create' },
  'tasks.list':   { access: 'authenticated', permission: 'tasks:read' },
} as const satisfies Record<EndpointId, EndpointPolicy>;
```

**What this guarantees:** any endpoint **listed in `EndpointId`** must have a policy of the declared shape, with known permission names.

**What it does not guarantee:** a new Nest route cannot be silently added outside that manifest. Solve that with a convention such as a required typed route registration wrapper **or** a custom AST check ensuring every controller handler is explicitly annotated as public or protected and registered in the manifest. Tests should compare the discovered route inventory with policy inventory. In the Nest application, an `APP_GUARD` can enforce **deny by default** when no policy metadata is present, allowing explicit `@Public()` exceptions only. Test those exceptions and do not conflate bypassing login with resource authorization.

Even where a type is correct, authorization requires **runtime checks** for object ownership, membership, resource sharing, tenant boundaries, and current permission state. Query filters and/or DB-level RLS may provide extra defense; every sensitive action needs negative tests.

### 5.3 Mandatory permission test matrix

For each protected capability:

| Case | Expected |
| --- | --- |
| Authenticated permitted role, own workspace | Allow |
| Unauthenticated | 401 or approved unauthenticated behavior |
| Authenticated with no capability | 403 |
| Correct role but different workspace/tenant | Deny without information leak |
| Revoked membership / disabled user | Deny |
| Altered resource id / forged client role | Deny |
| Explicit public route | Allow only exactly intended access |

Treat policy regressions and cross-tenant access as blocking release failures.

---

## 6. Program design: the missing step between architecture and code

For every meaningful feature, create a short design in `docs/work/FEATURE-ID/program-design.md` *before* implementation. It should answer the decisions a coding agent otherwise makes invisibly.

Required sections:

1. **Scope / touched use cases:** what changes and what must remain unchanged.
2. **File-tree diff:** files to add/change with a one-line responsibility for each.
3. **Domain types and public contracts:** key types, interfaces, function signatures only — implementation bodies not yet needed.
4. **Call-stack trees:** happy path and important failure path, from UI/API to domain to persistence/integration.
5. **Dependency impact:** which modules are touched and which boundary rules apply.
6. **Data changes:** schemas, ownership, migrations, query patterns, transaction implications.
7. **Authorization matrix:** route/use-case permission plus resource conditions.
8. **Test plan:** unit/domain, architecture, contract, integration, E2E, negative security scenarios.
9. **Risky decisions / alternatives:** what merits human review now rather than later.
10. **Vertical-slice sequence:** small increments, each independently demonstrable.

Example call tree:

```text
TaskCreateForm.submit
  -> typedApi.tasks.create(payload)
     -> TasksController.create(actor, payload)
        -> AuthorizationPolicy.assertCanCreate(actor, workspace)
        -> CreateTaskUseCase.execute(command)
           -> TasksRepository.insert(entity)
           -> Outbox.record(TaskCreated)
        -> mapToTaskResponse(result)
```

The tree is a design tool, not a promise about exact final class names. The key is exposing accidental complexity **before code exists**.

Approval question: *"Can a competent developer read just these contracts and confidently understand where a future behavior change would go?"*

---

## 7. Vertical slices and how to run agent sessions

### 7.1 One session, one bounded objective

Use a reliable handoff file rather than dragging every past chat into context. Typical division:

- **Session A — research:** read relevant use cases, existing implementation, dependency graph, tests and prior ADRs. Output facts, evidence, proposed impact, unanswered questions; no production code edits.
- **Session B — design:** propose affected modules, contracts, signatures, tests and slice plan. Human approves consequential decisions.
- **Session C — implementation:** implement a small approved slice; execute tests; provide concise report with paths, behavior, test results and deviations.
- **Session D — independent verification/review:** assess behavior and security, interfaces and architecture, changed code and regression risk; request fixes rather than polishing arbitrarily.

Small changes can collapse these sessions. Large ambiguous changes should keep boundaries explicit. Research/design context should be compressed into a **durable artifact** so implementation can start in a fresh window.

### 7.2 Suggested vertical-slice order

1. Define/publicly validate API contract and minimal stub/mocked response.
2. Exercise a representative UI flow against mock data if a UI is involved.
3. Wire controller/transport to the application use case with in-memory ports.
4. Add owned DB migration/repository and prove persistence in integration tests.
5. Implement complete business invariants and policy/error paths.
6. Verify E2E workflow, accessibility/security, observability and operational behavior.

This is one good order for many features, not an absolute prescription. Some domain-heavy flows should begin from the domain state machine. Always choose the order that exposes **the largest uncertainty earliest**.

### 7.3 Guardrails for agents

- No new library or cross-module dependency without documented reason and approval at agreed thresholds.
- Do not weaken tests or rewrite architecture checks to make a failing implementation pass.
- Do not edit unrelated files, silently alter product behavior, or invent product roles.
- Follow public exports and generated contracts; internal imports of other modules are prohibited.
- Generate code from templates for new endpoints/modules; do not hand-invent plumbing.
- Run relevant tests before committing, and report **actual commands/results**, not claims.
- No secrets in prompts, logs, code or sample data.
- Never merge or deploy on an unreviewed failure.

### 7.4 Review agent: different responsibilities, not just "make pretty"

Use formatting and lint autofix for mechanical polish. Use a separate **review agent** to independently check:

- Did the code implement the exact use cases and negative scenarios?
- Did it place logic in the correct module and layer?
- Are module public interfaces still minimal?
- Did the change introduce avoidable wrappers, duplication, surprising coupling or extra libraries?
- Are database ownership, transaction and auth boundaries preserved?
- Would one likely future change stay localized?

An agent may suggest refactors, but architectural judgment and behavior review remain human-reviewed where risk warrants. Avoid automated cosmetic rewrites that obscure the functional diff.

---

## 8. Architecture tests and fitness functions as CI contracts

**Definition:** executable checks of architectural invariants, run repeatedly like tests. They cannot prove "good architecture" in the abstract, but can stop **known bad drift**.

### 8.1 Hard, deterministic rules (CI blockers)

| Invariant | Check method | When |
| --- | --- | --- |
| No cross-domain imports of internal files | dependency-cruiser + package export rules | PR |
| Domain never imports frameworks or infrastructure | dependency-cruiser / eslint boundaries | PR |
| No circular module/package dependency | dependency-cruiser / Nx graph / custom checker | PR |
| Every controller handler has public/protected policy | AST analyzer + runtime route inventory test | PR |
| Protected endpoints deny absent/incorrect permissions | authorization integration/E2E tests | PR |
| API input/output adheres to declared schema | schema contract tests / OpenAPI diff | PR |
| New migrations can build fresh database | migration smoke/integration tests | PR |
| Module tables modified only by owner paths | query/import policy + ownership metadata review | PR |
| Shared wire package never imports server internals | dependency-cruiser | PR |
| TS strictness and compiler constraints hold | `tsc --noEmit`, `tsconfig` validation | PR |

Tools worth evaluating: [dependency-cruiser](https://github.com/sverweij/dependency-cruiser), [eslint-plugin-boundaries](https://github.com/javierbrea/eslint-plugin-boundaries), custom TypeScript AST checks where source structure is the contract, `tsc`, Playwright, and your normal Nest integration testing stack. Each rule should have a **deliberately invalid fixture** demonstrating it fails (a meta-test for the guardrail).

### 8.2 Illustrative dependency-cruiser shape

**This is a policy sketch; regenerate/validate actual matching paths after choosing the monorepo layout.** Its purpose is to convey rules, not claim a ready-to-paste config:

```js
module.exports = {
  forbidden: [
    { name: 'no-circular', severity: 'error', from: {}, to: { circular: true } },
    { name: 'domain-not-to-infrastructure', severity: 'error',
      from: { path: '/domain/' },
      to: { path: '/infrastructure/' } },
    { name: 'web-not-to-backend', severity: 'error',
      from: { path: '^apps/web/' },
      to: { path: '^apps/api/' } },
  ],
};
```

Add a generated per-module ownership/boundary matrix and checks that imports from `modules/A` to `modules/B` go **only through** module B's published interface. Lock down package exports so TypeScript tools and runtime resolution agree on what is public. Beware path aliases that accidentally bypass the rule.

### 8.3 Soft metrics (ratchets and review signals)

Track on changed code and over time:

- Cycle count and package/module dependency violations.
- Cross-module coupling and graph propagation cost.
- Source duplication and cloned-line percentage.
- Cyclomatic/cognitive complexity, high-complexity hotspots.
- Trivial wrappers, one-use abstractions, unused exports, suspicious growth in files/functions.
- Test stability, regression counts, PR size, rework rate, and changed-files-per-feature.

**Do not use a one-number "architecture score" as a substitute for judgment.** Complexity can be valid inside a deep module; splitting it into thin wrappers can game the score. Begin with trend reports and baselines. Block only high-confidence violations after tuning false positives.

### 8.4 SlopCodeBench: what to borrow and what not to borrow

SlopCodeBench evaluates agents over evolving requirements at checkpoints; it measures correctness retention and various deterministic signs of structural erosion. The paper describes **20 problems and 93 checkpoints**. Dex highlights quality signals such as complexity, duplication, decomposition, lint patterns and dependency-graph metrics. His own report cautions that the link between any one metric and *actual maintainability* is not established; at the time of his evaluation, many published detectors were Python-oriented, so do not assume plug-and-play parity for TypeScript.

**Borrow the method:** create a small internal **future-change benchmark** using your own domain, with 3–5 sequential feature requests that the agent does not see all at once. For each checkpoint, run previous and new black-box tests, measure boundary violations, count touched modules, and inspect complexity/duplication trend. This provides much more credible feedback than saying "the code looks clean".

### 8.5 Behavioral change simulation — the most valuable architecture test

For each major module, record two or three plausible extensions, e.g.:

- Add another notification transport (email → WhatsApp) without editing task domain entities or core use cases.
- Add a new workspace role without changing controller implementation across ten unrelated modules.
- Replace an external payment provider by editing its adapter and tests, not billing business rules.

Evaluate *blast radius* using actual changed files, modules, public interfaces and test fixtures. Compare to planned boundaries. This is a **design exercise** at bootstrap and a repeatable maintenance evaluation later, not a perfectly objective unit test.

---

## 9. Pre-commit, pull request CI, and scheduled deeper checks

### 9.1 Three-speed quality pipeline

**Fast / at save or staged pre-commit (seconds, auto-fix where safe):** Prettier, ESLint autofix on changed files, secret scanning or high-confidence prohibited patterns, no obvious forbidden imports if fast enough, staged-file formatting. Use `husky` + `lint-staged` or equivalent. Avoid running full test suites on every local commit.

**Full / PR CI (hard gate):** clean install from lockfile; TypeScript typecheck; lint; architecture tests; permission route inventory; unit/domain tests; contract tests; DB migration/integration tests; relevant E2E; build; security/dependency scan. Run in parallel as appropriate. Make branch protection require green CI.

**Deep / nightly or weekly (report first):** broader E2E browser paths, mutation testing on critical policies, dependency graph analysis, code growth/duplication trends, generated future-change exercises where feasible, drift and outdated ADR reporting.

```text
agent edits source
  -> optional local targeted tests
  -> pre-commit: safe auto-format / lint-staged / fast deterministic gates
  -> PR CI: typecheck + architecture + policy + unit + integration + E2E
  -> independent behavior/architecture review
  -> merge under branch protection
  -> deploy / monitor / learn
```

**Technical caveat:** A Git pre-commit hook does not automatically make an AI agent "correct itself." It rejects or transforms staged changes. A coding-agent driver can parse the failure, run safe `--fix` commands and iterate within a bounded number of attempts. No bypass or weakening of policy files is allowed without authorized approval. Local hooks can be skipped, so enforcement must happen again in server-side CI.

### 9.2 Minimum package scripts (names to implement, not assumed existing)

```json
{
  "scripts": {
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "lint": "eslint .",
    "typecheck": "<monorepo-specific TypeScript check>",
    "arch:test": "<validated dependency + AST policy checks>",
    "test": "<selected unit/domain test runner>",
    "test:integration": "<DB and HTTP integration suite>",
    "test:e2e": "<Playwright or selected E2E runner>",
    "build": "<workspace build>"
  }
}
```

Resolve actual runner commands based on chosen `pnpm` workspace / Turborepo / Nx toolchain. Don't copy placeholder commands directly into live CI.

### 9.3 GitHub Actions sketch

```yaml
name: quality
on:
  pull_request:
  push:
    branches: [main]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: <pin-to-team-version>
      - uses: actions/setup-node@v4
        with:
          node-version: <pin-supported-LTS>
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm format:check
      - run: pnpm lint
      - run: pnpm typecheck
      - run: pnpm arch:test
      - run: pnpm test
      - run: pnpm build
      # Additional integration/E2E jobs with real ephemeral services
```

This is **illustrative only** (the angle-bracket placeholders deliberately require decisions). Build valid workflow config only after choices are confirmed; CI should run green on fresh checkout. Use pinned actions/versions according to the organization's supply-chain policy.

---

## 10. The reusable NestJS + Next.js project template

**The template is a factory for starting projects**, not a fixed business application. It includes foundation plumbing and design placeholders. Domain modules are generated only when use cases justify them.

Suggested initial monorepo skeleton:

```text
software-factory-template/
├── AGENTS.md                         # small entrypoint, links to policies and docs
├── README.md                         # start, workflows, commands
├── package.json / pnpm-workspace.yaml
├── .github/workflows/quality.yml
├── .husky/ / lint-staged config
├── .dependency-cruiser.cjs / eslint config / tsconfig.base.json
├── apps/
│   ├── api/                         # NestJS composition root, modules, controllers
│   │   ├── src/app/
│   │   └── src/modules/
│   │       └── [generated-business-module]/
│   │           ├── index.ts         # intentionally exported public surface
│   │           ├── domain/
│   │           ├── application/
│   │           ├── infrastructure/
│   │           └── presentation/
│   └── web/                         # Next.js app router and feature UI
│       └── src/features/
├── packages/
│   ├── contracts/                   # public schemas/DTOs / stable API types
│   ├── authz/                       # typed policies and helpers
│   ├── config/                      # validated runtime configuration
│   └── tooling/                     # only actually shared rules/build config
├── tools/
│   ├── generate-module/            # one supported path for creating a module
│   ├── generate-use-case/
│   ├── generate-endpoint/
│   └── architecture-tests/         # policy analyzers and negative fixtures
├── docs/
│   ├── product/
│   │   ├── vision.md
│   │   ├── personas.md
│   │   ├── use-cases/UC-TEMPLATE.md
│   │   └── decisions.md
│   ├── prototypes/README.md
│   ├── architecture/
│   │   ├── overview.md
│   │   ├── modules/README.md
│   │   ├── dependency-policy.md
│   │   ├── database.md
│   │   ├── api-contract.md
│   │   ├── identity-and-permissions.md
│   │   ├── observability.md
│   │   └── adr/ADR-TEMPLATE.md
│   ├── work/FEATURE-TEMPLATE/
│   │   ├── discovery.md
│   │   ├── program-design.md
│   │   └── slices.md
│   └── quality/architecture-fitness.md
└── .agents/skills/                   # portable agent skills where supported
    ├── discover-use-cases/
    ├── prototype/
    ├── design-architecture/
    ├── design-program/
    ├── implement-slice/
    ├── review-architecture/
    └── verify-feature/
```

**Scaffold decisions to lock down once (only after validation):** TypeScript strict mode; package manager/lockfile; monorepo runner; framework versions; formatting; test tools; error envelope; OpenAPI/schema style; auth provider and session strategy; migration/ORM provider; database; migrations/testing strategy; telemetry/logger; deployment profile; secret strategy; validation library; module import policy; API client generation; license/update policy; security tooling. Other environment-specific choices should be **profiles**, not invented global mandates.

Create a `template-config` checklist (or interactive bootstrap prompts) covering: product name, expected deployments, tenant model, persistence needs, external providers, auth integration, initial personas/roles, first three use cases, domains, constraints and the desired project complexity tier.

### 10.1 Golden path/reference slice

Before scaling agents, implement **one real sample** through UI → typed client → Nest endpoint → auth policy → use case → domain invariant → repository → DB → response → E2E. It should demonstrate new-module generation, migration conventions, error paths, trace IDs, verification and clean architecture. Keep it small. Do not create ten showcase modules.

The template's scaffolding generator should create appropriate public exports, internal files, contract schemas, policy identifiers, tests and docs, and refuse to generate an endpoint with undefined auth intent.

---

## 11. Agent skills and governance

A skill is **a repeatable workflow with input, output, explicit stop conditions, and verification**, not a generic exhortation to "write clean code." Put detailed guidance in skills; keep `AGENTS.md` short and linkable.

| Skill | Input | Output | Hard stop |
| --- | --- | --- | --- |
| `define-product` | problem + intended users | vision, goals, non-goals | Ambiguous core outcome |
| `discover-use-cases` | personas + outcomes | prioritized use-case specs | Missing business decision |
| `prototype` | one uncertainty/question | disposable logic/UI experiment + verdict | Unanswered experiment question |
| `design-architecture` | confirmed behaviors | module map, ADR candidates, contracts | New ownership/security decision |
| `design-program` | accepted architecture + feature | tree diff, type signatures, call tree, tests | Architectural ambiguity |
| `implement-slice` | approved design + slice | minimal code/tests and actual results | Tests/boundaries fail |
| `review-architecture` | diff + specs | prioritized violations and change-cost review | Confirmed blocker |
| `verify-feature` | acceptance cases + runnable environment | E2E and policy verification report | Unmet acceptance criterion |
| `capture-learning` | completed PR | updated docs, ADRs, new tested guardrails | Unowned drift |

**Subagents are useful for bounded research, independent review and parallel test runs.** Avoid multiple autonomous agents editing the same module without coordination. Independent reviewers should not silently rewrite the code they are reviewing.

Rules for skill implementation:

- Provide templates and exact expected artifacts.
- Require reading only the relevant current module context; avoid large global context dumps.
- Include a known-good reference sample from the golden slice.
- Distinguish advisory checks from release blockers.
- Never let a generative agent self-approve changes to the factory's guardrail rules.
- Emit compact session handoffs: what changed, evidence, remaining blockers, next bounded task.

---

## 12. Measuring maintainability and architecture quality honestly

Architecture quality is mostly about **the cost and risk of future change**, not line count or tests passing today. No compile-time or CI metric fully proves it. Use complementary signals:

### 12.1 Contract fitness (binary checks)

These are useful hard gates: module boundaries, no cycles, no unsafe auth gaps, public API compatibility, migrations and invariants. They tell us whether the agreed architecture is being respected.

### 12.2 Operational and engineering outcomes (trend measures)

Track over several features:

- Median elapsed time from accepted change spec → verified PR.
- PR rework / number of iterations after review.
- Number of modules and public interfaces affected per ordinary feature.
- Number of incidents/regressions attributable to previous architectural decisions.
- Complexity and duplication trend *within relevant modules*, not vanity project averages.
- Proportion of change contained behind a stable public interface.
- Effort for onboarding a fresh agent session into one module.

Normalize for feature size and risk where possible; do not make a hard score that agents can game.

### 12.3 Change-scenario test (periodic qualitative benchmark)

At bootstrap, define 3–5 realistic future feature requests. On the golden path and later periodically, let an agent attempt each request from a fresh context **in a temporary branch**. Record:

- Did existing regression/behavior tests remain green?
- What public contracts did it have to change?
- How many modules had to be edited?
- Did it require bypassing policy or introducing direct DB access?
- Did it add suspicious wrappers, copy/paste or new dependencies?
- How many review iterations were needed?

This directly tests the stated thesis: *does the original design make tomorrow's work local and unsurprising?*

---

## 13. New product versus existing product

| Concern | New product | Existing product |
| --- | --- | --- |
| Product understanding | Write vision/personas/use cases | Inspect existing behaviors, usage, specs and tests |
| Architecture | Propose initial domains and foundations | Reconstruct current boundaries before making changes |
| Prototypes | Validate unknown business/UX choices | Validate risky changes or confusing existing behavior |
| Guardrails | Start strict on new code | Baseline current violations; prevent new ones, reduce old ones over time |
| Program design | Elaborate first golden slice | Design only changed files, contracts and adjacent flows |
| Database | Establish conventions and first migrations | Plan backward-compatible expand/migrate/contract changes |
| Rollout | Build tiny reference end to end | Introduce change incrementally with regression tests |
| Outcome | Product can grow safely | Existing product becomes easier to extend without a rewrite |

For brownfield adoption, do not insist on a large rewrite merely to match folder names. Introduce module interfaces and tests around the areas actually being changed. Baseline existing violations rather than switching on a failing blanket rule on day one.

---

## 14. Implementation plan for the coding session

This section is the **order of work** for implementing the template itself. Every phase should leave a green, usable repo. Do not run all phases at once without checkpoints.

### Phase 0 — Decisions and evaluation criteria (human + design agent)

1. Confirm exact stack, package manager, database/ORM, deployment, auth approach, testing tools and monorepo tooling.
2. Identify 1 representative trial product and its first 2–3 use cases (do not build the trial product yet).
3. Decide architecture requirements: tenants, roles, integrations, data/latency/security constraints.
4. Write an ADR for the template's essential defaults and a table of open decisions.
5. Establish definition of success: new repo bootstraps, one vertical slice builds, known boundary/security violations fail the required check.

**Exit:** approved `docs/template-decisions.md` and acceptance checklist.

### Phase 1 — Minimal runnable monorepo

- Create Nest + Next + TypeScript monorepo with strict compiler settings, shared `contracts` package and root scripts.
- Ensure clean install, local dev start, HTTP health endpoint, single web page, logger and env validation.
- Add formatting and lint config, local hook and basic GitHub Actions job.

**Exit:** `pnpm install`, dev, typecheck, lint and build work from fresh checkout; CI green.

### Phase 2 — Executable module architecture

- Define intended domain/application/adapters structure and public exports.
- Introduce dependency-cruiser (and optionally eslint boundary enforcement).
- Add failing fixtures for imports to another module's internals, domain importing infrastructure, web importing backend, and a cycle.
- Put module policy under `docs/architecture/dependency-policy.md`.

**Exit:** each deliberate architecture violation fails a test; valid reference module passes.

### Phase 3 — Identity, policy and typed contracts

- Choose actual authn integration; do not fabricate identity provider.
- Create typed role/permission/capability registry; explicit route policy or required decorator.
- Wire default-deny Nest guard, object/tenant policy hooks and policy inventory check.
- Define shared schemas and typed API client generation/usage.
- Test denied-by-default, missing policies and cross-tenant access.

**Exit:** purposely adding an unprotected route or unknown permission fails at compile/build/test, with documented exception path for public routes.

### Phase 4 — Data layer and first golden slice

- Choose DB/ORM/migrations, ownership conventions and ephemeral test DB.
- Implement one complete real feature on the golden path, with error cases.
- Include E2E browser or HTTP acceptance proof, ownership/security negative tests and an observability trace example.
- Verify the shape and make any necessary structural corrections **before templating**.

**Exit:** representative use case works locally and in CI, while forbidden changes fail.

### Phase 5 — Generators, docs and agent skills

- Implement `generate-use-case`, `generate-module` and `generate-endpoint` (simple CLI scripts are enough at first).
- Use generators to produce policies, exports, tests, and approved structure.
- Fill placeholder product/architecture templates and ADR examples.
- Create skills one at a time: discover → program-design → implement-slice → review → verify; add prototype skill as an optional detour.
- Add a tiny `AGENTS.md` index with only stable rules and links.

**Exit:** generated module passes checks without manual structural repairs, and an agent can follow documented commands.

### Phase 6 — Prove leverage on the trial product

- Instantiate the template on a *real new product*, fill vision/personas/use cases, prototype only uncertainties.
- Execute two or three sequential feature changes with separate design/code reviews.
- Record time, PR rework, modules touched, new dependencies and guardrail failures.
- Deliberately challenge architecture with a realistic future-change scenario.
- Improve only the template rules/generators demonstrated to be useful. Avoid building a giant harness speculatively.

**Exit:** the trial product ships a useful workflow, and the template demonstrably makes subsequent changes easier without hiding maintainability problems.

---

## 15. Definition of done: the factory itself

The first version of the factory is accepted only when:

- [ ] A fresh project can be generated and run from the documented commands.
- [ ] Product vision, personas, use cases and open questions have usable placeholders.
- [ ] Architecture, database, API and auth decisions have explicit, findable records.
- [ ] A business module can be generated with a deliberately small published interface.
- [ ] TypeScript strictness is on and the build succeeds.
- [ ] Static module-boundary and no-cycle tests demonstrably catch violations.
- [ ] New routes must explicitly declare policy; runtime deny-by-default and policy tests work.
- [ ] Server/database internals cannot be imported casually into the Next frontend.
- [ ] Each DB table has an owner and migrations have validation.
- [ ] One realistic vertical slice includes UI, API, domain, DB, errors, auth and E2E verification.
- [ ] Pre-commit only runs fast checks; full CI re-enforces hard constraints independently.
- [ ] Agents have short, reusable workflows with explicit handoffs and stop conditions.
- [ ] An independent reviewer can identify where changes belong using module contracts.
- [ ] At least one sequential change scenario has been performed to measure evolution cost.
- [ ] Dependencies and security policy changes require review, not opportunistic green-test editing.

**Avoid false success:** generated files existing is not enough. We need testable architectural enforcement and proof under **sequential change**.

---

## 16. Common failure modes to actively avoid

1. **"Set architecture once forever."** High-level intentions can remain stable, but architecture must evolve through explicit, reviewable decisions.
2. **Ceremonial clean architecture.** Extra wrappers and boilerplate can hurt maintainability. Use deep modules and meaningful seams rather than automatic five-layer decomposition.
3. **Global shared-types dumping ground.** It becomes the highest-coupled package in the app. Share contracts selectively and freeze true semantics.
4. **Trusting types to secure data.** `satisfies` catches invalid declarations, not forged HTTP tokens or cross-tenant resource access. Runtime default-deny and negative authorization tests remain essential.
5. **Treating SlopCodeBench as a CI plugin.** It is a benchmark; adapt vetted structural metrics and sequential evaluation, not blindly its source rule set.
6. **AI review replacing architecture ownership.** Models can spot suspicious code, but they can also rationalize poor abstractions. Consequential boundary changes need accountable review.
7. **All tests pre-commit.** Slow hooks lead to bypassing. Keep local checks cheap, PR checks comprehensive and independent.
8. **Unclear module owner.** If any feature can write any table or import any service, local changes eventually become shotgun surgery.
9. **Autofix making unrelated changes.** Mechanical fixes on staged files are good; broad style refactors during functional work hide the signal in code review.
10. **Framework before product.** Start from user use cases; technical architecture is the means to serve changeable behavior, not the reason the product exists.
11. **Testing only the happy path.** Unauthorized actors, retries, failures and cross-tenant behavior are first-class contract cases.
12. **Agent sessions with no handoff artifact.** Research, decisions, deltas and actual verification results must survive context resets.

---

## 17. The first coding session: copy/paste prompt

> **Mission:** Help me build a reusable, agent-friendly TypeScript software-factory project template using NestJS and Next.js. Read the attached `AI_Software_Factory_Blueprint.md` as our design brief. The purpose is maintainable software under repeated AI-driven changes, not maximal initial code volume.
>
> **Start with Phase 0 only. Do not scaffold the whole repository yet.** Interview me on the truly consequential unknown choices: exact third stack/tool if any, pnpm/Turborepo/Nx, Node version, database/ORM/migrations, auth provider, deploy target, testing stack, tenancy and first trial product. Offer sound defaults but never treat them as approved. Record decisions and disagreements in a short draft ADR and `docs/template-decisions.md`.
>
> Then show me a proposed repository tree, module ownership rule, dependency matrix, typed authorization strategy (compile/build + runtime deny-by-default), database ownership model, contracts strategy, representative golden vertical slice, CI gates and a phased implementation plan. Distinguish executable hard constraints from advisory architecture metrics. Highlight where my approval is required. Optimize for **deep modules, narrow public interfaces and low future change cost**. Build one working phase at a time, prove it with real commands, and pause for approval at architecture-changing decisions.
>
> **Definition of done:** new projects can start with product/persona/use-case templates, agents can follow a golden path, prohibited dependencies fail CI, undocumented endpoint security fails CI or defaults to deny, runtime auth policies are tested, and one reference vertical slice works across Next → typed contract → Nest → domain → DB. We also exercise sequential future-change scenarios before calling the factory successful.

---

## 18. Primary references and reading order

1. Dex Horthy, **Why Software Factories Fail** — https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md
2. Dex Horthy, **Advanced Context Engineering for Coding Agents** — https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md
3. HumanLayer, **Skills** — https://github.com/humanlayer/skills
4. Matt Pocock, **Prototype skill** — https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype
5. SprocketLab, **SlopCodeBench** — https://github.com/SprocketLab/slop-code-bench
6. SlopCodeBench paper — https://arxiv.org/abs/2603.24755
7. Dex Horthy, **Benchmarking Opus 5 on SlopCodeBench** — https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md
8. **dependency-cruiser** docs — https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md
9. **eslint-plugin-boundaries** — https://github.com/javierbrea/eslint-plugin-boundaries
10. Robert C. Martin, **Clean Architecture** (book); John Ousterhout, **A Philosophy of Software Design** (book).

**Source integrity note:** We discussed a Matt Pocock/Uncle Bob interview, but its exact episode was not confidently verified during this research; the blueprint follows broadly established design concepts rather than attributing specific words to that recording. The "slop" tools discussed were also ambiguous: SlopCodeBench is confirmed and distinct from third-party code linters such as `slop-mop`, `slopscore` or other similarly named utilities. Treat any such tool as a separate evaluation, not as the definitive source of architectural quality.

---

**Governing maxim:** Decide high-leverage principles explicitly. Make the good path automatic. Make violations visible. Review consequential design before coding. Test future change, not merely today's behavior. Let the agents execute within constraints that preserve human understanding.
