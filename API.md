# API Documentation

## Base URL

```
http://127.0.0.1:8000
```

## Endpoints

### Home

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Home page |

---

### Owners

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/owners/` | List all owners |
| GET | `/owners/?q=<name>` | Search owners by first or last name |
| GET | `/owners/new/` | Add new owner form |
| POST | `/owners/new/` | Create new owner |
| GET | `/owners/<id>/` | View owner detail + pets + visit history |
| GET | `/owners/<id>/edit/` | Edit owner form |
| POST | `/owners/<id>/edit/` | Update owner details |

**Owner fields:**

| Field | Type | Required |
|-------|------|----------|
| first_name | string (max 50) | Yes |
| last_name | string (max 50) | Yes |
| address | string (max 200) | Yes |
| city | string (max 100) | Yes |
| telephone | string (max 20) | Yes |

---

### Pets

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/owners/<owner_id>/pets/new/` | Add pet form for owner |
| POST | `/owners/<owner_id>/pets/new/` | Register new pet for owner |

**Pet fields:**

| Field | Type | Required |
|-------|------|----------|
| name | string (max 50) | Yes |
| birth_date | date (YYYY-MM-DD) | Yes |
| pet_type | integer (PetType ID) | Yes |

---

### Visits

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/pets/<pet_id>/visits/new/` | Add visit form for pet |
| POST | `/pets/<pet_id>/visits/new/` | Record new visit for pet |

**Visit fields:**

| Field | Type | Required |
|-------|------|----------|
| visit_date | date (YYYY-MM-DD) | Yes |
| vet | integer (Vet ID) | Yes |
| description | text | Yes |

---

### Veterinarians

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/vets/` | List all veterinarians with specialties |

---

### Admin Panel

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/admin/` | Django admin — manage all data |

Full CRUD for all entities available through the admin panel.

---

## Search Example

```
GET /owners/?q=Smith
```

Returns a filtered list of owners where first name or last name contains "Smith".
