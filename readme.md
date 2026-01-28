# Bitácora de Viajes: Recorriendo la Patagonia 🏔️🐍

Proyecto final para el curso de Python en Coderhouse. Una aplicación web estilo blog para amantes de la naturaleza y los viajes.

## Estudiante
* **Sofía Hernandez** 

## Video Demostrativo
[PARA VER EL VIDEO DE LA PRESENTACIÓN DEL PROYECTO](https://youtu.be/InKrw9GjwGQ)

## Funcionalidades principales:
- **Blog Dinámico:** Listado y detalle de destinos con ficha técnica de dificultad, transporte y servicios.
- **CRUD Completo:** El administrador puede crear, editar y borrar actividades desde la propia interfaz.
- **Perfiles:** Registro de usuarios con edición de biografía, links sociales y foto de perfil.
- **Mensajería:** Sistema de comunicación interna para consultas entre viajeros y con el administrador.


### 💻 Desarrollo Técnico y Conceptos Aplicados

Este proyecto fue desarrollado aplicando de manera integral los conocimientos de **Python** y el framework **Django**, logrando una arquitectura escalable, segura y visualmente atractiva.

#### **🐍 Fundamentos de Python y Programación Orientada a Objetos (OOP)**
*   ***Herencia de Clases***: Uso intensivo de la herencia para extender las funcionalidades nativas de Django en las vistas (**ListView**, **DetailView**, **CreateView**, **UpdateView** y **DeleteView**) y modelos.
*   ***Métodos Personalizados y Lógica Core***: Implementación del método `get_servicios_list` en el modelo `Blog`, utilizando **List Comprehensions** para procesar cadenas de texto y transformarlas en listas dinámicas de servicios con una sola línea de código.
*   ***Métodos Especiales (Dunder Methods)***: Implementación de `__str__` para garantizar una representación legible de los objetos (viajes, perfiles y mensajes) dentro del panel de administración.
*   ***Decoradores***: Aplicación de `@login_required` para modificar el comportamiento de las funciones de forma declarativa, asegurando la privacidad de las rutas de usuario.
*   ***Tratamiento de Datos***: Gestión eficiente de diccionarios de contexto y **f-strings** para la construcción dinámica de perfiles, nombres de autor y mensajes de respuesta.

#### **🚀 Arquitectura y Framework Django**
*   ***Patrón de diseño MTV (Model-Template-View)***: Separación estricta de la lógica de negocio, la estructura de datos y la interfaz visual para garantizar un código limpio y mantenible.
*   ***Vistas Basadas en Clases (CBV)***: Implementación de una arquitectura CRUD completa, optimizando el tiempo de desarrollo y permitiendo una reutilización de código eficiente.
*   ***Manejo de Base de Datos (ORM)***: Creación de un esquema relacional avanzado utilizando **ForeignKey** para la autoría de blogs y mensajería, y **OneToOneField** para la extensión de perfiles de usuario.
*   ***Consultas Complejas (Object Q)***: Uso del objeto `Q` de Django para realizar filtros avanzados en la base de datos, permitiendo un sistema de mensajería fluido donde se visualizan envíos y recepciones en una sola bandeja.
*   ***Seguridad y Permisos***: Protección de formularios mediante tokens `{% csrf_token %}` y uso de **Mixins** de autenticación (**LoginRequiredMixin**, **UserPassesTestMixin**) para restringir las acciones de edición y borrado exclusivamente al administrador.
*   ***Gestión de Archivos Media***: Configuración de almacenamiento dinámico para permitir la subida y el renderizado en tiempo real de imágenes de perfil y portadas de los destinos de la bitácora a traves de la Configuración de `MEDIA_ROOT`.