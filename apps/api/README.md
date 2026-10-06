# apps/api/

API HTTP con FastAPI. Hoy está vacía; la construyen las tareas `BE-*`.

- `main.py`: la aplicación (BE-001 en adelante).
- Contrato de la API: `docs/ARQUITECTURA.md`, sección *API*.

Arrancar (cuando exista), desde la raíz del repo:

```bash
uvicorn apps.api.main:app --reload     # http://localhost:8000/docs
```
