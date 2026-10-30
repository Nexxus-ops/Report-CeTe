# Revisión del informe · Formato, DDD y datos

**Fecha:** 30/10/2026 · **Estado:** preparado para revisión conjunta.

[Informe completo](../README.md) · [Requisitos](../03-Chapter-3.md) · [Diseño](../04-Chapter-4.md) · [Evidencias](../05-Chapter-5.md) · [Diagramas](../diagrams/README.md) · [Diccionario de datos](diccionario-datos.md)

## Cambios de presentación

| Observación | Corrección preparada |
| :--- | :--- |
| EPIC-10 aparece como texto fuera de la tabla. | Se incorporó al bloque de epics con el mismo formato. |
| TS28–TS35 aparecen como párrafos unidos por barras. | Se reconstruyeron las tablas y se verificó la presencia de todas las historias. |
| Las tablas de historias son muy extensas. | Se agruparon por epic y se separaron US de TS. La relación con el epic queda en el encabezado de cada grupo. |
| Criterios añadidos con formato distinto. | Se uniformaron los pasos y saltos de línea Given–When–Then, conservando el contenido y los identificadores. |
| Backlog difícil de recorrer. | Se dividió en cuatro tramos consecutivos, conservando prioridad, 42 US, 35 TS y 139 SP propuestos. El beneficio se resume sin duplicar toda la historia. |
| Numeración irregular en Sprint 2 y Sprint 3. | Se corrigieron niveles de encabezado y la sección principal de Sprint 2. |
| Captura de compras precedida por `#!` y evidencias sin explicación. | Se añadió una galería con títulos, pies y una vista desplegable para boleta móvil/impresión. |
| Configuración descrita como un despliegue futuro. | Se actualizó 5.1.4 con los recursos públicos y se identificó la planificación histórica por separado. |
| Enlaces técnicos y pendientes poco claros. | Se incorporaron enlaces directos y redacción académica que distingue resultados técnicos, aceptación y evidencia del equipo. |
| README y capítulos pueden divergir. | Se sincronizaron los capítulos revisados con el informe completo y se incorporó una comprobación reproducible. |

La carátula, la matriz ABET, las entrevistas históricas, los registros de Sprint 1/2 y las calificaciones de performance conservan su contenido histórico. Las inconsistencias identificadas se registran abajo; no se sustituyen por datos supuestos.

## Correcciones de arquitectura

| Artefacto | Hallazgo | Resultado documental |
| :--- | :--- | :--- |
| Big Picture y lenguaje ubicuo | Compra, recepción, artículo y saldo se usaban con significados ambiguos. | Se diferenciaron orden/recepción, producto/saldo y boleta académica/factura fiscal; se conservó el tablero histórico. |
| DDD estratégico | Solo se describían dos contextos y se mezclaban límites de diseño con implementación. | Se documentaron cinco responsabilidades lógicas, la proyección del dashboard y los límites todavía compartidos del código. |
| EventStorming de diseño | Una venta parecía descontar stock mediante un evento posterior. | Se explicó la coordinación transaccional síncrona de venta y recepción. Los hechos son lenguaje de análisis, sin bus implementado. |
| C4 nivel 1 | SUNAT y correo aparecían como integraciones actuales. | Se representó ExchangeRate-API, que es la integración implementada. |
| C4 nivel 2 | Faltaban la integración externa y el enlace landing–SPA. | Se incorporaron responsabilidades, direcciones, protocolos y unidades reales de ejecución. |
| C4 nivel 3 | Se mostraban InventoryController/Service/Repository inexistentes. | Se sustituyeron por Program/Minimal APIs, Operations, Authentication, CurrentUser, dominio y CeTeDb. |
| UML | Clases y métodos no correspondían al código y se afirmaba encapsulación total. | Cuatro vistas actuales muestran tipos reales, setters restringidos donde existen y reglas coordinadas en aplicación. |
| ER | Solo se veía una parte del modelo y algunos mínimos de cardinalidad se confundían con reglas del caso de uso. | Se generaron seis vistas por área y una vista física completa desde las FK del SQL. |
| Base de datos | El resumen de tablas no permitía auditar campos ni relaciones. | Se añadió un diccionario de las 35 tablas y 182 columnas, con nulabilidad, claves, relaciones e índices únicos. |

Los 21 diagramas incluyen fuente Mermaid y SVG ampliable. El capítulo IV identifica el alcance de cada vista y las estructuras que todavía no tienen un flujo de producto.

## Comprobación estructural

Se comparó `CeTe-Api/schema.sql` con una exportación `pg_dump --schema-only` de la instancia local de PostgreSQL. Coinciden las definiciones de **35 tablas, 182 columnas, 35 PK, 33 claves alternativas, 67 FK y ocho índices únicos de negocio**. La comparación excluye comentarios y nombres históricos de restricciones; no copia datos ni credenciales. No constituye una nueva auditoría del contenido de la base pública.

Fuentes de implementación revisadas: `Program.cs`, `Domain/Entities.cs`, `Application/Ports.cs`, `Application/Operations.cs`, `Infrastructure/Authentication.cs`, `Infrastructure/CeTeDb.cs` y `schema.sql`, en la rama `codex/av2-corrections` de [CeTe-Api](https://github.com/Nexxus-ops/CeTe-Api/tree/codex/av2-corrections). La revisión documental parte del commit API `3b19598`; no modifica el código de los otros productos.

La comprobación de estructura documental puede repetirse con:

```powershell
python tools/verify-report.py
```

Para contrastar también nombres de tablas/columnas/FK con la copia local de la API:

```powershell
python tools/verify-report.py --api-root ../CeTe-Api
```

**Resultado de la revisión local:** comprobación estructural aprobada; 21 fuentes Mermaid parseadas y renderizadas, SVG con XML válido y sin imágenes rotas; tablas sin filas sueltas; enlaces y capítulos sincronizados. Se inspeccionó la presentación en Edge con tema claro y oscuro. Estas comprobaciones no sustituyen una revisión posterior de la rama publicada en GitHub.

## Asuntos para revisar juntos

1. **Datos y DDD:** acordar la prioridad de migraciones, restricciones SQL, fuente única de roles, límites de agregados y conexión de maestros. El detalle y los criterios de cierre están en 4.8.4; son cambios futuros de implementación.
2. **Requisitos:** aceptar o refinar historias parciales, contratos pendientes y estimaciones. Conservar una tabla no acredita que todos sus escenarios estén terminados.
3. **Contribuciones:** completar participación real de al menos tres integrantes en frontend con commits, revisión y demostración individual.
4. **Validación:** realizar las entrevistas faltantes de la ronda AV2 y registrar resultados, sin presentar sesiones pendientes como realizadas.
5. **Material de sustentación:** revisar los videos About-the-Product/About-the-Team y la ficha de performance con el coordinador.
6. **Inconsistencia histórica de commits:** la relación inicial del informe lista 3 + 16 + 7 + 12 + 2 = 40, pero declara «Total de commits en AV1: 16». Confirmar repositorio, periodo y criterio de conteo antes de corregirlo; no se inventa un total histórico.

Esta revisión mejora la fidelidad y la lectura del informe. Los hallazgos técnicos que requieren modificar la API y las evidencias humanas pendientes permanecen identificados para su cierre verificable.
