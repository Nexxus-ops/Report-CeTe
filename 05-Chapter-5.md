# Capítulo V: Product Implementation, Validation & Deployment

[Configuración](#51-software-configuration-management) · [Sprint 1](#521-sprint-1) · [Sprint 2](#522-sprint-2) · [Sprint 3 / AV2](#523-sprint-3--consolidación-av2) · [Validación](#53-validation-interviews)

## 5.1. Software Configuration Management

La Gestión de Configuración de Software (SCM) es la disciplina que permite identificar, controlar, versionar y auditar los distintos componentes de un sistema durante todo su ciclo de vida. Su aplicación asegura la trazabilidad de los cambios realizados sobre el código fuente, la documentación y los artefactos de diseño, reduciendo la probabilidad de errores de integración y facilitando el trabajo colaborativo del equipo.

En el caso de **CeTe**, la solución está compuesta por una Landing Page informativa, una Frontend Web Application y un RESTful API de elaboración interna. Durante el **Sprint 1** se priorizó la implementación, validación y despliegue de la primera versión de la **Landing Page**, desarrollada con HTML5, CSS3 y JavaScript (ES6+), manteniendo un comportamiento 100% responsive y sin dependencias de frameworks externos.

### 5.1.1. Software Development Environment Configuration

A continuación se listan los productos de software utilizados por el equipo, organizados por tipo de actividad del ciclo de vida. Para cada herramienta se indica su propósito dentro de CeTe y la ruta de referencia o descarga.

**1. Project Management**

*Descripción:* La gestión del proyecto permite organizar las actividades necesarias para alcanzar los objetivos del Sprint, asignar responsables, dar seguimiento al avance y mantener la comunicación entre los integrantes del equipo.

**Trello y GitHub Projects:**
Los sprints históricos conservan sus capturas de Trello. El seguimiento actual de Sprint 3 se consulta en el [tablero público de Nexxus](https://github.com/orgs/Nexxus-ops/projects/1/views/1), creado el 12/11/2026 para consolidar tareas, estados y evidencias. La imagen de Jira siguiente pertenece al registro inicial de herramientas y no acredita que Sprint 3 se haya gestionado allí.
<p align="center">
  <img src="Images/Jira.png" alt="Jira" title="Jira" width="250">
</p>

**Google Meet & WhatsApp:**
Empleados para las ceremonias formales de Scrum (Daily, Planning, Review) y como canales de comunicación asincrónica para coordinar avances diarios.
<p align="center">
  <img src="Images/Meet.png" alt="Google Meet" title="Meet" width="250">
  <img src="Images/Whatsapp.png" alt="WhatsApp" title="WhatsApp" width="250">
</p>

**2. Requirements Management**

**UXPressia:**
Utilizado para la elaboración de los User Personas, Empathy Maps, Journey Maps e Impact Maps, facilitando la identificación de necesidades de los dueños de MYPEs y operarios logísticos. ([UXPressia](https://uxpressia.com/))
<p align="center">
  <img src="Images/UXPressia.png" alt="UXPressia" title="UXPressia" width="250">
</p>

**3. Product UX/UI Design**

**Figma:**
Herramienta de diseño colaborativo en la nube empleada para elaborar los wireframes, mockups y el prototipo interactivo de CeTe, documentando nuestro Design System. ([Figma](https://www.figma.com/))
<p align="center">
  <img src="Images/Figma.png" alt="Figma" title="Figma" width="250">
</p>

**4. Software Development**

**Visual Studio Code / WebStorm:**
Editores principales para el desarrollo Frontend (HTML, CSS, JS, Vue.js). La configuración de formato se estandariza mediante el archivo `.editorconfig`. ([VS Code](https://code.visualstudio.com/))
<p align="center">
  <img src="Images/Visual Studio Code.png" alt="Visual Studio Code" title="Visual Studio Code" width="250">
</p>

**JetBrains Rider / Visual Studio:**
Entornos contemplados por el equipo para trabajar con C#. El backend actual tiene como destino `net10.0` y utiliza ASP.NET Core 10; requiere un IDE y un SDK compatibles. La imagen de Visual Studio 2022 se conserva como referencia del entorno inicial, sin atribuirle compatibilidad con toda versión del proyecto.
<p align="center">
  <img src="Images/Visual Studio 2022.png" alt="Visual Studio 2022" title="Visual Studio 2022" width="250">
</p>

**HTML5 / CSS3 / JavaScript (ES6+):**
Tecnologías base de la Landing Page desplegada en el Sprint 1.
<p align="center">
  <img src="Images/HTML5.png" alt="HTML5" title="HTML5" width="200">
  <img src="Images/CSS3.png" alt="CSS3" title="CSS3" width="200">
  <img src="Images/JavaScript.png" alt="JavaScript" title="JavaScript" width="200">
</p>

**Vue.js & PrimeVue:**
Framework progresivo y biblioteca de componentes seleccionados para el desarrollo de la Single Page Application (Web App de Inventario y Ventas).
<p align="center">
  <img src="Images/Vue.png" alt="Vue.js" title="Vue.js" width="250">
</p>

**ASP.NET Core & C#:**
Framework y lenguaje utilizados para el desarrollo del RESTful API de CeTe, responsable de la lógica de negocio orientada a dominio (DDD).
<p align="center">
  <img src="Images/ASP.NET Core.png" alt="ASP.NET Core" title="ASP.NET Core" width="250">
</p>

**Entity Framework Core & PostgreSQL:**
Entity Framework Core 10 con Npgsql y PostgreSQL 17 proporcionan la persistencia del incremento AV2. El esquema físico se documenta con 35 tablas; los módulos todavía previstos se distinguen de los flujos implementados en el capítulo IV.
<p align="center">
  <img src="Images/PostgreSQL.png" alt="PostgreSQL" title="PostgreSQL" width="250">
</p>

**Git & GitHub:**
Sistema de control de versiones y plataforma de colaboración para alojar repositorios, aplicar GitFlow y Pull Requests.
<p align="center">
  <img src="Images/GitHub.png" alt="GitHub" title="GitHub" width="250">
</p>

**5. Software Deployment**

**GitHub Pages:**
Servicio de alojamiento estático utilizado para publicar la primera versión de la Landing Page de CeTe directamente desde la rama `main`.
<p align="center">
  <img src="Images/GitHub Pages.png" alt="GitHub Pages" title="GitHub Pages" width="250">
</p>

**Render y Docker:**
Render publica la landing y el frontend como sitios estáticos y la API como servicio Docker conectado a PostgreSQL administrado. Docker Compose reproduce API y base de datos en el entorno local. Las ramas de despliegue vigentes se indican en 5.1.4.

**Swagger / OpenAPI y herramientas de verificación:**
Swagger documenta los contratos HTTP de la API. Las comprobaciones de dominio en C#, las pruebas HTTP en Python y los recorridos de navegador respaldan la evidencia técnica; no reemplazan la validación con usuarios. El [repositorio de la API](https://github.com/Nexxus-ops/CeTe-Api) conserva las instrucciones reproducibles.

<div style="page-break-after: always"></div>

### 5.1.2. Source Code Management

La administración del código fuente es un pilar del trabajo colaborativo del equipo. En este apartado se define el modelo organizativo y de control de versiones aplicado mediante GitHub y el flujo de trabajo GitFlow.

**1. Establecimiento de repositorios en GitHub**

La solución distribuida de CeTe se organiza en repositorios independientes:
* **Landing Page:** Repositorio dedicado al sitio web promocional del producto.
* **Frontend Web Application:** Repositorio destinado a la aplicación web (Vue.js).
* **RESTful API:** Repositorio que aloja la lógica del backend (ASP.NET Core).
* **Project Report:** Repositorio destinado a la redacción del informe en Markdown.

**2. Workflow de control de versiones (GitFlow)**

| Nombre de la rama | Descripción |
| :--- | :--- |
| **Main Branch** (`main`) | Base integrada del informe, frontend y API. Render publica frontend y API desde `main`; no se generaliza esa configuración a la landing. |
| **Develop Branch** (`develop`) | Rama de integración cuando existe en el repositorio. En la landing es, además, la rama configurada para la publicación actual en Render. |
| **Feature Branches** (`feature/*`) | Ramas temporales para desarrollar funcionalidades aisladas. <br> **Convención:** `feature/nombre-de-la-funcionalidad` |
| **Release Branches** (`release/*`) | Ramas de estabilización previas al pase a producción. <br> **Convención:** `release/vX.Y.Z` |
| **Hotfix Branches** (`hotfix/*`) | Convención prevista para correcciones urgentes sobre una versión publicada. No se acredita su uso únicamente por definir el nombre. |

El flujo anterior es la convención del equipo. Las integraciones AV2 también emplean ramas `refactor/*`, `fix/*`, `improve/*`, `integrate/*` y `docs/*`, con Pull Requests enlazados en 5.2.3.4. El historial de cada repositorio determina qué ramas y revisiones se utilizaron realmente.

**3. Versionado Semántico (Semantic Versioning 2.0.0)**

CeTe adopta el estándar **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`).
* Ejemplo: `v1.0.0` (Primera versión desplegada de la Landing Page).

**4. Convenciones de mensajes de commit (Conventional Commits)**

* `feat:` incorpora una funcionalidad nueva.
* `fix:` corrige un error.
* `docs:` modifica exclusivamente documentación.
* `style:` aplica ajustes de formato visual.
* `refactor:` reestructura código existente sin añadir funcionalidades.
* `chore:` tareas de mantenimiento y configuración.

### 5.1.3. Source Code Style Guide & Conventions

Como regla transversal, **toda la nomenclatura técnica (identificadores, clases, variables, funciones y métodos) se redacta exclusivamente en inglés**.

**HTML & CSS**
* Indentación de 2 espacios.
* Uso de metodología **BEM** (Block, Element, Modifier) para las clases CSS.
* Uso de *Custom Properties* (`:root`) para la paleta de colores corporativa (Primary Blue, Accent Orange).

**C# (.NET Core)**
* Indentación de 4 espacios.
* Nomenclatura `PascalCase` para clases y métodos (`StockBalance`, `Receive`), `camelCase` para variables locales.
* Aplicación estricta de inyección de dependencias y programación asíncrona (`Async`).

### 5.1.4. Software Deployment Configuration

El incremento AV2 se publica en Render. La landing y el frontend se sirven como sitios estáticos. La API se ejecuta en Docker y se conecta internamente a PostgreSQL administrado.

| Producto | Construcción y ejecución | Publicación AV2 | Captura |
| :--- | :--- | :--- | :--- |
| Landing | HTML, CSS y JavaScript. Rama `develop`. | [Sitio público](https://cete-landing-av2.onrender.com/) · [Release v1.1.0](https://github.com/Nexxus-ops/nexxus-landing-page/releases/tag/v1.1.0). | [<img src="AV2/evidence/landing-desktop.png" alt="Landing publicada de CeTe" width="260">](AV2/evidence/landing-desktop.png) |
| Frontend | Vue/Vite, compilación a `dist` y navegación por hash. Rama `main`. | [Aplicación pública](https://cete-web-av2.onrender.com/) · [Release v1.1.0](https://github.com/Nexxus-ops/FrontEnd-CeTe/releases/tag/v1.1.0). | [<img src="AV2/evidence/dashboard-desktop.png" alt="Dashboard publicado con datos ficticios" width="260">](AV2/evidence/dashboard-desktop.png) |
| API | Docker, ASP.NET Core 10, CORS, JWT y configuración por variables de entorno. Rama `main`. | [Swagger público](https://cete-api-av2.onrender.com/swagger) · [Salud](https://cete-api-av2.onrender.com/health). | [<img src="AV2/evidence/api-swagger-public.png" alt="Swagger servido por la API pública" width="260">](AV2/evidence/api-swagger-public.png) |
| Base de datos | PostgreSQL 17. Conexión interna desde la API. | Servicio administrado. El endpoint de salud comprueba la conexión. | La evidencia se observa a través de la API y sus flujos persistidos. |

Para desarrollo, Docker Compose inicia la API y PostgreSQL. La [vista de despliegue](04-Chapter-4.md#463-software-architecture-container-diagrams) detalla la comunicación entre servicios. El [README de la API](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/README.md) incluye los pasos reproducibles. Las capturas del frontend corresponden a la revalidación pública del 12/11/2026 con datos ficticios.

**Versión de API publicada.** La refactorización DDD integrada por el equipo en [PR #2](https://github.com/Nexxus-ops/CeTe-Api/pull/2) se desplegó desde `main`, commit [`4df092e`](https://github.com/Nexxus-ops/CeTe-Api/commit/4df092e49cef5033476add1c7b2caf410d35eac9), el 12/11/2026 a las 11:35 (Lima). Se conservaron las 28 operaciones HTTP y el esquema físico. La prueba de continuidad recuperó una sesión y una boleta creadas antes del despliegue. Sus resultados se presentan en [5.2.3.5. Execution Evidence](#5235-execution-evidence-for-sprint-review).

## 5.2. Landing Page, Services & Applications Implementation

### 5.2.1. Sprint 1

Durante el Sprint 1, el equipo de Nexxus se concentró en la implementación y despliegue de la primera versión funcional y responsive de la Landing Page de CeTe, diseñada para captar a nuestro público objetivo (Dueños de MYPEs y Operarios).

#### 5.2.1.1. Sprint Planning 1

| Sprint # | Sprint 1 |
| :--- | :--- |
| **Sprint Planning Background** | |
| Date | 08/09/2026 |
| Time | 8:00 PM |
| Location | Google Meet (reunión virtual) |
| Prepared By | Salazar Marquina, Kevin Junior |
| Attendees | Anahua Ancachi, Liz Maribel<br>Campoblanco Guzman, Diego Roberto<br>Montes Chang, Piero Francisco<br>Salazar Marquina, Kevin Junior<br>Salazar Quiche, Darikson Bill |
| **Sprint 1 Review Summary** | Durante este primer ciclo el equipo consolidó los artefactos de UX definidos en los capítulos anteriores y los tradujo en una implementación web funcional. Se desarrolló y desplegó la primera versión de la Landing Page de CeTe. Todo el ciclo de vida del desarrollo, desde la asignación de tareas hasta su paso a "Done", fue monitoreado y gestionado mediante nuestro tablero Kanban en Trello, garantizando transparencia en el avance. |
| **Sprint 1 Retrospective Summary** | El equipo evaluó positivamente la distribución del trabajo mediante la convención de ramas feature/* de GitFlow, reduciendo colisiones de código. El uso de Trello facilitó la visualización de los cuellos de botella en la fase de revisión de los Pull Requests. Como oportunidad de mejora, se debe afinar la estimación de las tareas de internacionalización (i18n) en la herramienta para el próximo ciclo. |
| **Sprint Goal & User Stories** | |
| **Sprint 1 Goal** | *Our focus is on* publicar la primera versión funcional y responsive de la Landing Page de CeTe.<br>*We believe it delivers* a las MYPES una comprensión rápida de nuestra solución B2B.<br>*This will be confirmed when* el sitio sea accesible desde cualquier dispositivo, mostrando claramente la propuesta y los planes de suscripción. |
| **Sprint 1 Velocity** | 24 |
| **Sum of Story Points** | 24 |

#### 5.2.1.2. Aspect Leaders and Collaborators

| Team Member | Landing Page (código) | Diseño UI/UX | Documentación | Deployment |
| :--- | :--- | :--- | :--- | :--- |
| Anahua Ancachi, Liz | Colaborador | Líder | Colaborador | Colaborador |
| Campoblanco, Diego | Colaborador | Colaborador | Colaborador | Líder |
| Montes Chang, Piero | Colaborador | Colaborador | Líder | Colaborador |
| Salazar, Kevin | Líder | Colaborador | Colaborador | Colaborador |
| Salazar, Darikson | Colaborador | Colaborador | Colaborador | Colaborador |

#### 5.2.1.3. Sprint Backlog 1

| Story ID | Work Item / Task Title | Description | Est. (h) | Assigned To | Status |
| :--- | :--- | :--- | :---: | :--- | :---: |
| US24 | Estructuración base e implementación del Hero | Creación del esqueleto semántico (`header`, `main`, `section`, `footer`) y propuesta de valor principal. | 4 | Salazar, Kevin | Done |
| US25 | Implementación de la sección de Funcionalidades | Maquetación de la grilla mostrando "Inventario en tiempo real", "Dashboard", etc. | 3 | Anahua, Liz | Done |
| US26 | Maquetación de la sección de Planes | Tarjetas de suscripción con precios para las MYPES. | 3 | Salazar, Darikson | Done |
| US29 | Implementación de navegación responsive | Desarrollo del header fijo, scroll suave y menú hamburguesa para móviles. | 4 | Campoblanco, Diego | Done |
| US33 | Implementación del Footer Institucional | Creación del pie de página con enlaces legales y redes sociales. | 2 | Montes, Piero | Done |
| US34 | Despliegue en GitHub Pages | Configuración del repositorio y publicación de la versión v1.0.0. | 2 | Campoblanco, Diego | Done |

La gestión de las historias de usuario y tareas técnicas correspondientes a este Sprint se realizó a través de la herramienta Trello. A continuación, se presenta la evidencia del tablero Kanban utilizado durante la ejecución del Sprint:

<p align="center">
  <img src="Images/Trello-Backlog-1.png" width="800" alt="Evidencia-Produt-Backlog-Trello">
</p>

Tablero Kanban del Sprint 1 gestionado en Trello, mostrando el flujo de desarrollo de la Landing Page.

Enlace al tablero: https://trello.com/invite/b/6ac45ef9360979a18e3bdcb8/ATTI9b6472f77acb5d72e55d42fac34aa3a7F2643D2F/cete-product-backlog-1

<div style="page-break-after: always"></div>

#### 5.2.1.4. Development Evidence for Sprint Review

Esta sección expone la evidencia técnica del progreso alcanzado. La Landing Page de CeTe fue desarrollada utilizando HTML5, CSS3 y JavaScript bajo un enfoque Mobile-First.

**Registro recuperado del historial de Sprint 1:**

Los commits siguientes corresponden a la implementación inicial de la landing. La rama consultada identifica dónde son alcanzables actualmente; el historial no permite atribuirles los nombres de ramas de trabajo consignados en la tabla anterior. Las fechas son las del commit, no horas de trabajo ni fechas de aceptación.

| Repositorio | Rama consultada | Commit | Mensaje original | Cuerpo original | Fecha y hora de commit (Lima) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| nexxus-landing-page | `develop` | [`30cf770`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/30cf770e4699ea705ac9ef87b4e6ee68210e64eb) | chore: setup of html structure and global styles | Sin cuerpo adicional. | 14/09/2026 23:35:04 -0500 |
| nexxus-landing-page | `develop` | [`69a5775`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/69a5775ad6b29b26306194a87f7fb149701b02a2) | feat: implement navbar and main hero section | Sin cuerpo adicional. | 14/09/2026 23:38:20 -0500 |
| nexxus-landing-page | `develop` | [`7385c80`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/7385c80bf2840b332184f89433174eb6aae1d091) | feat: add benefits, solutions and cta sections | Sin cuerpo adicional. | 14/09/2026 23:39:57 -0500 |
| nexxus-landing-page | `develop` | [`47cef62`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/47cef62ff73586b341c47d611733e517aa7106f7) | feat: add footer, responsive design and mobile menu logic | Sin cuerpo adicional. | 14/09/2026 23:42:04 -0500 |

<p align="center">
  <img src="Images/Evidencia de Código.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>
<p align="center">
  <img src="Images/Evidencia de Código 1.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>
<p align="center">
  <img src="Images/Evidencia de Código 2.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>

#### 5.2.1.5. Execution Evidence for Sprint Review

Se validó el comportamiento responsive, el menú móvil y las secciones de la Landing Page en navegadores de escritorio y dispositivos móviles.

<p align="center">
  <img src="Images/Ejecución Desktop 1.png" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecución Desktop 2.png" alt="Ejecución Desktop 2" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecución Desktop 3.png" alt="Ejecución Desktop 3" title="Execution Desktop" width="700">
</p>

<p align="center">
  <img src="Images/Ejecución Mobile.png" alt="Ejecución Mobile" title="Execution Mobile" width="200">
  <img src="Images/Ejecución Mobile 1.png" alt="Ejecución Mobile 1" title="Execution Mobile" width="200">
  <img src="Images/Ejecución Mobile 2.png" alt="Ejecución Mobile 2" title="Execution Mobile" width="200">
  <img src="Images/Ejecución Mobile 3.png" alt="Ejecución Mobile 3" title="Execution Mobile" width="200">
</p>

<div style="page-break-after: always"></div>

#### 5.2.1.6. Services Documentation Evidence for Sprint Review

Durante el Sprint 1, la Landing Page es un sitio estático informativo. La integración con los servicios RESTful internos (endpoints de autenticación, inventario y despacho documentados mediante Swagger/OpenAPI) se incorporará en los siguientes Sprints desde la Web Application en Vue.js.

#### 5.2.1.7. Software Deployment Evidence for Sprint Review

La versión `v1.0.0` de la Landing Page fue publicada exitosamente utilizando GitHub Pages automatizando el despliegue a partir de la rama `main`.

<p align="center">
  <img src="Images/Deloyment Evidence.jpeg" alt="Despliegue GitHub Pages" title="Deployment Evidence" width="700">
</p>

#### 5.2.1.8. Team Collaboration Insights during Sprint

El equipo gestionó el desarrollo utilizando repositorios de GitHub. Se aplicaron Pull Requests con revisiones cruzadas. A continuación, las analíticas de colaboración:

<p align="center">
  <img src="Images/Team Collaboration Insights.jpeg" alt="GitHub Insights" title="Collaboration Evidence" width="700">
</p>

<div style="page-break-after: always"></div>

### 5.2.2. Sprint 2

> **Registro histórico TB1.** La planificación y la retrospectiva siguientes se conservan como fueron declaradas. Sus referencias a DDD, arquitectura hexagonal y responsabilidades no sustituyen la comprobación de los límites reales ni la evidencia individual. La arquitectura actual se contrasta con el código en el capítulo IV.

#### 5.2.2.1. Sprint Planning 2

| Sprint # | Sprint 2 |
| :--- | :--- |
| **Sprint Planning Background** | |
| Date | 06/10/2026 |
| Time | 8:00 PM |
| Location | Google Meet (reunión virtual) |
| Prepared By | Campoblanco Guzman, Diego Roberto |
| Attendees | Anahua Ancachi, Liz Maribel <br> Campoblanco Guzman, Diego Roberto <br> Montes Chang, Piero Francisco <br> Salazar Marquina, Kevin Junior <br> Salazar Quiche, Darikson Bill |
| **Sprint 2 Review Summary** | Durante este segundo ciclo, el equipo materializó la arquitectura basada en Domain-Driven Design (DDD) construyendo la Web Application (Frontend) interactiva utilizando Vue.js 3, Vite, y PrimeVue. Se implementaron los Bounded Contexts core de la plataforma: IAM, Inventario, Ventas y Logística, integrados con un servidor de desarrollo mockeado (JSON-Server) para simular la persistencia de datos relacionales y las respuestas de la API. |
| **Sprint 2 Retrospective Summary** | El equipo evaluó positivamente el uso de Pinia para la gestión del estado y la implementación de la Arquitectura Hexagonal en el frontend, lo cual permitió separar claramente la capa de dominio, infraestructura (API calls) y presentación (vistas/componentes). Como oportunidad de mejora, se debe planificar la sustitución progresiva del Mock Backend (`db.json`) por la integración oficial con el RESTful API en C# (ASP.NET Core) en el siguiente ciclo. |
| **Sprint Goal & User Stories** | |
| Sprint 2 Goal | **Our focus is on** publicar la primera versión funcional de la Single Page Application (SPA) para la gestión logística. <br><br> **We believe it delivers** a los operarios de almacén y dueños de MYPEs una interfaz de "cero fricción" para registrar inventarios, procesar ventas y programar rutas. <br><br> **This will be confirmed when** el sistema permita navegar fluidamente entre módulos mediante el Vue Router, proteger rutas con el `authentication.guard.js`, y soportar la internacionalización (ES/EN) de forma reactiva. |
| Sprint 2 Velocity | 24 |
| Sum of Story Points | 24 |

#### 5.2.2.2. Aspect Leaders and Collaborators

| Team Member | Web App (Frontend) | Diseño UI/UX | Mock API / Arquitectura | Deployment |
| :--- | :--- | :--- | :--- | :--- |
| Anahua Ancachi, Liz | Lider | Colaborador | Colaborador | Colaborador |
| Campoblanco, Diego | Colaborador | Colaborador | Lider | Colaborador |
| Montes Chang, Piero | Colaborador | Colaborador | Colaborador | Lider |
| Salazar, Kevin | Colaborador | Lider | Colaborador | Colaborador |
| Salazar, Darikson | Colaborador | Colaborador | Colaborador | Colaborador |

#### 5.2.2.3. Sprint Backlog 2

> **Aclaración TB1.** Las siete estimaciones suman 25 h (4 + 5 + 5 + 3 + 4 + 2 + 2). Esto no prueba 25 horas reales de trabajo. Tres actividades están por debajo de 4 h y varias agrupan módulos completos. Se conserva el registro histórico. Las asignaciones y estados requieren contraste con commits y tablero y no prueban por sí solos la participación declarada.


| Story ID | Work Item / Task Title | Description | Est. (h) | Assigned To | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US02** | Implementación de vistas de Autenticación y Guardias (IAM) | Desarrollo de `sign-in-form.vue`, `sign-up-form.vue` y protección de rutas con `authentication.guard.js` y persistencia en LocalStorage usando `iam.store.js`. | 4 | Anahua, Liz | Realizado/Revisado/Hecho |
| **US09 / US10** | Desarrollo del Módulo Core de Inventario | Construcción de `inventory-list.vue` (Kardex interactivo) y `inventory-form.vue` para el registro/ajuste de stock de SKUs y manejo de mermas. | 5 | Montes, Piero | Realizado/Revisado/Hecho |
| **US15 / US16** | Implementación del Punto de Venta (POS) interactivo | Desarrollo de `point-of-sale.vue` incluyendo un carrito de ventas reactivo, buscador integrado y validación/descuento automático de stock agotado (Stock Out). | 5 | Salazar, Darikson | Realizado/Revisado/Hecho |
| **US17** | Maquetación del Historial de Ventas | Implementación de `sales-list.vue` utilizando `pv-data-table` para listar transacciones y procesar anulaciones mediante `sales.store.js`. | 3 | Salazar, Kevin | Realizado/Revisado/Hecho |
| **US19 / US21** | Desarrollo del Módulo de Rutas y Despacho | Construcción de `dispatch-form.vue` para generar nuevos manifiestos asociando ventas completadas, y `dispatch-list.vue` para actualizar el monitoreo de las rutas. | 4 | Campoblanco, Diego | Realizado/Revisado/Hecho |
| **US33** | Configuración de Internacionalización (i18n) | Implementación de `vue-i18n` cargando diccionarios dinámicos (`es.json` y `en.json`) y el componente `language-switcher.vue` para la barra superior. | 2 | Montes, Piero | Realizado/Revisado/Hecho |
| **TS** | Configuración del Mock Backend (JSON-Server) | Creación de base de datos simulada (`db.json`) y rutas RESTful personalizadas (`routes.json`) en el puerto 5222 para proveer datos a la SPA sin depender del servidor C#. | 2 | Anahua, Liz | Realizado/Revisado/Hecho |


<p align="center">
  <img src="Images/Trello-Backlog-2.png" width="800" alt="Evidencia-Sprint-Backlog-2-Trello">
</p>

Tablero Kanban del Sprint 2 gestionado en Trello, mostrando el flujo de desarrollo del Frontend.

Enlace al tablero: https://trello.com/invite/b/6ac48ac544b95ec0d7179e1b/ATTId5582c14f0a61ddde82968ca79935a3f89ED4899/cete-sprint-backlog-2

#### 5.2.2.4. Development Evidence for Sprint Review

Esta sección expone la evidencia técnica del progreso alcanzado. El Frontend de CeTe fue desarrollada utilizando JavaScript, Vue3, CSS y HTML haciendo uso de DDD.

**Registro recuperado del historial de Sprint 2:**

Se conserva el mensaje original de cada commit. La referencia a DDD en el historial describe lo declarado en esa entrega; la revisión de los límites actuales se encuentra en el capítulo IV. `main` es la rama consultada para recuperar los commits, sin reconstruir nombres de ramas históricas no acreditados.

| Repositorio | Rama consultada | Commit | Mensaje original | Cuerpo original | Fecha y hora de commit (Lima) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FrontEnd-CeTe | `main` | [`b081cb6`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/b081cb67ae6dda0977d59a2e9a33ee47fbc2a6a3) | chore: Mock API configuration (json-server) and environment documentation | Sin cuerpo adicional. | 06/10/2026 00:12:57 -0500 |
| FrontEnd-CeTe | `main` | [`fba33be`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/fba33be4489f09844d08087445a420d3a95895ef) | feat: Implementation of DDD architecture (IAM, Inventory, Logistics, Sales) and base configuration of Vue/Vite | Sin cuerpo adicional. | 06/10/2026 00:14:46 -0500 |
| FrontEnd-CeTe | `main` | [`b663e5a`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/b663e5a13de43a90a27407b06a7b2c87ec538df4) | ci: configuración de despliegue automático con GitHub Actions | Sin cuerpo adicional. | 06/10/2026 00:32:29 -0500 |
| FrontEnd-CeTe | `main` | [`be033a3`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/be033a308ec4652e35a5ba06ba4bc0b4d9c86b50) | Update README with project structure and contexts | Added project structure and bounded contexts to README. | 06/10/2026 01:06:46 -0500 |

<p align="center">
  <img src="Images/Registro-De-Commits-2.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>

<p align="center">
  <img src="Images/Codigo-Sprint-21.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>
<p align="center">
  <img src="Images/Codigo-Sprint-22.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>
<p align="center">
  <img src="Images/Codigo-Sprint-23.png" alt="Evidencia de Código" title="Development Evidence" width="700">
</p>


#### 5.2.2.5. Execution Evidence for Sprint Review

Se validó el comportamiento del Frontend de la aplicacion que respondiera adecuadamente según las US propuestas para este sprint.

<p align="center">
  <img src="Images/Ejecucion-21.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-22.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-23.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-24.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-25.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-26.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-27.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-28.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-29.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-210.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-211.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-212.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-213.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-214.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-215.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-216.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-217.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-218.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>
<p align="center">
  <img src="Images/Ejecucion-219.jpg" alt="Ejecución Desktop 1" title="Execution Desktop" width="700">
</p>

<div style="page-break-after: always"></div>

#### 5.2.2.6. Services Documentation Evidence for Sprint Review

Durante el Sprint 2, la implementación de la Single Page Application (SPA) requirió el diseño de una capa de infraestructura robusta para el consumo de servicios web. Dado que el RESTful API oficial en ASP.NET Core se encuentra en fase de desarrollo, el equipo implementó un Fake API y construyó los Gateways de Infraestructura en el frontend siguiendo los principios de la Arquitectura Hexagonal. Esta separación asegura que el frontend esté listo para conectarse al backend real en los próximos sprints sin necesidad de refactorizar la lógica de negocio.

#### 5.2.2.7. Software Deployment Evidence for Sprint Review

La versión `v1.0.0` del Frontend fue publicada exitosamente utilizando GitHub Pages automatizando el despliegue a partir de la rama `main`.

<p align="center">
  <img src="Images/Deployment-Evidence.png" alt="Despliegue GitHub Pages" title="Deployment Evidence" width="700">
</p>

#### 5.2.2.8. Team Collaboration Insights during Sprint

El equipo gestionó el desarrollo utilizando repositorios de GitHub. Se aplicaron Pull Requests con revisiones cruzadas. A continuación, las analíticas de colaboración:

<p align="center">
  <img src="Images/Sprint-2-Collaboration-Insight.png" alt="GitHub Insights" title="Collaboration Evidence" width="700">
</p>

<div style="page-break-after: always"></div>

### 5.2.3. Sprint 3 / consolidación AV2

Material de sustentación: [presentación técnica AV2 editable](AV2/CeTe-AV2-revision-tecnica.pptx). Las evidencias de participación y validación se completan en sus secciones correspondientes.

#### 5.2.3.1. Sprint Planning 3

Este registro consolida el **cierre técnico y documental del Sprint 3 al 12/11/2026**. Distingue los resultados respaldados por código, pruebas y entrevistas del esfuerzo estimado y de los materiales audiovisuales en edición.

**Base de estimación retrospectiva.** El equipo no conserva un control de horas ni el horario completo de sus sesiones. Para dimensionar el trabajo se adopta un ciclo de cuatro semanas y se conserva la estimación de 94 horas-persona del backlog. Estas cifras son un modelo de planificación reconstruido; no son horas consumidas, registros de asistencia ni mediciones de velocidad.

| Sprint # | Sprint 3 · AV2 |
| :--- | :--- |
| **Sprint Planning Background** | **Registro retrospectivo de planificación y cierre** |
| Fecha de reunión registrada | Martes **03/11/2026**, fecha confirmada por el equipo. |
| Horario y lugar de la sesión | No registrados. La coordinación del incremento combinó sesiones presenciales, mensajería y revisión de los repositorios. |
| Preparado por | Salazar Marquina, Kevin Junior · 12/11/2026. |
| Equipo participante en el incremento | Liz Anahua, Diego Campoblanco, Piero Montes, Kevin Salazar y Darikson Salazar. Corresponde a los aportes del sprint; no se utiliza como lista de asistencia de una reunión particular. |
| Calendario de referencia estimado | **16/10/2026–12/11/2026**, 28 días calendario inclusivos. Se adopta como reconstrucción del ciclo de trabajo, tomando como referencia el intervalo de cuatro semanas de las planificaciones anteriores y el corte de AV2. |
| **Sprint 2 Review Summary** | El registro TB1 muestra el frontend con Fake API. La revisión identificó mejoras de estimación, internacionalización y footer, historias técnicas, modelo de datos, boleta, evidencias de ejecución y participación. |
| **Sprint 2 Retrospective Summary** | El incremento siguiente debía conectar los flujos con persistencia real, contrastar DDD con el código y hacer trazables las tareas y pruebas. Esta síntesis se basa en el feedback y los artefactos conservados. |
| Sprint 3 Goal | **Our focus is on** permitir registrar abastecimiento, vender con stock consistente y consultar una boleta histórica desde una aplicación integrada y una landing bilingüe. **We believe it delivers** trazabilidad operativa para el dueño y el operario. **This will be confirmed when** los flujos conservan datos, protegen stock y acceso por empresa y las fichas de validación permiten identificar dificultades y siguientes mejoras. |
| Sprint Review 3 · resultado | API modular y PostgreSQL integrados; compras y recepción parcial separadas; venta atómica, boleta histórica y despachos verificados; landing por segmento e idiomas. Se consolidan seis fichas de validación acumuladas y el análisis de sus hallazgos. |
| Sprint Retrospective 3 · síntesis | Funcionó separar responsabilidades de dominio y revisar el recorrido completo. La publicación centralizada exigió reforzar la trazabilidad individual. Para TF se priorizan navegación y retroalimentación de recepción, mediciones de usabilidad y ampliación de la muestra operativa. No se presentan estas conclusiones como transcripción de acuerdos verbales no registrados. |
| Revisión y retrospectiva · duración de referencia | **60 minutos de revisión y 30 minutos de retrospectiva**, como estimación orientativa para dimensionar el cierre. No identifican la hora ni la duración real de la reunión del 03/11. |
| Sprint 3 Velocity | **No medida.** No se convierten tareas técnicas ni horas en puntos aceptados. La referencia histórica de Sprint 2 es 24 SP, sin atribuir ese resultado a Sprint 3. |
| Sum of Story Points | **60 SP de alcance de referencia** en US10, US11, US14, US19–22, US28–29, US34–36 y US39–42. Las historias parciales conservan sus límites en el Product Backlog y las TS no se suman dos veces. |
| Capacidad estimada | **94 horas-persona**, en tareas de 4 a 8 h. Como referencia aritmética para cinco integrantes y cuatro semanas, equivalen a 18,8 h por persona en el ciclo o 4,7 h semanales; no representan disponibilidad ni esfuerzo individual observado. |

**Criterios técnicos revisados.** Crear una compra no incrementa stock; recibir parcialmente conserva el saldo; el reintento de venta no duplica la operación; la boleta conserva los datos históricos y permite impresión; las consultas aíslan empresas y permisos; la landing y las vistas comprobadas admiten idiomas, teclado y móvil. Los resultados se enlazan en 5.2.3.5. Los hallazgos cualitativos de usuarios no se convierten en porcentajes de mejora.

**Alcance del cierre.** Se consolida el incremento implementado y la ronda AV2 entregada de seis fichas. La ampliación de participantes y las nuevas comprobaciones de usabilidad se programan para TF. La presentación y las versiones audiovisuales finales conservan su estado de edición o revisión hasta disponer de los enlaces y archivos correspondientes.

**Definition of Done de una tarea técnica.** Cambio integrado, criterio acotado comprobado y evidencia enlazada. El cierre de una tarea no declara terminados todos los criterios de las US relacionadas ni funciones que quedan expresamente fuera del incremento.

#### 5.2.3.2. Aspect Leaders and Collaborators

Los aspectos se organizan por bounded context y por los productos que permiten demostrar el flujo. La matriz LACX refleja el reparto explicado por Kevin y los aportes integrados. **L** indica liderazgo del aspecto; **C**, colaboración; **—**, sin responsabilidad específica informada. Diego coordina la revisión DDD transversal. La matriz no equivale a un conteo de commits ni atribuye a todos la autoría de todos los archivos.

| Team Member (Last Name, First Name) | GitHub Username | Estructura DDD / Inventory | Procurement / Identity e integración | Sales / Logistics | UI/UX, boleta y landing | Informe / validación |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Anahua Ancachi, Liz Maribel | [lizzanahua-rgb](https://github.com/lizzanahua-rgb) | C | — | C | L | C |
| Campoblanco Guzman, Diego Roberto | [diegocampoblancog-droid](https://github.com/diegocampoblancog-droid) | L | C | C | C | L |
| Montes Chang, Piero Francisco | [PieroMchang](https://github.com/PieroMchang) | L | C | — | C | C |
| Salazar Marquina, Kevin Junior | [AresSalamar](https://github.com/AresSalamar) | C | L | C | C | L |
| Salazar Quiche, Darikson Bill | [darikson26](https://github.com/darikson26) | — | — | L | C | C |

Piero estructura los contextos y las reglas de inventario; Kevin integra abastecimiento, identidad, frontend/API y publicación; Darikson aporta Ventas y Logística; Liz aporta el flujo de boleta y diseño e integra las mejoras de acceso y metadatos; Diego revisa los límites DDD y coordina con Piero las entrevistas. Los commits y PR enlazados en 5.2.3.4 permiten distinguir la implementación, la integración y la revisión informadas por el equipo.

#### 5.2.3.3. Sprint Backlog 3

El backlog descompone el objetivo en tareas de ingeniería y entregables de validación, colaboración y comunicación. El [tablero público del Sprint 3](https://github.com/orgs/Nexxus-ops/projects/1/views/1) se creó el **12/11/2026** para registrar el estado actual. No se presenta como evidencia de movimientos anteriores en Trello ni como un historial reconstruido de trabajo diario.

![Tablero del Sprint 3 al cierre documental: 13 Done, 2 To Review y 1 In Process](AV2/evidence/sprint3-board-close.jpg)

*Corte de cierre del 12/11/2026. Los estados corresponden al alcance técnico y documental descrito en la tabla; no son un registro de horas ni de aceptación de todas las historias del producto.*

| US / TS y título | Task ID | Task Title | Task Description / resultado al corte | Estimation (h) | Assigned To | Status |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| US35/36 · Pago registrado y descuento de stock; TS11/31 | T3-01 | Sales: cierre atómico e idempotencia | Venta, rollback, reintentos y última unidad comprobados. Se cierra la tarea técnica de pago registrado y stock; US35 conserva el límite académico sin pasarela. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/bc369f5). | 8 | Kevin | Done |
| US39 · Visualizar e imprimir boleta; TS28 | T3-02 | Sales: boleta histórica e impresión | Cabecera, detalle, consulta histórica e impresión móvil comprobados. Las mejoras de acceso y jerarquía sugeridas en las entrevistas pasan al seguimiento de TF. [Evidencia](https://github.com/Nexxus-ops/FrontEnd-CeTe/pull/5). | 6 | Liz | Done |
| US40/41 · Orden de compra y recepción parcial; TS29/30 | T3-03 | Procurement: compra y recepción parcial | Verificar que crear una orden no mueva stock y que cada recepción incremente solo lo recibido. Flujo público y rechazo de exceso comprobados. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/00c1ec3). | 6 | Kevin | Done |
| US10/11/14 · Entradas, salidas e historial; TS07–09 | T3-04 | Inventory: entradas, salidas e historial | Verificar invariantes de saldo, motivo e historial y el contrato IInventoryFacade. Reglas encapsuladas y pruebas de stock aprobadas. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/f8f2eb3). | 6 | Piero | Done |
| US19–22 · Despachos, recursos, estados e incidencias; TS14–17 | T3-05 | Logistics: recursos, estados e incidencias | Elegibilidad de ventas, recursos, transiciones e incidencias contrastados con el flujo de navegador y las pruebas HTTP. Se cierra la revisión técnica del incremento. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/84f14c7). | 6 | Darikson | Done |
| US42/34 · Idioma y términos de la landing | T3-06 | Landing: idioma, footer y acceso por segmento | Verificar ambos idiomas, recarga, cuatro recursos del footer, teclado y 390 px; comprobar CTA de dueño a registro y operario a acceso. Publicación comprobada. [Evidencia](https://github.com/Nexxus-ops/nexxus-landing-page/pull/3). | 6 | Liz | Done |
| US28/29 · Usuarios y roles; TS21/22 | T3-07 | Identity: alta directa y permisos AV2 | Alta directa, permisos y aislamiento comprobados. El envío de correo de invitación de US28 queda fuera del incremento y continúa como evolución. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/2930433). | 6 | Kevin | Done |
| US29 · Restricción por roles; TS33 | T3-08 | Datos: esquema y aislamiento de empresa | Contrastar las 35 tablas, 182 columnas y 67 claves foráneas con diccionario, diagrama y código; comprobar aislamiento por empresa. Verificación técnica aprobada. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/AV2/diccionario-datos.md). | 6 | Piero | Done |
| TS34 · Pruebas de dominio, HTTP y navegador | T3-09 | Calidad: pruebas de dominio, HTTP y navegador | Ejecutar compilación, reglas, integración con PostgreSQL y flujo público. Comprobar continuidad de sesión/boleta e idempotencia tras desplegar. Resultado aprobado el 12/11. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/tests/api_smoke.py). | 8 | Kevin | Done |
| TS32 · Docker y publicación | T3-10 | Deployment: publicación y recorrido público | Publicar API refactorizada, frontend integrado y landing por segmento. Confirmar los commits desplegados y acceso público. Continuidad futura de PostgreSQL fuera de este cierre. [Evidencia](https://github.com/Nexxus-ops/FrontEnd-CeTe/pull/4). | 6 | Kevin | Done |
| Presentación · Evidencia del incremento | T3-11 | Presentación: incremento AV2 y Sprint 2 | Existe una presentación técnica editable. Faltan revisión conjunta, actualización de resultados de validación y preparación de la sustentación final. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/AV2/CeTe-AV2-revision-tecnica.pptx). | 4 | Darikson | To Review |
| Validación · Dos segmentos | T3-12 | Validación: seis fichas AV2 y análisis | Se incorporan las seis fichas entregadas, incluidas las entrevistas de Diego y Piero, con cobertura y análisis diferenciados. La ampliación de la muestra operativa y las mediciones comparativas se trasladan a TF. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/pull/28). | 6 | Diego y Piero | Done |
| SO5 · Colaboración y revisión | T3-13 | Colaboración: trazabilidad y revisión retrospectiva | Matriz LACX, aportes por producto, commits e integraciones consolidados. La síntesis de revisión y coordinación se documenta retrospectivamente; no se reconstruyen horarios ni asistencias. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/pull/25). | 4 | Diego | Done |
| About-the-Product · Video del producto | T3-14 | About-the-Product: verificar video y enlace | Al corte del 12/11 solo estaba el promocional de diez segundos. Actualización 13/11: montaje de aproximadamente 2:20 editado y publicado en YouTube, con demostración real y opiniones de Nicol y Jaime. Siguen pendientes Stream e incrustación en la landing. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/05-Chapter-5.md#54-video-about-the-product). | 6 | Darikson | To Review |
| About-the-Team · Video del equipo | T3-15 | About-the-Team: aportes y reflexión | Montaje del equipo en Canva con clips recibidos y edición en curso. Completar la versión final, revisar los cinco testimonios y publicar enlaces definitivos. [Montaje](https://www.canva.com/d/mA3bW8S9nOk7TK0). | 6 | Equipo | In Process |
| Comunicación · Informe y conclusiones | T3-16 | Comunicación: conclusiones y coherencia | Informe consolidado: estimaciones retrospectivas, cierre de alcance AV2, seis entrevistas, hallazgos, conclusiones y roadmap para TF. Revisión de estructura y coherencia completada antes de la exportación. [Informe](https://github.com/Nexxus-ops/Report-CeTe). | 4 | Kevin | Done |

**Esfuerzo estimado de referencia: 94 horas-persona.** Las 13 tareas técnicas y documentales cerradas representan **78 h estimadas**; los tres materiales en edición o revisión, **16 h estimadas**. No son horas trabajadas ni esfuerzo restante medido. Las 4 h de T3-13 dimensionan preparación, seguimiento y documentación de coordinación dentro del modelo de esfuerzo.

**Balance al corte del 12/11:** 13 tareas Done, 2 To Review y 1 In Process. Los materiales de presentación, Product y Team continúan como complementos de publicación de AV2. US35 mantiene el pago académico y US28 el alta directa sin correo de invitación; no se elevan a historias completas por cerrar sus tareas técnicas.

**Actualización audiovisual del 13/11.** El About-the-Product ya está editado y [publicado en YouTube](https://youtu.be/V49TZ5P5Rsk). T3-14 continúa en revisión por su alcance completo: falta la publicación en Stream y la incrustación en la landing. La actualización no modifica las estimaciones ni reconstruye estados anteriores del tablero.

**Revisión de la coordinación.** El reparto y los resultados se sustentan en la matriz y en los artefactos. Se conserva la fecha confirmada de la sesión y se sintetiza la coordinación a partir de las fuentes disponibles. Para las siguientes iteraciones se incorpora el registro oportuno de acuerdos, asistencia y aportes individuales como mejora del proceso.

#### 5.2.3.4. Development Evidence for Sprint Review

Los siguientes commits acreditan el incremento técnico. Los mensajes seleccionados constan de asunto y carecen de cuerpo. Los registros de octubre documentan la implementación inicial; la refactorización del 12/11/2026 fue integrada en `main` mediante el commit `4df092e`.

| Repositorio | Rama integrada | Commit | Mensaje | Cuerpo | Fecha |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CeTe-Api | `main` | [`8c81227`](https://github.com/Nexxus-ops/CeTe-Api/commit/8c81227) | feat: implement CeTe AV2 API with PostgreSQL and Docker | — | 29/10/2026 |
| FrontEnd-CeTe | `main` | [`7075e28`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/7075e28) | feat: connect CeTe AV2 to real API and add historical sales receipts | — | 29/10/2026 |
| FrontEnd-CeTe | `main` | [`711fe93`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/711fe93) | feat: receive purchase orders partially from the web interface | — | 29/10/2026 |
| nexxus-landing-page | `develop` | [`13326ec`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/13326ec) | feat: improve CeTe landing internationalization and functional resources | — | 29/10/2026 |
| Report-CeTe | `main` | [`8d87183`](https://github.com/Nexxus-ops/Report-CeTe/commit/8d87183) | docs: reconcile CeTe AV2 backlog, evidence and presentation | — | 29/10/2026 |
| CeTe-Api | `main` | [`5c38d2b`](https://github.com/Nexxus-ops/CeTe-Api/commit/5c38d2b) | refactor(domain): organize existing models by bounded context | — | 12/11/2026 |
| CeTe-Api | `main` | [`f8f2eb3`](https://github.com/Nexxus-ops/CeTe-Api/commit/f8f2eb3) | refactor(inventory): encapsulate stock rules and expose context contracts | — | 12/11/2026 |
| CeTe-Api | `main` | [`f1b4799`](https://github.com/Nexxus-ops/CeTe-Api/commit/f1b4799) | refactor(receipts): isolate historical receipt queries and snapshots | — | 12/11/2026 |
| CeTe-Api | `main` | [`bc369f5`](https://github.com/Nexxus-ops/CeTe-Api/commit/bc369f5) | refactor(sales): separate checkout commands and sales persistence | — | 12/11/2026 |
| CeTe-Api | `main` | [`84f14c7`](https://github.com/Nexxus-ops/CeTe-Api/commit/84f14c7) | refactor(logistics): isolate dispatch lifecycle and sales integration | — | 12/11/2026 |
| CeTe-Api | `main` | [`00c1ec3`](https://github.com/Nexxus-ops/CeTe-Api/commit/00c1ec3) | refactor(procurement): separate purchase and receiving use cases | — | 12/11/2026 |
| CeTe-Api | `main` | [`2930433`](https://github.com/Nexxus-ops/CeTe-Api/commit/2930433) | refactor(identity): isolate account services and credential adapters | — | 12/11/2026 |
| CeTe-Api | `main` | [`b5a6ad6`](https://github.com/Nexxus-ops/CeTe-Api/commit/b5a6ad6) | refactor(integrations): move exchange rate endpoint to REST adapter | — | 12/11/2026 |
| CeTe-Api | `main` | [`dc266f9`](https://github.com/Nexxus-ops/CeTe-Api/commit/dc266f9) | refactor(shared): integrate context boundaries and compatibility checks | — | 12/11/2026 |
| FrontEnd-CeTe | `main` | [`9cc78f6`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/9cc78f6) | fix(web): complete application metadata | — | 10/11/2026 |
| FrontEnd-CeTe | `main` | [`f7449ac`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/f7449ac) | fix(web): integrate metadata and preserve title during navigation | — | 12/11/2026 |
| nexxus-landing-page | `develop` | [`b5bb09e`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/b5bb09e) | feat: add audience-specific landing CTAs | — | 11/11/2026 |
| nexxus-landing-page | `develop` | [`6495243`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/6495243) | feat(landing): integrate audience-specific access paths | — | 12/11/2026 |
| FrontEnd-CeTe | `main` | [`65889d8`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/65889d8) | fix(sales): improve checkout layout and mobile receipt readability | — | 12/11/2026 |

Las integraciones de frontend y landing fueron incorporadas mediante [PR #4 de FrontEnd-CeTe](https://github.com/Nexxus-ops/FrontEnd-CeTe/pull/4) y [PR #3 de la landing](https://github.com/Nexxus-ops/nexxus-landing-page/pull/3). Liz figura como autora de la integración; se conservaron los commits originales de Kevin y Darikson. El frontend conserva el título y los metadatos al navegar, y la landing distingue el acceso de dueños y operarios en ambos idiomas.

La recepción parcial ejecuta `PurchaseOrder.Receive`, registra su evidencia y solicita el ingreso mediante `IInventoryFacade`, dentro de la transacción de `IUnitOfWork`. [Código versionado](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/Procurement/Application/Internal/CommandServices/ProcurementCommandService.cs)

![Extracto versionado de ProcurementCommandService.Receive](AV2/evidence/api-receive-source.png)

El contrato de Inventario entrega instantáneas y concentra los ajustes de saldo solicitados por otros contextos. La captura siguiente reproduce el [contrato de la versión publicada](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/Inventory/Application/Services/IInventoryFacade.cs).

![Contrato IInventoryFacade entre bounded contexts](AV2/evidence/api-inventory-contract.png)

#### 5.2.3.5. Execution Evidence for Sprint Review

Las siguientes capturas corresponden a ejecución pública con datos ficticios en Render. Presentan el producto y su resultado; la evidencia de participación y validación con usuarios se registra en sus secciones específicas.

La revalidación del **12/11/2026** comprobó la API refactorizada mediante compilación, pruebas de dominio, suite HTTP con PostgreSQL y el recorrido completo desde el frontend publicado. Las capturas de dashboard, compras y boleta se renovaron durante esa ejecución. La prueba de continuidad recuperó, después del despliegue, una sesión y una boleta creadas previamente; reenviar la venta con el mismo UUID no volvió a descontar stock. `/health` respondió HTTP 200 con estado `healthy`. El endpoint conserva `version: 0.2.0`; el commit publicado en [5.1.4](#514-software-deployment-configuration) identifica la revisión del código.

**E1 · Dashboard operativo**

![Dashboard AV2 con indicadores de operación](AV2/evidence/dashboard-desktop.png)

*Resumen de ventas y existencias de la empresa autenticada.*

**E2 · Compras y recepción parcial**

![Compra y recepción parcial AV2](AV2/evidence/purchases-desktop.png)

*La orden conserva cantidades pedidas y recibidas; el stock aumenta al recibir físicamente.*

**E3 · Boleta de compra en escritorio**

![Boleta AV2 con cabecera y detalle](AV2/evidence/receipt-desktop.png)

*Empresa, orden, fecha/hora, lugar, responsable, artículos, cantidades, precios y total.*

<details>
<summary>Ver boleta en pantalla móvil y documento de impresión</summary>

<p align="center"><img src="AV2/evidence/receipt-mobile.png" width="300" alt="Boleta AV2 en móvil de 390 píxeles"></p>

![Documento de la boleta para impresión](AV2/evidence/receipt-document.png)

</details>

**E4 · Landing bilingüe**

![Landing AV2 con propuesta y acceso al producto](AV2/evidence/landing-desktop.png)

*Propuesta comercial, captura del producto y navegación a recursos funcionales.*

| Grupo de pruebas | Resultado registrado | Evidencia |
| :--- | :--- | :--- |
| Dominio y API | Aprobado: stock, tenant, permisos, recepción parcial, rollback, idempotencia, boleta histórica, anulación, revocación, concurrencia y despacho. | [Pruebas HTTP](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/tests/api_smoke.py) · [Comprobaciones de dominio](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/tests/Domain/Program.cs). |
| Integración externa | Consulta informativa USD/PEN aprobada; no modifica la moneda de las ventas. | [Adaptador cambiario](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/Integrations/Interfaces/REST/ExchangeRatesController.cs) y caso incluido en las pruebas HTTP. |
| Navegador | Recorrido local y público, POS por teclado, boleta, impresión, idiomas, recarga y móvil de 390 px aprobados. | [Pruebas reproducibles](https://github.com/Nexxus-ops/FrontEnd-CeTe/blob/a1e594fc0f6b3d6d8bc8376955c36c9000cc4179/tests/browser/full-flow.cjs). |
| Landing | Dos idiomas persistentes, cuatro recursos del footer, anclas, captura, menú móvil y CTA por segmento aprobados. | [Captura del producto](AV2/evidence/landing-desktop.png) · [Landing publicada](https://cete-landing-av2.onrender.com/). |

La comprobación adicional del 12/11/2026 sobre las integraciones publicadas verificó las etiquetas y destinos de los CTA en `en_US` y `es_419`, navegación por teclado, persistencia de idioma, los cuatro recursos del footer, menú móvil y ausencia de desbordamiento a 390 px. Se comprobó el título del frontend al pasar entre acceso y registro. Se repitió el recorrido desde la landing de Render y la publicación de GitHub Pages.

Las pruebas utilizan empresas y datos ficticios. Acreditan los casos registrados; no equivalen a una auditoría integral de accesibilidad, rendimiento o preparación para producción. El build del frontend informa un bundle principal mayor de 500 kB, pendiente de optimización. El cliente espera hasta 90 s al iniciar la API Free; conviene comprobar Swagger antes de la sustentación. Las instrucciones para reproducir las pruebas están en el [README de la API](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/README.md).

#### 5.2.3.6. Services Documentation Evidence for Sprint Review

El flujo integrado de AV2 se documenta en [Swagger](https://cete-api-av2.onrender.com/swagger) y en el [contrato OpenAPI](https://cete-api-av2.onrender.com/swagger/v1/swagger.json). Los endpoints de la tabla requieren token Bearer y los permisos del contexto. Los ejemplos son extractos ilustrativos de las respuestas.

| Método y ruta | Datos de entrada | Respuesta de ejemplo |
| :--- | :--- | :--- |
| `POST /api/v1/purchases` | `supplierName`, `productId` (UUID), `quantity`, `unitCost` y `warehouseId` opcional. | `200 {"status":"ORDERED"}` — crea la orden sin mover stock. |
| `POST /api/v1/purchases/{id}/receive` | `id` de la orden y cuerpo `{"quantity":2}`. | `200 {"status":"PARTIAL"}` — conserva saldo pendiente cuando aún faltan unidades. |
| `POST /api/v1/sales` | `id` de idempotencia, `customerName`, `items` con `inventoryItemId` y `quantity`, `paymentMethod` y `warehouseId` opcional. | `200 {"status":"COMPLETED","totalAmount":290}` — confirma la venta y registra el pago académico. |
| `GET /api/v1/sales/{id}/receipt` | `id` de la venta en la ruta. | `200 {"currency":"PEN","total":290,"documentType":"DEMONSTRATION_RECEIPT"}` — además devuelve el detalle histórico. |
| `POST /api/v1/dispatches` | `driverName`, `licensePlate` y `saleIds` como lista de UUID. | `200 {"status":"PENDING"}` — asigna ventas elegibles sin descontar nuevamente el stock. |

La captura de Swagger en [5.1.4](#514-software-deployment-configuration) muestra los servicios publicados. El commit [`4df092e`](https://github.com/Nexxus-ops/CeTe-Api/commit/4df092e49cef5033476add1c7b2caf410d35eac9) integra los controladores, recursos y resultados tipados sin cambiar las rutas consumidas por el frontend. La [boleta del recorrido de prueba](AV2/evidence/receipt-document.png) muestra el resultado del contrato de consulta desde la aplicación.

#### 5.2.3.7. Software Deployment Evidence for Sprint Review

Docker Compose ejecuta API y PostgreSQL localmente. El mismo Dockerfile se publica en Render. La API, frontend y landing están publicados en Render. El recorrido público verifica registro, acceso, compra, recepción parcial, venta, selección por teclado, boleta, impresión y persistencia de idioma. Ver [resultados de ejecución](#5235-execution-evidence-for-sprint-review) y [commits del incremento](#5234-development-evidence-for-sprint-review). La base Free tiene vencimiento registrado para el **28/11/2026 a las 22:30, hora de Lima** (29/11/2026 a las 03:30 UTC).

| Producto | Rama y commit publicado | Fecha/hora de publicación (Lima) | Acceso |
| :--- | :--- | :--- | :--- |
| API | `main` · [`4df092e`](https://github.com/Nexxus-ops/CeTe-Api/commit/4df092e49cef5033476add1c7b2caf410d35eac9) | 12/11/2026 · 11:35 | [Swagger](https://cete-api-av2.onrender.com/swagger) |
| Frontend | `main` · [`ce72e6a`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/ce72e6a0c95f10a469232f4baeab1d0109405c95) | 12/11/2026 · 19:19 | [Aplicación](https://cete-web-av2.onrender.com/) |
| Landing | `develop` · [`389ac46`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/389ac468182c5967406d22f48c4a7ff8b31201dc) | 12/11/2026 · 14:43 | [Landing](https://cete-landing-av2.onrender.com/) |

**Respaldo comprobado.** El 12/11/2026 se exportó la base pública con `pg_dump` 17 en formato custom y TLS con verificación del servidor. El archivo se restauró con `pg_restore --exit-on-error` en un PostgreSQL 17 aislado: se recuperaron las 35 tablas y 67 claves foráneas, además de ventas, boletas y sesiones. La autorización de red externa se retiró al finalizar. El respaldo y su manifiesto SHA-256 se conservan de forma privada fuera de Git. Esta prueba acredita recuperación al momento de la copia; siguen pendientes una periodicidad de respaldo y la continuidad del servicio antes del vencimiento Free.

#### 5.2.3.8. Team Collaboration Insights during Sprint

Los cinco integrantes aportaron al incremento mediante diseño, implementación, integración o revisión técnica, según el reparto informado por Kevin. La [matriz LACX](#5232-aspect-leaders-and-collaborators) relaciona aspectos, líderes y colaboradores. Las [analíticas de colaboración](README.md#analíticas-verificadas-de-colaboración-av2) fijan las revisiones examinadas, los recuentos y las capturas de los cuatro repositorios. El [cuadro ABET 5](README.md#abet---eac---student-outcome-5) relaciona las acciones de cada integrante con ambos criterios del outcome.

| Observación / necesidad | Colaboración y decisión aplicada | Resultado verificable |
| :--- | :--- | :--- |
| Consolidar DDD en el backend | Piero aporta estructura e Inventario; Darikson, Ventas y Logística; Liz, consulta histórica de boletas; Kevin, Abastecimiento, Identidad e integración; Diego, revisión e integración transversal. | [API PR #2](https://github.com/Nexxus-ops/CeTe-Api/pull/2): cinco contextos, repositorios y servicios por módulo, manteniendo las 28 operaciones HTTP. |
| Corregir acceso y recorrido desde la landing | Darikson aporta CTA para dueños y operarios, Liz integra el cambio y Kevin publica la versión. Se conserva la autoría de cada registro. | [Landing PR #3](https://github.com/Nexxus-ops/nexxus-landing-page/pull/3): destinos reales, ambos idiomas, teclado y móvil comprobados. |
| Mejorar boleta y claridad de la interfaz | El equipo incorpora el flujo de boleta propuesto por Liz, los aportes de Ventas y la integración del frontend. Kevin consolida la mejora de lectura y controles tras priorizar los comentarios de UI/UX. | [Frontend PR #5](https://github.com/Nexxus-ops/FrontEnd-CeTe/pull/5): carrito adaptable, acción visible de boleta y detalle móvil legible, conservando la impresión. Build y recorrido con API local aprobados; nueva versión publicada en Render. |
| Dar trazabilidad a la participación | La documentación distingue diseño, implementación, revisión e integración. No se altera el historial para igualar contadores. | En frontend constan Kevin y Diego como autores de commits sin merge y Liz como autora de la integración [`f7449ac`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/f7449ac), que incluye un ajuste de navegación. Las gráficas de GitHub excluyen los merges. Los aportes informados de Piero y Darikson requieren sus artefactos o testimonios individuales. |
| Contrastar el producto con usuarios | Diego entrega las entrevistas de Raúl y Carmen; Piero entrega las de Nicol y Jaime con fichas, capturas y enlaces. Las recomendaciones se registran antes de decidir las siguientes mejoras. | [Entrevistas incorporadas](#532-registro-de-entrevistas). Las seis fichas recibidas conforman la ronda entregada de AV2; la ampliación de la muestra y la revalidación se programan para TF. |

**Lectura del resultado.** Las integraciones publicadas y la evidencia enlazada permiten seguir la colaboración entre aspectos del producto. No acreditan automáticamente que todos hayan trabajado el mismo número de horas o en todos los archivos. La tarea documental de colaboración queda consolidada con los aportes y las evidencias disponibles. Los testimonios están en montaje y el performance corresponde a la evaluación del líder. No se atribuyen horarios, asistencia ni declaraciones personales que no constan en las fuentes.

## 5.3. Validation Interviews

> **Ronda de validación entregada en AV2.** Se conservan dos entrevistas históricas y se incorporan las de Raúl y Carmen, realizadas por Diego Campoblanco, y las de Nicol y Jaime, aportadas por Piero Montes. Hay seis fichas en total; la cobertura de la ronda actual se desglosa al final de 5.3.2. Se cierra la incorporación de las seis fichas disponibles y se conserva su procedencia y alcance. La ampliación de la muestra y la medición comparativa de los indicadores se programan para TF; los enlaces consolidados y los tiempos de edición se completarán con las publicaciones audiovisuales.

### 5.3.1. Diseño de entrevistas

Para el proceso de validación, hemos diseñado sesiones interactivas donde los usuarios evalúan nuestros productos digitales de CeTe, basándonos en escenarios reales de uso.
El protocolo utiliza la landing y la aplicación desplegadas para **ambos segmentos**, según los permisos de cada rol. Las mediciones comparativas y la ampliación de la muestra continúan en TF. Las dos entrevistas históricas conservan las condiciones en que se realizaron, incluida la evaluación de Figma por Luis; no se reclasifican como pruebas de la aplicación AV2.

| Segmento | Tareas en la landing | Tareas en la aplicación | Registro esperado |
| :--- | :--- | :--- | :--- |
| Dueños y administradores | Explicar la propuesta, localizar la propuesta comercial, cambiar idioma e ingresar por el acceso del segmento. | Interpretar las métricas, registrar una venta con datos ficticios, consultar su boleta académica y ubicar el despacho relacionado. | Éxito sin ayuda, tiempo, errores, comprensión y comentarios espontáneos. |
| Operarios de almacén y logística | Identificar para quién sirve CeTe, cambiar idioma y localizar el acceso de operarios. | Buscar un producto, distinguir orden de compra de recepción, recibir parcialmente y consultar el saldo y los movimientos; revisar un despacho si el rol lo permite. | Éxito sin ayuda, tiempo, errores y comprensión de las cantidades recibidas y pendientes. |

Las tareas se realizarán sin guiar al participante hacia la respuesta. Los hallazgos se registrarán con captura, severidad, heurística y recomendación según el Anexo D, distinguiendo propuestas de funcionalidades ya implementadas.

### 5.3.2. Registro de Entrevistas

**Entrevista de Validación 1 (Segmento 1 - Dueño/Administrador)**
* **Nombre:** Jesús V.C.
* **Edad:** 28 años
* **Distrito:** San Miguel
* **URL del Video:** [Ver entrevista (OneDrive)](https://1drv.ms/v/c/e88873f5d7dca6f3/IQBGbGRWY2rUQ538hXef1EzLAdgfob7Mw59Zjm2DJZ55iCg?e=hPPCtx)
<p align="center">
  <img src="jesusentrevistas.png" width="400" alt="Captura Entrevista Jesús">
</p>

* **Resumen de la evaluación:**
  El usuario interactuó con la Landing Page. Comprendió rápidamente que el sistema centraliza inventario, ventas y facturación. Destacó como funcionalidades más valiosas el "Balance Inteligente" (para cruzar compras y ventas) y el "Monitoreo y Alertas" (para evitar quiebres de stock). Se identificó plenamente con el dolor de no poder estar físicamente en el local todo el día, validando la necesidad del Dashboard. Como sugerencias críticas, indicó que la página carece de una sección explícita de precios o planes y recomendó fuertemente implementar un botón flotante de WhatsApp para consultas rápidas.

**Entrevista de Validación 2 (Segmento 2 - Operario de Almacén)**
* **Nombre:** Luis Llanos
* **Edad:** 28 años
* **Distrito:** Santiago de Surco
* **URL del Video:** [Ver entrevista (OneDrive)](https://1drv.ms/v/c/e88873f5d7dca6f3/IQBrUEoZT2CBRJ2rlCxRdA_zAfMIUn-hNsRdc9TrtVkJP1k?e=bM1yV4)
<p align="center">
  <img src="guillermoentrevista.png" width="400" alt="Captura Entrevista Luis">
</p>

* **Resumen de la evaluación:**
  El usuario interactuó con los mockups de alta fidelidad en Figma. Identificó intuitivamente el menú lateral para la "Gestión de Inventario" y el botón para "Registrar Entrada". Al evaluar el formulario de ingreso, sugirió implementar una función para escanear códigos de barras con la cámara del celular, a fin de agilizar el proceso y evitar errores de tipeo. Al analizar la pantalla de alertas, observó que falta un flujo o botón específico para registrar "Mermas" o productos dañados, lo cual es crítico para no alterar los reportes.

#### Entrevistas de validación aportadas por Diego Campoblanco

Diego Campoblanco realizó las dos entrevistas y elaboró los siguientes resúmenes. Las grabaciones corresponden al segmento de dueños y administradores. Los enlaces conservan el destino de Google Drive entregado por el entrevistador.

**Entrevista de Validación 3 (Segmento 1 - Dueño/Administrador)**

* **Nombre:** Raúl
* **Edad:** 48 años
* **Distrito:** San Juan de Lurigancho
* **URL del Video:** [Ver entrevista en Google Drive](https://drive.google.com/file/d/1Gbca9G1cy2FEQeqxRSqb1tDTqoGmf4Eq/view?usp=sharing)
<p align="center">
  <img src="Images/Validation/raul-av2.png" width="600" alt="Captura de la entrevista de validación a Raúl">
</p>

* **Resumen de la evaluación:** El usuario interactuó con la Landing Page y la plataforma de prueba. Comprendió rápidamente que el sistema busca centralizar el control del almacén y la caja, reemplazando su actual método con cuadernos. Destacó como muy valiosa la visualización directa de las ventas del día ("Revenue today") en la pantalla de inicio. Sin embargo, encontró confusa y abrumadora la navegación por el menú lateral para ver detalles de boletas o registrar ingresos manuales. Como sugerencias críticas, enfatizó la necesidad de recibir notificaciones y alertas automáticas directas sobre pedidos incompletos, y recalcó que el sistema debe estar pensado para un uso cien por ciento móvil, ya que él opera exclusivamente desde su celular.

---

**Entrevista de Validación 4 (Segmento 1 - Dueña/Administradora)**

* **Nombre:** Carmen
* **Edad:** 52 años
* **Distrito:** Los Olivos
* **URL del Video:** [Ver entrevista en Google Drive](https://drive.google.com/file/d/1wLylfhxjysJQac-Uy6r0eAj5kVPu48L1/view?usp=sharing)
<p align="center">
  <img src="Images/Validation/carmen-av2.png" width="600" alt="Captura de la entrevista de validación a Carmen">
</p>

* **Resumen de la evaluación:** La usuaria interactuó con la Landing Page y valoró positivamente la propuesta de unificar compras y ventas, especialmente para monitorear el negocio a distancia. Destacó el Dashboard por su facilidad para visualizar los ingresos diarios al instante. No obstante, mostró frustración con el flujo de registro de mercancías por ser manual y basado en texto, recordando las razones por las que abandonó Excel. Como sugerencias críticas, exigió la integración de una función para escanear códigos de barras usando la cámara del celular, la necesidad imperativa de un campo para rastrear fechas de vencimiento, y la implementación de alertas visuales automáticas para productos pendientes o a punto de quebrar stock.

#### Entrevistas de validación aportadas por Piero Montes

Piero Montes entregó las fichas, enlaces y capturas de las siguientes entrevistas. La entrevista de Nicol corresponde al segmento de dueños y administradores; la de Jaime, al de operarios. Los resúmenes se incorporan como material del entrevistador. Se comprobaron los títulos y las duraciones de los videos, sin atribuirles una evaluación independiente del contenido completo.

**Entrevista de Validación 5 (Segmento 1 - Dueña/Administradora)**

* **Nombre:** Nicol Loyola
* **Edad:** 34 años
* **Distrito:** Santiago de Surco
* **Fecha de realización:** 07/11/2026, confirmada por Kevin al incorporar la ficha.
* **Entrevistador y autor del resumen:** Piero Montes.
* **URL del video:** [Ver entrevista en YouTube](https://youtu.be/b9s07-VS1xE).
* **Duración del archivo individual:** `00:05:27`, comprobada en el reproductor el 12/11/2026.
* **Referencia temporal:** archivo individual desde `00:00:00`; inicio en el video consolidado de validaciones pendiente de registrar.
* **Microsoft Stream:** enlace pendiente de incorporar.

<p align="center">
  <img src="Images/Validation/nicol-av2.jpeg" width="820" alt="Captura aportada por Piero de la entrevista de validación a Nicol Loyola con la aplicación CeTe">
</p>

* **Resumen de la evaluación (aportado por Piero):** La usuaria interactuó con la Landing Page y la plataforma de prueba asumiendo el rol de dueña de negocio. Comprendió de inmediato el valor de la herramienta para centralizar el control de stock, compras y ventas, destacando que le permitiría dejar de usar hojas de Excel y sumar todo automáticamente en tiempo real. Valoró mucho encontrar el resumen de "Ventas del día" apenas ingresó al Dashboard. Sin embargo, al realizar la tarea de buscar el detalle de una boleta, presentó una leve confusión intuitiva: intentó hacer clic sobre la fila entera de la venta en lugar de usar el botón específico de "Ver detalle / Comprobante" a la derecha. Como sugerencias críticas, mencionó la necesidad de visualizar de forma más grande y clara el método de pago utilizado (Yape, tarjeta, efectivo) y el estado de envío del comprobante. Además, recomendó fuertemente que el cuadro de "Ventas del día" en el inicio sea cliqueable, para que la dirija directamente a las boletas de la fecha sin necesidad de navegar a través del menú lateral.

---

**Entrevista de Validación 6 (Segmento 2 - Operario de Almacén)**

* **Nombre:** Jaime Ronceros
* **Edad:** 29 años
* **Distrito:** Callao
* **Fecha de realización:** 11/11/2026, confirmada por Kevin al incorporar la ficha.
* **Entrevistador y autor del resumen:** Piero Montes.
* **URL del video:** [Ver entrevista en YouTube](https://youtu.be/9EMUt0QUeOk).
* **Duración del archivo individual:** `00:05:43`, comprobada en el reproductor el 12/11/2026.
* **Referencia temporal:** archivo individual desde `00:00:00`; inicio en el video consolidado de validaciones pendiente de registrar.
* **Microsoft Stream:** enlace pendiente de incorporar.

<p align="center">
  <img src="Images/Validation/jaime-av2.jpeg" width="820" alt="Captura aportada por Piero de la entrevista de validación a Jaime Ronceros con la aplicación CeTe">
</p>

* **Resumen de la evaluación (aportado por Piero):** El usuario interactuó con la Landing Page y la plataforma de prueba asumiendo el rol de operario de almacén. Comprendió rápidamente que el sistema está enfocado en organizar la parte operativa, controlando entradas, salidas y órdenes de compra. Durante la tarea de registrar una recepción parcial de mercadería (llegaron 4 de 10 unidades), presentó una leve confusión en la navegación inicial: se dirigió primero a la pestaña de "Inventario" intentando sumar los productos de forma directa, hasta darse cuenta de que debía ir a "Compras" para descontar desde el pedido original al proveedor. Valoró mucho que el sistema actualice los saldos pendientes al instante, ya que esto le evitaría tener que marcar guías físicas y avisar por WhatsApp a otras áreas. Como sugerencias críticas, señaló que hace falta un mensaje de alerta visible tras guardar que confirme el nuevo stock total ("El stock subió de X a Y"), para no tener que ir a verificarlo al inventario. Además, recomendó implementar un botón de acceso directo en el inicio que diga "Recibir mercadería pendiente" para agilizar la recepción cuando el proveedor ya está en la puerta.

Las cuatro primeras fichas conservan pendientes sus fechas, marcas de tiempo, duración y enlaces a Microsoft Stream. Las fichas 5 y 6 incorporan las fechas confirmadas y la duración de cada archivo individual; el video consolidado en Stream y sus marcas de inicio siguen pendientes. Los resúmenes recogen apreciaciones de los entrevistados, no métricas de efectividad medidas por el equipo.

#### 5.3.2.1. Cobertura de la ronda de validación

| Segmento | Registro histórico | Nuevas entrevistas AV2 recibidas | Resultado del corte y continuidad |
| :--- | :--- | :--- | :--- |
| Dueños y administradores | Jesús: evaluación histórica de la landing. | Raúl, Carmen y Nicol. | Tres fichas nuevas incorporadas al cierre AV2. La observación de uso y los metadatos audiovisuales se conservan con el alcance de cada ficha. |
| Operarios de almacén | Luis: evaluación histórica de mockups en Figma. | Jaime: evaluación de la plataforma de prueba, incluida recepción parcial. | Una ficha nueva sobre la plataforma. Ampliar la muestra operativa con al menos dos participantes adicionales en TF para contrastar los hallazgos sobre la aplicación. |

El total acumulado es de **cuatro dueños/administradores y dos operarios**. No se suma la prueba histórica de Figma a la muestra de uso de la aplicación AV2. Las duraciones de los videos no son tiempos de ejecución de tareas ni permiten calcular los indicadores G1–G3. Los enlaces individuales de YouTube tampoco sustituyen el consolidado en Microsoft Stream y sus marcas de inicio.

### 5.3.3. Evaluaciones según heurísticas

La evaluación distingue los hallazgos históricos de las nuevas fichas. Los principios de usabilidad se contrastan con las [heurísticas de Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/). Las severidades nuevas son una valoración de revisión documental, no una puntuación dada por los participantes ni un resultado de revalidación.

#### 5.3.3.1. Registro histórico de hallazgos

La tabla siguiente conserva lo registrado en la entrega anterior. Su descripción corresponde a la versión evaluada entonces; no prueba que cada problema persista en la versión publicada actualmente.

| # | Problema | Escala de severidad | Heurística / Principio violado |
| :---: | :--- | :---: | :--- |
| 1 | La Landing Page no cuenta con una sección explícita de "Precios" o "Planes", lo que frena la decisión de registro del usuario y genera incertidumbre. | 3 (Problema mayor) | Arquitectura de la Información / Coincidencia entre el sistema y el mundo real. |
| 2 | Ausencia de un canal de contacto rápido (botón de WhatsApp o soporte flotante) para resolver dudas antes de crear la cuenta B2B. | 2 (Problema menor) | Usabilidad: Ayuda y documentación. |
| 3 | El formulario de ingreso de mercadería requiere tipear el SKU a mano, lo que aumenta el riesgo de error humano y demora el proceso. | 3 (Problema mayor) | Usabilidad: Flexibilidad y eficiencia de uso. |
| 4 | No existe un botón o flujo específico y claro para registrar productos dañados (Mermas) desde la vista del operario. | 3 (Problema mayor) | Usabilidad: Prevención de errores. |

#### 5.3.3.2. Evaluación de las entrevistas 5 y 6

**UX Heuristics & Principles Evaluation · Usability – Inclusive Design – Information Architecture**

| Campo | Registro |
| :--- | :--- |
| Carrera / curso / sección | Ingeniería de Software · Aplicaciones Web · NRC 8168. |
| Docente | Humberto Alex Sánchez Ponce. |
| Grupo auditor | Nexxus. Entrevistas y resúmenes: Piero Montes. Integración de la evaluación documental: Kevin Salazar. |
| Participantes | Nicol Loyola, 07/11/2026; Jaime Ronceros, 11/11/2026. |
| Sitios evaluados según las fichas | Landing CeTe y plataforma de prueba. Las fichas no identifican la revisión exacta desplegada durante la sesión. |
| Fecha de integración de hallazgos | 12/11/2026. |

**Tareas incluidas:** comprender la propuesta; interpretar las ventas del día; localizar el detalle de una venta y su boleta; registrar una recepción parcial de cuatro de diez unidades y consultar el saldo pendiente. El registro identifica dificultades de navegación y solicitudes de mejora. No incluye medición comparativa de tiempos, auditoría integral de accesibilidad, emisión fiscal, cobro real ni una función terminada de envío de comprobantes.

**Escala de severidad del Anexo D:**

| Nivel | Criterio aplicado |
| :---: | :--- |
| 1 | Dificultad superficial o fácilmente superable; mejora de baja urgencia. |
| 2 | Dificultad menor que añade esfuerzo, pero permite continuar. |
| 3 | Problema mayor que se repite o dificulta resolver la tarea; prioridad alta. |
| 4 | Problema crítico que impide continuar; corregir antes de publicar. |

**Tabla resumen de nuevos hallazgos:**

| # | Problema o mejora identificada | Severidad propuesta | Heurística / principio | Ficha y trazabilidad |
| :---: | :--- | :---: | :--- | :--- |
| 5 | Abrir una boleta desde la fila de venta. | 2 | Usabilidad: consistencia y estándares; reconocimiento antes que recuerdo. | Nicol · US17, US39. |
| 6 | Jerarquía del método de pago y expectativa de envío. | 2 | Usabilidad: visibilidad del estado del sistema. | Nicol · US39. |
| 7 | Acceso desde Ventas del día al historial. | 1 | Usabilidad: flexibilidad y eficiencia de uso. | Nicol · US23, US17. |
| 8 | Ubicación de la recepción parcial de una compra. | 2 | Usabilidad: correspondencia con el mundo real; reconocimiento antes que recuerdo. | Jaime · US41. |
| 9 | Confirmación del saldo tras recibir mercancía. | 2 | Usabilidad: visibilidad del estado del sistema. | Jaime · US41. |
| 10 | Acceso directo a recepciones pendientes. | 1 | Usabilidad: flexibilidad y eficiencia de uso. | Jaime · US41. |

**Descripción y recomendaciones:**

Las capturas aportadas por Piero se incluyen en las fichas 5 y 6. Son capturas contextuales: la de Nicol muestra el registro y la de Jaime una vista de movimientos. No muestran todos los momentos descritos en los resúmenes. Falta seleccionar el fotograma y la marca de tiempo de cada incidencia para completar su evidencia específica conforme al Anexo D. No se asigna un resultado cuantitativo de diseño inclusivo a partir de estas imágenes.

**PROBLEMA #5: Abrir una boleta desde la fila de venta**

* **Severidad propuesta:** 2. **Principio:** Consistencia y estándares; reconocimiento antes que recuerdo.
* **Descripción:** Nicol intentó seleccionar la fila completa de una venta en lugar del control específico de detalle. La ficha describe una confusión leve, no un bloqueo del flujo.
* **Captura disponible:** [contexto de la entrevista de Nicol](Images/Validation/nicol-av2.jpeg); fotograma específico y marca de tiempo por registrar.
* **Recomendación:** Hacer evidente la acción de consultar la boleta; evaluar un enlace en el identificador o una fila accesible por teclado. Mantener la consulta de Sales sin repetir la confirmación de la venta.
* **Estado de cierre AV2:** hallazgo documentado. La priorización, implementación y revalidación de esta mejora se programan para TF.

**PROBLEMA #6: Jerarquía del método de pago y expectativa de envío**

* **Severidad propuesta:** 2. **Principio:** Visibilidad del estado del sistema.
* **Descripción:** Nicol solicitó ver con mayor claridad el método de pago registrado y conocer el estado de envío del comprobante. La solicitud no demuestra que exista una función de envío.
* **Captura disponible:** [contexto de la entrevista de Nicol](Images/Validation/nicol-av2.jpeg); fotograma específico y marca de tiempo por registrar.
* **Recomendación:** Destacar el método realmente registrado. Diferenciar el estado de la venta de una eventual entrega del comprobante; no mostrar un estado de envío ficticio. Definir el envío como alcance futuro si el equipo lo prioriza.
* **Estado de cierre AV2:** hallazgo documentado. La priorización, implementación y revalidación de esta mejora se programan para TF.

**PROBLEMA #7: Acceso desde Ventas del día al historial**

* **Severidad propuesta:** 1. **Principio:** Flexibilidad y eficiencia de uso.
* **Descripción:** Nicol propuso que la tarjeta de ventas del día conduzca al historial de esa fecha, evitando una navegación adicional por el menú. Se registra como oportunidad de eficiencia, no como una tarea imposible de realizar.
* **Captura disponible:** [contexto de la entrevista de Nicol](Images/Validation/nicol-av2.jpeg); fotograma específico y marca de tiempo por registrar.
* **Recomendación:** Evaluar un enlace accesible con el filtro del día y respetar los permisos del usuario. Contrastar el criterio de fechas de US17 antes de considerarlo implementado.
* **Estado de cierre AV2:** hallazgo documentado. La priorización, implementación y revalidación de esta mejora se programan para TF.

**PROBLEMA #8: Ubicación de la recepción parcial de una compra**

* **Severidad propuesta:** 2. **Principio:** Correspondencia con el mundo real; reconocimiento antes que recuerdo.
* **Descripción:** En el caso de recibir cuatro de diez unidades, Jaime buscó primero la acción en Inventario y después identificó Compras como el lugar de recepción del pedido. La ficha describe recuperación de la navegación.
* **Captura disponible:** [contexto de la entrevista de Jaime](Images/Validation/jaime-av2.jpeg); fotograma específico y marca de tiempo por registrar.
* **Recomendación:** Usar una etiqueta clara como Recibir compra y una ayuda contextual que conecte la orden con su recepción. Procurement debe registrar la recepción y coordinar el saldo con Inventory; no sumar stock desde un atajo que omita la orden.
* **Estado de cierre AV2:** hallazgo documentado. La priorización, implementación y revalidación de esta mejora se programan para TF.

**PROBLEMA #9: Confirmación del saldo tras recibir mercancía**

* **Severidad propuesta:** 2. **Principio:** Visibilidad del estado del sistema.
* **Descripción:** Jaime solicitó una confirmación visible del stock resultante después de guardar una recepción, para evitar consultar Inventario solo para comprobar el efecto.
* **Captura disponible:** [contexto de la entrevista de Jaime](Images/Validation/jaime-av2.jpeg); fotograma específico y marca de tiempo por registrar.
* **Recomendación:** Mostrar una confirmación solo después del éxito de la API, con cantidad recibida, pendiente y saldo confirmado cuando el contrato lo permita. No calcular un éxito ficticio ni repetir la recepción.
* **Estado de cierre AV2:** hallazgo documentado. La priorización, implementación y revalidación de esta mejora se programan para TF.

**PROBLEMA #10: Acceso directo a recepciones pendientes**

* **Severidad propuesta:** 1. **Principio:** Flexibilidad y eficiencia de uso.
* **Descripción:** Jaime sugirió un acceso desde el inicio a la mercancía pendiente de recibir, especialmente cuando el proveedor está esperando. Se trata de una propuesta de acceso rápido.
* **Captura disponible:** [contexto de la entrevista de Jaime](Images/Validation/jaime-av2.jpeg); fotograma específico y marca de tiempo por registrar.
* **Recomendación:** Evaluar un enlace a compras pendientes filtradas, visible para roles autorizados y sin ejecutar automáticamente una recepción. Comprobar que la persona identifica la orden correcta.
* **Estado de cierre AV2:** hallazgo documentado. La priorización, implementación y revalidación de esta mejora se programan para TF.

---

## 5.4. Video About-the-Product

**[Ver About-the-Product AV2 de CeTe en YouTube](https://youtu.be/V49TZ5P5Rsk)**

La versión AV2 presenta el problema de los registros dispersos en la MYPE, el recorrido integrado de CeTe y la propuesta comercial del equipo. El montaje incluye una demostración real del software con datos ficticios y fragmentos auténticos de las entrevistas de Nicol Loyola, del segmento de dueños y administradores, y de Jaime Ronceros, del segmento operativo. Las entrevistas fueron realizadas por Piero Montes.

El video fue editado y publicado el **13/11/2026**, después del corte documental del 12/11. Tiene una duración aproximada de **00:02:20** —139,96 segundos en el MP4— y resolución **1920 × 1080**. Se publica como **no listado**: cualquier persona con el enlace puede verlo. La reproducción se comprobó desde la página del video y YouTube completó su revisión inicial de derechos de autor sin encontrar problemas.

[![About-the-Product de CeTe publicado en YouTube, con título y visibilidad no listada](AV2/evidence/product-video-youtube.jpg)](https://youtu.be/V49TZ5P5Rsk)

*Captura de la reproducción publicada. El título identifica la entrega AV2 y la descripción enlaza al producto, al informe y a las fuentes de las entrevistas.*

### Pauta de contenido del video publicado

Las marcas de inicio corresponden al montaje exportado y se redondean al segundo para facilitar la navegación.

| Inicio aproximado | Sección | Contenido |
| :---: | :--- | :--- |
| `00:00:00` | Problema y presentación | Registros dispersos, público objetivo y propuesta de CeTe. Las escenas ilustrativas están identificadas como generadas con IA. |
| `00:00:16` | Indicadores | Vista real del inicio de la aplicación con una empresa ficticia. |
| `00:00:23` | Compra y recepción parcial | Orden de diez unidades; recepción de cuatro y seis pendientes. El stock cambia al recibir físicamente. |
| `00:00:34` | Venta | Carrito, método de pago registrado y confirmación de dos unidades de café. |
| `00:00:44` | Boleta académica | Detalle histórico de la venta por S/37,00 y acceso al documento. Sin emisión fiscal. |
| `00:00:52` | Despacho | Asignación y seguimiento de la entrega sin descontar nuevamente el inventario. |
| `00:01:00` | Opinión de dueña o administradora | Fragmento de Nicol Loyola; conserva su valoración del registro y la dificultad de adaptación inicial. |
| `00:01:25` | Opinión de operario | Fragmento de Jaime Ronceros; conserva su valoración de los pendientes y la dificultad de digitación de varios productos. |
| `00:01:52` | Modelo comercial | Propuesta académica SaaS B2B de S/80 por empresa al mes; todavía no se cobran suscripciones. |
| `00:02:06` | Invitación | Acceso a la landing y presentación de los flujos conectados. |
| `00:02:15` | Créditos | Identificación de las escenas de IA, la locución sintética, la demostración y las entrevistas reales. |

### Evidencia y alcance de la demostración

![Detalle de la boleta real de demostración incluido en el video](AV2/evidence/product-video-receipt.png)

La grabación utiliza el frontend y la API del proyecto en un entorno local aislado. La empresa, el cliente, el proveedor y las operaciones son ficticios. El caso inicia con veinte unidades de café, recibe cuatro, vende dos y termina con **veintidós unidades**, una boleta de **S/37,00** y el despacho entregado. La secuencia se contrastó con el estado de la API; no se trata de una animación que simula una interfaz ni de una operación comercial real. Esta grabación complementa las evidencias de despliegue público de 5.2.3.5.

Las opiniones proceden de las [entrevistas de validación de Nicol y Jaime](#532-registro-de-entrevistas). Sus fragmentos no se presentan como una garantía de ahorro, adopción o rendimiento medido. La voz narradora es sintética y las escenas de almacén de apertura y cierre son ilustraciones generadas con IA; los créditos y la descripción del video lo indican.

| Evidencia de entrega | Estado actualizado al 13/11/2026 |
| :--- | :--- |
| Montaje AV2 de 1–3 minutos | Editado, exportado y comprobado: aproximadamente 2:20, Full HD, video H.264 y audio AAC. |
| Interacción real y opiniones de ambos segmentos | Incluidas: demostración con datos ficticios y fragmentos reales de Nicol Loyola y Jaime Ronceros. |
| YouTube | Publicado como no listado en [V49TZ5P5Rsk](https://youtu.be/V49TZ5P5Rsk); reproducción comprobada y revisión inicial sin problemas detectados. |
| Microsoft Stream | Publicación pendiente; no se consigna un enlace hasta disponer del archivo publicado. |
| Captura y duración | Captura de YouTube y vista de boleta incorporadas; duración del MP4 verificada. |
| Incrustación en la landing | Pendiente de integración. La publicación en YouTube permite incorporación, pero no acredita que el sitio ya la incluya. |

**Antecedente conservado.** El [promocional introductorio anterior](https://youtu.be/EBS8s4CFWRo), de diez segundos, permanece como recurso histórico. El enlace principal de esta sección corresponde al montaje AV2 completo.

---
