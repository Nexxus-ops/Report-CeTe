# Capítulo V: Product Implementation, Validation & Deployment

[Configuración](#51-software-configuration-management) · [Sprint 1](#521-sprint-1) · [Sprint 2](#522-sprint-2) · [Sprint 3 / AV2](#523-sprint-3--consolidación-av2) · [Validación](#53-validation-interviews)

## 5.1. Software Configuration Management

La Gestión de Configuración de Software (SCM) es la disciplina que permite identificar, controlar, versionar y auditar los distintos componentes de un sistema durante todo su ciclo de vida. Su aplicación asegura la trazabilidad de los cambios realizados sobre el código fuente, la documentación y los artefactos de diseño, reduciendo la probabilidad de errores de integración y facilitando el trabajo colaborativo del equipo.

En el caso de **CeTe**, la solución está compuesta por una Landing Page informativa, una Frontend Web Application y un RESTful API de elaboración interna. Durante el **Sprint 1** se priorizó la implementación, validación y despliegue de la primera versión de la **Landing Page**, desarrollada con HTML5, CSS3 y JavaScript (ES6+), manteniendo un comportamiento 100% responsive y sin dependencias de frameworks externos.

### 5.1.1. Software Development Environment Configuration

A continuación se listan los productos de software utilizados por el equipo, organizados por tipo de actividad del ciclo de vida. Para cada herramienta se indica su propósito dentro de CeTe y la ruta de referencia o descarga.

**1. Project Management**

*Descripción:* La gestión del proyecto permite organizar las actividades necesarias para alcanzar los objetivos del Sprint, asignar responsables, dar seguimiento al avance y mantener la comunicación entre los integrantes del equipo.

**Jira Software / Trello:**
Utilizado para la gestión del Product Backlog, Sprint Backlog y el seguimiento de las User Stories y Technical Stories. ([Atlassian](https://www.atlassian.com/software/jira))
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

**Visual Studio 2022 / JetBrains Rider:**
Entornos de desarrollo integrados (IDE) robustos utilizados para la programación del Backend en C# con .NET 8.
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
ORM y base de datos relacional definidos para almacenar el estado transaccional, inventario y métricas de CeTe.
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
| **Main Branch** (`main`) | Rama base que refleja el estado de producción. Es la rama publicada por GitHub Pages. |
| **Develop Branch** (`develop`) | Rama de integración del equipo. Unifica el código de las funcionalidades en curso. |
| **Feature Branches** (`feature/*`) | Ramas temporales para desarrollar funcionalidades aisladas. <br> **Convención:** `feature/nombre-de-la-funcionalidad` |
| **Release Branches** (`release/*`) | Ramas de estabilización previas al pase a producción. <br> **Convención:** `release/vX.Y.Z` |

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

**Registro de commits del Sprint 1:**

| Repository | Branch | Commit Id | Commit Message | Commited on |
| :--- | :--- | :--- | :--- | :--- |
| cete-landing-page | `feature/hero-section` | `[COMMIT_ID]` | feat: implement hero section with value proposition | `[DD/MM/2026]` |
| cete-landing-page | `feature/plans-section` | `[COMMIT_ID]` | feat: add B2B subscription plans cards | `[DD/MM/2026]` |
| cete-landing-page | `feature/responsive-nav` | `[COMMIT_ID]` | feat: add mobile burger menu and sticky header | `[DD/MM/2026]` |
| cete-landing-page | `main` | `[COMMIT_ID]` | chore: prepare release v1.0.0 and trigger gh-pages | `[DD/MM/2026]` |

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

**Registro de commits del Sprint 1:**

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

Este registro consolida el incremento AV2 y su situación al **12/11/2026**. Integra la reunión informada por el equipo, los cambios versionados y las pruebas realizadas. El calendario se estima a solicitud de Kevin porque el equipo no conserva las fechas exactas; no se presenta como un acta de planificación redactada al inicio del sprint.

| Sprint # | Sprint 3 · AV2 |
| :--- | :--- |
| **Sprint Planning Background** | **Registro de consolidación** |
| Fecha de reunión informada | Martes **03/11/2026**, confirmada por Kevin. |
| Horario y lugar | Pendientes de confirmación. |
| Preparado por | Salazar Marquina, Kevin Junior, el 12/11/2026. |
| Asistentes | Pendiente la confirmación de la lista de asistentes. La matriz siguiente describe al equipo y sus aportes; no sustituye la asistencia a esta sesión. |
| Calendario estimado | **16/10/2026–12/11/2026**, 28 días calendario inclusivos. Se toma como referencia el intervalo de 28 días entre las planificaciones históricas del 08/09 y 06/10 y se fija el corte en la entrega AV2 del 12/11. Es una aproximación pendiente de confirmación, no una duración histórica comprobada. |
| **Sprint 2 Review Summary** | El registro TB1 muestra el frontend integrado con una Fake API. El feedback exige revisar las estimaciones, internacionalización y footer, Technical Stories, modelo de datos, evidencias de ejecución, boleta y participación de al menos tres integrantes en frontend. |
| **Sprint 2 Retrospective Summary** | La revisión del feedback evidencia la necesidad de conectar el flujo completo a una API persistente, contrastar DDD con el código y vincular cada tarea con criterios y pruebas. Es la síntesis documental del feedback recibido; no se atribuyen acuerdos verbales a la reunión del 03/11. |
| Sprint 3 Goal | **Our focus is on** permitir a una MYPE registrar abastecimiento, vender con stock consistente y entregar una boleta consultable, accediendo desde una landing bilingüe. **We believe it delivers** trazabilidad de compras y ventas y menor doble registro para el dueño y el operario. **This will be confirmed when** el recorrido público conserve los datos, rechace stock insuficiente y acceso ajeno, y las validaciones de ambos segmentos documenten resultados y mejoras. |
| Sprint 3 Velocity | **Pendiente de cierre y aceptación por el equipo.** Las pruebas técnicas no permiten asignar automáticamente puntos a historias con criterios incompletos. La velocidad declarada de Sprint 2 fue 24 SP; no se extrapola como resultado de Sprint 3. |
| Sum of Story Points | **60 SP de alcance de referencia** en 16 US: US10, US11, US14, US19–22, US28–29, US34–36 y US39–42. Son las estimaciones existentes del Product Backlog, no un compromiso retrospectivo ni puntos terminados. Las TS no suman puntos adicionales. |
| Capacidad | **94 horas-persona estimadas**, distribuidas en tareas de 4 a 8 h. No existe un registro consolidado de horas efectivamente trabajadas ni disponibilidad individual para contrastar la capacidad. |

**Criterios de aceptación del incremento.** Crear una compra sin incrementar stock; recibir parcialmente y conservar el saldo; vender una sola vez ante reintentos; consultar e imprimir una boleta histórica; aislar empresas y permisos; navegar en ambos idiomas y desde móvil. Los casos técnicos se documentan en 5.2.3.5. La validación con usuarios, los videos y la aceptación de historias parciales mantienen su estado pendiente o en curso.

**Definition of Done de una tarea técnica.** Cambio integrado en la rama de publicación, criterio de la tarea comprobado y evidencia enlazada. Esto no cierra toda una US ni acredita validación de usabilidad. Para el cierre del sprint, el equipo debe aceptar el alcance, registrar la revisión y completar los entregables académicos restantes.

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

![Tablero del Sprint 3: tareas pendientes y en proceso](AV2/evidence/sprint3-board.png)

*Vista izquierda: To Do e In Process, con validaciones, colaboración y comunicación en curso.*

![Tablero del Sprint 3: tareas completadas y en revisión](AV2/evidence/sprint3-review.png)

*Vista derecha: Done y To Review. Las dos capturas corresponden al mismo tablero; las tarjetas detallan el criterio, responsable, estimación y evidencia enlazada.*

| US / TS y título | Task ID | Task Title | Task Description / resultado al corte | Estimation (h) | Assigned To | Status |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| US35/36 · Pago registrado y descuento de stock; TS11/31 | T3-01 | Sales: cierre atómico e idempotencia | Comprobar rollback, reintento y última unidad. Pruebas aprobadas; US35 conserva el límite de pago académico sin pasarela. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/bc369f5). | 8 | Kevin | To Review |
| US39 · Visualizar e imprimir boleta; TS28 | T3-02 | Sales: boleta histórica e impresión | Contrastar cabecera, detalle, consulta histórica e impresión móvil con el flujo de diseño aportado por Liz. Ejecución aprobada; aceptación de usabilidad pendiente. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/f1b4799). | 6 | Liz | To Review |
| US40/41 · Orden de compra y recepción parcial; TS29/30 | T3-03 | Procurement: compra y recepción parcial | Verificar que crear una orden no mueva stock y que cada recepción incremente solo lo recibido. Flujo público y rechazo de exceso comprobados. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/00c1ec3). | 6 | Kevin | Done |
| US10/11/14 · Entradas, salidas e historial; TS07–09 | T3-04 | Inventory: entradas, salidas e historial | Verificar invariantes de saldo, motivo e historial y el contrato IInventoryFacade. Reglas encapsuladas y pruebas de stock aprobadas. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/f8f2eb3). | 6 | Piero | Done |
| US19–22 · Despachos, recursos, estados e incidencias; TS14–17 | T3-05 | Logistics: recursos, estados e incidencias | Contrastar elegibilidad de ventas y transiciones con el frontend. API probada; revisión funcional del conjunto de historias pendiente. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/84f14c7). | 6 | Darikson | To Review |
| US42/34 · Idioma y términos de la landing | T3-06 | Landing: idioma, footer y acceso por segmento | Verificar ambos idiomas, recarga, cuatro recursos del footer, teclado y 390 px; comprobar CTA de dueño a registro y operario a acceso. Publicación comprobada. [Evidencia](https://github.com/Nexxus-ops/nexxus-landing-page/pull/3). | 6 | Liz | Done |
| US28/29 · Usuarios y roles; TS21/22 | T3-07 | Identity: empleados y permisos | Verificar alta directa y aislamiento desde cliente y API. Pruebas aprobadas; correo de invitación de US28 todavía pendiente. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/commit/2930433). | 6 | Kevin | To Review |
| US29 · Restricción por roles; TS33 | T3-08 | Datos: esquema y aislamiento de empresa | Contrastar las 35 tablas, 182 columnas y 67 claves foráneas con diccionario, diagrama y código; comprobar aislamiento por empresa. Verificación técnica aprobada. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/AV2/diccionario-datos.md). | 6 | Piero | Done |
| TS34 · Pruebas de dominio, HTTP y navegador | T3-09 | Calidad: pruebas de dominio, HTTP y navegador | Ejecutar compilación, reglas, integración con PostgreSQL y flujo público. Comprobar continuidad de sesión/boleta e idempotencia tras desplegar. Resultado aprobado el 12/11. [Evidencia](https://github.com/Nexxus-ops/CeTe-Api/blob/4df092e49cef5033476add1c7b2caf410d35eac9/tests/api_smoke.py). | 8 | Kevin | Done |
| TS32 · Docker y publicación | T3-10 | Deployment: publicación y recorrido público | Publicar API refactorizada, frontend integrado y landing por segmento. Confirmar los commits desplegados y acceso público. Continuidad futura de PostgreSQL fuera de este cierre. [Evidencia](https://github.com/Nexxus-ops/FrontEnd-CeTe/pull/4). | 6 | Kevin | Done |
| Presentación · Evidencia del incremento | T3-11 | Presentación: incremento AV2 y Sprint 2 | Existe una presentación técnica editable. Faltan revisión conjunta, actualización de resultados de validación y preparación de la sustentación final. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/AV2/CeTe-AV2-revision-tecnica.pptx). | 4 | Darikson | To Review |
| Validación · Dos segmentos | T3-12 | Validación: 3–5 entrevistas por segmento | Diego entregó dos entrevistas nuevas del segmento dueño/administrador, incorporadas al informe. Piero está realizando la siguiente ronda; faltan fichas y cobertura por segmento. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/05-Chapter-5.md#532-registro-de-entrevistas). | 6 | Diego y Piero | In Process |
| SO5 · Colaboración y revisión | T3-13 | Colaboración: acuerdos y evidencias SO5 | Vincular aportes, revisión y resultados con evidencia individual. Reunión del 03/11 informada por Kevin; faltan horario, lugar, asistentes confirmados y acuerdos de la sesión. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe#colaboración-por-producto). | 4 | Diego | In Process |
| About-the-Product · Video del producto | T3-14 | About-the-Product: verificar video y enlace | Kevin informa que el video ya está realizado. Recibir URL, duración y captura, comprobar navegación pública y asociar testimonios. No se acredita publicación sin el enlace. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/05-Chapter-5.md#54-video-about-the-product). | 6 | Darikson | To Review |
| About-the-Team · Video del equipo | T3-15 | About-the-Team: aportes y reflexión | Preparar y publicar la primera versión requerida para AV2 con participación y reflexión de cada integrante. Grabación y enlaces aún no recibidos. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/blob/main/06-Conclusions.md). | 6 | Equipo | To Do |
| Comunicación · Informe y conclusiones | T3-16 | Comunicación: conclusiones y coherencia | Se corrigieron formato, diagramas y correspondencia DDD/código. Falta cierre conjunto de conclusiones, bibliografía y resultados de validación antes de exportar la entrega. [Evidencia](https://github.com/Nexxus-ops/Report-CeTe/pull/22). | 4 | Kevin | In Process |

**Total estimado: 94 horas-persona.** Se conserva la base de estimación de la versión anterior; no es tiempo restante ni tiempo efectivamente consumido. Las tareas técnicas completadas suman 38 h estimadas, no 38 h trabajadas. El resto del esfuerzo sigue distribuido entre revisión y entregables pendientes. Los responsables identifican la coordinación de cada tarea y pueden recibir los aportes indicados en la matriz LACX.

**Estado al corte:** 6 tareas Done, 6 To Review, 3 In Process y 1 To Do. US35 conserva el alcance de pago académico sin pasarela y US28 mantiene pendiente el correo de invitación. Los estados de las tareas no elevan estas historias a completadas. Faltan por confirmar el horario, lugar, asistentes y acuerdos de la reunión; estos datos no se estiman.

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
| Frontend | `main` · [`0eac94e`](https://github.com/Nexxus-ops/FrontEnd-CeTe/commit/0eac94e7b929a7f5579313988cbfc3f724e764cc) | 12/11/2026 · 13:06 | [Aplicación](https://cete-web-av2.onrender.com/) |
| Landing | `develop` · [`389ac46`](https://github.com/Nexxus-ops/nexxus-landing-page/commit/389ac468182c5967406d22f48c4a7ff8b31201dc) | 12/11/2026 · 14:43 | [Landing](https://cete-landing-av2.onrender.com/) |

**Respaldo comprobado.** El 12/11/2026 se exportó la base pública con `pg_dump` 17 en formato custom y TLS con verificación del servidor. El archivo se restauró con `pg_restore --exit-on-error` en un PostgreSQL 17 aislado: se recuperaron las 35 tablas y 67 claves foráneas, además de ventas, boletas y sesiones. La autorización de red externa se retiró al finalizar. El respaldo y su manifiesto SHA-256 se conservan de forma privada fuera de Git. Esta prueba acredita recuperación al momento de la copia; siguen pendientes una periodicidad de respaldo y la continuidad del servicio antes del vencimiento Free.

#### 5.2.3.8. Team Collaboration Insights during Sprint

Los cinco integrantes aportaron al incremento mediante diseño, implementación, integración o revisión técnica. La [matriz de colaboración por producto](README.md#colaboración-por-producto) identifica los roles informados por el equipo y enlaza los resultados integrados. La autoría individual visible en GitHub se registra por separado.

El historial integrado de frontend contiene aportes visibles de Kevin, Diego y Liz. El PR #4 incorpora la integración de Liz y conserva el cambio previo de Kevin; el informe mantiene separados los roles de diseño y revisión de la autoría Git. La participación y los resultados individuales todavía deben completarse en el cierre de colaboración y Student Outcome 5. Diego y Piero coordinan las entrevistas. Diego aportó las grabaciones, capturas y resúmenes de Raúl y Carmen, incorporados en el [registro de entrevistas](#532-registro-de-entrevistas). Las fichas restantes se incorporarán conforme se reciban.

## 5.3. Validation Interviews

> **Validación AV2 en curso.** Se conservan dos entrevistas históricas y se incorporan las entrevistas de Raúl y Carmen, realizadas por Diego Campoblanco para el segmento de dueños y administradores. La ronda requiere de 3 a 5 participantes por segmento usando la landing y la aplicación desplegadas, con tareas, captura, enlace a Stream, marcas de tiempo y hallazgos según el Anexo D.

### 5.3.1. Diseño de entrevistas

Para el proceso de validación, hemos diseñado sesiones interactivas donde los usuarios evalúan nuestros productos digitales de CeTe, basándonos en escenarios reales de uso.
* **Segmento 1 (Dueños/Gerentes):** Se evalúa la Landing Page en su versión Desktop, analizando la comprensión de la propuesta de valor, claridad de precios y la intención de conversión.
* **Segmento 2 (Operarios/Logística):** Se evaluará el prototipo interactivo de la Web Application (Módulo de Inventario), midiendo la facilidad de uso y prevención de errores (Stock Out).

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

Las fichas aún requieren la fecha de realización, las marcas de tiempo, la duración y el enlace a Microsoft Stream solicitado en el enunciado. Los resúmenes recogen las apreciaciones de los entrevistados y se utilizarán para la siguiente evaluación de usabilidad.

### 5.3.3. Evaluaciones según heurísticas

A partir del feedback recopilado, analizamos la interfaz basándonos en las heurísticas de Nielsen para aplicar mejoras iterativas al producto.

| # | Problema | Escala de severidad | Heurística / Principio violado |
| :---: | :--- | :---: | :--- |
| 1 | La Landing Page no cuenta con una sección explícita de "Precios" o "Planes", lo que frena la decisión de registro del usuario y genera incertidumbre. | 3 (Problema mayor) | Arquitectura de la Información / Coincidencia entre el sistema y el mundo real. |
| 2 | Ausencia de un canal de contacto rápido (botón de WhatsApp o soporte flotante) para resolver dudas antes de crear la cuenta B2B. | 2 (Problema menor) | Usabilidad: Ayuda y documentación. |
| 3 | El formulario de ingreso de mercadería requiere tipear el SKU a mano, lo que aumenta el riesgo de error humano y demora el proceso. | 3 (Problema mayor) | Usabilidad: Flexibilidad y eficiencia de uso. |
| 4 | No existe un botón o flujo específico y claro para registrar productos dañados (Mermas) desde la vista del operario. | 3 (Problema mayor) | Usabilidad: Prevención de errores. |

---

## 5.4. Video About-the-Product

**Enlace del Video Promocional:** [PROMO - CeTe (YouTube)](https://youtu.be/EBS8s4CFWRo)

---
