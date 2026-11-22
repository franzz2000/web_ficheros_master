# Página de descarga de ejercicios

Página web estática, compatible con GitHub Pages.

## Cómo preparar el material

1. Copia `datos.zip` a la raíz del proyecto, junto a `index.html`.
2. Copia los Excel de los alumnos a `hojas_ejercicios/`. Cada nombre debe cumplir `IDENTIFICADOR_NombreApellidos.xlsx`, por ejemplo `12345678Z_AnaEjemplo.xlsx` (identificador ficticio).
3. Genera el índice desde la raíz del proyecto:

   ```bash
   python3 scripts/generar_indice.py
   ```

4. Sube a GitHub **todos** los archivos, incluido `hojas_ejercicios/indice.json`.
5. En el repositorio, activa **Settings → Pages → Build and deployment → Deploy from a branch** y elige `main` y `/ (root)`.
6. Abre la dirección proporcionada por GitHub Pages. Si el repositorio se llama `ejercicios`, será normalmente `https://USUARIO.github.io/ejercicios/`.

Repite los pasos 2, 3 y 4 cada vez que incorpores, elimines o renombres un Excel.

## Cómo funciona

El navegador descarga el fichero público `indice.json`, compara el documento introducido con el prefijo del nombre del archivo (ignorando espacios, puntos, guiones y mayúsculas) y descarga el Excel correspondiente. Funciona con NIF, NIE y pasaportes sin realizar validaciones específicas del formato.

## Aviso importante sobre privacidad

**GitHub Pages es público**. Todos los archivos de `hojas_ejercicios/` y `indice.json` serán accesibles directamente, aunque la web muestre un formulario. Introducir el NIF/NIE/pasaporte **NO** autentica al alumno ni protege su archivo: el índice revela los nombres y los documentos incluidos en ellos. **No uses esta solución con NIF reales, nombres de alumnos u otros datos personales sin abordar antes las implicaciones de privacidad y protección de datos.** Para archivos privados se requiere un servicio con autenticación y comprobación de permisos en el servidor, o distribuirlos mediante otro canal seguro.

No hace falta instalar nada en GitHub Pages; Python solo se usa localmente para regenerar el índice.
