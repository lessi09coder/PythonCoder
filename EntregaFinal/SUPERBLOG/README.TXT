# SUPERBLOG

SUPERBLOG es una aplicación tipo blog desarrollada en Django que permite a los usuarios registrados crear, editar, eliminar y ver artículos. También incluye funcionalidades de registro de usuarios y autenticación.

## Características

- Registro de usuarios: Los usuarios pueden registrarse en la aplicación utilizando un formulario de registro.
- Autenticación: Los usuarios pueden iniciar sesión y cerrar sesión en la aplicación.
- Creación de artículos: Los usuarios autenticados pueden crear nuevos artículos proporcionando un título y contenido.
- Edición de artículos: Los usuarios pueden editar los artículos que han creado previamente.
- Eliminación de artículos: Los usuarios pueden eliminar los artículos que han creado previamente.
- Visualización de artículos: Todos los usuarios pueden ver los artículos publicados en el blog.

## Instalación

Para ejecutar el proyecto localmente, sigue estos pasos:

1. Clona este repositorio en tu máquina local utilizando el siguiente comando:

    ```
    git clone https://github.com/lessi09coder/PythonCoder.git
    ```

2. Navega a la carpeta `EntregaFinal/SUPERBLOG`.

3. Instala las dependencias del proyecto utilizando el siguiente comando:

    ```
    pip install -r requirements.txt
    ```

4. Aplica las migraciones de la base de datos utilizando el siguiente comando:

    ```
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo con el siguiente comando:

    ```
    python manage.py runserver
    ```

6. Abre tu navegador web y navega a `http://127.0.0.1:8000` para ver la aplicación.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama para tu función o corrección de errores: `git checkout -b feature/nueva-funcion` o `git checkout -b fix/arreglo`.
3. Realiza tus cambios y haz commits con mensajes descriptivos.
4. Sube tus cambios a tu fork: `git push origin feature/nueva-funcion`.
5. Crea un pull request en este repositorio.

## Tecnologías Utilizadas

- Django: Framework de desarrollo web en Python utilizado para construir la aplicación.
- HTML/CSS: Lenguajes de marcado y estilo utilizados para diseñar las páginas web.
- Bootstrap: Framework de CSS utilizado para estilizar la interfaz de usuario.
- SQLite: Sistema de gestión de bases de datos utilizado para almacenar los datos del blog.

## Créditos

Este proyecto fue desarrollado por Alexis Bonetti.