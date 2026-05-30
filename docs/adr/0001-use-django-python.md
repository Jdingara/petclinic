# ADR-0001: Use Python + Django as the Technology Stack

**Date:** 2026-05-30
**Status:** Accepted

## Context

The boot camp challenge required building a Veterinary Clinic Management System inspired by Spring PetClinic. The challenge allowed any technology stack.

## Decision

Use Python 3.11 + Django 6.0 + SQLite for development.

## Reasons

- Django is "batteries included" — admin panel, ORM, authentication, and forms built-in
- Python is readable — AI-generated code is easy to review and validate
- SQLite requires zero configuration — suitable for development and demo
- Faster delivery compared to Java + Spring Boot for this scope and timeline

## Consequences

- Positive: Rapid development, clean structure, built-in security features
- Positive: Any developer can clone and run in under 2 minutes
- Trade-off: SQLite not suitable for high-concurrency production use (switch to PostgreSQL for production)
