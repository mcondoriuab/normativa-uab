# INV-013: RAG a mano: con y sin los artículos

**Autor(es):** Sandra Condori · **Fecha:** 2026-11-12

## Pregunta

¿Responde mejor un chatbot sobre la normativa de la UAB si le pegamos los
artículos relevantes y le pedimos que responda solo con ellos (RAG a mano)?
¿Cita bien? ¿Qué hace cuando la respuesta no está?

## Lo que encontramos

Sin contexto, ChatGPT no sabía de qué universidad hablábamos: buscó en internet
y contestó con el reglamento de otra universidad (la Católica Boliviana de
Cochabamba). Ninguna de las 3 respuestas fue correcta para la UAB, y en P2 dijo
lo contrario de nuestro reglamento (que la beca **sí** cubre el verano). En la
pregunta sin respuesta (P4) tampoco dijo "no lo sé", sino que respondió con
seguridad sobre la otra universidad.

Cuando le dijimos que era la UAB pero sin darle el texto, ya no se inventó nada:
dijo que no podía confirmarlo y pidió el PDF.

Con los 5 artículos pegados acertó las 3 preguntas, citó el fragmento correcto
en las 3 y en P4 dijo "No lo encuentro en la normativa". Sin la frase de rechazo
respondió lo mismo en P4.

## Evidencia

### Montaje del experimento

- **Chatbot:** ChatGPT (chatgpt.com) sin iniciar sesión, versión gratuita; la
  web no muestra el modelo exacto · **Fecha de las pruebas:** 2026-11-12
- **Reglamento:** *Reglamento de Becas* de la Universidad Adventista de Bolivia
  (2016), público en <https://paginanueva.uab.edu.bo/reglamentos-uab/> (ver
  `docs/CORPUS.md`). Usamos los artículos 2, 3, 5, 25 y 26.
- Cada bloque se hizo en una **conversación nueva**, para que el chatbot no
  recuerde lo anterior, salvo la prueba extra y la repetición, que se indican
  donde aparecen. Sin iniciar sesión, ChatGPT no tiene memoria entre
  conversaciones.

### Las 4 preguntas

| # | Pregunta | Respuesta correcta según el reglamento |
|---|---|---|
| P1 | ¿Qué porcentaje de beca recibe el segundo mejor promedio de una facultad con la Beca a la Excelencia? | 50 % del costo de enseñanza del semestre (Art. 26.2) → fragmento [5] |
| P2 | ¿La beca cubre los cursos de verano? | No, los cursos de verano e invierno no están cubiertos (Art. 3.1) → fragmento [2] |
| P3 | ¿Puedo pasarle mi beca a otro estudiante? | No, las becas son intransferibles (Art. 5.2) → fragmento [3] |
| P4 | ¿Cuál es la fecha límite para presentar la solicitud de beca? | **No está** en estos artículos ni en el reglamento (el Art. 6.2 remite a la convocatoria). Debe decir "No lo encuentro en la normativa" |

### Mensaje exacto con los artículos

Se pega tal cual en una conversación nueva, con las 4 preguntas añadidas al
final del mismo mensaje (se envía todo de una vez).

```text
Te paso unos fragmentos del Reglamento de Becas (2016) de la Universidad Adventista de Bolivia (UAB).

[1] Artículo 2.- (Definición de Beca) Por Beca se entiende el beneficio de exención de pago por concepto de enseñanza que otorga la "UAB" en favor del estudiante nacional o extranjero solicitante. Esta exención puede ser total o parcial con una duración de una gestión académica y/o semestre según corresponda. Excepto la beca social que tiene la duración de toda la carrera.

[2] Artículo 3.- (Conceptos no cubiertos por la Beca) Los conceptos no cubiertos por la beca son: 1. Cursos de verano e invierno, 2. Exámenes de suficiencia, segundas instancias y apoyo-nivelación, 3. Cursos y actividades extracurriculares, 4. Aranceles por extensión de documentación académica, Habilitación, Titulación y Graduación, 5. Aranceles por formación complementaria y extracurricular (simposios, seminarios, talleres y otros), 6. Aranceles que deben ser pagados a instituciones externas por prácticas profesionales, 7. Aranceles por servicios de: residencias estudiantiles, alimenticias, atenciones médicas, seguro contra accidentes y riesgos.

[3] Artículo 5.- (Condiciones de otorgación de Becas) Las Becas otorgadas por la "UAB" están sujetas a las siguientes condiciones: 1. Son acumulables hasta un 25% del costo de enseñanza semestral, sumando a este porcentaje la beca asociado de manera independiente. Se exceptúa la beca excelencia académica que puede tener porcentajes mayores, 2. Son intransferibles, 3. Su asignación es revisada semestralmente juntamente con el aprovechamiento académico y situación disciplinaria del becario, 4. La solicitud de beca debe presentarse en forma personal, adjuntando la documentación necesaria y la justificación de su solicitud de beca, 5. Los alumnos becarios o candidatos a beca, deberán cursar como mínimo en el semestre el promedio semestral de créditos de su carrera, salvo los alumnos becarios de traspaso que seguirán el orden de las asignaturas convalidadas.

[4] Artículo 25.- (Del cupo de la Beca a la excelencia) Se asignará la beca a los tres (3) mejores promedios académicos de cada Facultad.

[5] Artículo 26.- (Del Porcentaje de la Beca) De acuerdo al promedio obtenido, la Beca se asigna de la siguiente manera: 1. El primer lugar, tiene el 75% de beca, del costo de enseñanza dentro de un periodo académico semestral, 2. El segundo lugar, tiene el 50% de beca, del costo de enseñanza dentro de un periodo académico semestral. 3. El tercer lugar, tiene el 25% de beca, del costo de enseñanza dentro de un periodo académico semestral.

Responde solo con los fragmentos. Cita [n] después de cada afirmación. Si la respuesta no está, di 'No lo encuentro en la normativa'.
```

Para la prueba **sin instrucción de rechazo** se usa el mismo mensaje, en otra
conversación nueva, quitando solo la última frase: *"Si la respuesta no está,
di 'No lo encuentro en la normativa'."*

### Respuestas sin contexto (literales)

Conversación nueva, solo la pregunta, sin artículos. El chatbot **buscó en la
web** (cita cba.ucb.edu.bo, lpz.ucb.edu.bo y Studocu) y supuso que estamos en
Cochabamba. Las 4 preguntas se hicieron seguidas en la misma conversación.

**P1.**

```text
El porcentaje depende del reglamento de la universidad que otorga la Beca a la Excelencia. No necesariamente el segundo mejor promedio recibe el mismo porcentaje que el primer lugar.

¿Te refieres a la Universidad Mayor de San Simón (UMSS) u otra universidad de Cochabamba?

Dime el nombre de la universidad y te confirmo qué porcentaje corresponde al segundo mejor promedio de la facultad.
```

**P2.**

```text
¡Sí, si te refieres a la Universidad Católica Boliviana (UCB), sede Cochabamba!

El reglamento establece que la Beca a la Excelencia Académica cubre el 80% de los derechos académicos, incluyendo los periodos de verano e invierno, con un límite de 35 créditos.

cba.ucb.edu.bo
+1

Puedes consultar el reglamento aquí: Becas UCB Cochabamba .

¿Es la UCB a la que te refieres?
```

**P3.**

```text
No. Según el Artículo 38 del Reglamento del Sistema de Becas de la Universidad Católica Boliviana (UCB), la Beca a la Excelencia Académica no se puede transferir voluntariamente a otro estudiante.

Sin embargo, hay una excepción importante:

Si tú ya tienes otra beca y esta te ofrece un mayor beneficio, se desactiva la Beca a la Excelencia.

En ese caso, la Beca a la Excelencia se activa para el estudiante que tenga el siguiente mayor puntaje académico.

Es decir, si renuncias al beneficio o este se desactiva, podría pasar al siguiente estudiante con mejor promedio, pero no puedes elegir libremente a quién dársela.

lpz.ucb.edu.bo
+1

Puedes confirmarlo con la oficina de Becas de la UCB Cochabamba: Programa de becas UCB Cochabamba .
```

**P4.**

```text
Si te refieres a la Universidad Católica Boliviana (UCB), sede Cochabamba, hay una distinción importante:

Beca a la Excelencia Académica: no necesitas presentar una solicitud. Se otorga automáticamente según los promedios del semestre anterior, después del procesamiento interno de calificaciones.

Otras becas: sí tienen fechas límite establecidas en cada convocatoria.

Studocu
+1

Por tanto, si buscas la Beca a la Excelencia, no tienes que preocuparte por una fecha límite de postulación.

Puedes consultar las convocatorias en la página oficial de Becas UCB Cochabamba .
```

### Prueba extra: sin artículos pero diciendo la universidad

No estaba en el plan, pero sirve. En la misma conversación de las respuestas sin
contexto, después de P4, se repitieron las 4 preguntas añadiendo "quiero saber
estas respuestas para la universidad adventista de bolivia". Respuesta literal:

```text
Para la Universidad Adventista de Bolivia (UAB), ubicada en Vinto, Cochabamba, hay que tomar como referencia su propio Reglamento de Becas, no el de la Universidad Católica Boliviana.

Encontré la página oficial de la UAB donde está publicado el Reglamento de Becas.

Universidad Adventista de Bolivia

Respuestas a tus cuatro preguntas
1. ¿Qué porcentaje recibe el segundo mejor promedio?

No pude verificar el porcentaje exacto en el reglamento de la UAB. Tampoco puedo asegurar que el segundo mejor promedio reciba automáticamente una beca.

2. ¿La beca cubre los cursos de verano?

No encontré una disposición oficial que confirme si cubre los cursos de verano. Es necesario verificarlo con el Departamento de Becas.

3. ¿Puedo transferir mi beca a otro estudiante?

No pude confirmar si el reglamento permite transferirla o si, al renunciar al beneficio, este pasa al siguiente estudiante con mejor promedio.

4. ¿Cuál es la fecha límite para solicitarla?

No encontré una fecha límite publicada que pueda confirmar. Es posible que dependa de la convocatoria de cada gestión académica.

Reglamento oficial de la UAB
09/02/2024 – Universidad Adventista de Bolivia

Universidad Adventista de Bolivia

Secretaría General – Reglamentos universitarios

Consultar Reglamento de Becas
Quiero ayudarte a conseguir las respuestas exactas. Si puedes descargar el Reglamento de Becas desde esa página y adjuntármelo aquí en PDF, puedo revisar los artículos correspondientes y responderte las cuatro preguntas con precisión, sin confundir las normas de la UAB con las de otras universidades.
```

En otra conversación nueva se enviaron las 4 preguntas con la frase "Si la
respuesta no está, di 'No lo encuentro en la normativa'", **pero sin pegar los
artículos**. Respuesta literal:

```text
Para responder correctamente necesito identificar la institución, porque existen distintas normativas de Beca a la Excelencia y los porcentajes y condiciones pueden variar.

¿De qué universidad o facultad es la normativa? Si tienes el PDF o puedes adjuntarlo, también puedes compartirlo.

Te responderé las cuatro preguntas basándome exclusivamente en ese documento. Cuando algún dato no figure en la normativa, indicaré exactamente:

«No lo encuentro en la normativa».
```

### Respuestas con contexto (literales)

Conversación nueva, mensaje exacto con los artículos y las 4 preguntas.
ChatGPT contestó las 4 en una sola respuesta:

```text
1. ¿Qué porcentaje de beca recibe el segundo mejor promedio?

Recibe un 50% de beca sobre el costo de enseñanza durante un periodo académico semestral. [5]

2. ¿La beca cubre los cursos de verano?

No. Los cursos de verano e invierno no están cubiertos por la beca. [2]

3. ¿Puedo pasarle mi beca a otro estudiante?

No. Las becas de la UAB son intransferibles. [3]

4. ¿Cuál es la fecha límite para presentar la solicitud de beca?

No lo encuentro en la normativa. El reglamento indica que la solicitud debe presentarse personalmente, adjuntando la documentación necesaria y la justificación correspondiente, pero no establece una fecha límite en los fragmentos proporcionados. [3]
```

**Repetición.** El mismo mensaje con artículos y frase de rechazo se pegó
también en la conversación del bloque anterior (las 4 preguntas sin artículos,
donde el chatbot había pedido el PDF). No es una conversación limpia, pero sirve
para ver si la respuesta es estable:

```text
1. ¿Qué porcentaje de beca recibe el segundo mejor promedio de una facultad con la Beca a la Excelencia?

Recibe el 50% de beca sobre el costo de enseñanza durante un periodo académico semestral. [5]

2. ¿La beca cubre los cursos de verano?

No. Los cursos de verano e invierno no están cubiertos por la beca. [2]

3. ¿Puedo pasarle mi beca a otro estudiante?

No. Las becas son intransferibles. [3]

4. ¿Cuál es la fecha límite para presentar la solicitud de beca?

No lo encuentro en la normativa.
```

Las dos dan los mismos datos y las mismas citas. La única diferencia es P4: la
primera añade lo que sí dice el fragmento [3] (presentación en persona) y la
repetición solo dice la frase de rechazo.

### Tabla comparativa

Sí / No / Parcial. "Cita correcta" solo aplica con contexto: el [n] que pone
debe ser el fragmento que de verdad dice eso. "Rechaza cuando debe" solo aplica
a P4.

| Pregunta | Sin contexto: correcta | Con contexto: correcta | Con contexto: cita correcta | Rechaza cuando debe |
|---|---|---|---|---|
| P1 | No: no da el dato y pregunta si es la UMSS | Sí: 50 % | Sí: [5] | — |
| P2 | No: dice que **sí** cubre el verano (habla de la UCB) | Sí: no cubre | Sí: [2] | — |
| P3 | No: dice "no", pero citando el Art. 38 de la UCB | Sí: intransferibles | Sí: [3] | — |
| P4 | — | — | Sí: [3] solo para lo de "en forma personal", que es cierto | Sin contexto: **No**, contesta sobre la UCB · Con contexto: **Sí** |

Sin contexto acierta 0 de 3 y no rechaza P4. Con contexto acierta 3 de 3, cita
bien las 3 y rechaza P4.

### Sin la instrucción de rechazo

Conversación nueva, mensaje sin la última frase y solo la pregunta P4.

**P4 sin instrucción de rechazo.**

```text
No lo encuentro en la normativa.
```

¿Qué cambió? Nada: tampoco se inventó una fecha. Con "Responde solo con los
fragmentos" le bastó para no inventar. Pero **ojo**: usó exactamente nuestra
frase "No lo encuentro en la normativa", que en este mensaje no aparece.
Comprobamos que fue una conversación nueva y sin sesión iniciada (sin memoria),
así que la coincidencia es curiosa pero no se explica por la conversación. Con
una sola prueba no podemos concluir que la instrucción de rechazo sobre.

### Verificación por otro integrante

Pendiente: la hará quien revise el pull request. Debe abrir ChatGPT en una
conversación nueva, pegar el mensaje exacto con las 4 preguntas y comparar su
respuesta a P1 con la nuestra (50 % [5]). El resultado se anotará en el PR.

### Uso de IA

Usamos un asistente de IA (Claude) para elegir los artículos del reglamento a
partir de `data/fragmentos.json` (salida de IA-002), redactar las preguntas y
preparar la plantilla de este informe. Comprobamos el texto de los 5 artículos
contra el PDF original (páginas 2 y 5): coincide palabra por palabra. También
buscamos en todo el PDF "plazo", "fecha" y "límite" para confirmar que P4 no
tiene respuesta: el reglamento solo remite a "los plazos ... establecidos en la
convocatoria respectiva" (Art. 6.2), sin dar ninguna fecha. Las respuestas del
chatbot las obtuvimos nosotros a mano y están copiadas sin editar. Claude también rellenó la tabla comparativa a
partir de esas respuestas; la revisamos comparándola con el reglamento.

## Conclusión para el proyecto

Esto es lo que **concluimos nosotros** a partir del experimento.

- **Pasarle los artículos cambia el resultado de 0 a 3 aciertos.** Es evidencia
  propia a favor de RAG para INV-002. El problema sin contexto no es solo que el
  modelo "no sepa": es que mezcla nuestra universidad con otras y lo dice con
  seguridad.
- **Hay que dejar la instrucción de rechazo en el prompt del sistema**
  (`docs/PROMPTS.md`). En esta prueba no hizo falta, pero fue una sola prueba
  y en el producto real la búsqueda traerá artículos que *parecen*
  relacionados sin serlo. Es más barato dejar la frase que arriesgarse.
- **Las citas fueron correctas, pero con 5 fragmentos es fácil.** En P4 citó [3]
  junto a "No lo encuentro", lo que podría confundir a un usuario. En IA-016
  conviene comprobar en código que cada [n] existe y decidir qué hacer con citas
  en respuestas rechazadas.

## Preguntas abiertas

- ¿Pasa lo mismo con 20 fragmentos en vez de 5, o con fragmentos que parecen
  relacionados pero no responden? Es lo que pasará con la búsqueda real.
- ¿Sin la frase de rechazo se inventaría algo si repetimos la prueba varias
  veces? ¿De dónde sacó nuestra frase exacta?
- ¿Da lo mismo con el modelo que usaremos en el producto (INV-010) que con
  ChatGPT web?
