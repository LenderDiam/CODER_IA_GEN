# CODER-IA-GEN

A course project to get started with AI-assisted development. Simple full-stack application with persistent counter using FastAPI, React/Vite, and PostgreSQL.

## Table of Contents

- [Description](#-description)
- [Prerequisites](#️-prerequisites)
- [Installation & Launch](#-installation--launch)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [API Endpoints](#-api-endpoints)
- [Development](#️-development)
- [Learning Objectives](#-learning-objectives)
- [Developed with AI](#-developed-with-ai)

## Description

This project demonstrates a complete architecture with:
- **Backend**: REST API with FastAPI and PostgreSQL database
- **Frontend**: React interface with Vite
- **Database**: PostgreSQL for data persistence
- **Containerization**: Docker Compose to orchestrate all services

The application allows you to increment, view, and reset a counter stored in the database.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [Git](https://git-scm.com/) to clone the project

## Installation & Launch

1. **Clone the project**
   ```bash
   git clone https://github.com/LenderDiam/CODER_IA_GEN.git
   cd CODER_IA_GEN
   ```

2. **Launch the application with Docker Compose**
   ```bash
   docker compose up -d
   ```

3. **Access the services**
   - **React Frontend**: http://localhost:5173
   - **FastAPI API**: http://localhost:8000
   - **PostgreSQL Database**: localhost:5432

## Project Structure

```
CODER-IA-GEN/
├── docker-compose.yml          # Services orchestration
├── back-fastapi/              # FastAPI Backend
│   ├── app/
│   │   ├── main.py           # API entry points
│   │   ├── models/           # SQLAlchemy models
│   │   └── dockerfile        # Backend Docker image
│   └── pyproject.toml        # Python dependencies
└── coder-ia-gen/             # React/Vite Frontend
    ├── src/
    │   ├── App.tsx          # Main component
    │   └── ...
    ├── dockerfile           # Frontend Docker image
    └── package.json         # Node.js dependencies
```

## Features

-  **View counter**: Display current value
-  **Increment**: Increase value by 1
-  **Reset**: Set counter back to 0
-  **Persistence**: Data is saved in PostgreSQL database

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/count` | Get counter value |
| POST | `/count/increment` | Increment counter |
| POST | `/count/reset` | Reset counter to zero |

## Development

### Stop services
```bash
docker compose down
```

### Rebuild after changes
```bash
docker compose build
docker compose up -d
```

### View logs
```bash
docker compose logs
docker compose logs coder-ia-gen-api  # Backend logs
docker compose logs coder-ia-gen-frontend  # Frontend logs
```

### Access database
```bash
docker exec -it coder-ia-gen-postgres psql -U postgres
```
