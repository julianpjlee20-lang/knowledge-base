# 4-Agent Team Development Prompt Template

**Project**: [[Claude Code Setup Documentation]]BMAD Accounting SaaS
**Created**: 2025-10-30
**Purpose**: Structured prompts for PM, Architecture, Frontend, and Backend agents

---

## Universal Resources (All Agents)

### Available to All Agents:
- **MCP Servers**:  Obsidian, ref-tools, YouTube
- **Universal Skills**: 
  - `bmad-method` - For structured planning and workflows
  - `context-engineering` - For CLAUDE.md and documentation
  - `ref-tools` - For accessing technical documentation
- **Documentation Access**: Use `ref-tools` MCP before any technical implementation

---

## Agent 1: Product Manager (PM) Agent

### Primary Responsibilities
- Requirements gathering and PRD creation
- User story definition
- Sprint planning and backlog management
- Stakeholder communication
- Feature prioritization

### Dedicated Skills
```
Skill(bmad-method)              # BMAD PM agent workflows
Skill(context-engineering)       # Creating INITIAL.md and PRPs
```

### Dedicated MCP Servers
- Obsidian: Project management, roadmaps, documentation
- Playwright: Market research, competitor analysis
- **Obsidian**: Meeting notes, decision logs

### Specialized Agents (via Task Tool)
- `general-purpose` - Multi-step research and analysis
- `code-documentation:docs-architect` - Creating comprehensive product documentation
- `code-documentation:tutorial-engineer` - User guides and tutorials

### Sample PM Prompt
```
Using the PM Agent capabilities:

1. First, read `bmad-method` skill for PM best practices
2. Use Obsidian to check current project roadmap
3. Create a PRD for [FEATURE NAME] that includes:
   - Problem statement
   - User stories with acceptance criteria
   - Technical requirements
   - Success metrics
   - Timeline estimates

4. Use Brave Search to research:
   - Competitor features in accounting SaaS
   - Industry best practices for [SPECIFIC FEATURE]

5. Document findings in Obsidian for team reference
6. Create Obsidian database entry for sprint planning

Tools to use:
- Skill(bmad-method)
- brave_web_search
- obsidian_append_content
```

---

## Agent 2: Architecture Agent

### Primary Responsibilities
- System design and architecture decisions
- Database schema design
- API design and contracts
- Infrastructure planning
- Security and scalability considerations

### Dedicated Skills
```
Skill(bmad-method)                                    # BMAD Architect agent workflows
Skill(backend-development:architecture-patterns)       # Clean Architecture, DDD
Skill(backend-development:api-design-principles)       # REST/GraphQL design
Skill(backend-development:microservices-patterns)      # Service boundaries
Skill(python-development:async-python-patterns)        # Async architecture
Skill(cloud-infrastructure)                           # Cloud-native patterns
```

### Dedicated MCP Servers
- **ref-tools**: SQLAlchemy, FastAPI, PostgreSQL documentation
- **Notion**: Architecture Decision Records (ADRs)
- **Obsidian**: Technical diagrams, design docs

### Specialized Agents (via Task Tool)
- `backend-development:backend-architect` - Scalable API design
- `kubernetes-operations:kubernetes-architect` - Cloud-native infrastructure
- `cloud-infrastructure:cloud-architect` - AWS/Azure/GCP architecture
- `full-stack-orchestration:security-auditor` - Security review
- `code-review-ai:architect-review` - Architecture pattern reviews

### Sample Architecture Prompt
```
Using the Architecture Agent capabilities:

1. Read relevant skills:
   - Skill(backend-development:architecture-patterns)
   - Skill(backend-development:api-design-principles)

2. Use ref-tools to get current best practices:
   - resolve-library-id: "FastAPI"
   - get-library-docs: FastAPI async patterns
   - resolve-library-id: "SQLAlchemy"
   - get-library-docs: SQLAlchemy 2.0 async ORM

3. Design [FEATURE] architecture:
   - Database schema (ERD)
   - API endpoints and contracts
   - Service layer design
   - Authentication/authorization flow
   - Caching strategy
   - Error handling patterns

4. Create ADR in Notion documenting:
   - Context and problem
   - Considered options
   - Decision and rationale
   - Consequences

5. Use Task tool with `backend-architect` agent for validation:
   Task(
     subagent_type="backend-development:backend-architect",
     instruction="Review this architecture design for scalability and best practices"
   )

6. Save architecture diagrams to Obsidian

Tools to use:
- Skill(backend-development:architecture-patterns)
- resolve-library-id + get-library-docs
- notion_create_page (ADRs)
- Task(backend-architect)
```

---

## Agent 3: Backend Agent

### Primary Responsibilities
- FastAPI endpoint implementation
- Database models and migrations
- Business logic and service layer
- Background tasks and async operations
- API testing and validation

### Dedicated Skills
```
Skill(python-development:async-python-patterns)        # Asyncio patterns
Skill(python-development:python-testing-patterns)      # pytest, TDD
Skill(python-development:python-performance-optimization) # Profiling
Skill(python-development:uv-package-manager)           # Fast dependency management
Skill(backend-development:api-design-principles)       # API best practices
```

### Dedicated MCP Servers
- **ref-tools**: FastAPI, SQLAlchemy, Pydantic, pytest documentation
- **Obsidian**: Code snippets, technical notes

### Specialized Agents (via Task Tool)
- `python-development:fastapi-pro` - FastAPI implementation
- `python-development:python-pro` - Python optimization
- `backend-development:tdd-orchestrator` - TDD workflows
- `full-stack-orchestration:test-automator` - Test automation
- `code-documentation:code-reviewer` - Code quality review
- `debugging-toolkit:debugger` - Error debugging
- `unit-testing:test-automator` - Unit test creation

### Sample Backend Prompt
```
Using the Backend Agent capabilities:

1. Read relevant skills first:
   - Skill(python-development:async-python-patterns)
   - Skill(python-development:python-testing-patterns)

2. Get current documentation via ref-tools:
   - resolve-library-id: "FastAPI"
   - get-library-docs: FastAPI dependency injection and async
   - resolve-library-id: "SQLAlchemy" 
   - get-library-docs: SQLAlchemy 2.0 async session management
   - resolve-library-id: "Pydantic"
   - get-library-docs: Pydantic v2 validation

3. Implement [FEATURE] with Task agent:
   Task(
     subagent_type="python-development:fastapi-pro",
     instruction="Implement the following API endpoints:
     - POST /api/v1/invoices - Create invoice
     - GET /api/v1/invoices/{id} - Get invoice
     - PATCH /api/v1/invoices/{id} - Update invoice
     
     Requirements:
     - Use async/await throughout
     - SQLAlchemy 2.0 async patterns
     - Pydantic v2 validation
     - Proper error handling
     - JWT authentication
     - Include docstrings
     "
   )

4. Create comprehensive tests:
   Task(
     subagent_type="unit-testing:test-automator",
     instruction="Create pytest tests for invoice API with:
     - Happy path scenarios
     - Error cases (404, 400, 401, 403)
     - Edge cases
     - Async test fixtures
     - 80%+ coverage target
     "
   )

5. Code review:
   Task(
     subagent_type="code-documentation:code-reviewer",
     instruction="Review invoice implementation for:
     - Security vulnerabilities
     - Performance issues
     - Code quality and patterns
     - Best practices compliance
     "
   )

6. Document implementation in Obsidian:
   - API examples
   - Common patterns used
   - Gotchas and lessons learned

Tools to use:
- Skill(python-development:async-python-patterns)
- resolve-library-id + get-library-docs
- Task(fastapi-pro)
- Task(test-automator)
- Task(code-reviewer)
- obsidian_append_content
```

---

## Agent 4: Frontend Agent

### Primary Responsibilities
- React/Next.js component development
- State management implementation
- UI/UX implementation
- API integration
- Frontend testing

### Dedicated Skills
```
Skill(javascript-typescript:modern-javascript-patterns)  # ES6+, async/await
Skill(javascript-typescript:typescript-advanced-types)   # Advanced TypeScript
Skill(javascript-typescript:javascript-testing-patterns) # Jest, Vitest
```

### Dedicated MCP Servers
- **ref-tools**: React, Next.js, TypeScript, TanStack Query documentation
- **Obsidian**: Component library, design patterns

### Specialized Agents (via Task Tool)
- `frontend-mobile-development:frontend-developer` - React/Next.js implementation
- `javascript-typescript:typescript-pro` - TypeScript patterns
- `javascript-typescript:javascript-pro` - Modern JavaScript
- `full-stack-orchestration:test-automator` - Frontend testing
- `code-documentation:code-reviewer` - Code review
- `debugging-toolkit:debugger` - UI debugging

### Sample Frontend Prompt
```
Using the Frontend Agent capabilities:

1. Read relevant skills:
   - Skill(javascript-typescript:modern-javascript-patterns)
   - Skill(javascript-typescript:typescript-advanced-types)

2. Get documentation via ref-tools:
   - resolve-library-id: "React"
   - get-library-docs: React hooks and performance
   - resolve-library-id: "Next.js"
   - get-library-docs: Next.js 14 app router and server components
   - resolve-library-id: "TypeScript"
   - get-library-docs: TypeScript generics and utility types

3. Implement [FEATURE] UI:
   Task(
     subagent_type="frontend-mobile-development:frontend-developer",
     instruction="Create Invoice Management Dashboard:
     
     Components needed:
     - InvoiceList (server component with pagination)
     - InvoiceCard (client component)
     - InvoiceForm (with validation)
     - InvoiceDetails (with real-time updates)
     
     Requirements:
     - TypeScript strict mode
     - TanStack Query for API calls
     - Zod for validation
     - Shadcn/ui components
     - Responsive design
     - Loading and error states
     - Optimistic updates
     "
   )

4. Implement state management:
   - Use Zustand for global state
   - TanStack Query for server state
   - React Hook Form for forms

5. Create tests:
   Task(
     subagent_type="full-stack-orchestration:test-automator",
     instruction="Create frontend tests:
     - Component unit tests (Vitest + Testing Library)
     - Integration tests for invoice flow
     - E2E tests for critical paths
     - Accessibility tests
     "
   )

6. Code review:
   Task(
     subagent_type="code-documentation:code-reviewer",
     instruction="Review frontend code for:
     - Performance (React profiler)
     - Accessibility (WCAG 2.1)
     - Type safety
     - Best practices
     "
   )

7. Document components in Obsidian:
   - Component API
   - Usage examples
   - Props documentation

Tools to use:
- Skill(javascript-typescript:modern-javascript-patterns)
- resolve-library-id + get-library-docs
- Task(frontend-developer)
- Task(typescript-pro)
- Task(test-automator)
- obsidian_append_content
```

---

## Cross-Agent Workflows

### Example: Full Feature Implementation Flow

```
STEP 1: PM Agent - Requirements
────────────────────────────────
1. Skill(bmad-method) for PM workflows
2. Create PRD in Notion
3. Define user stories
4. Research via Brave Search
5. Document in Obsidian

STEP 2: Architecture Agent - Design
────────────────────────────────────
1. Skill(backend-development:architecture-patterns)
2. Use ref-tools for FastAPI/SQLAlchemy docs
3. Design database schema
4. Design API contracts
5. Create ADR in Notion
6. Task(backend-architect) for validation
7. Document in Obsidian

STEP 3: Backend Agent - Implementation
───────────────────────────────────────
1. Skill(python-development:async-python-patterns)
2. Use ref-tools for current docs
3. Task(fastapi-pro) for API implementation
4. Task(test-automator) for test creation
5. Task(code-reviewer) for quality check
6. Document patterns in Obsidian

STEP 4: Frontend Agent - UI Implementation
───────────────────────────────────────────
1. Skill(javascript-typescript:modern-javascript-patterns)
2. Use ref-tools for React/Next.js docs
3. Task(frontend-developer) for component creation
4. Task(test-automator) for testing
5. Task(code-reviewer) for review
6. Document components in Obsidian

STEP 5: All Agents - Integration & Deployment
──────────────────────────────────────────────
1. Task(deployment-engineer) for CI/CD
2. Task(security-auditor) for security scan
3. Task(performance-engineer) for optimization
4. Update Notion with completion status
5. Create release notes in Obsidian
```

---

## Best Practices for Agent Prompts

### 1. Always Start with Skills
```
Before implementing anything:
1. Read relevant Skill() for best practices
2. Use ref-tools to get current documentation
3. Then proceed with implementation
```

### 2. Use Task Tool for Specialized Work
```
Don't try to do everything yourself:
- Use Task(subagent_type) for specialized implementations
- Let expert agents handle their domain
- Focus on orchestration and coordination
```

### 3. Document Everything
```
After each major step:
- Notion: Official decisions, roadmaps, ADRs
- Obsidian: Technical notes, patterns, learnings
```

### 4. Chain Agents Properly
```
PM → Architecture → Backend/Frontend → Testing → Deployment
Each agent builds on previous agent's output
```

### 5. Leverage ref-tools Heavily
```
ALWAYS use ref-tools before implementation:
1. resolve-library-id: "library-name"
2. get-library-docs: specific topic
3. Get 60-95% token efficiency vs traditional docs
```

---

## Quick Reference Commands

### PM Agent Commands
```bash
Skill(bmad-method)
notion_create_page(database_id, properties, content)
brave_web_search(query)
obsidian_append_content(filepath, content)
Task(subagent_type="general-purpose", instruction="...")
```

### Architecture Agent Commands
```bash
Skill(backend-development:architecture-patterns)
resolve-library-id(libraryName)
get-library-docs(context7CompatibleLibraryID, topic)
notion_create_page(database_id, properties, content)
Task(subagent_type="backend-development:backend-architect", instruction="...")
obsidian_append_content(filepath, content)
```

### Backend Agent Commands
```bash
Skill(python-development:async-python-patterns)
resolve-library-id(libraryName)
get-library-docs(context7CompatibleLibraryID, topic)
Task(subagent_type="python-development:fastapi-pro", instruction="...")
Task(subagent_type="unit-testing:test-automator", instruction="...")
Task(subagent_type="code-documentation:code-reviewer", instruction="...")
obsidian_append_content(filepath, content)
```

### Frontend Agent Commands
```bash
Skill(javascript-typescript:modern-javascript-patterns)
resolve-library-id(libraryName)
get-library-docs(context7CompatibleLibraryID, topic)
Task(subagent_type="frontend-mobile-development:frontend-developer", instruction="...")
Task(subagent_type="javascript-typescript:typescript-pro", instruction="...")
Task(subagent_type="full-stack-orchestration:test-automator", instruction="...")
obsidian_append_content(filepath, content)
```

---

## Example: Complete Feature Request

### User Request: "Build invoice management feature"

#### PM Agent Response:
```
Acting as PM Agent:

1. First, let me read the BMAD methodology for PM workflows:
   Skill(bmad-method)

2. Research existing accounting SaaS invoice features:
   brave_web_search("accounting SaaS invoice management best practices")

3. Create PRD in Notion:
   notion_create_page(
     database_id="projects",
     properties={
       "Name": "Invoice Management Feature",
       "Status": "In Planning",
       "Priority": "High"
     },
     content={
       "Problem Statement": "...",
       "User Stories": "...",
       "Acceptance Criteria": "...",
       "Technical Requirements": "...",
       "Success Metrics": "..."
     }
   )

4. Document research findings:
   obsidian_append_content(
     filepath="Projects/Invoice Management/Research.md",
     content="# Invoice Feature Research..."
   )

Output: PRD complete, ready for Architecture phase
```

#### Architecture Agent Response:
```
Acting as Architecture Agent:

1. Read architecture patterns:
   Skill(backend-development:architecture-patterns)
   Skill(backend-development:api-design-principles)

2. Get latest FastAPI and SQLAlchemy documentation:
   resolve-library-id("FastAPI")
   get-library-docs("/tiangolo/fastapi", "async patterns dependency injection")
   
   resolve-library-id("SQLAlchemy")
   get-library-docs("/sqlalchemy/sqlalchemy", "async ORM relationships")

3. Design architecture with expert agent:
   Task(
     subagent_type="backend-development:backend-architect",
     instruction="Design invoice management architecture:
     
     Database Schema:
     - invoices table (id, user_id, client_id, amount, status, created_at)
     - invoice_items table (id, invoice_id, description, quantity, price)
     - Relationships: one-to-many
     
     API Endpoints:
     - POST /api/v1/invoices
     - GET /api/v1/invoices (with pagination, filters)
     - GET /api/v1/invoices/{id}
     - PATCH /api/v1/invoices/{id}
     - DELETE /api/v1/invoices/{id}
     - POST /api/v1/invoices/{id}/send
     
     Consider: caching, rate limiting, authentication, validation
     Provide: SQLAlchemy models, Pydantic schemas, FastAPI router structure
     "
   )

4. Create ADR in Notion:
   notion_create_page(
     database_id="ADRs",
     properties={
       "Title": "ADR-001: Invoice Architecture",
       "Status": "Approved"
     },
     content={
       "Context": "...",
       "Decision": "...",
       "Consequences": "..."
     }
   )

5. Document architecture:
   obsidian_append_content(
     filepath="Architecture/Invoice-System.md",
     content="# Invoice System Architecture..."
   )

Output: Architecture documented, ready for implementation
```

#### Backend Agent Response:
```
Acting as Backend Agent:

1. Read async patterns:
   Skill(python-development:async-python-patterns)
   Skill(python-development:python-testing-patterns)

2. Get implementation docs:
   resolve-library-id("FastAPI")
   get-library-docs("/tiangolo/fastapi", "async dependency injection")
   
   resolve-library-id("Pydantic")
   get-library-docs("/pydantic/pydantic", "v2 validation")

3. Implement API with expert agent:
   Task(
     subagent_type="python-development:fastapi-pro",
     instruction="Implement invoice API endpoints based on architecture.
     
     Files to create:
     - app/models/invoice.py (SQLAlchemy models)
     - app/schemas/invoice.py (Pydantic schemas)
     - app/services/invoice.py (business logic)
     - app/api/v1/endpoints/invoices.py (FastAPI router)
     
     Requirements:
     - Full async/await
     - SQLAlchemy 2.0 async patterns
     - Pydantic v2 validation
     - Proper error handling (HTTPException)
     - JWT authentication via dependency
     - Pagination for list endpoint
     - Comprehensive docstrings
     "
   )

4. Create tests:
   Task(
     subagent_type="unit-testing:test-automator",
     instruction="Create pytest suite for invoice API:
     - tests/test_invoice_api.py
     - Async test fixtures
     - Test all endpoints (CRUD + send)
     - Happy paths and error cases
     - Mock external services
     - Target 85%+ coverage
     "
   )

5. Code review:
   Task(
     subagent_type="code-documentation:code-reviewer",
     instruction="Review invoice implementation for:
     - SQL injection vulnerabilities
     - Authentication bypass risks
     - N+1 query problems
     - Async best practices
     - Error handling completeness
     "
   )

6. Document patterns:
   obsidian_append_content(
     filepath="Backend/Invoice-Implementation.md",
     content="# Invoice API Implementation Notes..."
   )

Output: Backend complete with tests, ready for frontend integration
```

#### Frontend Agent Response:
```
Acting as Frontend Agent:

1. Read TypeScript patterns:
   Skill(javascript-typescript:modern-javascript-patterns)
   Skill(javascript-typescript:typescript-advanced-types)

2. Get frontend docs:
   resolve-library-id("Next.js")
   get-library-docs("/vercel/next.js", "app router server components")
   
   resolve-library-id("React")
   get-library-docs("/facebook/react", "hooks performance optimization")

3. Implement UI with expert agent:
   Task(
     subagent_type="frontend-mobile-development:frontend-developer",
     instruction="Create invoice management UI:
     
     Pages:
     - app/invoices/page.tsx (list with server-side pagination)
     - app/invoices/[id]/page.tsx (detail view)
     - app/invoices/new/page.tsx (create form)
     
     Components:
     - components/invoices/InvoiceList.tsx
     - components/invoices/InvoiceCard.tsx
     - components/invoices/InvoiceForm.tsx
     - components/invoices/InvoiceStats.tsx
     
     Requirements:
     - TypeScript strict mode
     - TanStack Query for API calls
     - Zod validation on forms
     - Shadcn/ui components
     - Responsive design (mobile-first)
     - Loading/error states
     - Optimistic updates
     - Real-time status updates (optional)
     "
   )

4. Create tests:
   Task(
     subagent_type="full-stack-orchestration:test-automator",
     instruction="Create frontend tests:
     - Unit tests for components (Vitest + Testing Library)
     - Integration tests for invoice flow
     - Mock API responses
     - Accessibility tests
     "
   )

5. Document components:
   obsidian_append_content(
     filepath="Frontend/Invoice-Components.md",
     content="# Invoice UI Components..."
   )

Output: Frontend complete, feature ready for deployment
```

---

## Templates for Common Scenarios

### Scenario 1: New API Endpoint
```
Architecture Agent → Design API
Backend Agent → Implement + Test
Frontend Agent → Integrate + UI
```

### Scenario 2: Database Migration
```
Architecture Agent → Design schema changes
Backend Agent → Create migration + Update models
Frontend Agent → Update types + API calls
```

### Scenario 3: Bug Fix
```
Backend/Frontend Agent → Use debugging-toolkit:debugger
Task(subagent_type="debugging-toolkit:debugger", instruction="Debug issue...")
```

### Scenario 4: Performance Optimization
```
Architecture Agent → Analyze bottlenecks
Backend Agent → Task(performance-engineer)
Frontend Agent → Task(performance-engineer)
```

### Scenario 5: Security Audit
```
All Agents → Task(security-auditor)
Review findings → Fix vulnerabilities
Document in Notion
```

---

## Tips for Effective Agent Collaboration

1. **Clear Handoffs**: Each agent should produce output that next agent can consume
2. **Documentation First**: Always document decisions before implementation
3. **Use ref-tools Early**: Get latest docs before any implementation
4. **Leverage Task Agents**: Don't reinvent the wheel, use specialized agents
5. **Review Everything**: Use code-reviewer agent after major implementations
6. **Test Continuously**: Use test-automator agent throughout development
7. **Keep Obsidian Updated**: Personal knowledge base for quick reference
8. **Notion for Official Records**: Single source of truth for team decisions

---

**Tags**: #agents #workflow #prompting #best-practices #bmad #accounting-saas
