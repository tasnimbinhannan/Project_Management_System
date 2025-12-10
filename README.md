# Project Management System

A modular, object-oriented Project Management System intended as an OOP2 course project. This repository contains the source for managing projects, tasks, users, roles and reporting. The design emphasizes strong OOP principles (encapsulation, single-responsibility, separation of concerns) and is suitable for extension and testing.

## Table of Contents
- Overview
- Key Features
- Architecture & Design
- Getting Started
    - Prerequisites
    - Folder structure
    - Configuration
    - Build & Run
- Usage
    - Core concepts
    - Typical workflows
- Testing
- Contributing
- Coding Guidelines
- License
- Contact

## Overview
This system provides core project management capabilities:
- Create and manage projects and associated tasks
- Assign users and roles (e.g., Admin, Manager, Developer, Viewer)
- Task lifecycles and status tracking (To Do, In Progress, Done)
- Time estimates and simple reporting
- Persistent storage with a pluggable data layer
- Import/export for backup or integration

The implementation follows an object-oriented layered approach enabling unit testing, swapping persistence layers and adding UI or API adapters.

## Key Features
- Project CRUD (create, read, update, delete)
- Task CRUD with subtasks and dependencies
- User management and role-based access checks
- Task assignment, status transitions and history/audit
- Simple reporting (project progress, overdue tasks)
- Data import/export (JSON/CSV)
- Configuration-driven persistence (in-memory, file-based, or DB adapter)
- Unit tests and sample data seeds

## Architecture & Design
- Layers:
    - Presentation: CLI / API / UI adapters (kept thin)
    - Application/Service: Use cases and orchestration
    - Domain: Entities, value objects, domain services, validations
    - Persistence: Repository interfaces and concrete adapters
- Design principles:
    - SOLID principles
    - Clear separation of responsibilities
    - Dependency inversion (interfaces for repositories/services)
    - Basic patterns: Repository, Factory/Builder for DTOs, Observer for notifications (optional)
- Suggested UML: Entities include Project, Task, User, Role, Assignment, Timestamp/Audit

## Getting Started

### Prerequisites
- Development language runtime and toolchain (e.g., JDK/Node/.NET/Python) — choose per implementation
- Git
- Optional: Database (SQLite/Postgres/MySQL) if using DB adapter
- Build tool (Maven/Gradle/npm/dotnet/pipenv) as applicable

### Suggested Folder Structure
- /src
    - /domain
    - /services
    - /adapters
        - /persistence
        - /api (or /cli)
    - /config
- /tests
- /docs
- /data (seed files, sample exports)
- README.md

### Configuration
- Use a single config file (e.g., config.yaml / .env) for:
    - persistence adapter and connection settings
    - seed data toggle
    - logging level
- Provide default development config checked into repo and documentation for production overrides.

### Build & Run (generic)
1. Clone:
     git clone https://github.com/tasnimbinhannan/Project_Management_System.git
2. Install dependencies:
     - Java/Maven: mvn clean install
     - Node: npm install
     - .NET: dotnet restore
     - Python: pip install -r requirements.txt
3. Configure environment (copy sample config and edit):
     cp config.example.yaml config.yaml
4. Seed sample data (optional):
     ./scripts/seed-data
5. Run:
     - Java: mvn exec:java
     - Node: npm start
     - .NET: dotnet run
     - Python: python -m app

Replace commands according to actual implementation.

## Usage

Core concepts:
- Project: container for tasks and meta information
- Task: unit of work with status, assignee, estimate and logs
- User & Role: authentication/authorization model (for this project the example role model is sufficient)

Typical workflows:
- Create project -> add tasks -> assign users -> change task statuses -> generate project report
- Export project to JSON/CSV for backups or offline review

Example CLI/API endpoints should be documented in docs/ once implemented.

## Testing
- Unit tests live under /tests
- Run tests with chosen test runner:
    - Maven: mvn test
    - npm: npm test
    - dotnet: dotnet test
    - pytest: pytest
- Aim for high coverage in domain and service layers; use mocks for persistence adapters.

## Contributing
- Fork the repository and open feature branches (feature/<short-desc>)
- Follow coding guidelines and run tests locally
- Create clear pull requests with descriptions and related issue numbers
- Add unit tests for new features and update documentation

## Coding Guidelines
- Follow language idiomatic style and linter rules
- Keep methods small and single-responsibility
- Use interfaces/abstractions for external dependencies (IRepository, IService)
- Document public APIs and critical design decisions in docs/

## License
This project is provided under the MIT License. See LICENSE file for details.

Notes:
- Replace placeholder sections (build commands, runtime, maintainers) with details matching the chosen implementation language and environment.
- Add API documentation or UI usage guide in /docs when endpoints or user interfaces are implemented.