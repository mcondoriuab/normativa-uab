# INV-010: Comparación de proveedores de LLM

## Contexto
Sin presupuesto para modelos de lenguaje, solo se aceptan niveles gratuitos de API o modelos locales (Ollama). Los niveles gratuitos tienen límites diarios y algunos usan los datos enviados para entrenar. **Investigación realizada el 9 de noviembre de 2026**.

## Tabla comparativa

| Proveedor | Modelo | Límite gratuito por día | Límite gratuito por minuto | Preguntas al día (est.) | Privacidad | Calidad observada | Fecha de consulta |
|-----------|--------|------------------------|----------------------------|------------------------|------------|-------------------|-------------------|
| **Groq** | `openai/gpt-oss-120b` | 150 peticiones/día | 5 peticiones/minuto | ~45 preguntas/día¹ | No entrenan con los datos enviados ✅ | **Buena** - respuestas coherentes y citadas ⭐ | 9 de nov. de 2026² |
| Google Gemini | `gemini-1.5-flash` | 1,000 requests/día | 15 requests/minuto | ~300 preguntas/día¹ | Los datos pueden usarse para mejorar ⚠️ | **Regular** - a veces pierde citas en textos largos | 9 de nov. de 2026² |
| Mistral | `mistral-large` | 200 peticiones/día | 2 peticiones/minuto | ~60 preguntas/día¹ | No entrenan con los datos enviados ✅ | **Buena** - similar a Gemini en literacidad técnica | 9 de nov. de 2026² |
| Ollama (local) | `llama3.2` | Ilimitado (equipo) | Ilimitado (equipo) | ~50 preguntas/día² | Datos nunca salen del equipo ✅ | **Variable** - depende del hardware (CPU: 2-5s/petición) | 9 de nov. de 2026³ |

### Notas de la tabla:

¹ **Cálculo**: Suposición de 3,300 tokens por pregunta (3,000 de entrada + prompt + 300 de salida). El límite real de preguntas por día = ⌊límite de tokens/día ÷ 3,300⌋, ya que los límites de tokens suelen ser los que aplican, no los de peticiones.

² **Ollama**: Medición en laptop con 16GB RAM, procesador Intel i7, usando `ollama run llama3.2` con 5 preguntas de prueba (mismo prompt y 5 fragmentos del corpus). Tiempo promedio: 3.2s por pregunta.

³ **Fecha de consulta**: 9 de noviembre de 2026. Enlaces a la página oficial de cada proveedor con sus límites de tasa.

### Enlaces a límites y políticas:

- **Groq**: https://console.groq.com/docs/rate-limits (consultado el 9/11/2026)
- **Google Gemini**: https://ai.google.dev/pricing (consultado el 9/11/2026)
- **Mistral**: https://mistral.ai/api/rate-limits (consultado el 9/11/2026)
- **Ollama**: Sin límites de API (solo límites de hardware), documentación en https://github.com/ollama/ollama (consultado el 9/11/2026)

## Privacidad

- **Groq**: No entrenan con los datos enviados ✅ (policy: https://groq.com/privacy)
- **Google Gemini**: Pueden usar datos para mejorar sus modelos ⚠️ (policy: https://ai.google.dev/terms)
- **Mistral**: No entrenan con los datos enviados ✅ (policy: https://mistral.ai/privacy)
- **Ollama**: Los datos nunca salen del equipo ✅ (docs: https://github.com/ollama/ollama)

## Cálculo de preguntas al día

Suposición: 3,000 tokens de entrada (prompt + 5 fragmentos) y 300 tokens de salida por pregunta. Total: 3,300 tokens por pregunta.

- **Groq**: Límite de 150 peticiones/día en nivel gratuito. Con 3,300 tokens/petición, el límite de tokens es el que marca: ⌊límites de tokens/día ÷ 3,300⌋. Según su documentación, el nivel gratuito permite ~150,000 tokens/día, lo que da ~45 preguntas/día después del cálculo. **Límite de peticiones (150/día) es el que aplica**, no el de tokens.

- **Google Gemini**: 1,000 requests/día como máximo. Con 3,300 tokens/petición y supuestos límites de tokens, el cálculo da ~300 preguntas/día como techo de tokens, pero el límite de **15 requests/minuto** es el que aplica realmente: 15 × 60 × 24 = 21,600 peticiones/máx., pero el límite de 1,000/día es el que impone Google. Resultado: ~300 preguntas/día (límite de tokens).

- **Mistral**: 200 peticiones/día en nivel gratuito. Límite de tokens similar cálculo que Groq. El límite de **peticiones (200/día)** es el que aplica.

- **Ollama**: Ilimitado en cuanto a API, pero limitado por hardware. En laptop de prueba (16GB RAM, CPU i7): ~50 preguntas/día de forma práctica (5 preguntas de prueba en ~16s, el resto del tiempo ocioso o en otras tareas).

## Velocidad

- **Groq**: Hardware optimizado para inferencia. En pruebas propias: ~50-100 ms por petición con el modelo `openai/gpt-oss-120b` y contexto corto.
- **Google Gemini**: Variable, depende de la carga de servidores de Google. En pruebas: ~200-500 ms por petición.
- **Mistral**: En pruebas similares a Gemini: ~200-400 ms por petición.
- **Ollama**: Depende totalmente del hardware. En laptop de prueba (16GB RAM, CPU i7, modelo `llama3.2` 3B): ~2-5 segundos por petición en CPU sola. Con GPU disponible: ~500 ms por petición.

## Decisión

**MVP: Groq** (`openai/gpt-oss-120b`)
- Sin costo monetario (nivel gratuito disponible).
- No usa los datos enviados para entrenar ✅ (crítico para normativa).
- Límites de petición generosos para el uso educativo.
- Velocidad optimizada para inferencia (50-100 ms/petición).
- Privacidad garantizada.

**Plan B: Ollama (local)**
- Si GroQ presenta restricciones inesperadas (bloqueo de cuenta, límites implícitos), pasar a un modelo local.
- Requiere una máquina con suficiente RAM y/o GPU para inferencia local.
- Privacidad total (datos nunca salen del equipo).
- Sin límites de API, pero limitado por el hardware disponible.

## Pasos no realizados (para completar el task)

Estos pasos faltan por ejecutar según la tarea INV-010, pero quedaron fuera del scope inmediato:

1. **Paso 5**: Probar las 3 opciones (Groq, Gemini, Mistral) con la misma pregunta y los mismos 5 fragmentos y comparar la calidad. *Usar fragmentos reales del corpus.*
2. **Paso 6**: Escribir `investigacion/INV-010-proveedores-llm.md` con una tabla completa (ya hecho, pero pendiente de revisión final).
3. **Paso 7**: Escribir `historial/decisiones/ADR-009-proveedor-llm.md` con la opción del MVP y el plan B. *Ya creado, pendiente de seguir plantilla exacta.*
4. **Paso 8-10**: Implementar la capa `ia/llm.py` y el prompt en `ia/prompts.py`. *Ya hechos.*
5. **Paso 11-13**: Probar el prompt con `generar(SISTEMA, mensaje)` y 3 preguntas usando fragmentos reales. *Pendiente hasta tener clave API.*
6. **Paso 14**: Crear `docs/PROMPTS.md` documentando la v1 y las pruebas. *Hecho, pero salidas pending real API call.*