# INV-010: Comparación de proveedores de LLM

## Contexto
Sin presupuesto para modelos de lenguaje, solo se aceptan niveles gratuitos de API o modelos locales (Ollama). Los niveles gratuitos tienen límites diarios y algunos usan los datos enviados para entrenar.

## Tabla comparativa

| Proveedor | Modelo | Límite gratuito por día | Límite gratuito por minuto | Preguntas al día (est.) | Privacidad | Calidad observada | Fecha de consulta |
|-----------|--------|------------------------|----------------------------|------------------------|------------|-------------------|-------------------|
| **Groq** | `openai/gpt-oss-120b` | Ilimitado (hasta la fecha) | Desconocido | ~100+ | No entrenan con los datos enviados | -- | [En web oficial](https://groq.com/) |
| Google Gemini | `gemini-1.5-flash` | 1,000 requests/día | 15 requests/minuto | ~20+ | Los datos pueden usarse para mejorar | -- | [En web oficial](https://ai.google/) |
| Mistral (via Groq o directo) | `mistral-large` | 1,000 requests/día | Desconocido | ~20+ | No entrenan con los datos enviados | -- | [En web oficial](https://mistral.ai/) |
| Ollama (local) | `llama3.2` | Ilimitado (equipo) | Ilimitado (equipo) | ~50+ (depende del hardware) | Datos nunca salen del equipo | -- | [En web oficial](https://ollama.ai/) |

## Cálculo de preguntas al día
Suposición: 3,000 tokens de entrada (prompt + 5 fragmentos) y 300 tokens de salida por pregunta.

- **Groq**: Sin límite público conocido, por lo que se estima suficiente para el MVP.
- **Google Gemini**: 1,000 requests/día / 1 pregunta = 1,000 preguntas/día como máximo, pero el límite por minuto (15) restringe a 14,400 si se distribuye. Con 3,000+300 = 3,300 tokens por petición, el límite real sería ~1,000 preguntas/día.
- **Mistral**: Similar a Gemini, 1,000 requests/día.
- **Ollama**: Limitado solo por la RAM y velocidad del procesador. En una máquina con 16GB de RAM, llama3.2 puede procesar ~50 preguntas/día de forma práctica.

## Privacidad
- **Groq**: No entrenan con los datos enviados ✅
- **Google Gemini**: Pueden usar datos para mejorar sus modelos ⚠️
- **Mistral**: No entrenan con los datos enviados ✅
- **Ollama**: Los datos nunca salen del equipo ✅

## Velocidad
- **Groq**: Hardware optimizado para inferencia, ~50-100 ms por petición con modelos pequeños.
- **Google Gemini**: Variable, depende de la carga de servidores.
- **Mistral**: Similar a Gemini.
- **Ollama**: Depende del hardware; en CPU única puede tardar 2-5 segundos por petición.

## Decisión
**MVP: Groq** (`openai/gpt-oss-120b`)
- Sin costo monetario (nivel gratuito).
- No usa los datos enviados para entrenar.
- Límites generosos o desconocidos.
- Velocidad optimizada para inferencia.

**Plan B: Ollama (local)**
- Si GroQ presenta restricciones inesperadas, pasar a un modelo local.
- Requiere una máquina con suficiente RAM (16GB+ para llama3.2).
- Privacidad total (datos nunca salen del equipo).
- Sin límites de API, pero limitado por el hardware disponible.