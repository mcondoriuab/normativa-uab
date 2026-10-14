# Preparar el entorno de trabajo

Todo el código Python del proyecto se ejecuta dentro de un **entorno virtual**
(`.venv`): una carpeta con su propio Python y sus propias librerías, separada
del resto de tu computadora. Así todos tenemos exactamente las mismas versiones
(las de `requirements.txt`) y no rompemos nada del sistema.

Necesitas:

- Python **3.11 o superior**
- git
- Una cuenta de GitHub con acceso al repositorio (cómo autenticarte: `docs/GIT.md`)

## macOS y Linux

Probado en macOS con Python 3.12. Los pasos de Linux (Ubuntu/Debian) **aún no
los ha probado nadie del equipo**: si los sigues, corrige esta sección con lo
que te pase.

### 1. Instalar Python y git

**macOS.** El `python3` que trae macOS suele ser antiguo (3.9). Comprueba:

```bash
python3 --version
git --version
```

Si sale 3.10 o menos, instala uno nuevo con [Homebrew](https://brew.sh):

```bash
brew install python@3.12 git
```

o descarga el instalador de [python.org](https://www.python.org/downloads/).
Cierra y vuelve a abrir la terminal, y repite `python3 --version`.

**Linux (Ubuntu/Debian), sin probar.**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git
python3 --version
```

Ubuntu 24.04 y Debian 12 traen 3.11 o superior. Ubuntu 22.04 trae 3.10, que **no
sirve**: pregunta en el grupo antes de seguir.

### 2. Clonar el repositorio

```bash
git clone https://github.com/mcondoriuab/normativa-uab.git
cd normativa-uab
```

Todos los comandos siguientes se ejecutan desde esta carpeta (la *raíz* del
repositorio).

### 3. Crear y activar el entorno virtual

```bash
python3 -m venv .venv          # crea la carpeta .venv (solo la primera vez)
source .venv/bin/activate      # activa el entorno (cada vez que abras una terminal)
```

Cuando está activo, la línea de la terminal empieza con `(.venv)`. Dentro del
entorno ya puedes escribir `python` en lugar de `python3`:

```bash
python --version               # debe decir 3.11 o superior
```

Para salir del entorno: `deactivate`.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Al principio `requirements.txt` está casi vacío y no instala nada: cada tarea
añade las librerías que necesita. Repite este comando cada vez que hagas
`git pull` y cambie `requirements.txt`.

Si aparece `[notice] A new release of pip is available`, no es un error; puedes
ignorarlo.

### 5. Crear tu `.env`

```bash
cp .env.ejemplo .env
```

`.env` guarda las claves (base de datos, APIs). Déjalo con los valores vacíos:
el docente te los pasará por un canal privado cuando una tarea los necesite.
**`.env` nunca se sube a git.**

### 6. Comprobar que todo está bien

```bash
git status
```

No deben aparecer ni `.venv/` ni `.env`: los ignora `.gitignore`. Si aparecen,
avisa antes de hacer commit.

### Problemas conocidos

| Síntoma | Causa | Solución |
|---|---|---|
| `python3 --version` dice 3.9 en macOS | Es el Python de Apple | Instalar Python con Homebrew o python.org (paso 1) |
| `pip: command not found` | El entorno no está activado | `source .venv/bin/activate` |
| `The virtual environment was not created successfully because ensurepip is not available` (Linux) | Falta el paquete `python3-venv` | `sudo apt install python3-venv` |
| La terminal ya no muestra `(.venv)` | Abriste una terminal nueva | Vuelve a activarlo; el entorno no se borra |

## Windows

Sigue estos pasos desde **PowerShell**. Los comandos se ejecutan desde la
carpeta raíz del repositorio, salvo donde se indique lo contrario.

### 1. Instalar Python y Git

1. Descarga Python 3.11 o superior desde [python.org](https://www.python.org/downloads/windows/).
   Durante la instalación, marca **Add python.exe to PATH**.
2. Instala [Git for Windows](https://git-scm.com/download/win).
3. Abre una ventana nueva de PowerShell y comprueba que ambos están disponibles:

   ```powershell
   python --version
   git --version
   ```

   La versión de Python debe ser 3.11 o superior. Si `python` no se reconoce,
   vuelve a ejecutar el instalador de Python con la opción para añadirlo a
   `PATH` y abre otra ventana de PowerShell.

### 2. Clonar el repositorio

Elige una carpeta donde guardar el proyecto y ejecuta allí:

```powershell
git clone https://github.com/mcondoriuab/normativa-uab.git
cd normativa-uab
```

### 3. Crear y activar el entorno virtual

Desde la raíz del repositorio, crea el entorno y actívalo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Cuando esté activo, el nombre `(.venv)` aparecerá al inicio de la línea de
PowerShell. Comprueba la versión que se está usando dentro del entorno:

```powershell
python --version
```

Debe mostrar Python 3.11 o superior. El entorno virtual instala las
dependencias del proyecto de forma aislada, sin modificar la instalación
global de Python.

Si PowerShell bloquea `Activate.ps1` por la política de ejecución, permite
scripts locales para tu usuario y vuelve a activar el entorno:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Confirma el cambio de política cuando PowerShell lo solicite. `CurrentUser`
limita el cambio a tu cuenta de Windows.

### 4. Instalar las dependencias

Con el entorno activo, instala las dependencias declaradas en
`requirements.txt`:

```powershell
pip install -r requirements.txt
```

Si el archivo solo contiene un comentario, no hay paquetes que instalar aún.
Cada tarea añadirá allí las dependencias que necesite.

### 5. Preparar las variables de entorno cuando se necesiten

Desde la raíz del repositorio, copia la plantilla:

```powershell
Copy-Item .env.ejemplo .env
```

Los valores de `.env` los proporcionará el docente cuando una tarea los
necesite. No inventes valores ni compartas el archivo: `.env` contiene
configuración local y está excluido de Git.

### 6. Comprobar el estado

Con el entorno activo, ejecuta:

```powershell
python --version
pip install -r requirements.txt
git status
```

La versión debe ser Python 3.11 o superior. `.venv/` y `.env` no deben aparecer
como archivos pendientes en `git status`; ambos están excluidos en
`.gitignore`.
