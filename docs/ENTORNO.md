## macOS y Linux

La guía para macOS y Linux corresponde a SET-001.

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
