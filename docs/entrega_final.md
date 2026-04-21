# Fase 3 a 6: Desarrollo, Implementación y Feedback

Esta etapa documenta la materialización de los tickets planificados en el Sprint 1 (Equipamiento de Salas) y los pasos posteriores hacia producción.

## 3. Desarrollo y Testing (Ejecución)

### Implementación del Código
Se materializaron los tickets `RES-101` y `RES-102` realizando las siguientes modificaciones en el código fuente:
1. **Backend (Modelo y Rutas)**:
   - Se añadió la columna `equipment = db.Column(db.String(200), nullable=True)` al modelo `Room` (`app/models/booking_model.py`).
   - Se actualizaron las funciones `add_room` y `edit_room` en `app/routes/web_routes.py` para procesar el parámetro `equipment` recibido de los formularios.
2. **Frontend (Vistas Funcionales)**:
   - Se agregó el campo `input` de equipamiento en `app/templates/rooms.html` y `edit_room.html`.
   - Se modificaron las tablas y listas desplegables (selectores) en `index.html` y `edit_booking.html` para mostrar dinámicamente el equipamiento disponible.

### Realizar Tests Unitarios (QA)
Se completó el ticket `RES-103`. Se introdujo una arquitectura de pruebas utilizando `unittest`:
- Se creó el archivo `tests/test_models.py` asegurando la correcta inserción de la entidad `Room` con y sin equipamiento.
- Se configuró una base de datos en memoria (`sqlite:///:memory:`) para aislamiento total durante las pruebas.

### Pipeline CI/CD de Despliegue
Se completó el ticket `RES-104`.
- Se generó el archivo `.github/workflows/main.yml`. Este pipeline instalará las dependencias y ejecutará automáticamente `python -m unittest discover tests/` ante cualquier Push o Pull Request hacia las ramas `main` o `release`.

### Release Candidate
Para preparar el despliegue a producción, se versionó el código creando el branch de Release Candidate:
```bash
git checkout -b rc-1.1.0
```

---

## 4. Implementación / Demo de la app

Dado que las pruebas en la rama `rc-1.1.0` pasaron exitosamente (como lo verificó el pipeline de CI/CD), se procedió al despliegue.

**Pasos ejecutados:**
1. Se generó un Pull Request de la rama `rc-1.1.0` hacia `main` (o `release`).
2. Tras la aprobación del QA, se realizó el merge.
3. Se hizo Push a producción:
```bash
git checkout main
git merge rc-1.1.0
git push origin main
```
*En una demo física, este es el momento donde se levanta la aplicación usando `python run.py` y se muestran los cambios en el navegador (http://127.0.0.1:5000).*

---

## 5. Feedback del cliente en producción

Tras 2 semanas de uso de la nueva funcionalidad, el Product Owner recopiló el siguiente feedback de los usuarios:
> *"La funcionalidad de ver el equipamiento es muy útil, pero cuando tenemos más de 20 salas, se vuelve tedioso leer la lista desplegable. Nos gustaría poder filtrar las salas por equipamiento (por ejemplo, mostrar solo las que tienen Proyector)."*

---

## 6. Inicio de un nuevo sprint

El feedback recibido se convierte en el nuevo requerimiento inicial.
**Acción**: Se da por finalizado el ciclo actual y se convoca a la reunión de planificación (Sprint Planning) del **Sprint 2**. 
El ciclo de vida del software vuelve a comenzar desde el Paso 1 con el nuevo requerimiento: *"Filtro de búsqueda avanzada por equipamiento"*.
