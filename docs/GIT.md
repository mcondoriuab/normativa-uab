# Guía de git para el equipo

Los comandos exactos de nuestro flujo y cómo salir de los tres problemas más
frecuentes. El *porqué* del flujo está en `CONTRIBUTING.md`.

Ideas mínimas:

- **Repositorio:** la carpeta del proyecto con todo su historial. Hay una copia
  en GitHub (`origin`) y otra en tu computadora.
- **Commit:** una foto de los cambios, con un mensaje.
- **Rama:** una línea de trabajo separada. `main` es la versión buena; cada
  tarea se hace en su propia rama.
- **Pull request (PR):** la petición de llevar tu rama a `main`. Alguien la
  revisa antes de aceptarla.

## 1. Configuración inicial (una sola vez)

### Tu nombre y correo

Aparecen en cada commit. Usa tu correo institucional:

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "nombre.apellido@uab.edu.bo"
git config --global init.defaultBranch main
```

Compruébalo con `git config --global --list`.

### Autenticarte en GitHub (HTTPS con el navegador)

GitHub ya no acepta tu contraseña en la terminal. Usamos el inicio de sesión por
navegador:

- **Windows:** Git for Windows trae *Git Credential Manager*. La primera vez que
  hagas `git push`, se abre el navegador para que inicies sesión en GitHub.
  Después ya no lo vuelve a pedir.
- **macOS y Linux:** instala [GitHub CLI](https://cli.github.com) (`brew install
  gh` en macOS) y ejecuta:

  ```bash
  gh auth login
  ```

  Responde: `GitHub.com` → `HTTPS` → *Authenticate Git with your GitHub
  credentials?* `Yes` → `Login with a web browser`. Copia el código que te
  muestra y pégalo en la página que se abre.

Comprueba con `gh auth status` (macOS/Linux) o simplemente haciendo tu primer
`git push`.

> **Alternativa: SSH.** Si ya usas claves SSH, también sirve: crea una clave con
> `ssh-keygen -t ed25519 -C "tu-correo"`, súbela en GitHub → *Settings* → *SSH
> and GPG keys*, y clona con la URL `git@github.com:mcondoriuab/normativa-uab.git`.
> Si no sabes qué es, usa HTTPS.

### Clonar el repositorio

```bash
git clone https://github.com/mcondoriuab/normativa-uab.git
cd normativa-uab
```

## 2. El flujo de una tarea

Ejemplo con la tarea SET-004 (issue #4). Cambia el ID y la descripción por los
de tu tarea.

```bash
# 1. Actualiza main antes de empezar
git switch main
git pull

# 2. Crea tu rama: ID de la tarea + dos o tres palabras
git switch -c SET-004-guia-git

# 3. Trabaja en los archivos de la tarea. Mira qué cambió:
git status
git diff

# 4. Guarda los cambios en un commit (el mensaje empieza por el ID)
git add docs/GIT.md
git commit -m "SET-004: guía de git para el equipo"

# 5. Sube la rama a GitHub (-u solo la primera vez)
git push -u origin SET-004-guia-git
```

El `push` muestra un enlace *Create a pull request*. Ábrelo (o entra al
repositorio en GitHub y pulsa *Compare & pull request*) y:

1. Título: `SET-004: guía de git para el equipo`.
2. En la descripción escribe `Closes #4` (el número del issue) y qué hiciste.
3. Mueve el issue a *En revisión* en el tablero.

Si después de abrir el PR haces más cambios, basta con `git add`, `git commit`
y `git push` en la misma rama: el PR se actualiza solo.

**Quién aprueba:** `main` está protegida. Nadie puede subir directo a ella, y
para mergear un PR hace falta la aprobación del docente. Pide también a un
compañero que lo revise y deje comentarios: revisar es parte del aprendizaje.

`git add` con `.` sube *todo* lo que cambió. Es más seguro nombrar los archivos
(`git add docs/GIT.md`) y mirar `git status` antes del commit.

## 3. Tres problemas frecuentes

Todos se probaron en un repositorio de práctica con dos personas simuladas.

### "Me olvidé de crear la rama y trabajé en `main`"

**a) Todavía no hiciste commit.** Crea la rama ahora: los cambios sin commit se
vienen contigo.

```bash
git switch -c IA-003-detectar-articulos
git status        # tus cambios siguen ahí, ahora en la rama nueva
```

**b) Ya hiciste commit en `main`** (`git status` dice `ahead 1`). Lleva el
commit a una rama nueva y deja `main` como estaba en GitHub:

```bash
git branch IA-003-detectar-articulos    # 1. la rama nueva guarda tu commit
git reset --hard origin/main            # 2. main vuelve a ser igual que GitHub
git switch IA-003-detectar-articulos    # 3. sigue trabajando en tu rama
git log --oneline -3                    # tu commit está aquí
```

⚠️ Haz el paso 1 **antes** que el 2: `reset --hard` borra de `main` todo lo que
no esté en GitHub.

Si intentas hacer `git push` a `main`, GitHub lo rechaza por la protección de
la rama. Usa la solución b) y sube tu rama.

### "Mi rama está desactualizada respecto a `main`"

Otros mergearon PRs mientras trabajabas. Trae lo nuevo de `main` a tu rama:

```bash
git switch main
git pull                                # actualiza tu main
git switch IA-003-detectar-articulos
git merge main                          # mezcla lo nuevo en tu rama
git push                                # actualiza tu PR
```

Si se abre un editor pidiendo el mensaje del merge, guarda y ciérralo tal cual
(en `vim`: escribe `:wq` y Enter). Si `git merge main` dice `CONFLICT`, sigue
con el problema siguiente.

### "Tengo un conflicto al hacer merge"

Pasa cuando tú y otra persona cambiaron **las mismas líneas** de un archivo.
git no sabe con cuál quedarse y te lo pregunta:

```
CONFLICT (content): Merge conflict in notas.md
Automatic merge failed; fix conflicts and then commit the result.
```

1. Mira qué archivos tienen conflicto: `git status` (aparecen como
   *both modified*).
2. Abre cada uno. Verás algo así:

   ```
   <<<<<<< HEAD
   linea 2 versión de Beto          ← lo tuyo (tu rama)
   =======
   linea 2 versión de Ana           ← lo que viene de main
   >>>>>>> main
   ```

3. Edita el archivo para que quede como **debe** quedar (lo tuyo, lo otro o una
   mezcla) y **borra las tres líneas de marcas** (`<<<<<<<`, `=======`,
   `>>>>>>>`). VS Code muestra botones (*Accept Current*, *Accept Incoming*,
   *Accept Both*) que hacen lo mismo.
4. Marca el conflicto como resuelto y termina el merge:

   ```bash
   git add notas.md
   git commit --no-edit
   git push
   ```

Si te lías y quieres volver a como estabas antes del merge:

```bash
git merge --abort
```

Si no sabes cuál de las dos versiones es la correcta, **pregunta** a quien
escribió la otra antes de borrar nada.

## 4. Lo que nunca hay que hacer

- **`git push --force` a `main`** (o a la rama de otra persona): reescribe el
  historial y borra el trabajo de los demás. `main` además lo bloquea.
- **Subir `.env`**: tiene claves privadas. Si lo subes por error, avisa al
  docente **enseguida**: hay que cambiar las claves, porque borrar el archivo
  no basta (queda en el historial).
- **Subir PDFs** de la normativa ni la carpeta `data/`: no se versionan (ver
  `.gitignore` y `docs/CORPUS.md`).
- **Hacer commit de `.venv/`**: se recrea con `requirements.txt`.
- **Mergear tu propio PR sin revisión**, o trabajar en la rama de otra persona
  sin avisarle.

## Chuleta

| Quiero… | Comando |
|---|---|
| Ver en qué rama estoy y qué cambió | `git status` |
| Ver los cambios línea a línea | `git diff` |
| Ver los últimos commits | `git log --oneline -5` |
| Actualizar main | `git switch main && git pull` |
| Crear una rama y cambiarme a ella | `git switch -c ID-descripcion` |
| Cambiar de rama | `git switch nombre-rama` |
| Descartar los cambios de un archivo (sin commit) | `git restore archivo` |
| Sacar un archivo del próximo commit | `git restore --staged archivo` |
