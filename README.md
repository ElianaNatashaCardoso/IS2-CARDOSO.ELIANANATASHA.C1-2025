# Sistema de Gestión de Biblioteca IS2 - [ELIANA NATASHA CARDOSO]

Este proyecto implementa un sistema básico de gestión de préstamos de una biblioteca, siguiendo una arquitectura de capas clara para separar responsabilidades.

## 1. Arquitectura del Sistema (Capas)

El sistema se organiza en una arquitectura de tres capas.
**Presentación ** | Simula la interacción del sistema con el usuario y gestiona el flujo de la aplicación. | **`main.py`** |
|**Lógica de Negocio** | Coordina las operaciones del sistema (préstamos, devoluciones, validaciones). Utiliza los atributos y entidades para el procesamiento. | **`logica_negocio`** (ej. `prestamo_service.py`) |
| **Datos / Dominio** | Define las clases del dominio (entidades) y la estructura de la base de datos (DB). | **`domain`** (Modelos: `socio.py`, `libro.py`, `prestamo.py`) y la carpeta **`db`**. |

## 2. Decisión de Diseño: Patrón Singleton

Para resolver el **Problema** de un **acceso centralizado a la base de datos**, se ha elegido implementar el **Patrón de Diseño Singleton**.

**¿Por qué Singleton?**
Asegura que solo exista una instancia de un objeto, proporciona un punto de acceso global y evita problemas de concurrencia al gestionar recursos críticos.

**Aplicación a la Conexión a la Base de Datos:**

* **Garantiza Unidad:** El sistema solo necesita una conexión activa (por ejemplo, para una **SQLAlchemy Session**).
El Singleton asegura que solo exista una instancia de este gestor de recursos.
* **Consistencia:** Todos los servicios de la Lógica de Negocio acceden al mismo punto de datos, lo que evita inconsistencias.

## 3. Instalación y Requisitos

**Requisitos:**
* Python 3.8+

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## 4. Ejecución del Sistema (Demo)

Para simular el flujo de trabajo (préstamos exitosos y fallidos):

```bash
python app/main.py

