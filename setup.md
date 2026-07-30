# Beeta Lab Development Setup

## Requirements

- Git
- Node.js 22 LTS
- Python 3.11.14
- uv
- VS Code

---

## Clone Repository

```bash
git clone <repository-url>
cd beeta-lab
```

---

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Backend

```bash
cd backend

uv venv --python 3.11.14

# Windows PowerShell
.venv\Scripts\Activate.ps1

uv sync

uv run uvicorn app.main:app --reload
```

---

## Frontend URL

http://localhost:3000

---

## Backend URL

http://localhost:8000

---

## API Documentation

http://localhost:8000/docs