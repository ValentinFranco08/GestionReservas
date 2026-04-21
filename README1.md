# 🗓️ Gestión de Reservas de Salas de Reunión

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white)

Este proyecto es una aplicación web robusta y sencilla diseñada para gestionar reservas de salas de reunión, usuarios y las propias salas. Desarrollada con **Flask**, **SQLAlchemy** y **Tailwind CSS**, implementa buenas prácticas de desarrollo como el patrón de diseño **Builder** para la creación segura de reservas y la integración de actualizaciones asíncronas en tiempo real mediante **AJAX**.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Gestión y Planificación (Trello)](#-gestión-y-planificación)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Arquitectura y Patrones](#-arquitectura-y-patrones)

---

## 🚀 Características

### 🔹 CRUD Completo
- **Usuarios**: Gestión integral (Alta, Baja, Modificación y Listado).
- **Salas**: Administración de salas de reuniones especificando capacidades y equipamiento.
- **Reservas**: Sistema completo de agenda y reservas de salas por usuarios.

### 🔹 Validaciones Robustas
- Verificación automática de disponibilidad para evitar superposiciones de horarios.
- Prevención de creación de reservas con fechas/horas en el pasado.
- Resolución de conflictos en tiempo real al editar reservas existentes.

### 🔹 Interfaz de Usuario y UX
- **Actualizaciones en Tiempo Real**: Los estados de las reservas (*Próxima, Ocupada, Finalizada*) se sincronizan dinámicamente sin recargar la página.
- **Diseño Moderno y Responsivo**: UI/UX cuidada utilizando la potencia de **Tailwind CSS**.
- **Filtros Avanzados**: Búsqueda de reservas específicas por usuario o por sala.
- **Feedback Interactivo**: Notificaciones (flash messages) informativas sobre el resultado de las operaciones.

---

## 🛠️ Tecnologías Utilizadas

| Backend | Frontend | Base de Datos |
| :--- | :--- | :--- |
| **Python** 3.12+ | **HTML5** | **SQLite** (Motor BD) |
| **Flask** (Framework) | **Tailwind CSS** (Estilos) | **SQLAlchemy** (ORM) |
| **Flask-SQLAlchemy** | **JavaScript Vanilla** (AJAX) | |
| | **Font Awesome** (Iconos)| |

---

## 📊 Gestión y Planificación

Este proyecto sigue una metodología ágil de desarrollo de software para asegurar la trazabilidad, la calidad y la entrega continua.

**Tablero Kanban:**  
🔗 [Ver Tablero de Gestión de Reservas en Trello](https://trello.com/invite/b/69e7eb11d76f99289740c9d2/ATTI58d6e621476597d47155b90abea6e3ef4603EAA3/gestiondereservas)

En el tablero se administran los requerimientos, los tickets (tareas de desarrollo), bugs y documentación durante los Sprints.

---

## ⚙️ Instalación y Ejecución

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local.

### Prerrequisitos
- Tener instalado **Python 3.12** o superior.
- Tener `git` instalado.

### 1. Clonar el Repositorio
```bash
git clone <url_del_repositorio>
cd Gestion_Reservas
```

### 2. Crear y Activar Entorno Virtual
Se recomienda el uso de un entorno virtual para aislar las dependencias.
```bash
python3 -m venv venv

# En Linux/macOS:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Inicializar la Base de Datos y Ejecutar
La base de datos SQLite (`site.db`) se creará automáticamente la primera vez que se corra el proyecto y se inicialicen los modelos.

```bash
python3 run.py
```

### 5. Acceder a la Aplicación
Abre tu navegador web y visita:  
👉 **http://127.0.0.1:5000**

---

## 📐 Arquitectura y Patrones

El proyecto aplica principios de **Programación Orientada a Objetos (POO)** y patrones de diseño para mantener el código limpio y escalable:
- **Modelo de Dominio**: Clases `User`, `Room` y `Booking` que reflejan fielmente las entidades del negocio.
- **Patrón Builder**: Delegación de la lógica de creación y validación compleja de objetos `Booking` a la clase `Builder`, garantizando la integridad de las reservas creadas.


