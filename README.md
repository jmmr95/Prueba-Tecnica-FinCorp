# Proyecto FinCorp UiPath: Automatización de Migración Financiera

**Diseñado por: Joan Manuel Moreno Rojas**

Repositorio de la prueba técnica diseñada para procesar transacciones masivas de FinCorp. Esta solución utiliza una arquitectura desacoplada para garantizar escalabilidad, resiliencia y trazabilidad total.

---

### Conceptos y Tecnologías Aplicadas

En esta solución se implementaron estándares de arquitectura empresarial para RPA:

* **Modelo Productor-Consumidor (Dispatcher/Performer):** Separación de responsabilidades para permitir el procesamiento paralelo.
* **REFramework (State Machine):** Implementación de una Máquina de Estados para la gestión profesional de excepciones y reintentos.
* **Integración Híbrida (Python + UiPath):** Procesamiento de lógica de impuestos compleja mediante scripts externos para facilitar el mantenimiento.
* **UI Resilience (Fuzzy & Anchors):** Uso de selectores difusos y anclajes para navegar en el portal dinámico de RPA Challenge.
* **Gestión Dinámica (Config):** Centralización de rutas, nombres de colas y carpetas de Orchestrator para evitar valores hardcoded.
* **BPM & Auditoría:** Diseño enfocado en la visibilidad del negocio con reportes detallados de éxito, falla y exclusión.

---

### Estructura del Repositorio

* **[01Dispatcher](./01_Dispatcher):** Carga masiva de datos desde Excel hacia Orchestrator Queues.
* **[02Performer](./02_Performer):** Lógica transaccional, procesamiento en Python e ingreso de datos en portal web.
* **[Documentation](./Documentation):** Carpeta con el detalle técnico y funcional del proyecto.

---

### Videos

Haz clic en los enlaces para acceder al video:

1. [**¿Cómo se realizó el Proyecto?**](https://drive.google.com/file/d/1G2dvGu0uGvrWk_IExAf69jzX5zvtlEjd/view?usp=drive_link)
2. [**Instructivo**](https://drive.google.com/file/d/1G16WP2X4xqpZhteka5ZrZRywyTEzKetU/view?usp=drive_link)

---

### Documentación del Proyecto

Haz clic en los enlaces para acceder a la documentación detallada:

1.  [**Análisis del Problema (BPM)**](./Documentation/Analisis_del_Problema.pdf): Análisis AS-IS vs TO-BE.
2.  [**Decisiones de Arquitectura (ADR)**](./Documentation/Decisiones_de_Arquitectura.pdf): Justificación técnica del diseño y manejo de errores.
3.  [**Instructivo de Configuración**](./Documentation/Instructivo.pdf): Guía para configurar el entorno y los Assets.
4.  [**Diccionario de Datos 01 Dispatcher**](./Documentation/Diccionario_Datos_01Dispatcher.pdf): Diccionario con entradas,salidas, variables.
5.  [**Diccionario de Datos 02 Performer**](./Documentation/Diccionario_Datos_02Performer.pdf): Diccionario con entradas,salidas, variables.
6.  [**Evidencias de Ejecución Colas**](./Documentation/Log_Resultados_Cola.pdf): Reporte de resultados y logs.
7.  [**Evidencias de Ejecución 01Dispatcher**](./Documentation/Log_01Dispatcher.pdf): Reporte de resultados y logs.
8.  [**Evidencias de Ejecución 02Performer**](./Documentation/Log_02Performer.pdf): Reporte de resultados y logs.
---

### Requisitos de Instalación

1.  **UiPath Studio:** Versión actualizada.
2.  **Python:** Versión 3.9 o superior (Añadido al PATH) x64bits
3.  **Orchestrator:** Carpeta moderna (ej. `Shared`) y cola creada con el nombre `FinCorp_Invoices`.
4.  **Configuración:** Actualizar el archivo `Data/Config.xlsx` con las rutas locales de tu computador.

---
Generado para la prueba técnica de FinCorp - 2026.
