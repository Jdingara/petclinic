# AI Usage Notes

## Tool Used
Claude (Anthropic) — via Claude Code CLI

## How AI Was Used

### Requirements Interpretation
AI helped break down the functional requirements (FR-001 to FR-006) into concrete database models, views, and URL patterns. The requirements were mapped directly to Django components.

### Architecture Design
AI recommended the Python + Django + SQLite stack based on:
- Project scope (learning + boot camp demo)
- Speed of development required (one day)
- Readability and maintainability criteria from NFR-001

### Code Generation
AI generated all core application code including:
- `models.py` — 6 database models with correct relationships
- `views.py` — all view functions with search and CRUD logic
- `forms.py` — form classes with Bootstrap-compatible widgets
- `admin.py` — admin registration with inline editing
- `urls.py` — all URL patterns
- All 7 HTML templates with Bootstrap 5 styling
- `tests.py` — 17 unit and integration tests

### Documentation
AI generated README, ARCHITECTURE, API, and this AI_USAGE document.

## Where AI Accelerated Development

- **Boilerplate elimination** — models, forms, admin configuration written in seconds
- **Test generation** — 17 tests covering models and views generated automatically
- **Template consistency** — all 7 templates follow the same base layout without manual repetition
- **Debug resolution** — import errors and migration conflicts resolved immediately

## Where Manual Intervention Was Required

- **Tool approval** — every file write and command required human approval
- **Project direction** — decision to use Django over Java/Spring Boot was a human decision
- **Data entry** — sample data (owners, pets, vets, visits) was added manually through the admin panel
- **Requirements understanding** — understanding what the challenge actually required vs. what was optional was a human judgment call

## Lessons Learned

1. AI is highly effective at generating structured, repetitive code (models, forms, templates) that follows clear patterns
2. Human judgment is still required for architectural decisions and scope prioritization
3. AI-generated code requires validation — running tests and checking the browser confirmed correctness
4. The combination of AI speed + human review produced a working application in under 2 hours
5. Understanding WHY the code works (not just that it works) requires human engagement — AI explains but the engineer must understand
