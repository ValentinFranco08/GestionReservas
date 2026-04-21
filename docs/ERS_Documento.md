# Especificación de Requisitos de Software (ERS)
**Proyecto**: Sistema de Gestión de Reservas de Salas de Reunión
**Versión**: 1.1.0

---

## 1. Introducción

### 1.1 Propósito
El propósito de este documento es definir la Especificación de Requisitos de Software (ERS) para el "Sistema de Gestión de Reservas de Salas". Este documento describe tanto el comportamiento del sistema bajo un uso rutinario como los requerimientos funcionales desarrollados durante el Sprint actual (Módulo de Equipamiento).

### 1.2 Alcance del Sistema
El sistema permite a una organización gestionar sus salas de reuniones de forma digital. A través de una interfaz web, los usuarios pueden crear, leer, actualizar y eliminar (CRUD) registros de Usuarios, Salas y Reservas. Además, el sistema evita colisiones de horarios, y permite especificar el equipamiento tecnológico de cada sala para una mejor toma de decisiones al momento de reservar.

### 1.3 Definiciones y Acrónimos
*   **PO (Product Owner)**: Dueño del producto que define las prioridades.
*   **CRUD**: Create, Read, Update, Delete (Crear, Leer, Actualizar, Eliminar).
*   **Sistema**: Hace referencia a la aplicación web de Gestión de Reservas.

---

## 2. Descripción General

### 2.1 Perspectiva del Producto
El sistema es una aplicación web independiente construida sobre una arquitectura Cliente-Servidor. El backend está desarrollado en Python (Flask) con una base de datos relacional SQLite, mientras que el frontend utiliza HTML, JavaScript y Tailwind CSS.

### 2.2 Funciones Principales del Producto
1.  **Gestión de Usuarios**: ABM (Alta, Baja, Modificación) de empleados o usuarios del sistema.
2.  **Gestión de Salas**: ABM de los espacios físicos, controlando su capacidad máxima.
3.  **Gestión de Equipamiento (Nuevo Sprint)**: Capacidad de añadir detalles sobre las comodidades de una sala (proyector, pizarra, etc.).
4.  **Gestión de Reservas**: Creación de reservas validando que la sala esté disponible en el horario solicitado.
5.  **Monitoreo en Tiempo Real**: Visualización dinámica del estado de las reservas (Próxima, Ocupada, Finalizada).

### 2.3 Características de los Usuarios
*   **Administrador / Gestor**: Tiene permisos para administrar salas, equipamiento y usuarios.
*   **Empleado**: Utiliza el sistema para consultar disponibilidad, ver el equipamiento de las salas y agendar reuniones.

---

## 3. Requisitos Específicos

### 3.1 Requisitos Funcionales (Casos de Uso)

**RF-01: Gestionar Salas y Equipamiento**
*   **Descripción**: El sistema debe permitir crear y editar salas especificando nombre, capacidad y equipamiento.
*   **Precondición**: Acceso al sistema operativo.
*   **Flujo principal**: El usuario ingresa a la gestión de salas, completa el formulario con los detalles (incluyendo equipamiento como "TV, Proyector") y guarda los datos. El sistema persiste la información en la base de datos.

**RF-02: Gestionar Usuarios**
*   **Descripción**: El sistema debe permitir registrar usuarios con nombre y correo electrónico único.
*   **Excepción**: Si el correo ya existe, el sistema debe arrojar un error ("El correo ya existe").

**RF-03: Realizar Reserva de Sala**
*   **Descripción**: El sistema debe permitir a un usuario seleccionar una sala (visualizando su equipamiento), una fecha/hora de inicio y fin, y generar una reserva.
*   **Regla de Negocio**: El sistema debe rechazar reservas cuyas horas se superpongan con reservas existentes para la misma sala.
*   **Regla de Negocio**: La fecha de inicio no puede ser posterior a la fecha de fin.

**RF-04: Actualización de Estado Dinámico**
*   **Descripción**: El sistema debe actualizar el estado de las reservas visualmente (AJAX) sin necesidad de recargar la página.

### 3.2 Requisitos No Funcionales

*   **RNF-01 (Interfaz)**: El diseño debe ser responsivo y adaptarse a pantallas de dispositivos móviles y escritorios (Tailwind CSS).
*   **RNF-02 (Rendimiento)**: El sistema debe consultar el estado de las reservas cada 10 segundos sin degradar el servidor.
*   **RNF-03 (Tecnología)**: El sistema debe ser compatible con Python 3.12+ y los navegadores web modernos (Chrome, Firefox, Safari).

---

## 4. Criterios y Escenarios de Aceptación (Validación)

*Esta sección valida que los requisitos funcionales del último Sprint hayan sido construidos correctamente bajo el formato Given-When-Then.*

**Escenario 1: Añadir equipamiento a una sala nueva exitosamente**
*   **Dado** que el administrador se encuentra en el formulario de "Nueva Sala"
*   **Cuando** ingresa "Sala A", capacidad "10" y equipamiento "Proyector, Pantalla" y guarda
*   **Entonces** el sistema debe guardar la sala y mostrar la "Sala A" en el listado con "Proyector, Pantalla" en la columna Equipamiento.

**Escenario 2: Validar colisión de horarios**
*   **Dado** que existe una reserva en la "Sala A" de 10:00 a 11:00
*   **Cuando** un usuario intenta reservar la "Sala A" de 10:30 a 11:30
*   **Entonces** el sistema debe rechazar la operación y mostrar el error: "La sala ya está reservada en este horario."
