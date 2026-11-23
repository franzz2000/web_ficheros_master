
const formulario = document.querySelector('#buscar-form');
const campo = document.querySelector('#identificador');
const mensaje = document.querySelector('#mensaje');
const boton = document.querySelector('#buscar-boton');

function normalizar(valor) {
  return valor.trim().replace(/[\s.-]/g, '').toUpperCase();
}

function informar(texto, tipo = '') {
  mensaje.textContent = texto;
  mensaje.className = `message ${tipo}`;
}

formulario.addEventListener('submit', async (evento) => {
  evento.preventDefault();

  const documento = normalizar(campo.value);

  if (!documento) {
    informar('Introduce tu NIF, NIE o pasaporte.', 'error');
    campo.focus();
    return;
  }

  boton.disabled = true;
  informar('Buscando tu archivo…');

  try {
    const respuesta = await fetch(
      'hojas_ejercicios/indice.json',
      { cache: 'no-store' }
    );

    if (!respuesta.ok) {
      throw new Error('No se ha podido cargar el índice');
    }

    const archivos = await respuesta.json();

    const coincidencias = archivos.filter(nombre => {
      if (!nombre.toLowerCase().endsWith('.xlsx')) {
        return false;
      }

      // Eliminar extensión antes de comparar
      const identificador = nombre.replace(/\.xlsx$/i, '');

      return normalizar(identificador) === documento;
    });

    if (coincidencias.length === 0) {
      informar(
        'No se ha encontrado ningún ejercicio para ese identificador. Revisa los datos o consulta al profesor.',
        'error'
      );
    } else if (coincidencias.length > 1) {
      informar(
        'Hay varios archivos para este identificador. Consulta al profesor.',
        'error'
      );
    } else {
      const url = `hojas_ejercicios/${encodeURIComponent(coincidencias[0])}`;

      const enlace = document.createElement('a');
      enlace.href = url;
      enlace.download = coincidencias[0];

      document.body.append(enlace);
      enlace.click();
      enlace.remove();

      informar(
        'Se ha iniciado la descarga de tu hoja de ejercicios.',
        'success'
      );
    }
  } catch (error) {
    informar(
      'No se ha podido consultar el listado de ejercicios. Inténtalo de nuevo más tarde.',
      'error'
    );
    console.error(error);
  } finally {
    boton.disabled = false;
  }
});

