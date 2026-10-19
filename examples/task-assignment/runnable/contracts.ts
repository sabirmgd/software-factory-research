/** Illustrative public contracts. Authentication happens at a trusted boundary. */
export const PERMISSIONS = ['tasks:assign', 'tasks:read'] as const;
export type Permission = typeof PERMISSIONS[number];
export type Role = 'manager' | 'member' | 'guest';
export const GRANTS = {
  manager: ['tasks:assign', 'tasks:read'], member: ['tasks:read'], guest: ['tasks:read'],
} as const satisfies Record<Role, readonly Permission[]>;
export type EndpointId = 'tasks.assign' | 'tasks.read';
export type EndpointPolicy = { access: 'public' } | { access: 'authenticated'; permission: Permission };
export const ENDPOINT_POLICIES = {
  'tasks.assign': { access: 'authenticated', permission: 'tasks:assign' },
  'tasks.read': { access: 'authenticated', permission: 'tasks:read' },
} as const satisfies Record<EndpointId, EndpointPolicy>;

export interface AuthenticatedActor { id: string; authenticated: true }
export interface AssignCommand {
  workspaceId: string; taskId: string; assigneeId: string;
  expectedRevision: number; requestId: string;
}
export type Failure = 'invalid_command' | 'unauthenticated' | 'forbidden' | 'not_found'
  | 'ineligible_assignee' | 'revision_conflict' | 'idempotency_conflict' | 'storage_unavailable';
export type AssignResult =
  | { ok: true; taskId: string; assigneeId: string; revision: number; replayed: boolean }
  | { ok: false; error: Failure };
export interface Membership { userId: string; workspaceId: string; role: Role; active: boolean }
export interface Task {
  id: string; workspaceId: string; assigneeId: string | null; revision: number;
  visibility: 'workspace' | 'restricted'; sharedWith: string[];
}
export interface Audit { taskId: string; workspaceId: string; actorId: string; assigneeId: string; revision: number }
export interface Fixture { tasks: Task[]; memberships: Membership[] }
