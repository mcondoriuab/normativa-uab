/* ========================================
   app.js – FE-003
   Envía la pregunta a la API, muestra la
   respuesta con citas desplegables y maneja
   los cuatro estados de la interfaz.
   ======================================== */

const formulario = document.getElementById("formulario");
const seccionRespuesta = document.getElementById("respuesta");
const campoPregunta = document.getElementById("pregunta");
const botonEnviar = formulario.querySelector("button[type='submit']");
const burbujaPregunta = document.getElementById("pregunta-enviada");

/* ---------- funciones de pintado ---------- */

function mostrarCargando() {
  seccionRespuesta.replaceChildren();

  const parrafo = document.createElement("p");
  parrafo.textContent = "Buscando…";
  seccionRespuesta.appendChild(parrafo);
}

function mostrarServidorDespertando() {
  seccionRespuesta.replaceChildren();

  const parrafo = document.createElement("p");
  parrafo.textContent = "El servidor está despertando, puede tardar hasta un minuto.";
  seccionRespuesta.appendChild(parrafo);
}

function mostrarRespuesta(datos) {
  seccionRespuesta.replaceChildren();

  if (datos.rechazada) {
    mostrarRechazo(datos.respuesta);
    return;
  }

  mostrarExito(datos.respuesta, datos.citas);
}

function mostrarRechazo(texto) {
  const contenedor = document.createElement("div");
  contenedor.className = "rechazo";

  const parrafo = document.createElement("p");
  parrafo.textContent = texto;
  contenedor.appendChild(parrafo);

  const sugerencia = document.createElement("p");
  sugerencia.textContent = "Te sugerimos consultar en secretaría de carrera.";
  contenedor.appendChild(sugerencia);

  seccionRespuesta.appendChild(contenedor);
}

function mostrarExito(textoRespuesta, citas) {
  const parrafo = document.createElement("p");
  parrafo.textContent = textoRespuesta;
  seccionRespuesta.appendChild(parrafo);

  if (citas.length === 0) {
    return;
  }

  const tituloCitas = document.createElement("h3");
  tituloCitas.textContent = "Citas";
  seccionRespuesta.appendChild(tituloCitas);

  const lista = document.createElement("ol");
  lista.className = "citas-lista";

  for (const cita of citas) {
    const elemento = document.createElement("li");

    const detalle = document.createElement("details");
    detalle.className = "cita-detalle";

    const resumen = document.createElement("summary");
    resumen.textContent = construirCabeceraCita(cita);
    detalle.appendChild(resumen);

    const textoCita = document.createElement("p");
    textoCita.className = "cita-texto";
    textoCita.textContent = cita.texto;
    detalle.appendChild(textoCita);

    elemento.appendChild(detalle);
    lista.appendChild(elemento);
  }

  seccionRespuesta.appendChild(lista);
}

function construirCabeceraCita(cita) {
  /* Formato: [n] documento · Art. X · pág. Y
     Si articulo es null, quita "· Art. X". */
  let cabecera = `[${cita.n}] ${cita.documento}`;

  if (cita.articulo !== null) {
    cabecera += ` · Art. ${cita.articulo}`;
  }

  cabecera += ` · pág. ${cita.pagina}`;
  return cabecera;
}

function mostrarError() {
  seccionRespuesta.replaceChildren();

  const contenedor = document.createElement("div");
  contenedor.className = "error";

  const parrafo = document.createElement("p");
  parrafo.textContent = "No se pudo obtener respuesta. Inténtalo de nuevo.";
  contenedor.appendChild(parrafo);

  seccionRespuesta.appendChild(contenedor);
}

/* ---------- envío a la API ---------- */

async function enviarPregunta(textoPregunta) {
  botonEnviar.disabled = true;
  botonEnviar.textContent = "Buscando…";
  mostrarCargando();

  /* Temporizador para aviso de servidor despertando */
  const temporizador = setTimeout(function () {
    mostrarServidorDespertando();
  }, 5000);

  try {
    const respuesta = await fetch("/preguntar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pregunta: textoPregunta }),
    });

    if (!respuesta.ok) {
      mostrarError();
      return;
    }

    const datos = await respuesta.json();
    mostrarRespuesta(datos);

  } catch {
    mostrarError();

  } finally {
    clearTimeout(temporizador);
    botonEnviar.disabled = false;
    botonEnviar.textContent = "Preguntar";
  }
}

/* ---------- evento del formulario ---------- */

formulario.addEventListener("submit", function (evento) {
  evento.preventDefault();

  const textoPregunta = campoPregunta.value.trim();
  if (textoPregunta === "") {
    return;
  }

  /* La pregunta se muestra como burbuja; textContent evita XSS */
  burbujaPregunta.textContent = textoPregunta;
  burbujaPregunta.hidden = false;

  enviarPregunta(textoPregunta);
});
