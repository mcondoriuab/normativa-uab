# apps/web/

Interfaz web en HTML, CSS y JavaScript **sin framework ni npm**. Hoy está vacía;
la construyen las tareas `FE-*`.

| Archivo | Tarea |
|---|---|
| `index.html` | FE-001 |
| `estilos.css` | FE-002 |
| `app.js` | FE-003 en adelante |

Mientras no exista la API real, se trabaja contra el mock de BE-002, que sigue
el mismo contrato (`docs/ARQUITECTURA.md`). Cuando exista BE-005, la API sirve
esta carpeta en `http://localhost:8000/`.
