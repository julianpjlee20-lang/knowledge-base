# Ready-to-Use Claude Code Prompts

**Purpose**: Practical prompts you can copy-paste into Claude Code
**Project**: BMAD Accounting SaaS

---

## 🚀 Quick Start: New Feature Development

### Copy-Paste This:
```
I want to build [FEATURE NAME] for the BMAD Accounting SaaS project.

Let's follow this workflow:

PHASE 1: REQUIREMENTS & DESIGN
1. Create a PRD in Notion with:
   - Problem statement
   - User stories
   - Acceptance criteria
   - Technical requirements
   
2. Research best practices using Brave Search

3. Read relevant skills:
   - Skill(bmad-method)
   - Skill(backend-development:architecture-patterns)
   
4. Design architecture:
   - Database schema
   - API endpoints
   - Use ref-tools to get latest FastAPI/SQLAlchemy docs
   - Create ADR in Notion

PHASE 2: BACKEND IMPLEMENTATION
1. Read Skill(python-development:async-python-patterns)

2. Get current docs via ref-tools:
   - FastAPI (dependency injection, async)
   - SQLAlchemy 2.0 (async ORM)
   - Pydantic v2 (validation)

3. Implement using appropriate tools and patterns

4. Create comprehensive pytest tests

5. Document in Obsidian

PHASE 3: FRONTEND IMPLEMENTATION
1. Read Skill(javascript-typescript:modern-javascript-patterns)

2. Get docs via ref-tools:
   - Next.js 14 (app router)
   - React (hooks, performance)
   - TypeScript (advanced types)

3. Implement UI components

4. Create tests (Vitest + Testing Library)

5. Document components in Obsidian

After each phase, pause and let me review before proceeding.
```

---

## 📝 Template 1: Backend API Endpoint

### Copy-Paste This:
```
Create a new API endpoint: [ENDPOINT DESCRIPTION]

Step 1: Get latest documentation
- Use ref-tools to resolve library IDs for FastAPI, SQLAlchemy, and Pydantic
- Get docs on async patterns, ORM relationships, and validation

Step 2: Read best practices
- Skill(python-development:async-python-patterns)
- Skill(backend-development:api-design-principles)

Step 3: Implementation
Create the following files:
- app/models/[resource].py (SQLAlchemy model)
- app/schemas/[resource].py (Pydantic schemas)
- app/services/[resource].py (business logic)
- app/api/v1/endpoints/[resource].py (FastAPI router)

Requirements:
- Async/await throughout
- Proper error handling
- JWT authentication
- Input validation
- Comprehensive docstrings

Step 4: Testing
Create tests/test_[resource]_api.py with:
- Happy path tests
- Error case tests
- Edge cases
- 80%+ coverage

Step 5: Documentation
Document in Obsidian:
- API examples
- Common patterns
- Gotchas learned
```

---

## 🎨 Template 2: Frontend Component

### Copy-Paste This:
```
Create a new UI component: [COMPONENT DESCRIPTION]

Step 1: Get documentation
- Use ref-tools for Next.js app router patterns
- Use ref-tools for React hooks and performance
- Use ref-tools for TypeScript advanced types

Step 2: Read patterns
- Skill(javascript-typescript:modern-javascript-patterns)
- Skill(javascript-typescript:typescript-advanced-types)

Step 3: Implementation
Create:
- components/[name]/[Component].tsx (main component)
- components/[name]/[Component].test.tsx (tests)
- components/[name]/types.ts (TypeScript types)

Requirements:
- TypeScript strict mode
- Proper prop types
- Loading/error states
- Responsive design
- Accessibility (WCAG 2.1)

Step 4: Testing
- Unit tests (Vitest)
- Integration tests if needed
- Accessibility tests

Step 5: Documentation
Document in Obsidian:
- Component API
- Usage examples
- Props documentation
```

---

## 🏗️ Template 3: Database Schema Change

### Copy-Paste This:
```
I need to modify the database schema: [CHANGE DESCRIPTION]

Step 1: Design Review
- Read Skill(backend-development:architecture-patterns)
- Design the schema changes
- Consider migration impact
- Create ADR in Notion

Step 2: Get Documentation
- Use ref-tools for SQLAlchemy 2.0 migrations
- Use ref-tools for Alembic best practices

Step 3: Implementation
1. Update SQLAlchemy models in app/models/
2. Create Alembic migration script
3. Update Pydantic schemas if needed
4. Update any affected endpoints

Step 4: Testing
- Test migration up and down
- Test with existing data
- Update affected tests

Step 5: Documentation
- Document migration in Obsidian
- Update architecture docs
- Note any breaking changes
```

---

## 🐛 Template 4: Bug Fix

### Copy-Paste This:
```
Fix this bug: [BUG DESCRIPTION]

Step 1: Investigation
- Review error logs
- Identify root cause
- Check related code

Step 2: Get Context
- If backend: Read Skill(python-development:async-python-patterns)
- If frontend: Read Skill(javascript-typescript:modern-javascript-patterns)
- Use ref-tools if library-specific issue

Step 3: Fix Implementation
- Write failing test first (TDD)
- Implement fix
- Ensure test passes
- Check for similar issues elsewhere

Step 4: Verification
- Run full test suite
- Manual testing if UI-related
- Check for regression

Step 5: Documentation
- Document in Obsidian:
  - Root cause
  - Solution
  - Prevention measures
```

---

## 🔍 Template 5: Code Review Request

### Copy-Paste This:
```
Review this code for quality, security, and best practices:

[PASTE CODE OR FILE PATH]

Check for:
- Security vulnerabilities (SQL injection, XSS, auth bypass)
- Performance issues (N+1 queries, memory leaks)
- Code quality (patterns, readability, maintainability)
- Best practices compliance
- Test coverage gaps

Use ref-tools to verify against current best practices for [TECHNOLOGY].

Provide specific recommendations with code examples.
```

---

## ⚡ Template 6: Performance Optimization

### Copy-Paste This:
```
Optimize performance for: [COMPONENT/ENDPOINT]

Step 1: Benchmark
- Identify bottlenecks
- Measure current performance
- Set target metrics

Step 2: Get Best Practices
- Read Skill(python-development:python-performance-optimization) (backend)
- Read Skill(javascript-typescript:modern-javascript-patterns) (frontend)
- Use ref-tools for specific library optimization guides

Step 3: Implement Optimizations
Backend options:
- Database query optimization
- Caching (Redis)
- Async patterns
- Connection pooling

Frontend options:
- React.memo / useMemo / useCallback
- Code splitting
- Lazy loading
- Image optimization

Step 4: Verify
- Re-run benchmarks
- Compare metrics
- Ensure no regressions

Step 5: Document
- Document optimizations in Obsidian
- Note trade-offs made
```

---

## 📚 Template 7: Learning a New Technology

### Copy-Paste This:
```
I want to learn how to use [TECHNOLOGY] in this project.

Step 1: Get Documentation
- Use ref-tools to resolve library ID
- Get comprehensive documentation
- Focus on: [SPECIFIC TOPICS]

Step 2: Read Relevant Skills
[List applicable skills from CLAUDE_SETUP.md]

Step 3: Create Example Implementation
- Build a simple example showing key concepts
- Include comments explaining each part
- Add to Obsidian as learning reference

Step 4: Apply to Real Feature
- Identify where to use it in the project
- Implement with best practices
- Document learnings
```

---

## 🔄 Template 8: Refactoring

### Copy-Paste This:
```
Refactor [FILE/MODULE] to improve [CODE QUALITY/PERFORMANCE/MAINTAINABILITY]

Step 1: Analysis
- Read current code
- Identify issues/smells
- Define refactoring goals

Step 2: Get Best Practices
- Read relevant Skills for the technology
- Use ref-tools for current patterns
- Review architecture patterns if structural change

Step 3: Plan Refactoring
- Break into small steps
- Ensure tests exist first
- Plan for zero downtime

Step 4: Execute
- Refactor incrementally
- Run tests after each change
- Keep commits atomic

Step 5: Verify
- All tests pass
- Performance not degraded
- No new bugs introduced

Step 6: Document
- Update code comments
- Update architecture docs if needed
- Document in Obsidian: what changed and why
```

---

## 🎯 Daily Development Workflow

### Morning Standup Prompt:
```
Good morning! Let's plan today's work:

1. Check Notion for today's tasks
2. Review any blockers from yesterday (check Obsidian notes)
3. Prioritize tasks
4. For each task, identify:
   - Which skills to read first
   - What documentation to fetch via ref-tools
   - Estimated time

Let's start with the highest priority item.
```

### End of Day Prompt:
```
Let's wrap up today's work:

1. What did we complete today?
2. Any blockers for tomorrow?
3. Update Notion with task status
4. Document learnings in Obsidian:
   - What worked well
   - What to improve
   - Technical discoveries
   - Code patterns to reuse

Save everything before closing.
```

---

## 💡 Pro Tips

### When to Use Each Tool:

**ref-tools (ALWAYS USE FIRST)**
```
Before implementing ANYTHING:
1. resolve-library-id for the library
2. get-library-docs with specific topic
3. This gives you current, accurate documentation
```

**Skills (READ BEFORE CODING)**
```
Skills provide methodology and patterns:
- Read BEFORE asking Claude to implement
- Use for learning best practices
- Reference when stuck
```

**Notion (OFFICIAL RECORDS)**
```
Use for:
- PRDs and roadmaps
- Architecture Decision Records (ADRs)
- Sprint planning
- Team-facing documentation
```

**Obsidian (PERSONAL NOTES)**
```
Use for:
- Quick notes and scratchpad
- Code snippets
- Learning notes
- Personal reminders
- Technical discoveries
```

**Brave Search (CURRENT INFO)**
```
Use for:
- Market research
- Competitor analysis
- Recent news/updates
- "How do others solve this?"
```

---

## ⚠️ Common Mistakes to Avoid

1. **Don't skip ref-tools**: Always get current docs first
2. **Don't skip Skills**: Read methodology before implementing
3. **Don't implement everything at once**: Break into phases
4. **Don't forget tests**: Write tests as you go
5. **Don't skip documentation**: Future you will thank present you
6. **Don't ignore errors**: Fix them immediately, don't accumulate
7. **Don't forget to commit**: Commit working code frequently

---

## 🚦 Quick Decision Guide

**"Should I use ref-tools?"**
→ If you're about to write code using a library: YES

**"Should I read a Skill?"**
→ If you're implementing a pattern/architecture: YES

**"Should I document in Notion or Obsidian?"**
→ Notion: Official, team-facing
→ Obsidian: Personal, quick notes

**"Should I break this into phases?"**
→ If it takes more than 2 hours: YES

**"Should I write tests?"**
→ Always: YES

---

**Tags**: #ready-to-use #templates #workflow #daily-use
