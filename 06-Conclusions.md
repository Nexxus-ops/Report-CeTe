## Conclusiones

### Conclusiones y recomendaciones

El incremento AV2 conecta la aplicación Vue con una API propia en C# y PostgreSQL y amplía el recorrido de inventario, compras, recepción, ventas, boletas y despachos. Las pruebas técnicas y las fichas de entrevistas aportan evidencias diferentes: las primeras comprueban comportamientos del software; las segundas permiten identificar dificultades de uso y revisar las hipótesis del producto. Este cierre se basa en el código y las seis fichas disponibles al 12/11/2026, conservando la diferencia entre descubrimiento, validación del prototipo y uso de la aplicación.

#### Resultados técnicos del incremento

1. **Trazabilidad operativa.** La orden de compra y la recepción física están separadas. La venta confirma conjuntamente detalle, stock, pago registrado y boleta académica. La consulta conserva nombres y precios históricos; no existe emisión fiscal ni cobro electrónico integrado.
2. **Protección de las operaciones.** Las verificaciones documentadas cubren aislamiento por empresa, permisos, reintentos, recepción parcial, anulación y concurrencia sobre la última unidad. Estos resultados no equivalen a una auditoría completa de seguridad ni a una garantía de operación en producción.
3. **Coherencia de DDD.** El backend se organiza como un monolito modular con cinco contextos activos: Identity, Inventory, Procurement, Sales y Logistics. Los contratos y servicios de cada contexto se contrastan con EventStorming, C4, clases y esquema físico. Persisten una base de datos y una unidad de trabajo compartidas; no se presenta el diseño como microservicios ni como una implementación de eventos distribuidos.
4. **Diseño y experiencia.** La landing mantiene inglés/español, recursos funcionales en el footer y accesos por segmento. Ventas y boletas incorporan mejoras de alineación, acceso visible y lectura móvil. La regresión de navegador respalda su funcionamiento; falta comprobar con nuevos participantes si resuelve las dificultades observadas.
5. **Alcance del modelo.** Las 35 tablas documentan el esquema, no 35 capacidades terminadas. Lotes, vencimientos, variantes, ubicaciones avanzadas, devoluciones completas y suscripciones siguen delimitados como evolución. Aumentar tablas por sí solo no demuestra mayor calidad del dominio.

#### Contraste con Lean UX y los segmentos

| Planteamiento de los capítulos I y III | Evidencia disponible | Conclusión y siguiente comprobación |
| :--- | :--- | :--- |
| Problem Statement: seguimiento disperso mediante cuadernos y hojas de cálculo. | La ficha de Raúl relaciona el producto con su registro en cuadernos; Carmen valora reunir compras y ventas y explica sus dificultades con el ingreso manual. | Existe una señal cualitativa de relevancia para dueños y administradores. No demuestra reemplazo de sus herramientas ni adopción diaria. Observar el uso repetido y registrar una línea base. |
| Hypothesis 1: reducir el tiempo y esfuerzo del registro y control operativo. | Luis evaluó Figma; Carmen y Luis solicitaron escaneo y Carmen señaló vencimientos y alertas. Jaime valoró el saldo pendiente en una recepción parcial y describió dificultad para ubicar el flujo y confirmar el stock resultante. El registro continúa siendo manual. | La hipótesis no está validada. No hay comparación de tiempos con la aplicación AV2; las sugerencias identifican fricción y oportunidades que deben priorizarse antes de prometer ahorro. |
| Hypothesis 2: aumentar confianza y retención mediante visibilidad del negocio. | Raúl, Carmen y Nicol valoran las ventas del día y el dashboard. Nicol encontró fricción al abrir una boleta y propuso un acceso directo desde el indicador. Persisten solicitudes sobre navegación, notificaciones y registro de mercancía. | La utilidad percibida del panel es una señal inicial. No se midieron retención, confianza sostenida ni disposición a pagar; la propuesta de S/80 mensuales continúa siendo una hipótesis comercial. |
| G1: reducir 30% el tiempo de una venta. | Existe el flujo con boleta y su comprobación técnica. No se registraron mediciones comparables antes y después. | Medición programada para TF: cronometrar el mismo caso y comparar medianas; no informar el 30% como resultado. |
| G2: lograr 90% de coincidencia del stock. | Las pruebas técnicas comprueban recepciones, ventas y anulaciones con datos ficticios. La ficha de Jaime describe una recepción de cuatro de diez unidades, pero no aporta una medición de conciliación con la muestra requerida. | Medición programada para TF: conciliar las cantidades durante las sesiones y documentar coincidencias y diferencias. |
| G3: lograr 80% de éxito sin ayuda al consultar boleta y cambiar idioma. | Hay pruebas de navegador de boleta, teclado e idioma. La ficha de Nicol aporta una dificultad para localizar la boleta, sin un registro completo de éxito por participante en ambos segmentos. | Medición programada para TF: medir éxito, tiempo y errores sin asistencia con la muestra requerida; la automatización no sustituye esa medición. |

El registro contiene seis fichas: cuatro de dueños/administradores —Jesús, Raúl, Carmen y Nicol— y dos de operarios —Luis y Jaime—. La ronda nueva de AV2 reúne tres dueños/administradores y un operario. Luis evaluó Figma en la entrega histórica y se conserva esa distinción. El cierre documental AV2 incorpora las seis fichas disponibles; para TF se programa ampliar la muestra operativa con al menos dos participantes adicionales, completar las mediciones comparativas y revalidar las mejoras. Los metadatos de edición y el consolidado audiovisual se incorporarán cuando se publiquen los archivos correspondientes.

#### Recomendaciones y roadmap

| Prioridad | Próximo resultado | Criterio para considerarlo cerrado |
| :--- | :--- | :--- |
| Cierre documental de AV2 | Incorporar la ronda de seis entrevistas y sus hallazgos. | Fichas y capturas integradas, cobertura diferenciada y evaluación documental registrada. Ampliación de muestra y revalidación programadas para TF. |
| Cierre de AV2 | Completar la distribución audiovisual de Product y Team y enlazar la navegación del incremento. | Product editado y publicado en [YouTube](https://youtu.be/V49TZ5P5Rsk) el 13/11/2026, con duración aproximada de 2:20. Quedan Stream, incrustación en la landing y publicación final de Team. Los clips de IA se identifican como ilustraciones. |
| Cierre de AV2 | Consolidar colaboración y entregables. | Aportes y evidencias documentados; estimaciones retrospectivas identificadas. Performance actualizado con la evaluación de 20/20 para los cinco integrantes indicada por el equipo; conservar coherencia entre informe, PDF, presentación y videos. |
| Siguiente iteración | Evaluar la navegación móvil, el ingreso manual y las alertas priorizadas por usuarios. | Prototipar y validar una solución, vincularla al backlog y medir si disminuye la dificultad observada. |
| Siguiente iteración | Evolucionar agregados, integridad y mantenimiento de datos. | Aplicar los criterios del capítulo IV: migraciones ensayadas, restricciones consistentes, referencias de origen y responsabilidades de contexto verificadas. |

El Sprint 3 consolida el incremento técnico y su documentación, con seis entrevistas acumuladas, hallazgos identificados y un roadmap de continuidad para TF. Las evidencias disponibles sustentan los flujos implementados y señales cualitativas de utilidad; no permiten afirmar resultados medidos de adopción, ahorro o retención. La presentación y las publicaciones audiovisuales completan la entrega y conservarán enlaces actualizables.

## Video About-the-Team

El About-the-Team documentará el proceso real de trabajo de Nexxus: distribución de responsabilidades, decisiones de diseño con DDD, revisión de cambios, integración y aprendizajes individuales. Incluirá escenas de sesiones reales de trabajo acompañadas de narración y el testimonio ante cámara de los cinco integrantes.

**Montaje en curso:** [About-the-Team en Canva · vista del diseño](https://www.canva.com/d/mA3bW8S9nOk7TK0). Al revisar el diseño se comprobaron clips del equipo ya insertados. Es la fuente de edición y no sustituye los enlaces de la versión final en Stream y YouTube. La [carpeta de evidencias](https://drive.google.com/drive/folders/1xVEEo9wgbIuEtw1UIYaJLxzBtxMa2upI?usp=sharing) se mantiene como recurso complementario.

| Evidencia de entrega | Estado |
| :--- | :--- |
| Retrospectiva grupal y escenas reales de trabajo | Material en preparación y edición dentro del montaje. |
| Testimonio individual | Clips recibidos en el montaje. Al terminar se comprobará la participación de Diego, Piero, Darikson, Liz y Kevin y la correspondencia de sus aportes. |
| Captura representativa y enlaces | Canva enlazado como material en edición. La captura definitiva y los enlaces de Stream y YouTube se añadirán después de exportar y publicar. |

La primera versión se solicita desde AV2, conforme a las consideraciones de entrega y al Anexo C del enunciado. Las descripciones documentadas de los aportes y las capturas de GitHub complementan esta evidencia, pero no reemplazan los testimonios ni permiten dar por completado el video.
