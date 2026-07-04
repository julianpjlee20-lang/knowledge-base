

**Project**: BMAD Accounting SaaS

**Last Updated**: 2025-10-30

**Purpose**: Track MCP servers, agents, and skills configuration for this project

  

---

  

## MCP (Model Context Protocol) Servers

  

### 1. MCP_DOCKER (Primary MCP Server)

Containerized MCP server providing multiple integrations:

  

#### Notion Integration

- **Create/Read/Update/Delete**: Pages, databases, blocks, comments

- **Query**: Database queries with filters and sorting

- **Search**: Search across workspace

- **User Management**: Get user profiles and bot info

  

#### Brave Search API

- `brave_web_search` - General web search with rich metadata

- `brave_local_search` - Local business and places search

- `brave_news_search` - News articles search

- `brave_image_search` - Image search

- `brave_video_search` - Video search

- `brave_summarizer` - AI-generated summaries of search results

  

#### LINE Messaging API

- **Push Messages**: Text and Flex messages to users

- **Broadcast Messages**: Send to all followers

- **Rich Menus**: Create and manage interactive menus

- **User Profiles**: Get user information

- **Quota Management**: Check message quotas

  

#### Browser Automation (Playwright)

- **Navigation**: Navigate, back, tabs management

- **Interaction**: Click, type, hover, drag, fill forms

- **Evaluation**: Execute JavaScript on pages

- **Snapshots**: Accessibility snapshots and screenshots

- **Network**: Monitor requests and console messages

  

#### YouTube Integration

- `get_transcript` - Retrieve video transcripts

- `get_timed_transcript` - Transcripts with timestamps

- `get_video_info` - Video metadata

  

#### Obsidian Vault Integration

- **File Operations**: Read, write, append, delete files

- **Search**: Simple text search and complex JsonLogic queries

- **Periodic Notes**: Daily, weekly, monthly, quarterly, yearly notes

- **Patching**: Insert content relative to headings, blocks, or frontmatter

  

#### ref-tools (Documentation Reference)

- `resolve-library-id` - Find Context7-compatible library IDs

- `get-library-docs` - Fetch up-to-date technical documentation

- **Purpose**: Access current docs for APIs, services, libraries, frameworks

- **Token Efficiency**: 60-95% reduction vs traditional approaches

  

### 2. IDE Integration (VS Code)

- `getDiagnostics` - Get language diagnostics/errors

- `executeCode` - Execute Python code in Jupyter kernel

  

---

  

## Available Skills

  

### User Skills (Project-Specific)

  

#### 1. **bmad-method**

- **Type**: Project, gitignored

- **Purpose**: BMAD-METHOD framework guide (Breakthrough Method for Agile AI-Driven Development)

- **Use Cases**:

  - Plan projects using specialized AI agents (Analyst, PM, Architect, Dev, QA)

  - Create PRDs and architecture documents

  - Implement agile development workflows

  - Work with brownfield/greenfield projects

  

#### 2. **context-engineering**

- **Type**: Project, gitignored

- **Purpose**: AI coding projects with context engineering methodology

- **Use Cases**:

  - Creating CLAUDE.md files

  - INITIAL.md requirements

  - PRPs (Product Requirements Prompts)

  - Custom commands and subagents setup

  

#### 3. **crewai**

- **Type**: Project, gitignored

- **Purpose**: Multi-agent AI systems with CrewAI

- **Use Cases**:

  - Creating autonomous AI agents

  - Orchestrating agent crews

  - Defining tasks (sequential/hierarchical processes)

  - Implementing workflows with Flows

  - Integrating tools, memory, and deployment patterns

  

#### 4. **notion**

- **Type**: Project, gitignored

- **Purpose**: Notion MCP server guide

- **Use Cases**:

  - Managing Notion pages, databases, comments

  - Searching across Notion workspaces

  - Both official and open-source implementations

  

#### 5. **ref-tools**

- **Type**: Project, gitignored

- **Purpose**: Token-efficient MCP server for technical documentation

- **Use Cases**:

  - Working with external libraries, APIs, frameworks

  - Code generation with current documentation

  - Debugging and API integration

  - Supports public docs, private GitHub repos, PDFs

  

#### 6. **supabase**

- **Type**: Project, gitignored

- **Purpose**: Supabase development platform guide

- **Use Cases**:

  - Auth, Database, Storage, Realtime, Edge Functions

  - Database operations with RLS

  - Real-time subscriptions

  - Serverless functions deployment

  - Covers JS/TS, Python, Swift, Flutter, CLI

  

### Plugin Skills (claude-code-workflows)

  

#### Python Development

- `python-development:async-python-patterns` - Asyncio, concurrent programming

- `python-development:python-packaging` - Distributable packages, PyPI publishing

- `python-development:python-performance-optimization` - Profiling and optimization

- `python-development:python-testing-patterns` - pytest, TDD, mocking

- `python-development:uv-package-manager` - Fast dependency management

  

#### JavaScript/TypeScript

- `javascript-typescript:javascript-testing-patterns` - Jest, Vitest, Testing Library

- `javascript-typescript:modern-javascript-patterns` - ES6+, async/await, functional programming

- `javascript-typescript:nodejs-backend-patterns` - Express/Fastify, REST/GraphQL APIs

- `javascript-typescript:typescript-advanced-types` - Generics, conditional types, mapped types

  

#### Backend Development

- `backend-development:api-design-principles` - REST and GraphQL API design

- `backend-development:architecture-patterns` - Clean Architecture, Hexagonal, DDD

- `backend-development:microservices-patterns` - Service boundaries, event-driven communication

  

#### Kubernetes Operations

- `kubernetes-operations:gitops-workflow` - ArgoCD and Flux workflows

- `kubernetes-operations:helm-chart-scaffolding` - Helm charts for K8s apps

- `kubernetes-operations:k8s-manifest-generator` - Production-ready K8s manifests

  

#### Security Scanning

- `/security-scanning:security-sast` - Static Application Security Testing (SAST)

  

---

  

## Available Agents (via Task Tool)

  

### General Purpose

- **general-purpose** - Multi-step tasks, code search, research

  

### Documentation & Code Quality

- **code-documentation:code-reviewer** - AI-powered code analysis, security, performance

- **code-documentation:docs-architect** - Comprehensive technical documentation

- **code-documentation:tutorial-engineer** - Step-by-step tutorials and educational content

  

### Full-Stack Orchestration

- **full-stack-orchestration:deployment-engineer** - CI/CD, GitOps, deployment automation

- **full-stack-orchestration:performance-engineer** - Observability, optimization, scalability

- **full-stack-orchestration:security-auditor** - DevSecOps, cybersecurity, compliance

- **full-stack-orchestration:test-automator** - AI-powered test automation

  

### Frontend & Mobile

- **frontend-mobile-development:frontend-developer** - React components, Next.js, state management

- **frontend-mobile-development:mobile-developer** - React Native, Flutter, native apps

  

### Python Development

- **python-development:django-pro** - Django 5.x with async, DRF, Celery

- **python-development:fastapi-pro** - FastAPI, SQLAlchemy 2.0, async APIs

- **python-development:python-pro** - Python 3.12+, async, performance optimization

  

### JavaScript/TypeScript

- **javascript-typescript:javascript-pro** - Modern JavaScript, ES6+, async patterns

- **javascript-typescript:typescript-pro** - Advanced TypeScript, generics, type safety

  

### Backend Development

- **backend-development:backend-architect** - Scalable API design, microservices

- **backend-development:graphql-architect** - GraphQL federation, performance

- **backend-development:tdd-orchestrator** - TDD orchestration and governance

  

### Kubernetes & Cloud

- **kubernetes-operations:kubernetes-architect** - Cloud-native infrastructure, GitOps

- **cloud-infrastructure:cloud-architect** - AWS/Azure/GCP, IaC, FinOps

- **cloud-infrastructure:deployment-engineer** - CI/CD, GitOps

- **cloud-infrastructure:hybrid-cloud-architect** - Multi-cloud solutions

- **cloud-infrastructure:network-engineer** - Cloud networking, security

- **cloud-infrastructure:terraform-specialist** - Terraform/OpenTofu, IaC automation

  

### Incident Response & Debugging

- **incident-response:devops-troubleshooter** - Incident response, debugging

- **incident-response:incident-responder** - SRE incident management

  

### Code Review & Testing

- **code-review-ai:architect-review** - Architecture pattern reviews

- **debugging-toolkit:debugger** - Error and test failure debugging

- **debugging-toolkit:dx-optimizer** - Developer experience improvements

- **git-pr-workflows:code-reviewer** - Pull request code reviews

- **unit-testing:debugger** - Test failure debugging

- **unit-testing:test-automator** - Test automation

  

### Specialized

- **statusline-setup** - Configure Claude Code status line

- **output-style-setup** - Create Claude Code output styles

- **Explore** - Fast codebase exploration (quick/medium/very thorough)

- **Plan** - Fast codebase planning and exploration

  

---

  

## Pre-Approved Commands

  

Commands that don't require user approval:

  

```bash

# Python with venv

"C:\Users\user\Desktop\Coding\Accounting3\venv\Scripts\python" -c "..."

"venv\Scripts\python" -m uvicorn app.main:app --reload --port 8001

venv\Scripts\python.exe -m pip install:*

  

# File operations

rm:*

del nul

del SESSION_LOG.md

  

# PowerShell and CMD

powershell -Command:*

cmd.exe /c "dir /B"

cmd.exe /c "dir /S /B"

tree:*

  

# CrewAI installation

venvScriptspython -m pip install crewai crewai-tools

```

  

---

  

## Skills Usage

  

Skills are invoked using the `Skill` tool:

```

Skill(bmad-method)           # For project planning with BMAD methodology

Skill(context-engineering)   # For CLAUDE.md and PRP creation

Skill(crewai)               # For multi-agent AI systems

Skill(ref-tools)            # For accessing technical documentation

```

  

---

  

## Best Practices

  

### When to Use What

  

**MCP Servers:**

- Use `ref-tools` when working with external libraries/frameworks (FastAPI, SQLAlchemy, etc.)

- Use `Brave Search` for current information beyond knowledge cutoff

- Use `Notion` for project management and documentation

- Use `Obsidian` for personal knowledge management

  

**Agents:**

- Use `Explore` agent for codebase exploration (NOT direct Glob/Grep)

- Use `fastapi-pro` for FastAPI-specific tasks

- Use `python-pro` for general Python optimization

- Use `code-reviewer` for quality assurance after significant code changes

- Use `test-automator` for comprehensive testing strategies

  

**Skills:**

- Always run `ref-tools` skills for best practices of any tech spec

- Use `bmad-method` for structured project planning

- Use `context-engineering` for setting up AI development workflows

  

### Project-Specific Recommendations

  

For this **BMAD Accounting SaaS** project:

  

1. **Use ref-tools for:**

   - FastAPI best practices

   - SQLAlchemy 2.0 async patterns

   - Pydantic v2 validation

  

2. **Use agents:**

   - `fastapi-pro` for API development

   - `python-pro` for async optimization

   - `test-automator` for pytest integration tests

  

3. **Use skills:**

   - `python-development:async-python-patterns` for async/await patterns

   - `python-development:python-testing-patterns` for test coverage

   - `backend-development:api-design-principles` for REST API design

  

---

  

## Configuration Files

  

- **Global Instructions**: `C:\Users\user\.claude\CLAUDE.md`

- **Project Instructions**: `C:\Users\user\Desktop\Coding\Accounting3\CLAUDE.md`

- **This Document**: `C:\Users\user\Desktop\Coding\Accounting3\CLAUDE_SETUP.md`

  

**Note**: This file should be added to `.gitignore` per global instructions.

  

---

  

## Notes

  

- All MCP tools are accessible without requiring additional user approval

- Agents are launched via the `Task` tool with appropriate `subagent_type`

- Skills are executed via the `Skill` tool with skill name only

- This setup supports the full development lifecycle from planning → coding → testing → deployment