# 🌍 Asset & Travel Management Module for Odoo

![Odoo Version](https://img.shields.io/badge/Odoo-16.0%2F17.0-purple?style=flat-square&logo=odoo)
![License](https://img.shields.io/badge/license-AGPL--3-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-Active-green?style=flat-square)

Un módulo personalizado para Odoo diseñado para la gestión integral de una agencia de viajes estudiantil. Permite administrar alumnos, itinerarios de viaje, reservas, seguros y actividades extraescolares, asegurando la integridad de los datos mediante validaciones lógicas complejas.

## 🚀 Funcionalidades Principales

El módulo extiende la funcionalidad nativa de Odoo añadiendo 6 nuevos modelos interconectados:

* **🎓 Gestión de Alumnos:**
    * Cálculo automático de **edad**.
    * Control de validez de pasaportes (regla de los 6 meses de vigencia).
    * Historial de viajes realizado por alumno.
* **✈️ Gestión de Viajes:**
    * Control de fechas (Salida vs Regreso).
    * Cálculo automático de la **duración** en días.
    * Asociación con actividades extra y guías.
* **ticket Reservas y Compras:**
    * Generación automática de códigos de reserva aleatorios.
    * **Precios Dinámicos:** Descuento automático del 10% si la reserva se hace con más de 30 días de antelación.
* **🛡️ Seguros y Extras:**
    * Gestión de pólizas de seguro con validación de precios mínimos según cobertura.
    * Asignación de guías turísticos con validación de formato telefónico.

## 🛠️ Aspectos Técnicos Destacados

Este proyecto demuestra el dominio de la API del ORM de Odoo:

### 1. Computed Fields & Inverse Logic (`@api.depends`)
Se utilizan campos computados almacenados y no almacenados para cálculos en tiempo real:
* `precio_final`: Calcula descuentos basándose en `fecha_inscripcion` vs `fecha_salida`.
* `edad`: Calcula años basándose en `fecha_nacimiento`.

### 2. Constraints de Negocio (`@api.constrains`)
Validaciones robustas a nivel de base de datos (Python) para asegurar la calidad del dato:
* Evitar fechas de regreso anteriores a la salida.
* Impedir seguros 'Premium' por debajo de un precio coste.
* Bloquear actividades extra que ocurran fuera del rango de fechas del viaje.

### 3. UX Interactiva (`@api.onchange`)
Feedback inmediato al usuario en la interfaz:
* Alertas visuales (Warnings) si se introduce un pasaporte caducado al crear una reserva.
* Validación de longitud de número de teléfono en tiempo real.

### 4. Vistas y XML
* Uso de **Notebooks** para organizar relaciones `One2many`.
* Vistas **Tree** y **Form** personalizadas.
* Menús jerárquicos integrados en el backend de Odoo.

## 📂 Estructura del Módulo

```text
odoo-asset-lending-module/
├── models/
│   ├── __init__.py
│   ├── alumno.py           # Lógica de estudiante y edad
│   ├── viaje.py            # Lógica de fechas y duración
│   ├── compra.py           # Lógica de precios y descuentos
│   ├── seguro_viaje.py     # Validaciones de seguros
│   ├── actividad_extra.py  # Gestión de eventos
│   └── guia.py             # Gestión de personal
├── security/
│   └── ir.model.access.csv # ACLs y Permisos de acceso
├── views/
│   └── views.xml           # Definición de Vistas, Acciones y Menús
├── __init__.py
├── __manifest__.py         # Metadatos del módulo
└── README.md
🔧 Instalación y Despliegue
Este módulo está listo para ser desplegado en un entorno Odoo contenerizado (Docker).

Clonar el repositorio en tu carpeta de addons:

Bash

git clone [https://github.com/Megadeftro17/odoo-asset-lending-module.git](https://github.com/Megadeftro17/odoo-asset-lending-module.git)
Reiniciar el servicio de Odoo:

Bash

docker-compose restart odoo
Activar Modo Desarrollador en Odoo.

Ir a Aplicaciones -> Actualizar lista de aplicaciones.

Buscar "Asset Lending Management" e instalar.

Autor: [Jorge del Hoyo Ballestín] Desarrollado como proyecto de especialización en ERP Odoo.
