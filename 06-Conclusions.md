## Conclusiones

1. El incremento conecta Vue con una API propia y PostgreSQL. El recorrido verificado genera una boleta con dirección, fecha/hora, detalle y total, que conserva precios y nombres históricos.
2. La transacción serializable impide vender dos veces la última unidad. La prueba detectó y corrigió una respuesta 500 de un conflicto envuelto por EF, que ahora devuelve 409.
3. La ampliación agrega compras y recepciones separadas, movimientos, comprobantes y sesiones. Las 35 tablas no implican que lotes, devoluciones, paradas y suscripciones estén terminados.
4. La landing incorpora inglés/español persistentes, footer funcional y captura del producto. Las pruebas técnicas respaldan su funcionamiento y quedan por validar con usuarios.
5. Las TS son visibles en el backlog y las 25 horas estimadas de Sprint 2 se conservan como registro histórico. El equipo debe acordar las nuevas estimaciones y responsabilidades.
6. La publicación técnica está verificada. AV2 requiere al menos tres participantes reales en frontend, 3–5 validaciones por segmento y los videos del producto y equipo. El incremento todavía requiere ese cierre antes de evaluación.

