# Sesión 2026-11-09: primer despliegue en Render

**Asistentes:** Miguel Ángel Condori (docente) · **Fase:** 1

## Qué se trabajó

- BE-006 hecha: <https://normativa-uab-ldxj.onrender.com/salud> responde
  `{"estado":"ok"}` y cada merge a `main` se despliega solo (PR #68, #69, #70).
- Como BE-001 no estaba fusionada, se desplegó un `apps/api/hola.py`
  provisional. BE-001 (#72) lo retiró el mismo día: cambió el `startCommand`
  de `render.yaml` a `apps.api.main:app` y borró `hola.py`.
- BE-008 depende también de BE-001, porque su Parte 2 modifica
  `apps/api/main.py`. La Parte 1 (esquema y `ia/db.py`) puede empezar ya.

## Qué funcionó

- Crear el servicio como Blueprint (`render.yaml`) desde el conector de Render:
  el primer build salió a la primera.

## Qué falló o costó

- El merge de #69 no redesplegó. El Blueprint se creó con la URL pública del
  repo y la app de GitHub de Render no estaba instalada, así que Render no se
  enteraba de los push. Se instaló la app solo para `normativa-uab` y el merge
  de #70 ya se desplegó solo (`docs/DESPLIEGUE.md` §4).
- Chrome tenía abierta la cuenta personal de GitHub, que no puede instalar apps
  en los repos de `mcondoriuab`: hubo que cambiar de cuenta.

## Decisiones

- Desplegar un hola mundo provisional para no esperar a BE-001 (BE-006).

## Para la próxima sesión

- [x] BE-001: crear `main.py`, cambiar `render.yaml` y borrar `hola.py` —
      responsable de BE-001 (hecho en #72)
- [ ] Decidir la región de Render: el servicio está en Oregón y Supabase en São
      Paulo; Virginia queda más cerca. Cambiarla obliga a recrear el servicio —
      docente
- [ ] BE-008 Parte 1, conector MCP de Supabase y claves de embeddings y LLM
      (pasos 4–6 de `docs/DESPLIEGUE.md`) — docente
