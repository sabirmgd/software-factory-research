// These fixtures are compiled but are not run. Removing a type restriction makes
// its @ts-expect-error unused, which is itself a compiler error.
import type { Permission, EndpointId, EndpointPolicy, Role } from './contracts.js';
const known: Permission = 'tasks:assign';
// @ts-expect-error Unknown permission must not compile.
const unknown: Permission = 'tasks:erase';
// @ts-expect-error Every known endpoint must have a declaration.
const missingRoute: Record<EndpointId, EndpointPolicy> = { 'tasks.assign': { access: 'public' } };
// @ts-expect-error Every known role must be represented in this registry.
const missingRole: Record<Role, readonly Permission[]> = { manager: ['tasks:assign'], member: [] };
void [known, unknown, missingRoute, missingRole];
