# Atlas de diagramas · CeTe AV2

[Volver al capítulo IV](../04-Chapter-4.md#46-domain-driven-software-architecture) · [Diccionario de datos](../AV2/diccionario-datos.md)

Cada diagrama tiene una fuente Mermaid (`.mmd`) y un SVG ampliable. Las imágenes usan fondo claro explícito y texto oscuro para mantener legibilidad al visualizar el informe en GitHub con tema claro u oscuro. El SVG permite ampliar sin perder nitidez. Los diagramas se renderizan desde su fuente, no se editan por separado.

**Alcance.** C4 y UML representan la implementación actual. Los hechos de EventStorming son lenguaje de análisis, no mensajes publicados por la API. Los ER derivan del SQL versionado; los diagramas por área incluyen todas las columnas, pero omiten los enlaces repetidos a `Tenants` fuera de Identidad. El ER completo incluye las 35 tablas y sus 67 FK.

| Vista | Diagrama | Imagen | Fuente |
| :--- | :--- | :--- | :--- |
| DDD / comportamiento | Big Picture · Recorrido operativo del incremento AV2 | [SVG](business-timeline.svg) | [Mermaid](business-timeline.mmd) |
| C4 | C4 · Nivel 3 · Componentes reales de CeTe API · AV2 | [SVG](c4-components.svg) | [Mermaid](c4-components.mmd) |
| C4 | C4 · Nivel 2 · Contenedores de CeTe · AV2 | [SVG](c4-containers.svg) | [Mermaid](c4-containers.mmd) |
| C4 | C4 · Nivel 1 · Contexto actual de CeTe · AV2 | [SVG](c4-context.svg) | [Mermaid](c4-context.mmd) |
| C4 | C4 complementario · Despliegue actual de CeTe · AV2 | [SVG](c4-deployment.svg) | [Mermaid](c4-deployment.mmd) |
| UML | UML actual · Producto y saldo · CeTe API | [SVG](classes-inventory.svg) | [Mermaid](classes-inventory.mmd) |
| UML | UML actual · Despacho e incidencias · CeTe API | [SVG](classes-logistics.svg) | [Mermaid](classes-logistics.mmd) |
| UML | UML actual · Compra y recepción · CeTe API | [SVG](classes-procurement.svg) | [Mermaid](classes-procurement.mmd) |
| UML | UML actual · Venta y comprobante · CeTe API | [SVG](classes-sales.svg) | [Mermaid](classes-sales.mmd) |
| DDD / comportamiento | DDD · Mapa lógico de contextos · CeTe AV2 | [SVG](ddd-context-map.svg) | [Mermaid](ddd-context-map.mmd) |
| ER físico | ER físico completo · 35 tablas y 67 claves foráneas | [SVG](er-complete.svg) | [Mermaid](er-complete.mmd) |
| ER físico | ER físico · Identidad y empresa | [SVG](er-identity.svg) | [Mermaid](er-identity.mmd) |
| ER físico | ER físico · Inventario | [SVG](er-inventory.svg) | [Mermaid](er-inventory.mmd) |
| ER físico | ER físico · Logística y ventas | [SVG](er-logistics.svg) | [Mermaid](er-logistics.mmd) |
| ER físico | ER físico · Abastecimiento y sus referencias | [SVG](er-procurement.svg) | [Mermaid](er-procurement.mmd) |
| ER físico | ER físico · Expansión de devoluciones y notificaciones | [SVG](er-returns.svg) | [Mermaid](er-returns.mmd) |
| ER físico | ER físico · Ventas y sus referencias | [SVG](er-sales.svg) | [Mermaid](er-sales.mmd) |
| DDD / comportamiento | EventStorming de diseño · Recepción parcial · CeTe AV2 | [SVG](event-storming-receipt.svg) | [Mermaid](event-storming-receipt.mmd) |
| DDD / comportamiento | EventStorming de diseño · Confirmar venta · CeTe AV2 | [SVG](event-storming-sale.svg) | [Mermaid](event-storming-sale.mmd) |
| DDD / comportamiento | Vista dinámica · Venta atómica e idempotente · AV2 | [SVG](sequence-checkout.svg) | [Mermaid](sequence-checkout.mmd) |
| UML | Máquina de estados implementada · Dispatch.Transition | [SVG](state-dispatch.svg) | [Mermaid](state-dispatch.mmd) |

## Convenciones de mantenimiento

1. Actualizar el análisis y la fuente `.mmd` cuando cambie un contrato, clase o relación.
2. Renderizar y comprobar que no se corten etiquetas, flechas ni cardinalidades.
3. Contrastar los ER con `schema.sql` y el mapeo de EF Core; no añadir asociaciones que solo se deducen por el nombre de una tabla.
4. Mantener las mismas imágenes en el README y en los capítulos. El texto del capítulo es la explicación del alcance, no una sustitución de las reglas del código.

La revisión de 30/10/2026 usa Mermaid 12.2.0, con notación clásica y disposición Dagre. Los C4 se expresan con flowcharts tipados; C4 no exige una herramienta de dibujo concreta. Las fuentes no contienen secretos ni datos de clientes.

## Regeneración local

Se requiere Node.js 22.12 o posterior. Instalar las herramientas auxiliares sin modificar las dependencias de los otros productos:

```powershell
npm install --prefix tools --no-save --package-lock=false mermaid@12.2.0 playwright@1.62.1
node tools/render-diagrams.cjs
python tools/verify-report.py
```

Ejecutar los comandos desde la raíz de Report-CeTe. En Windows se utiliza Edge instalado; el proceso abre una instancia aislada en modo headless. En Linux se requiere Chromium de Playwright (`npx --prefix tools playwright install chromium`). La variable `CETE_DIAGRAM_BROWSER` permite escoger otro canal instalado. El aspecto se define en [mermaid-config.json](mermaid-config.json).
