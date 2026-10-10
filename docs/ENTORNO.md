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

_Pendiente: la escribe la tarea SET-003._
