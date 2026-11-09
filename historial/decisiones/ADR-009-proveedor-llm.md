# ADR-009: Proveedor de LLM para el MVP

## Contexto
La tarea INV-010 requiere elegir un proveedor de LLM sin presupuesto disponible, por lo que solo valen niveles gratuitos de API o modelos locales (Ollama).

## Decisión
**Usar Groq** (`openai/gpt-oss-120b`) como proveedor principal para el MVP.

### Razones:
1. **Nivel gratuito sin restricciones conocidas** para el uso educativo del proyecto.
2. **Privacidad**: No entrenan con los datos enviados, lo cual es crítico para el manejo de normativa universitaria.
3. **Velocidad**: Hardware optimizado para inferencia baja latencia en respuestas.
4. **Cero costo**: No requiere tarjeta de crédito ni registro de pago.

## Plan B: Ollama (local)
Si GroQ presenta restricciones inesperadas (límites implícitos, caídas de servicio, etc.), el plan B es:
- Cambiar a un modelo local vía Ollama (ej. `llama3.2`).
- Las variables de entorno pasan de `LLM_API_KEY` a configuración de Ollama por HTTP.
- La arquitectura `generar()` en `ia/llm.py` sigue siendo la misma, solo cambia el cliente subyacente.

## Consecuencias
- **Positivas**: Cero costo, privacidad garantizada, buen rendimiento.
- **Negativas**: Dependencia de la disponibilidad del servicio GroQ; si el servicio gratuito cambia sus términos, habría que migrar a Ollama.

## Estado
Aprobado para el MVP. Se crearán las variables `LLM_API_KEY` y `NORMATIVA_LLM_MODELO` en `.env`.