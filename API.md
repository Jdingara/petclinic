# API Documentation

## Base URL

```
http://127.0.0.1:8000
```

## Authentication

Owner, Pet, and Visit endpoints require staff login. Unauthenticated requests are redirected to `/admin/login/`.

- 🔓 **Public** — accessible without login
- 🔒 **Protected** — requires staff login

---

## Endpoints

### Home

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/` | 🔓 Public | Home page — auto-logs out any active session |

---

### Owners

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/owners/` | 🔒 Protected | List all owners |
| GET | `/owners/?q=<name>` | 🔒 Protected | Search owners by first or last name |
| GET | `/owners/new/` | 🔒 Protected | Add new owner form |
| POST | `/owners/new/` | 🔒 Protected | Create new owner |
| GET | `/owners/<id>/` | 🔒 Protected | View owner detail + pets + visit history |
| GET | `/owners/<id>/edit/` | 🔒 Protected | Edit owner form |
| POST | `/owners/<id>/edit/` | 🔒 Protected | Update owner details |

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

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/owners/<owner_id>/pets/new/` | 🔒 Protected | Add pet form for owner |
| POST | `/owners/<owner_id>/pets/new/` | 🔒 Protected | Register new pet for owner |

**Pet fields:**

| Field | Type | Required |
|-------|------|----------|
| name | string (max 50) | Yes |
| birth_date | date (YYYY-MM-DD) | Yes |
| pet_type | integer (PetType ID) | Yes |

---

### Visits

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/pets/<pet_id>/visits/new/` | 🔒 Protected | Add visit form for pet |
| POST | `/pets/<pet_id>/visits/new/` | 🔒 Protected | Record new visit for pet |

**Visit fields:**

| Field | Type | Required |
|-------|------|----------|
| visit_date | date (YYYY-MM-DD) | Yes |
| vet | integer (Vet ID) | Yes |
| description | text | Yes |

---

### Veterinarians

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/vets/` | 🔓 Public | List all veterinarians with specialties |

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
