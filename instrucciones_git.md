# Trabajando con Git y GitHub: Primeros pasos

En este documento se explican los pasos para trabajar con los proyectos de laboratorio, usando Git y GitHub. Debes tener instalado Git en tu ordenador, y haberte creado una cuenta en GitHub (suponemos que ya estás logueado antes de los pasos que se explican a continuación).

### 1. Crea tu propio repositorio a partir de la plantilla

Cada proyecto de laboratorio es una **plantilla** (*template*) que cada alumno debe usar para crear su propio repositorio personal. Sigue estos pasos:

1. Accede al repositorio de la plantilla en GitHub usando un navegador web.
2. Haz clic en el botón verde **"Use this template"** (puede aparecer también como **"Use template"**).
3. Selecciona **"Create a new repository"**.
4. Elige un nombre para tu repositorio (es recomendable que uses el mismo nombre del repositorio que estás copiando, por ejemplo `FP1-LAB01-Calculadora-de-viajes-espaciales`).
5. Pulsa **"Create repository from template"**.

Esto generará un nuevo repositorio en tu cuenta de GitHub, con el contenido de la plantilla.

---

### 2. Clona el repositorio en Visual Studio Code

Una vez creado tu repositorio personal, sigue estos pasos para clonarlo en tu ordenador:

1. Abre **Visual Studio Code**. Asegúrate de que no tienes abierta ninguna carpeta (o ciérrala, en su caso, mediante el menú **"Archivo"** -> **"Cerrar carpeta"**)
2. Haz clic en el **icono de Control de Código Fuente** en la barra lateral izquierda (el símbolo de ramas de Git).
3. Pulsa en el botón **"Clonar repositorio"**.
4. Cuando VS Code te pida la URL, ve a **tu nuevo repositorio** en GitHub:

   * Pulsa el botón verde **"Code"**.
   * Copia la URL que aparece bajo la opción **HTTPS**, que tendrá este aspecto:

     ```
     https://github.com/tuusuario/mi-proyecto-fundamentos.git
     ```
5. Vuelve a VS Code, **pega la URL**, y pulsa Enter.
6. Elige una carpeta de tu ordenador donde guardar el proyecto.
7. VS Code te preguntará si deseas abrir el proyecto recién clonado. Pulsa **"Abrir"**.

> 💡 Alternativamente, puedes usar `Ctrl+Shift+P` y buscar **Git: Clone** si no ves el botón directamente.

---

### 3. Configura tu nombre y correo en Git

Git necesita saber quién eres para registrar correctamente tus cambios. Esta configuración se hace solo una vez por entorno.

#### ✅ Si vas a trabajar en **tu propio ordenador** (configuración global):

Abre una terminal (menú **"Ver"** -> **"Terminal"**) y escribe:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@alum.us.es"
```

Esto guardará tu identidad para todos los repositorios que uses en ese equipo. Ya no tendrás que hacerlo para otros proyectos.

---

#### 🧪 Si estás usando un **ordenador del aula** (configuración local, solo para este repositorio):

Abre una terminal **dentro de la carpeta del repositorio clonado** (es la carpeta donde estarás si abres el terminal ahora) y escribe:

```bash
git config user.name "Tu Nombre"
git config user.email "tu.email@alum.us.es"
```

Esto asegura que tu identidad se aplique solo en este proyecto, sin afectar a otros. Deberás repetir el proceso para cada nuevo proyecto en el que trabajes.

---

Puedes comprobar la configuración activa con:

```bash
git config --list
```

Una vez hecho esto, ¡ya puedes empezar a trabajar en el proyecto! 🎉

---

### 4. Cómo registrar los cambios que hagas en el proyecto (commit) y subir esos cambios a GitHub

Una vez hayas avanzado en tu proyecto (por ejemplo, al final de la clase), sigue estos pasos para guardar y subir tus cambios al repositorio remoto en GitHub:

#### ✅ Desde la interfaz de Visual Studio Code:

1. Haz clic en el **icono de Control de Código Fuente** en la barra lateral izquierda.
2. Verás una lista de archivos modificados. Añade un **mensaje de commit** en la parte superior (por ejemplo: `Fin de la clase de laboratorio`).
3. Pulsa el botón con el **✓** (check) para hacer el commit. Si te pregunta si quieres seleccionar todos los archivos con cambios, contesta que **Sí**.
4. Luego pulsa el botón **"Sincronizar cambios"** (aparece en la parte inferior izquierda o justo encima de los archivos).
5. Si es la primera vez que usas GitHub desde VS Code, puede que te pida iniciar sesión. Acepta y sigue las instrucciones.

#### 💻 Alternativa: Desde la terminal

Si prefieres usar la terminal integrada, puedes ejecutar estos comandos desde la raíz del proyecto:

```bash
git add .
git commit -m "Primer commit"
git push origin main
```

---

Con esto habrás guardado tus cambios localmente y también los habrás subido a GitHub.
Ya puedes continuar trabajando en tu proyecto y haciendo commits regularmente. 

---

