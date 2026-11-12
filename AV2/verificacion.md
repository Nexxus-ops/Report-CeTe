# Verificación técnica AV2

**Actualización: 12/11/2026 (Lima).** La API publicada corresponde a `main`, commit [`4df092e49cef5033476add1c7b2caf410d35eac9`](https://github.com/Nexxus-ops/CeTe-Api/commit/4df092e49cef5033476add1c7b2caf410d35eac9), integrado por [PR #2](https://github.com/Nexxus-ops/CeTe-Api/pull/2). Render finalizó el despliegue a las 16:35 UTC (11:35 Lima). El identificador de despliegue es `dep-dbqul267bikc738c002g`.

- Landing: https://cete-landing-av2.onrender.com/
- Frontend: https://cete-web-av2.onrender.com/
- Swagger: https://cete-api-av2.onrender.com/swagger
- Salud: https://cete-api-av2.onrender.com/health

El recorrido público pasó con empresa y credenciales ficticias generadas en memoria: registro, acceso, alta de productos para prueba, compra de dos unidades, recepción parcial 1 + 1, stock, selección de producto por teclado, venta, boleta, impresión, cambio de idioma, recarga y móvil 390px. La impresión conserva el comprobante y oculta navegación, footer y controles de la aplicación. El footer compilado conserva contraste.

La landing pasó inglés/español, persistencia, cuatro recursos del footer, anclas, imagen y menú móvil. Las capturas no contienen credenciales reales ni tokens.

La suite HTTP pasó en Docker/PostgreSQL y en la API pública: autenticación, tenant, roles, SKU, recepción parcial, rollback, idempotencia, instantánea histórica, anulación única, revocación, última unidad concurrente, despachos e integración externa USD/PEN. Las pruebas crean datos ficticios y no deben ejecutarse sobre empresas reales.

La revalidación del 12/11/2026 aprobó compilación y comprobaciones de dominio de la refactorización, suite HTTP contra PostgreSQL local y contra la API pública, y recorrido completo de navegador sobre el frontend publicado. Las cinco capturas de dashboard, compras y boleta en `evidence/` se renovaron en esa ejecución. Swagger conserva las 28 operaciones HTTP anteriores y documenta recursos y resultados tipados de los nuevos controladores.

La prueba de continuidad creó una sesión, una venta y su boleta antes del despliegue. Después recuperó la misma sesión y los datos históricos, y reenvió la venta con su UUID sin duplicar el descuento de stock. `/health` devolvió HTTP 200 con estado `healthy`. El valor `version: 0.2.0` de ese endpoint se conservó por compatibilidad; el commit y el identificador de despliegue anteriores identifican la versión de código publicada.

Como antecedente, CI aprobó `e8cb3c090b709f093a11f3f798ddae6b7e1ee359` para la API inicial de octubre. Ese registro histórico no identifica la versión actual.

Las ramas publicadas se documentan en [Configuración de despliegue](../05-Chapter-5.md#514-software-deployment-configuration).

Build frontend aprobado. npm audit reportó cero vulnerabilidades al revisar. El build informa un bundle principal mayor de 500 kB, pendiente de optimización. La revisión no declara rendimiento de producción ni todos los criterios de todas las historias aprobados.

La base Free vence el **28/11/2026 a las 22:30 Lima** (29/11/2026 a las 03:30 UTC). Render Free puede tardar cerca de un minuto en despertar. El cliente web espera hasta 90 s; abrir Swagger antes de la sustentación permite comprobar disponibilidad. La continuidad del servicio después del vencimiento requiere renovación o migración.

## Respaldo y prueba de recuperación

El 12/11/2026 a las 11:51 Lima se exportó la base pública con `pg_dump` 17, formato custom, autenticación y TLS `verify-full`. El archivo se conserva fuera de los repositorios; no se adjuntan datos, credenciales ni tokens al informe.

| Comprobación | Resultado |
| :--- | :--- |
| Lectura del archivo | `pg_restore --list` aprobada. |
| Restauración independiente | `pg_restore --exit-on-error` aprobado en un PostgreSQL 17 temporal, sin puertos públicos. |
| Integridad estructural | 35 tablas y 67 claves foráneas recuperadas. |
| Datos operativos | Ventas, boletas, productos y sesiones recuperados. |
| Integridad del archivo | SHA-256 registrado en un manifiesto privado. |
| Red | Regla de IP temporal retirada; lista externa nuevamente vacía. La API conserva su conexión interna. |

La restauración finalizó a las 11:55 Lima. El contenedor temporal se cerró y eliminó al concluir la comprobación. Esta copia corresponde a un momento concreto, no a un respaldo automático periódico ni a recuperación continua. El [plan Free de Render no incluye las prestaciones de backup administrado](https://render.com/docs/postgresql-backups); falta acordar la frecuencia de exportación, la segunda ubicación de custodia y el destino de continuidad antes del vencimiento.

Siguen pendientes aceptación por el equipo, al menos tres autores reales de frontend, validaciones con usuarios, videos y ficha de performance revisada por el coordinador.

Registro inicial: 2026-10-29T23:50:40-05:00. Revalidación del despliegue, continuidad y respaldo: 12/11/2026 (Lima).

El frontend incluye la prueba de navegador reproducible `npm run test:e2e`.
