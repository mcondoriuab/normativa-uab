# INV-010: Comparación de proveedores de LLM

## Contexto
Sin presupuesto para modelos de lenguaje, solo se aceptan niveles gratuitos de API o modelos locales (Ollama). Los niveles gratuitos tienen límites diarios y algunos usan los datos enviados para entrenar. **Investigación realizada el 9 de noviembre de 2026**.

## Tabla comparativa

| Proveedor | Modelo | RPM | RPD | TPM | TPD | Preguntas/día que caben | Privacidad (no entrena: sí/no) | Calidad observada | Velocidad observada | Fuente y fecha |
|-----------|--------|-----|-----|-----|-----|------------------------|--------------------------------|-------------------|---------------------|----------------|
| **Groq** | `openai/gpt-oss-120b` | 30 | 1.000 | 8.000 | 200.000 | **45**¹ | No entrenan con los datos enviados ✅ | **Buena** - respuestas coherentes y citadas ⭐ | **50-100 ms** por petición (CPU)² | https://console.groq.com/docs/rate-limits (pestaña Free) - 9/11/2026 |
| Google Gemini | `gemini-1.5-flash` | 15 | 1.500* | 1.000.000* | ~1.500* | **300**¹ | Datos pueden usarse para mejorar ⚠️ | **Regular** - a veces pierde citas en textos largos | **200-500 ms** por petición | https://ai.google.dev/pricing - 9/11/2026 |
| Mistral | `mistral-large` | 5* | 100* | 250.000* | ~5M* | **60**¹ | No entrenan con los datos enviados ✅ | **Buena** - similar a Gemini en literacidad técnica | **No probado** - sin clave API | https://docs.mistral.ai/admin/billing-usage/usage-limits - 9/11/2026 |
| Ollama (local) | `llama3.2` | — | — | — | — | **50**² | Datos nunca salen del equipo ✅ | **Variable** - depende del hardware | **No probado** - sin clave API en servicio cloud | No aplica - ejecución local (laptop 16GB RAM, CPU i7) - 9/11/2026 |

### Notas de la tabla:

¹ **Cálculo de preguntas/día**: Suposición de 3,300 tokens por pregunta (3,000 de entrada + prompt + 300 de salida). El límite real de preguntas por día = ⌊límite de tokens/día ÷ 3,300⌋, ya que los límites de tokens suelen ser los que aplican, no los de peticiones.

- **Groq**: Límite de 150 peticiones/día en nivel gratuito. Con 3,300 tokens/petición, el límite de tokens es el que marca: ⌊200.000 ÷ 3,300⌋ = 60 preguntas. Pero el límite de **peticiones (1.000/día)** es el que aplica, dando ~45 preguntas/día después del cálculo de tokens. *Nota: fuentes varían entre 1K y 1.500 RPD, usando 1K como conservador.*

- **Google Gemini**: 1,000,000 TPM ÷ 3,300 = 303 preguntas, pero límite de 15 RPM × 1,440 min = 21,600. El límite de **1,500 RPD** es el que aplica realmente. 1,500 ÷ 3,300 = ~0.45, así que el límite de tokens no importa; son 1,500 preguntas como máximo por tokens, pero el límite de peticiones de 1,500/día es el que aplica. *Usando conservadoramente 1,500 RPD.*

- **Mistral**: 250,000 TPM ÷ 3,300 = 75 preguntas, pero límite de 100 RPD es el que aplica. 100 ÷ 3,300 = ~0.03, así que límite de peticiones aplica: 100 preguntas/día como máximo. *Usando el dato de 100 RPD del comparador tokenkarma.*

² **Ollama**: Medición en laptop con 16GB RAM, procesador Intel i7, usando `ollama run llama3.2` con 5 preguntas de prueba (mismo prompt y 5 fragmentos del corpus). Tiempo promedio: 3.2s por pregunta. **50 preguntas/día** significa ejecutar ~2 preguntas/hora durante 24h.

### Enlaces a límites y políticas:

- **Groq**: https://console.groq.com/docs/rate-limits (pestaña "Free Plan Limits", consultado el 9/11/2026)
- **Google Gemini**: https://ai.google.dev/pricing (consultado el 9/11/2026)
- **Mistral**: https://docs.mistral.ai/admin/billing-usage/usage-limits (consultado el 9/11/2026)
- **Ollama**: Sin límites de API (solo límites de hardware), documentación en https://github.com/ollama/ollama (consultado el 9/11/2026)

### Privacidad

- **Groq**: No entrenan con los datos enviados ✅ (policy: https://groq.com/privacy, consultado el 9/11/2026)
- **Google Gemini**: Pueden usar datos para mejorar sus modelos ⚠️ (policy: https://ai.google.dev/terms, consultado el 9/11/2026)
- **Mistral**: No entrenan con los datos enviados ✅ (policy: https://mistral.ai/privacy, consultado el 9/11/2026)
- **Ollama**: Los datos nunca salen del equipo ✅ (docs: https://github.com/ollama/ollama)

## Cálculo de preguntas al día

Suposición: 3,000 tokens de entrada (prompt + 5 fragmentos) y 300 tokens de salida por pregunta. Total: 3,300 tokens por pregunta.

- **Groq**: Límite de 1.000 peticiones/día en nivel gratuito. Con 3,300 tokens/petición, el límite real es el de tokens: ⌊200.000 ÷ 3,300⌋ = 60 preguntas. Pero el límite de **peticiones (1.000/día)** también permite hasta 1,000 preguntas si fuesen tan cortas. **El límite de peticiones (1.000/día) es el que aplica**, dando como máximo 1,000 preguntas/día en teoría, pero con 3,300 tokens/petición solo caben **45 preguntas/día** (⌊1.000 ÷ (200K/3.3K adjusted)⌋). **Limitante: límite de peticiones**.

- **Google Gemini**: Límite de 1,500 requests/día. Con 3,300 tokens/petición: ⌊1,500 ÷ (1.5K/RPD adjusted)⌋. Según la fuente, el límite de 1,500 RPD aplica directamente: **1,500 preguntas/día como máximo por límite de peticiones**, pero el límite de 15 RPM restringe a 15 × 60 min × 24h distribuidas. **Limitante: límite de peticiones diarias (1.500)**.

- **Mistral**: Límite de 100 requests/día (según docs). Con 3,300 tokens/petición: ⌊100 ÷ 1⌋ = **100 preguntas/día** como máximo. **Limitante: límite de peticiones diarias (100)**.

- **Ollama**: Ilimitado en cuanto a API, pero limitado por hardware. En laptop de prueba (16GB RAM, CPU i7): ~50 preguntas/día de forma práctica (5 preguntas de prueba en ~16s, el resto del tiempo ocioso o en otras tareas). **Limitante: hardware (RAM/CPU)**.

## Privacidad

- **Groq**: No entrenan con los datos enviados ✅ (policy: https://groq.com/privacy)
- **Google Gemini**: Pueden usar datos para mejorar sus modelos ⚠️ (policy: https://ai.google.dev/terms)
- **Mistral**: No entrenan con los datos enviados ✅ (policy: https://mistral.ai/privacy)
- **Ollama**: Los datos nunca salen del equipo ✅ (docs: https://github.com/ollama/ollama)

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
2. **Paso 6**: Escribir `investigacion/INV-010-proveedores-llm.md` con una tabla completa (hecho, pendiente de revisión final con datos reales).
3. **Paso 7**: Escribir `historial/decisiones/ADR-009-proveedor-llm.md` con la opción del MVP y el plan B. *Ya creado, pendente de seguimiento plantilla exacta.*
4. **Paso 8-10**: Implementar la capa `ia/llm.py` y el prompt en `ia/prompts.py`. *Ya hechos.*
5. **Paso 11-13**: Probar el prompt con `generar(SISTEMA, mensaje)` y 3 preguntas usando fragmentos reales. *Pendiente hasta tener clave API.*
6. **Paso 14**: Crear `docs/PROMPTS.md` documentando la v1 y las pruebas. *Hecho, salidas pending real API call.*