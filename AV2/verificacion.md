# Verificación técnica AV2

- Landing: https://cete-landing-av2.onrender.com/
- Frontend: https://cete-web-av2.onrender.com/
- Swagger: https://cete-api-av2.onrender.com/swagger
- Salud: https://cete-api-av2.onrender.com/health

El recorrido público pasó con empresa y credenciales ficticias generadas en memoria: registro, acceso, alta de productos para prueba, compra de dos unidades, recepción parcial 1 + 1, stock, selección de producto por teclado, venta, boleta, impresión, cambio de idioma, recarga y móvil 390px. La impresión conserva el comprobante y oculta navegación, footer y controles de la aplicación. El footer compilado conserva contraste.

La landing pasó inglés/español, persistencia, cuatro recursos del footer, anclas, imagen y menú móvil. Las capturas no contienen credenciales reales ni tokens.

La suite HTTP pasó en Docker/PostgreSQL y en la API pública: autenticación, tenant, roles, SKU, recepción parcial, rollback, idempotencia, instantánea histórica, anulación única, revocación, última unidad concurrente, despachos e integración externa USD/PEN. Las pruebas crean datos ficticios y no deben ejecutarse sobre empresas reales.

CI del backend aprobado para e8cb3c090b709f093a11f3f798ddae6b7e1ee359: build y comprobaciones de dominio. La API desplegada inicialmente usa 8c8122719f06f1861943c4abfb7819c21487f8ca. El commit posterior añade formato y documentación de ejecución, sin cambios de lógica.

Último frontend revisado: 8eba976 (rama codex/av2-corrections). Landing: 857faf4 (documentación actualizada; HTML verificado en 13326ec). Confirmar los hashes completos y el estado live del host al preparar la entrega final.

Build frontend aprobado. npm audit reportó cero vulnerabilidades al revisar. El build informa un bundle principal mayor de 500 kB, pendiente de optimización. La revisión no declara rendimiento de producción ni todos los criterios de todas las historias aprobados.

La base Free vence el 29/11/2026 UTC. Render Free puede tardar cerca de un minuto en despertar. El cliente web espera hasta 90 s; abrir Swagger antes de la sustentación permite comprobar disponibilidad. No cambiar a un plan de pago sin revisar el costo.

Siguen pendientes aceptación por el equipo, al menos tres autores reales de frontend, validaciones con usuarios, videos y ficha de performance revisada por el coordinador.

Registro generado: 2026-10-29T23:50:40-05:00 (Lima).

## Control posterior

La [revalidación del 30/10/2026](revalidacion-2026-10-30.md) actualiza los resultados y referencias de código. El frontend incluye una prueba de navegador reproducible mediante npm run test:e2e.
