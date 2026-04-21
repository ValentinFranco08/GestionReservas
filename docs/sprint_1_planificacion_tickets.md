# Fase 2: Planificación del Sprint

En esta fase tomamos los Casos de Uso y Escenarios generados en el Paso 1 y los convertimos en unidades de trabajo medibles y asignables (Tickets).

## Tablero (Simulación Jira/Trello)
**Sprint Actual**: Sprint 1 (Duración: 2 semanas)
**Objetivo del Sprint**: Implementar la visualización y gestión del equipamiento de salas y configurar el pipeline base de testing y CI/CD.

---

### Ticket 1: Modificación del Modelo de Datos
- **ID**: `RES-101`
- **Tipo**: Story / Backend
- **Título**: Agregar campo 'equipment' al modelo Room y actualizar persistencia.
- **Refinamiento (Descripción)**: 
  Se debe modificar la clase `Room` en `app/models/booking_model.py` para incluir una columna `equipment` de tipo String(200), que acepte valores nulos. Además, asegurarse de que al momento de la creación de la base de datos, este campo sea considerado.
- **Criterios de Aceptación**:
  - El modelo `Room` tiene el nuevo campo.
  - La base de datos guarda correctamente los datos al hacer un insert/update.
- **Estimación**: 3 Story Points (SP).
- **Asignado a**: Franco Valentin / Developer

---

### Ticket 2: Actualización de Vistas de Gestión de Salas
- **ID**: `RES-102`
- **Tipo**: Story / Frontend
- **Título**: Interfaz de usuario para agregar y listar Equipamiento.
- **Refinamiento (Descripción)**:
  Modificar las plantillas HTML para la gestión de salas (`rooms.html` o equivalentes).
  1. Agregar un `input` para "Equipamiento" en los formularios de creación y edición.
  2. Agregar una columna extra en la tabla de listado de salas para mostrar los equipos. Si está vacío, mostrar "N/A".
- **Criterios de Aceptación**:
  - Formularios muestran el campo de manera responsiva (usando Tailwind).
  - La tabla se adapta a la nueva columna sin romper el diseño.
- **Estimación**: 2 Story Points (SP).
- **Asignado a**: Franco Valentin / Developer Frontend

---

### Ticket 3: Testing Unitario
- **ID**: `RES-103`
- **Tipo**: Task / QA
- **Título**: Escribir tests unitarios para entidades del sistema.
- **Refinamiento (Descripción)**:
  Como es un requerimiento del ciclo de software, necesitamos iniciar una suite de pruebas. Crear directorio `tests/` e implementar `test_models.py` utilizando `pytest` o `unittest`. Se debe probar la creación de una Sala (Room) con y sin equipamiento.
- **Criterios de Aceptación**:
  - Los tests pueden ser ejecutados desde la terminal localmente (`python -m unittest` o `pytest`).
  - Cobertura mínima: creación correcta y fallida de Room.
- **Estimación**: 3 Story Points (SP).
- **Asignado a**: Franco Valentin / QA Engineer

---

### Ticket 4: Configuración de CI/CD Pipeline
- **ID**: `RES-104`
- **Tipo**: Task / DevOps
- **Título**: Configurar Pipeline de Integración Continua (CI).
- **Refinamiento (Descripción)**:
  Para cumplir con los estándares de despliegue, crear un archivo de configuración de GitHub Actions (`.github/workflows/main.yml`) que se ejecute en cada Pull Request o Push hacia `main` o `release`. Debe instalar las dependencias (requirements.txt) y correr los tests creados en `RES-103`.
- **Criterios de Aceptación**:
  - Archivo `.yml` válido creado en el repositorio.
  - El pipeline corre los tests exitosamente de manera aislada.
- **Estimación**: 5 Story Points (SP).
- **Asignado a**: Franco Valentin / DevOps

---

## Resumen de la Planificación
- **Velocidad Comprometida del Sprint**: 13 Story Points.
- **Estado**: *Ready for Development (Sprint Started).*
