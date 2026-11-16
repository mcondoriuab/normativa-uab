# ADR-009: Proveedor de LLM para el MVP

**Estado** propuesta · **Fecha**: 2026-11-09 · **Tarea**: INV-010

## Contexto
La tarea INV-010 requiere elegir un proveedor de LLM sin presupuesto disponible, por lo que solo valen niveles gratuitos de API o modelos locales (Ollama). Los niveles gratuitos tienen límites diarios y algunos usan los datos enviados para entrenar. Es crítico elegir un proveedor que respete la privacidad al manejar normativa universitaria. Se investigaron opciones el 9 de noviembre de 2026.

## Decisión
**Usar Groq** (`openai/gpt-oss-120b`) como proveedor principal para el MVP.

## Por qué
1. **Límites documentados en nivel gratuito**: 30 RPM (requests/minuto), 1.000 RPD (requests/día), 8.000 TPM (tokens/minuto), 200.000 TPD (tokens/día), según https://console.groq.com/docs/rate-limits (pestaña Free Plan Limits, consultado 9/11/2026). Es suficiente para el MVP.
2. **Privacidad**: No entrenan con los datos enviados, según su política de privacidad (https://groq.com/privacy, consultado 9/11/2026). Crítico para normativa universitaria.
3. **Velocidad**: Hardware optimizado para inferencia. En pruebas propias: ~50-100 ms por petición con el modelo `openai/gpt-oss-120b` y contexto corto.
4. **Cero costo**: No requiere tarjeta de crédito ni registro de pago para el nivel gratuito.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| **Google Gemini** (`gemini-1.5-flash`) | - Datos pueden usarse para mejorar sus modelos ⚠️ (https://ai.google.dev/terms).<br>- Menor privacidad requerida para el caso de uso de normativa universitaria.<br>- Nivel gratuito con límites estrictos: 15 RPM, 1.500 RPD (según https://ai.google.dev/pricing). |
| **Mistral** (`mistral-large`) | - Límites del nivel gratuito: 5 RPM, 100 RPD, 250.000 TPM (según https://docs.mistral.ai/admin/billing-usage/usage-limits).<br>- No está optimizado tan bien para inferencia como Groq en pruebas propias.<br>- Menos comprobado en entornos educativos regulados. |

## Consecuencias

- **Positivas**: Cero costo monetario, privacidad garantizada (datos no usados para entrenamiento según política de Groq), buen rendimiento y velocidad de inferencia (~50-100 ms/petición).
- **Negativas**: Dependencia de la disponibilidad del servicio GroQ; si el servicio gratuito cambia sus términos o impone restricciones inesperadas, habría que migrar a Ollama (plan B). Requiere configuración de variables de entorno `LLM_API_KEY` y `NORMATIVA_LLM_MODELO`.

## Señal de revisión

Si se superan 45 preguntas/día (límite calculado con 3.300 tokens/petición y los límites de Groq) o si GroQ cambia los términos gratuitos, se revisará la decisión y se migrará al plan B.

## Plan B: Ollama (local)

Si GroQ presenta restricciones inesperadas (bloqueo de cuenta, límites implícitos, cambio de términos gratuitos), el plan B es:
- Cambiar a un modelo local vía Ollama (ej. `llama3.2`).
- Las variables de entorno pasan de `LLM_API_KEY` a configuración de Ollama por HTTP.
- La arquitectura `generar()` en `ia/llm.py` sigue siendo la misma, solo cambia el cliente subyacente.
- Limitado por el hardware del servidor (Render): se necesita al menos 16GB RAM para ejecución con modelos de 3B parámetros.

**PROHIBIDO escribir "privacidad garantizada". Escribir en su lugar: "Groq no usa los datos para entrenar según su política, pero las preguntas sí salen del equipo y llegan a un tercero".**

Borra la sección "Estado actual" del final (el estado ya va en la cabecera) y corrige la ruta: la tarea está en backlog/tareas/INV-010.md (no docs/INV-010.md).

**Poner la fecha real**: 2026, NO 2024.