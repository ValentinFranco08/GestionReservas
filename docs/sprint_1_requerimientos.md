# Fase 1: Sprint Nuevo - Definición de Requerimientos

## 1. Toma de notas de la necesidad (Product Owner)
**Épica**: Gestión Avanzada de Salas.
**Historia de Usuario (User Story)**: 
> "Como empleado o gestor de reservas, necesito poder visualizar e indicar qué equipamiento tecnológico y físico posee cada sala (ej. proyector, pizarra, equipo de videoconferencia), para poder elegir la sala que mejor se adapte a las necesidades de mi reunión."

---

## 2. Casos de Uso (Use Cases)

### **CU-01: Gestionar Equipamiento de Salas**
- **Actor Principal**: Administrador / Gestor de Reservas.
- **Precondición**: El sistema debe estar funcionando y la base de datos operativa.
- **Flujo Principal**:
  1. El actor ingresa a la sección de "Gestión de Salas".
  2. El actor selecciona crear una nueva sala o editar una existente.
  3. El sistema muestra el formulario de sala, incluyendo un nuevo campo de texto/etiquetas llamado "Equipamiento".
  4. El actor ingresa el equipamiento (ej. "Proyector 4K, Pizarra blanca").
  5. El actor guarda los cambios.
  6. El sistema confirma el guardado y muestra el equipamiento en el listado principal de salas.
- **Postcondición**: La sala queda registrada en la base de datos con la información de su equipamiento.

### **CU-02: Consultar Equipamiento al Reservar**
- **Actor Principal**: Usuario común / Empleado.
- **Precondición**: Deben existir salas creadas con equipamiento asignado.
- **Flujo Principal**:
  1. El actor ingresa a realizar una nueva reserva.
  2. En el menú desplegable o lista de selección de salas, el sistema muestra el nombre de la sala junto con su capacidad y su equipamiento.
  3. El actor toma una decisión basada en esta información y completa la reserva.

---

## 3. Escenarios de Aceptación (Escenarios)

Utilizaremos el formato estándar BDD (Behavior-Driven Development: *Given-When-Then*).

**Escenario 1: Añadir equipamiento a una sala nueva exitosamente**
- **Dado (Given)** que el administrador se encuentra en el formulario de "Nueva Sala"
- **Cuando (When)** ingresa "Sala A", capacidad "10" y equipamiento "Proyector, Pantalla" y hace clic en guardar
- **Entonces (Then)** el sistema debe guardar la sala y mostrar el mensaje "Sala creada exitosamente"
- **Y (And)** la "Sala A" debe aparecer en el listado mostrando "Proyector, Pantalla" en la columna Equipamiento.

**Escenario 2: Dejar el equipamiento vacío**
- **Dado** que el administrador se encuentra en el formulario de "Nueva Sala"
- **Cuando** ingresa el nombre y la capacidad pero deja el campo "Equipamiento" en blanco y guarda
- **Entonces** el sistema debe permitir la creación
- **Y** en el listado debe mostrar "Sin equipamiento" o "N/A" para esa sala.

**Escenario 3: Actualizar equipamiento de sala existente**
- **Dado** que la "Sala B" no tiene equipamiento cargado
- **Cuando** el administrador edita la sala, agrega "TV 65 pulgadas" y guarda los cambios
- **Entonces** el sistema debe actualizar el registro y reflejar "TV 65 pulgadas" en la lista general.
