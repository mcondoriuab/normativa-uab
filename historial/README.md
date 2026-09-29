# historial/

La memoria del proyecto. Si alguien llega dentro de un año, aquí debe poder
reconstruir qué se hizo, por qué y qué salió mal.

| Carpeta | Qué va | Cuándo se escribe |
|---|---|---|
| `sesiones/` | Una entrada por sesión de trabajo del grupo | Al terminar cada sesión |
| `decisiones/` | ADRs: decisiones técnicas o de proyecto con su porqué | Cuando se decide algo que no es trivial revertir |
| `evaluaciones/` | Resultados de cada corrida de métricas | Cada vez que se ejecuta `eval/` |

Nombres de archivo:

- `sesiones/AAAA-MM-DD-tema.md`
- `decisiones/ADR-00N-tema.md` (numeración correlativa, nunca se reutiliza)
- `evaluaciones/AAAA-MM-DD-cambio-probado.md`

Regla: el historial **no se reescribe**. Si una decisión se revierte, se escribe
un ADR nuevo que la reemplaza y se marca el anterior como `reemplazada por ADR-00M`.
