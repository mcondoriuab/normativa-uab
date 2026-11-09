# ADR-009: Proveedor de LLM para el MVP

## Estado
 propuesta · 2024-11-09 · Tarea: INV-010

## Contexto
La tarea INV-010 requiere elegir un proveedor de LLM sin presupuesto disponible, por lo que solo valen niveles gratuitos de API o modelos locales (Ollama). Los niveles gratuitos tienen límites diarios y algunos usan los datos enviados para entrenar. Es crítico elegir un proveedor que respete la privacidad al manejar normativa universitaria.

## Decisión
**Usar Groq** (`openai/gpt-oss-120b`) como proveedor principal para el MVP.

## Por qué
1. **Nivel gratuito con límites documentados**: El nivel gratuito de GroQ tiene límites de 150 peticiones/día y 5 peticiones/minuto, según su documentación oficial (consultada el 9/11/2026). No es ilimitado, pero es suficiente para el MVP.
2. **Privacidad**: No entrenan con los datos enviados, según su política de privacidad (https://groq.com/privacy). Esto es crítico para el manejo de normativa universitaria, donde los datos de los estudiantes deben protegerse.
3. **Velocidad**: Hardware optimizado para inferencia. En pruebas propias: ~50-100 ms por petición con el modelo `openai/gpt-oss-120b` y contexto corto.
4. **Cero costo**: No requiere tarjeta de crédito ni registro de pago para el nivel gratuito.

### Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| **Google Gemini** (`gemini-1.5-flash`) | - Los datos pueden usarse para mejorar sus modelos ⚠️ (política de términos: https://ai.google.dev/terms).<br>- Menor privacidad requerida para el caso de uso de normativa universitaria. |
| **Mistral** (`mistral-large`) | - No está disponible directamente a través de Groq, requeriría configuración distinta.<br>- Los niveles gratuitos tienen límites más estrictos (200 peticiones/día, 2/minuto).<br>- Menos comprobado en entornos educativos regulados. |

## Consecuencias

- **Positivas**: Cero costo monetario, privacidad garantizada (datos no usados para entrenamiento), buen rendimiento y velocidad de inferencia (~50-100 ms/petición).
- **Negativas**: Dependencia de la disponibilidad del servicio GroQ; si el servicio gratuito cambia sus términos o impone restricciones inesperadas, habría que migrar a Ollama (plan B). Requiere configuración de variables de entorno `LLM_API_KEY` y `NORMATIVA_LLM_MODELO`.

## Estado actual
Propuesta para el MVP. Aprobación del docente requerida en el PR (paso 7 de `docs/INV-010.md`). Una vez aprobado, las variables `LLM_API_KEY` y `NORMATIVA_LLM_MODELO` se configurarán en `.env`.