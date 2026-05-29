# Architecture Overview

## High-Level Architecture

```
Browser
   │
   ▼
Django URL Router (config/urls.py)
   │
   ├── /admin/  →  Django Admin Panel (built-in)
   │
   └── /*       →  clinic/urls.py
                      │
                      ▼
                   views.py  (page logic)
                      │
                      ├── reads/writes → models.py → SQLite DB
                      │
                      └── renders → templates/clinic/*.html → Browser
```

## Component Responsibilities

| Component | File | Responsibility |
|-----------|------|---------------|
| Models | `clinic/models.py` | Database table definitions and relationships |
| Views | `clinic/views.py` | Handle requests, query database, return responses |
| URLs | `clinic/urls.py` | Map URL paths to view functions |
| Forms | `clinic/forms.py` | Validate and process user input |
| Templates | `clinic/templates/` | HTML rendered and returned to browser |
| Admin | `clinic/admin.py` | Django admin panel configuration |
| Settings | `config/settings.py` | Project-wide configuration |

## Database Design

```
Owner (1) ──────────── (Many) Pet
                                │
                         (Many) Visit ──── (1) Vet
                                               │
PetType (1) ──── (Many) Pet       Specialty (Many-to-Many) Vet
```

### Tables

| Table | Key Fields |
|-------|-----------|
| Owner | first_name, last_name, address, city, telephone |
| PetType | name |
| Pet | name, birth_date, pet_type (FK), owner (FK) |
| Specialty | name |
| Vet | first_name, last_name, specialties (M2M) |
| Visit | visit_date, description, pet (FK), vet (FK) |

## Design Decisions

### Django MTV Pattern (Model-Template-View)
Django follows the MTV pattern (equivalent to MVC):
- **Model** — data layer (models.py)
- **Template** — presentation layer (HTML files)
- **View** — business logic layer (views.py)

This separation means each layer has one job and can be changed independently.

### SQLite for Development
SQLite requires zero setup — the database is a single file (`db.sqlite3`). For production, switching to PostgreSQL requires one change in `settings.py`.

### Django Admin as Management Interface
All create/edit/delete operations for Vets, Pet Types, and Specialties are handled through Django's built-in admin panel. This avoids building duplicate admin UI and is standard practice.

### Bootstrap 5 via CDN
No frontend build step required. Bootstrap is loaded from CDN, keeping the project simple and setup-free.

## Tradeoffs

| Decision | Benefit | Tradeoff |
|----------|---------|----------|
| SQLite | Zero setup, portable | Not suitable for concurrent production use |
| Django Admin for management | Free CRUD, fast to build | Less customizable UI |
| Bootstrap CDN | No build step | Requires internet to load styles |
| Django Templates | Simple, server-rendered | Less interactive than React/Vue |
| Monolithic app structure | Simple to understand | Less scalable than microservices |
