# Treddy - Módulo de Productos en Django

Desarrollo del módulo de productos aplicando estrictamente POO, SOLID, DRY, y adaptando los estilos estéticos de Tailwind a **Bootstrap Local**.

## Requisitos
* Django 6.x
* Python 3.10+
* Las dependencias están listadas en `requirements.txt`.

## Instalación
1. Clonar el repositorio.
2. `python -m venv venv`
3. `.\venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py runserver`

## Arquitectura y Modelo C4

### Nivel 1: Contexto (System Context)
El **Sistema Treddy** interactúa con tres tipos de usuarios:
- **Administrador:** Gestiona todo el inventario y usuarios.
- **Vendedor:** Sube y gestiona sus propios productos.
- **Cliente:** Visualiza catálogo y realiza compras.

### Nivel 2: Contenedores (Containers)
- **Web Application (Django):** Maneja el renderizado SSR con plantillas y provee API endpoints internos para la funcionalidad SPA.
- **Database (SQLite/PostgreSQL):** Almacena los perfiles de usuarios, el inventario de productos y el historial de auditoría.
- **Static File Server:** Sirve Bootstrap local y los archivos multimedia (imágenes de productos).

### Nivel 3: Componentes (Components)
Dentro de la Web Application (Django):
- **User Authentication Component (`usuarios/views.py`):** Login seguro, sanitización de regex, control de roles.
- **SPA Routing Component (`base.html` / fetch JS):** Controlador en cliente que intercepta los clics e inyecta fragmentos HTML.
- **Product Management Component (`productos/views.py`):** Lógica CRUD de productos aplicando el patrón *Template Method* implícito de las vistas.
- **Audit Logging Component (`HistorialProducto`):** Sistema de tipo *Observer* que registra cada cambio en la DB.

### Nivel 4: Código (Code)
Detallado en `diagrama_clases.puml` (disponible en la raíz del proyecto). 

## 4 Capas de Seguridad Implementadas
1. **Frontend (UI):** Atributos `pattern` de HTML5 en campos de entrada.
2. **Controlador/Formulario:** `ModelForm` con validación Regex estricta (`clean_username`, `clean_password`) en Django para evitar inyecciones.
3. **Vistas:** Decoradores `@login_required` y validación de estado de cuenta.
4. **Base de Datos:** Sanitización nativa del ORM de Django (Consultas parametrizadas).
