# Casos de Prueba - Proyecto Final Python

### Caso 1: Registro de nuevo usuario y creación de perfil
- **Objetivo:** Verificar que el sistema permite crear un usuario y le asigna un perfil automáticamente.
- **Pasos:**
    1. Navegar a la sección de "Login" y luego a "Registrate acá" (`/accounts/signup/`).
    2. Completar los campos de Nombre de usuario, Email y Contraseña.
    3. Hacer clic en el botón "Registrarme".
- **Resultado esperado:** El sistema debe redirigir a la página de Inicio y, al ingresar a "Mi Perfil", los datos deben estar vinculados correctamente.

### Caso 2: Restricción de permisos para crear Blogs
- **Objetivo:** Asegurar que solo el administrador puede cargar nuevos destinos en la bitácora.
- **Pasos:**
    1. Iniciar sesión con un usuario que NO sea administrador.
    2. Intentar ingresar manualmente a la dirección `/pages/create/`.
- **Resultado esperado:** El sistema debe denegar el acceso o redirigir al login (gracias al Mixin de seguridad `UserPassesTestMixin`), impidiendo que un usuario normal publique contenido.

### Caso 3: Funcionamiento de la mensajería interna
- **Objetivo:** Validar que un usuario puede enviar una consulta y el destinatario recibirla en su bandeja.
- **Pasos:**
    1. Loguearse con el Usuario A.
    2. Entrar a una actividad de la bitácora y hacer clic en el botón amarillo "📩 ¿DUDAS? CONSULTAR".
    3. Escribir un mensaje y enviarlo.
    4. Salir e iniciar sesión con el Usuario B.
- **Resultado esperado:** El Usuario B debe ver un globo de notificación o el mensaje nuevo dentro de su sección "MENSAJES".