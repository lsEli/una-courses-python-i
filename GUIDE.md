# 1. Prerrequisitos recomendados

* Python 3.10+ correctamente instalado en tu sistema.
* `pip` actualizado:

  ```bash
  python -m pip install --upgrade pip
  ```
* Carpeta del proyecto con control de versiones (por ejemplo, Git).
* Añade `.venv/` a tu `.gitignore`.

# 2. Crear y gestionar el entorno virtual

Siempre que sea posible, usa una carpeta local llamada `.venv` en la raíz del proyecto.

## 2.1 Windows (PowerShell y CMD)

### Crear

```powershell
# PowerShell
python -m venv .venv
```

> Si PowerShell bloquea scripts de activación, puedes usar (solo para la sesión actual):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Activar

```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1
```

```bat
:: CMD
.\.venv\Scripts\activate.bat
```

### Desactivar

```powershell
deactivate
```

## 2.2 Linux y macOS (Bash/Zsh)

### Crear

```bash
python3 -m venv .venv
```

### Activar

```bash
source .venv/bin/activate
```

### Desactivar

```bash
deactivate
```

## 2.3 Comprobación rápida del entorno

Dentro del entorno activo:

```bash
which python      # Linux/macOS
where python      # Windows (CMD/PowerShell)
python -V
pip -V
```

Debes ver rutas que apunten a `.venv`.

# 3. Instalar dependencias en el entorno

Con el entorno ACTIVO:

```bash
pip install <paquete>            # instalación individual
pip install -r requirements.txt  # instalación masiva desde archivo
```

Buenas prácticas:

* Fijar versiones mínimas/compatibles para desarrollo inicial:

  ```text
  fastapi>=0.115,<0.116
  uvicorn>=0.30,<0.31
  ```
* Para despliegue, usa bloqueo exacto de versiones (ver §4).

# 4. Congelar dependencias (requirements)

Hay dos estrategias: “congelado directo” con `pip freeze` o bloqueo reproducible con herramientas de resolución (recomendado).

## 4.1 Congelado directo (rápido)

Con el entorno ACTIVO:

```bash
pip freeze > requirements.txt
```

Ventaja: simple.
Desventaja: incluye todo lo instalado (incluso paquetes que no usas) y no optimiza resoluciones.

## 4.2 Bloqueo reproducible (recomendado)

### Opción A: `pip-tools` (clásico y estable)

1. Crea `requirements.in` con tus dependencias de alto nivel:

```text
fastapi
uvicorn
```

2. Compila un “lockfile” exacto:

```bash
pip install pip-tools
pip-compile --generate-hashes -o requirements.txt requirements.in
```

3. Instala exactamente lo bloqueado:

```bash
pip-sync requirements.txt
```

* `pip-compile` resuelve versiones compatibles y añade hashes (seguridad).
* `pip-sync` instala solo lo que figura en `requirements.txt` y elimina lo demás, manteniendo el entorno limpio.

### Opción B: `uv` (muy rápido, de nueva generación)

```bash
# instalar uv (si no lo tienes)
pip install uv

# bloquear e instalar desde un archivo declarativo simple
uv pip compile -o requirements.txt requirements.in
uv pip sync requirements.txt
```

`uv` acelera instalaciones y sincronización y respeta el archivo de bloqueo.

# 5. Actualizar dependencias de forma controlada

Con `pip-tools`:

```bash
pip-compile --upgrade --generate-hashes -o requirements.txt requirements.in
pip-sync requirements.txt
```

Con `uv`:

```bash
uv pip compile --upgrade -o requirements.txt requirements.in
uv pip sync requirements.txt
```

# 6. Eliminar dependencias no utilizadas

## 6.1 Método recomendado (sincronización por lockfile)

Cuando utilices `pip-tools` o `uv`, cualquier paquete que NO esté en `requirements.txt` será desinstalado automáticamente al ejecutar:

```bash
pip-sync requirements.txt
# o
uv pip sync requirements.txt
```

Este es el enfoque más robusto, reproducible y “limpio”.

## 6.2 Auditorías útiles

* Ver árbol de dependencias:

  ```bash
  pip install pipdeptree
  pipdeptree
  ```
* Verificar integridad de instalaciones:

  ```bash
  pip check
  ```

## 6.3 Alternativa puntual (no recomendada como flujo principal)

* Desinstalar manualmente:

  ```bash
  pip uninstall <paquete>
  ```
* Herramientas auxiliares (bajo tu criterio): `pip-autoremove` o `pip-chill`. Son prácticas en casos puntuales, pero para equipos/proyectos es preferible basarse en `pip-compile`/`pip-sync` o `uv`.

# 7. Flujo de trabajo sugerido (equipo y CI/CD)

1. Crear entorno local por proyecto:

```bash
python -m venv .venv
# o python3 -m venv .venv en Linux/macOS
```

2. Activar entorno.
3. Declarar dependencias de alto nivel en `requirements.in`.
4. Compilar lockfile:

```bash
pip-compile --generate-hashes -o requirements.txt requirements.in
# o con uv:
uv pip compile -o requirements.txt requirements.in
```

5. Instalar y sincronizar:

```bash
pip-sync requirements.txt
# o
uv pip sync requirements.txt
```

6. Añadir `requirements.in` y `requirements.txt` al repositorio.
7. En CI/CD, construir entorno usando SOLO `requirements.txt` y `pip-sync` (o `uv pip sync`) para reproducibilidad y limpieza.
8. Para actualizar versiones, modifica `requirements.in` y recompila (`--upgrade`) el lockfile.

# 8. Consejos de calidad, seguridad y portabilidad

* Mantén `pip` actualizado y utiliza hashes en `requirements.txt` (`pip-compile --generate-hashes`).
* Evita privilegios elevados (`sudo`) al instalar librerías del proyecto; el entorno virtual aísla tus dependencias.
* Usa nombres de entorno coherentes: `.venv` en cada proyecto. Evita entornos globales.
* Para múltiples versiones de Python, considera `pyenv` (Linux/macOS) o instaladores oficiales en Windows; cada proyecto apunta a su propio intérprete.
* Documenta en el README cómo crear el entorno y sincronizar dependencias.
* En proyectos con `pyproject.toml`, puedes mantener una lista declarativa de dependencias y aun así generar `requirements.txt` para despliegue con `pip-compile`/`uv`.

# 9. Resumen operativo (chuleta)

| Acción                | Windows PowerShell                                                  | Windows CMD                    | Linux/macOS                 |
| --------------------- | ------------------------------------------------------------------- | ------------------------------ | --------------------------- |
| Crear venv            | `python -m venv .venv`                                              | `python -m venv .venv`         | `python3 -m venv .venv`     |
| Activar               | `.\.venv\Scripts\Activate.ps1`                                      | `.\.venv\Scripts\activate.bat` | `source .venv/bin/activate` |
| Desactivar            | `deactivate`                                                        | `deactivate`                   | `deactivate`                |
| Instalar una lib      | `pip install <pkg>`                                                 | `pip install <pkg>`            | `pip install <pkg>`         |
| Instalar desde lock   | `pip-sync requirements.txt`                                         | `pip-sync requirements.txt`    | `pip-sync requirements.txt` |
| Congelar rápido       | `pip freeze > requirements.txt`                                     | idem                           | idem                        |
| Bloquear reproducible | `pip-compile --generate-hashes -o requirements.txt requirements.in` | idem                           | idem                        |
| Sincronizar (limpia)  | `pip-sync requirements.txt`                                         | idem                           | idem                        |
