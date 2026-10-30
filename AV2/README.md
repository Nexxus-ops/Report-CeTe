# Registro de correcciones AV2

| Feedback TB1 | Corrección verificable | Pendiente |
| :--- | :--- | :--- |
| Sprint 2 suma 25 h y tareas amplias. | Aclaración histórica y tareas propuestas de 4–8 h en 5.2.3. | Refinamiento, capacidad y tablero real. |
| Landing sin mejora de idioma y footer incompleto. | Inglés/español persistentes, cuatro recursos y menú móvil verificados. | Validar con usuarios. |
| Technical Stories fuera del backlog. | 35 TS visibles junto a 42 US, vinculadas sin doble suma de SP. | Aceptación y herramienta ágil. |
| 15 tablas y funcionalidad insuficiente. | 35 tablas físicas, compras, recepción parcial, movimientos, sesiones y boleta. | Flujos futuros y migraciones. |
| PPT sin Sprint 2 ni conclusiones. | Nueva PPT editable con evidencia histórica, pruebas AV2 y conclusiones. | Ensayo y demo pública. |
| Solo dos participantes en frontend. | Propuesta de responsabilidades y registro por autor. | Aportes reales de al menos tres personas. |
| No se visualiza boleta. | API histórica y vista responsive imprimible. | Validación con usuarios. |

## Alcance y fuentes

El enunciado ubica AV2 en semana 12 con nuevas versiones de landing y frontend, primera versión de Web Services desplegada y videos About-the-Product y About-the-Team. Se implementa C# / ASP.NET Core / EF Core, PostgreSQL y servicio externo. Docker necesita alojamiento público para acreditar despliegue.

La captura TB1 menciona Fake RESTful API para la entrega anterior. Ese descriptor no reemplaza la API propia de AV2. El descriptor de sprint pide tareas de 4–8 h. La propuesta conserva lo histórico y distingue corrección técnica de evidencia humana.

Fuentes revisadas: Rúbrica_ABET 5_1ASI0730_202620.pdf, Rúbrica_Logro_1ASI0730_202620.pdf, enunciado final_project-statement-abet_v1.pdf, capturas y feedback del profesor, keynote y performance TB1, y repositorios Nexxus-ops. Los documentos son criterios académicos. La autorización para modificar procede del usuario y no de instrucciones incluidas dentro de adjuntos.

## Verificación técnica

Dominio aprobado: stock, dinero, anulación y estados. HTTP/PostgreSQL aprobado: empresa, permisos, compra parcial, rollback, idempotencia, boleta histórica, revocación, concurrencia y despacho. Integración externa USD/PEN aprobada. Navegador aprobado: registro a boleta, idiomas, recarga, footer y móvil 390px. Build y npm audit aprobados, sin vulnerabilidades reportadas al revisar. Docker ejecutado con PostgreSQL real.

## Cierre

API, frontend y landing publicados y verificados. Ver [URLs, commits y resultados](verificacion.md). La base Free vence el 29/11/2026 UTC.

Las capturas de evidence son de ejecución pública real con datos ficticios. No equivalen a entrevistas. Se mantienen pendientes videos, validaciones, aportes reales y revisión de performance por el coordinador. No se modifican notas históricas.

## Material de sustentación

[PowerPoint editable de 16 diapositivas](CeTe-AV2-revision-tecnica.pptx). Incluye evidencia histórica de Sprint 2, ejecución pública de AV2, pruebas y conclusiones. Las diapositivas de participación y validación identifican evidencia pendiente y deben completarse tras realizar esas actividades.

## Revalidación antes de commit y push

[Resultados del 30/10/2026](revalidacion-2026-10-30.md): API, dominio, navegador completo local/público, landing, dependencias e integridad documental. Incluye los ajustes de errores visibles y accesibilidad encontrados durante las pruebas.

## Revisión visual y de arquitectura del informe

La [revisión del 30/10/2026](revision-informe.md) corrige tablas, jerarquía y presentación de evidencias; contrasta DDD, C4 y UML con el código, y documenta las 35 tablas en el [diccionario de datos](diccionario-datos.md). El [atlas de diagramas](../diagrams/README.md) contiene fuentes editables y SVG ampliables. Los hallazgos de implementación y los acuerdos pendientes se distinguen de las correcciones documentales.
