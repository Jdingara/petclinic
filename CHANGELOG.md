# Changelog

All notable changes to PetClinic are documented here.

## [1.0.0] - 2026-05-30

### Added
- Owner management: create, update, search, view owners (FR-001)
- Pet management: register pets, associate with owners, view history (FR-002)
- Configurable pet types: Dog, Cat, Bird, Hamster (FR-003)
- Veterinarian management with specialties (FR-004)
- Visit management: schedule, record notes, view history (FR-005)
- Owner search and navigation (FR-006)
- Django admin panel with custom branding
- 17 automated tests covering models and views
- README, ARCHITECTURE, API, and AI_USAGE documentation

### Security
- Login required for all owner, pet, and visit views
- Auto-logout when returning to home page
- Session expires on browser close and after 1 hour
- CSRF protection on all forms
