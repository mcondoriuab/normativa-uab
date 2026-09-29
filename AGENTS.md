# Instrucciones para asistentes de IA

Este archivo es para cualquier asistente de IA (Claude, Copilot, Cursor, ChatGPT…)
que ayude a un estudiante a resolver una tarea de este repositorio. Léelo
entero antes de escribir nada.

## Contexto que debes conocer

- Es un proyecto **formativo**. Lo construyen estudiantes con poca experiencia.
  Tan importante como que el código funcione es que el estudiante **entienda y
  pueda explicar cada línea**.
- El producto es un asistente RAG sobre la normativa universitaria. Lee
  `docs/ARQUITECTURA.md` antes de tocar código: ahí están los **contratos**
  (formatos de datos y de la API) que todas las piezas deben respetar.
- Idioma: español para código (nombres de variables y funciones), comentarios,
  documentación y mensajes de commit.

## Cómo trabajar una tarea

1. Lee el archivo de la tarea en `backlog/tareas/<ID>.md` completo.
2. Comprueba que sus dependencias (`depende_de`) están cerradas: en el issue de
   la tarea en GitHub, o preguntándole al estudiante si no tienes acceso. Si no
   lo están, avisa y no sigas.
3. Lee los archivos listados en **Entradas**. No asumas cómo son.
4. Crea o modifica **solo** los archivos listados en **Entregables**. Si crees
   que hace falta tocar otro archivo, dilo y pregunta antes.
5. Respeta **Fuera de alcance**. No añadas funcionalidades, validaciones,
   refactorizaciones ni dependencias que la tarea no pida.
6. Ejecuta los comandos de **Cómo verificar** y muestra el resultado real. Si
   algo falla, dilo; no lo maquilles.
7. Ayuda al estudiante a rellenar **Notas de cierre** con sus palabras: qué
   aprendió, qué falló y en qué se usó la IA.

## Estilo del código

- Python 3.11+. Funciones cortas, nombres descriptivos en español, sin clases
  si una función basta.
- Explícito antes que ingenioso: nada de comprensiones anidadas ni trucos que un
  principiante no pueda leer.
- Comentarios solo donde el *porqué* no sea obvio.
- Nuevas dependencias: solo si la tarea las nombra, y se añaden a
  `requirements.txt`.
- Frontend: HTML, CSS y JavaScript sin framework ni npm.
- Seguridad: nunca insertes texto del usuario o del modelo como HTML sin
  escapar (usa `textContent`). No subas claves de API; van en `.env`.

## Qué no hacer

- No escribas la solución de tareas futuras "para adelantar".
- No cambies los contratos de `docs/ARQUITECTURA.md` sin una decisión
  registrada en `historial/decisiones/`.
- No subas PDFs, datos generados (`data/`) ni claves.
- No hagas commit ni push por el estudiante sin que lo pida.
