## Conclusiones

### Conclusiones y recomendaciones

El incremento AV2 conecta la aplicación Vue con una API propia en C# y PostgreSQL y amplía el recorrido de inventario, compras, recepción, ventas, boletas y despachos. Las pruebas técnicas y las fichas de entrevistas aportan evidencias diferentes: las primeras comprueban comportamientos del software; las segundas permiten identificar dificultades de uso y revisar las hipótesis del producto. Este cierre se basa en lo documentado al 12/11/2026; no atribuye resultados a entrevistas aún no recibidas.

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
| G1: reducir 30% el tiempo de una venta. | Existe el flujo con boleta y su comprobación técnica. No se registraron mediciones comparables antes y después. | Meta pendiente: cronometrar el mismo caso y comparar medianas; no informar el 30% como resultado. |
| G2: lograr 90% de coincidencia del stock. | Las pruebas técnicas comprueban recepciones, ventas y anulaciones con datos ficticios. La ficha de Jaime describe una recepción de cuatro de diez unidades, pero no aporta una medición de conciliación con la muestra requerida. | Meta pendiente: conciliar las cantidades durante las sesiones y documentar coincidencias y diferencias. |
| G3: lograr 80% de éxito sin ayuda al consultar boleta y cambiar idioma. | Hay pruebas de navegador de boleta, teclado e idioma. La ficha de Nicol aporta una dificultad para localizar la boleta, sin un registro completo de éxito por participante en ambos segmentos. | Meta pendiente: medir éxito, tiempo y errores sin asistencia con la muestra requerida; la automatización no sustituye esa medición. |

El registro contiene seis fichas: cuatro de dueños/administradores —Jesús, Raúl, Carmen y Nicol— y dos de operarios —Luis y Jaime—. La ronda nueva de AV2 reúne tres dueños/administradores y un operario. Luis evaluó Figma en la entrega histórica, por lo que faltan al menos dos participantes operativos sobre la aplicación AV2 para alcanzar tres en ese segmento. También quedan pendientes los metadatos, el consolidado en Stream y los fotogramas específicos de los hallazgos indicados en 5.3.

#### Recomendaciones y roadmap

| Prioridad | Próximo resultado | Criterio para considerarlo cerrado |
| :--- | :--- | :--- |
| Cierre de AV2 | Completar la ronda de validación y relacionar cada hallazgo con una decisión. | Entrevistas requeridas por segmento, tareas sobre los sitios desplegados, registros completos y evaluación conforme al Anexo D. |
| Cierre de AV2 | Editar y publicar Product, grabar Team y enlazar la navegación del incremento. | Evidencias en los destinos solicitados, capturas y tiempos reales; Product y Team incrustados en la landing. Los clips de IA son solo material ilustrativo. |
| Cierre de AV2 | Consolidar colaboración y entregables. | Confirmación de aportes, datos del acta, performance revisado por el líder y coherencia entre informe, PDF y presentación. No deducir desempeño de horas estimadas o cantidad de commits. |
| Siguiente iteración | Evaluar la navegación móvil, el ingreso manual y las alertas priorizadas por usuarios. | Prototipar y validar una solución, vincularla al backlog y medir si disminuye la dificultad observada. |
| Siguiente iteración | Evolucionar agregados, integridad y mantenimiento de datos. | Aplicar los criterios del capítulo IV: migraciones ensayadas, restricciones consistentes, referencias de origen y responsabilidades de contexto verificadas. |

El avance demuestra un incremento técnico integrado y una base para continuar la validación. La aceptación de AV2 requiere cerrar las evidencias humanas y de entrega pendientes; todavía no permite concluir que las hipótesis de adopción, ahorro y retención se hayan confirmado.

## Video About-the-Team

El About-the-Team documentará el proceso real de trabajo de Nexxus: distribución de responsabilidades, decisiones de diseño con DDD, revisión de cambios, integración y aprendizajes individuales. Incluirá escenas de sesiones reales de trabajo acompañadas de narración y el testimonio ante cámara de los cinco integrantes.

**Estado al 12/11/2026:** Kevin confirma que el video todavía no se ha grabado. La [carpeta registrada de evidencias](https://drive.google.com/drive/folders/1xVEEo9wgbIuEtw1UIYaJLxzBtxMa2upI?usp=sharing) se conserva como recurso de coordinación; no acredita un video terminado ni publicado.

| Evidencia de entrega | Estado |
| :--- | :--- |
| Retrospectiva grupal y escenas reales de trabajo | Pendiente de grabación y edición. |
| Testimonio individual | Pendiente para Diego, Piero, Darikson, Liz y Kevin. Cada participante describirá sus actividades, resultados y competencias con un ejemplo propio. |
| Duración | Por registrar tras la edición. El Anexo C orienta a considerar cinco minutos de retrospectiva y un minuto por integrante; la duración depende del contenido. |
| Pauta de secuencias | Pendiente de registrar los inicios reales de cada sección en formato `hh:mm:ss`. |
| Captura representativa y enlaces | Pendientes la captura del video y las publicaciones en Microsoft Stream y YouTube. |
| Incrustación en la landing | Pendiente de disponer del video publicado. |

La primera versión se solicita desde AV2, conforme a las consideraciones de entrega y al Anexo C del enunciado. Las descripciones documentadas de los aportes y las capturas de GitHub complementan esta evidencia, pero no reemplazan los testimonios ni permiten dar por completado el video.
