# API REST - Gestión de Monumentos

API REST desarrollada con Django REST Framework para gestionar los monumentos de una ciudad.
Incluye operaciones CRUD, paginación, filtrado, ordenado y autenticación con JWT.

## Tecnologías utilizadas

- Python 3.x
- Django
- Django REST Framework (DRF)
- djangorestframework-simplejwt

## Instalación

1. Clonar el repositorio:
   git clone https://github.com/rfresno-cei/dwes-ud06-refact1
   cd dwes-ud06-refact1

2. Crear y activar el entorno virtual (Windows):
   py -m venv venv
   venv\Scripts\activate

   En Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Aplicar migraciones:
   python manage.py makemigrations
   python manage.py migrate

5. Arrancar el servidor:
   python manage.py runserver

El servidor estará disponible en: http://127.0.0.1:8000

## Endpoints

### Autenticación

| Método | Ruta           | Descripción                        |
|--------|----------------|------------------------------------|
| POST   | /api/register  | Registrar un nuevo usuario         |
| POST   | /api/login     | Iniciar sesión y obtener tokens JWT|
| POST   | /api/refresh   | Renovar el token de acceso         |

### Monumentos (requieren token JWT)

| Método | Ruta                    | Descripción                        |
|--------|-------------------------|------------------------------------|
| GET    | /api/monuments          | Listar todos los monumentos        |
| GET    | /api/monuments/<id>     | Obtener un monumento por ID        |
| POST   | /api/monuments          | Crear un nuevo monumento           |
| PUT    | /api/monuments/<id>     | Actualizar un monumento            |
| DELETE | /api/monuments/<id>     | Eliminar un monumento              |

### Paginación, Filtrado y Ordenado

| Parámetro      | Ejemplo                  | Descripción                              |
|----------------|--------------------------|------------------------------------------|
| ?page          | ?page=2                  | Página a mostrar (5 elementos por defecto)|
| ?page_size     | ?page_size=10            | Número de elementos por página (máx. 50) |
| ?q             | ?q=torre                 | Filtrar por nombre                       |
| ?sort          | ?sort=name               | Ordenar por campo (ascendente)           |
| ?sort          | ?sort=-year              | Ordenar por campo (descendente)          |

Ejemplo combinado:
GET /api/monuments?q=catedral&sort=-year&page=1&page_size=3

## Autenticación JWT

Todas las rutas de monumentos están protegidas. Incluye el token en cada petición:

Authorization: Bearer <access_token>

El token incluye el username y el email del usuario.
Los tokens de acceso tienen una vida de 15 minutos.
Los tokens de refresco duran 7 días y rotan automáticamente.

## Estructura del Proyecto

