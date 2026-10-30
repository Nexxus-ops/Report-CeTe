# Capítulo III: Requirements Specification

La especificación reúne los requisitos de CeTe y sus habilitadores técnicos. Las historias conservan su identificador para mantener trazabilidad con el backlog, los casos de uso y las evidencias. Los criterios de aceptación usan Given–When–Then; describen lo que debe cumplirse y no equivalen a una declaración de implementación.

[Epics](#311-epics) · [User Stories](#312-user-stories) · [Technical Stories](#313-technical-stories) · [Impact Mapping](#32-impact-mapping) · [Product Backlog](#33-product-backlog)

## 3.1. User Stories

Se documentan **10 epics, 42 User Stories y 35 Technical Stories**. Los epics agrupan objetivos de negocio; las US expresan valor para el usuario y las TS identifican contratos o condiciones técnicas. El alcance pendiente permanece visible para no confundir requisito con producto entregado.

### 3.1.1. Epics

| Epic ID | Título | Descripción | Criterios de aceptación | Relacionado con |
| :--- | :--- | :--- | :--- | :--- |
| **EPIC-01** | Autenticación y cuenta | **Como** usuario de CeTe,<br>**deseo** gestionar el registro, inicio, cierre y recuperación de mi cuenta,<br>**para** acceder de forma segura a la plataforma según mi plan. | **Escenario: Validación del alcance de autenticación y cuenta**<br>**Given** que las historias US01, US02, US03, US04 pertenecen a este epic,<br>**When** el equipo evalúa el cumplimiento de EPIC-01,<br>**Then** el epic se considera aceptado únicamente cuando las historias incluidas cumplen sus criterios de aceptación; el epic por sí solo no acredita implementación. | — |
| **EPIC-02** | Gestión de Inventario | **Como** operario de almacén,<br>**deseo** gestionar las existencias, artículos y mermas,<br>**para** mantener el stock actualizado y evitar descuadres físicos y lógicos. | **Escenario: Validación del alcance de gestión de inventario**<br>**Given** que las historias US09, US10, US11, US12, US13, US14 pertenecen a este epic,<br>**When** el equipo evalúa el cumplimiento de EPIC-02,<br>**Then** el epic se considera aceptado únicamente cuando dichas historias cumplen sus criterios y respetan las reglas lógicas del stock. | — |
| **EPIC-03** | Transacciones Comerciales | **Como** dueño de negocio,<br>**deseo** gestionar el ciclo de vida de las ventas y transacciones diarias,<br>**para** registrar los ingresos y descontar productos del almacén. | **Escenario: Validación del ciclo de vida de una transacción**<br>**Given** que las historias US15, US16, US17, US18, US35, US36, US39 pertenecen a este epic,<br>**When** el equipo valida EPIC-03,<br>**Then** las operaciones respetan el flujo de ventas, impactan directamente en el inventario disponible y liberan o retornan stock si la venta es anulada. | — |
| **EPIC-04** | Logística y Despacho | **Como** jefe de logística,<br>**deseo** gestionar guías, manifiestos de despacho e incidencias,<br>**para** organizar la salida de mercadería y mantener la trazabilidad. | **Escenario: Validación de la gestión de despachos e incidencias**<br>**Given** que las historias US19, US20, US21, US22 pertenecen a este epic,<br>**When** se registra un manifiesto o una incidencia en ruta,<br>**Then** la información queda asociada a una venta verificada, es trazable y actualiza el estado logístico correctamente. | — |
| **EPIC-05** | Dashboard y Rentabilidad | **Como** dueño de negocio,<br>**deseo** visualizar métricas clave y reportes en tiempo real,<br>**para** localizar información financiera relevante y tomar decisiones. | **Escenario: Validación de reportes y dashboard**<br>**Given** que las historias US23, US24, US25, US37, US38 pertenecen a este epic,<br>**When** el usuario consulta sus KPIs o exporta datos,<br>**Then** el sistema devuelve únicamente información consolidada y autorizada que refleja el cruce exacto entre ventas e inventario. | — |
| **EPIC-06** | Notificaciones y Alertas | **Como** participante autorizado,<br>**deseo** recibir notificaciones sobre stock mínimo y vencimientos,<br>**para** reabastecer a tiempo sin monitorear manualmente cada producto. | **Escenario: Validación de notificaciones y alertas preventivas**<br>**Given** que las historias US26, US27 pertenecen a este epic,<br>**When** ocurre un evento notificable como un quiebre de stock,<br>**Then** el sistema genera avisos solo para los destinatarios autorizados y evita alertas duplicadas para el mismo evento. | — |
| **EPIC-07** | Roles y Permisos | **Como** administrador de la cuenta,<br>**deseo** gestionar los accesos y crear usuarios empleados,<br>**para** proteger la confidencialidad financiera de la empresa. | **Escenario: Validación de seguridad de roles**<br>**Given** que las historias US28, US29 pertenecen a este epic,<br>**When** un usuario intenta acceder a un recurso,<br>**Then** el epic exige que el sistema verifique el rol del usuario y deniegue o autorice el acceso a módulos específicos (ej. reportes). | — |
| **EPIC-08** | Perfil y preferencias | **Como** usuario registrado,<br>**deseo** administrar mis datos de empresa, contraseña e idioma,<br>**para** mantener mi cuenta actualizada y adaptar la interfaz. | **Escenario: Validación de perfil y preferencias**<br>**Given** que las historias US30, US31, US33 pertenecen a este epic,<br>**When** el usuario modifica información permitida de su cuenta,<br>**Then** el sistema valida los cambios, conserva las restricciones de seguridad y persiste las preferencias admitidas como el idioma. | — |
| **EPIC-09** | Landing page | **Como** visitante de CeTe,<br>**deseo** conocer la propuesta, funcionalidades, testimonios y planes,<br>**para** evaluar la solución antes de continuar a la plataforma. | **Escenario: Validación del contenido y navegación del landing page**<br>**Given** que las historias US05, US06, US07, US08, US32, US34, US42 pertenecen a este epic,<br>**When** el visitante navega por el landing page,<br>**Then** el contenido es accesible, no presenta funciones proyectadas como implementadas y permite continuar el recorrido de registro. | — |
| **EPIC-10** | Abastecimiento | **Como** encargado de almacén,<br>**deseo** controlar compras y recepciones,<br>**para** reponer mercadería con trazabilidad. | **Escenario 1: Flujo esperado**<br>**Given** una compra pendiente,<br>**When** recibo físicamente,<br>**Then** actualiza saldo y stock juntos. | — |

### 3.1.2. User Stories

#### 3.1.2.1. EPIC-01 · Autenticación y cuenta

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US01** | Registro de cuenta | **Como** visitante,<br>**deseo** registrar los datos de mi empresa,<br>**para** crear una cuenta administradora en CeTe. | **Escenario 1: Flujo esperado**<br>**Given** datos válidos y un RUC no registrado,<br>**When** solicita registro,<br>**Then** se crea la cuenta administradora y se informa el siguiente paso.<br><br>**Escenario 2: Validación**<br>**Given** un correo o RUC ya existente,<br>**When** solicita registro,<br>**Then** no se crea otra cuenta y se informa el error. |
| **US02** | Inicio de sesión | **Como** usuario registrado,<br>**deseo** autenticarme,<br>**para** acceder al espacio de trabajo de mi empresa. | **Escenario 1: Flujo esperado**<br>**Given** credenciales válidas,<br>**When** solicita acceso,<br>**Then** obtiene una sesión con su rol.<br><br>**Escenario 2: Validación**<br>**Given** credenciales incorrectas,<br>**When** solicita acceso,<br>**Then** recibe un error genérico sin revelar la existencia de la cuenta. |
| **US03** | Cierre de sesión | **Como** usuario autenticado,<br>**deseo** terminar mi sesión,<br>**para** proteger mi cuenta y la información del negocio. | **Escenario 1: Flujo esperado**<br>**Given** una sesión vigente,<br>**When** solicita cerrarla,<br>**Then** la sesión queda invalidada y es redirigido.<br><br>**Escenario 2: Validación**<br>**Given** una sesión ya cerrada,<br>**When** solicita un recurso protegido,<br>**Then** se rechaza el acceso. |
| **US04** | Recuperación de contraseña | **Como** usuario registrado,<br>**deseo** restablecer mi contraseña,<br>**para** recuperar acceso si la he olvidado. | **Escenario 1: Flujo esperado**<br>**Given** una solicitud con correo válido,<br>**When** la procesa el sistema,<br>**Then** devuelve confirmación genérica y envía enlace seguro.<br><br>**Escenario 2: Validación**<br>**Given** un enlace vencido o utilizado,<br>**When** intenta restablecer la contraseña,<br>**Then** se rechaza el cambio. |

#### 3.1.2.2. EPIC-02 · Gestión de Inventario

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US09** | Registro de Artículo (SKU) | **Como** operario,<br>**deseo** dar de alta un nuevo producto,<br>**para** que esté disponible<br>**para** futuras transacciones. | **Escenario 1: Flujo esperado**<br>**Given** datos válidos,<br>**When** guarda el registro,<br>**Then** el artículo se crea con stock inicial 0.<br><br>**Escenario 2: Validación**<br>**Given** un SKU ya existente,<br>**When** intenta registrarlo,<br>**Then** se rechaza la duplicación en la empresa. |
| **US10** | Ingreso de Mercadería | **Como** operario,<br>**deseo** sumar unidades físicas a un SKU existente,<br>**para** reflejar el abastecimiento del almacén. | **Escenario 1: Flujo esperado**<br>**Given** cantidad positiva,<br>**When** registra la entrada,<br>**Then** el stock total del SKU se incrementa atómicamente.<br><br>**Escenario 2: Validación**<br>**Given** cantidad negativa o nula,<br>**When** intenta registrar,<br>**Then** se impide la transacción. |
| **US11** | Salida Manual de Mercadería | **Como** operario,<br>**deseo** registrar el retiro manual de productos,<br>**para** reflejar consumos internos o ajustes. | **Escenario 1: Flujo esperado**<br>**Given** stock suficiente y motivo válido,<br>**When** registra la salida,<br>**Then** el inventario disminuye.<br><br>**Escenario 2: Validación**<br>**Given** retiro mayor al stock,<br>**When** solicita la acción,<br>**Then** emite alerta de insuficiencia. |
| **US12** | Registro de Mermas | **Como** operario,<br>**deseo** apartar productos dañados o caducados,<br>**para** evitar que sean vendidos por error. | **Escenario 1: Flujo esperado**<br>**Given** producto en mal estado,<br>**When** lo marca como merma,<br>**Then** se descuenta del stock y se registra como pérdida.<br><br>**Escenario 2: Validación**<br>**Given** producto marcado como merma,<br>**When** consulta Dashboard,<br>**Then** el costo impacta negativamente la rentabilidad. |
| **US13** | Buscador de Inventario | **Como** operario,<br>**deseo** buscar productos por nombre o SKU,<br>**para** localizarlos rápidamente sin listas largas. | **Escenario 1: Flujo esperado**<br>**Given** término coincidente,<br>**When** ingresa al menos 3 caracteres,<br>**Then** filtra la tabla en tiempo real.<br><br>**Escenario 2: Validación**<br>**Given** término sin coincidencias,<br>**When** busca,<br>**Then** obtiene resultado vacío sin errores. |
| **US14** | Historial de Movimientos | **Como** participante autorizado,<br>**deseo** ver el Kardex de un producto,<br>**para** auditar discrepancias o mermas. | **Escenario 1: Flujo esperado**<br>**Given** SKU con movimientos,<br>**When** consulta historial,<br>**Then** obtiene lista cronológica.<br><br>**Escenario 2: Validación**<br>**Given** producto recién creado,<br>**When** consulta historial,<br>**Then** tabla vacía sin error. |

#### 3.1.2.3. EPIC-03 · Transacciones Comerciales

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US15** | Armado de Orden de Venta | **Como** vendedor,<br>**deseo** agregar y editar productos en un listado de nueva venta,<br>**para** calcular el subtotal y total a cobrar. | **Escenario 1: Flujo esperado**<br>**Given** un catálogo con productos disponibles,<br>**When** selecciona artículos y cantidades,<br>**Then** se listan en la orden actualizando el subtotal.<br><br>**Escenario 2: Validación**<br>**Given** un intento de agregar un producto inactivo o inexistente,<br>**When** procesa la orden,<br>**Then** muestra un mensaje de error y bloquea la adición. |
| **US16** | Validación Automática de Stock | **Como** vendedor,<br>**deseo** bloqueo de productos agotados en caja,<br>**para** no prometer mercadería inexistente. | **Escenario 1: Flujo esperado**<br>**Given** producto con stock cero,<br>**When** intenta añadirlo,<br>**Then** botón se deshabilita preventivamente.<br><br>**Escenario 2: Validación**<br>**Given** 5 unidades y venta de 6,<br>**When** ingresa cantidad,<br>**Then** alerta exceso y ajusta al máximo. |
| **US17** | Historial de Ventas | **Como** participante autorizado,<br>**deseo** consultar transacciones pasadas,<br>**para** llevar el control de ingresos diarios. | **Escenario 1: Flujo esperado**<br>**Given** ventas registradas,<br>**When** consulta módulo,<br>**Then** las obtiene ordenadas por fecha.<br><br>**Escenario 2: Validación**<br>**Given** filtro de fechas invertido,<br>**When** intenta aplicar,<br>**Then** solicita corregir el rango. |
| **US18** | Anulación de Venta | **Como** dueño,<br>**deseo** revertir una venta equivocada,<br>**para** corregir métricas y devolver stock. | **Escenario 1: Flujo esperado**<br>**Given** venta completada,<br>**When** solicita anulación,<br>**Then** estado pasa a "Anulada" y stock se reintegra atómicamente.<br><br>**Escenario 2: Validación**<br>**Given** venta ya anulada,<br>**When** intenta anularla,<br>**Then** bloquea acción para evitar duplicidad. |
| **US35** | Procesamiento de Pago de Venta | **Como** vendedor,<br>**deseo** confirmar el método de pago y finalizar la transacción,<br>**para** formalizar el ingreso comercial. | **Escenario 1: Flujo esperado**<br>**Given** una orden armada y válida,<br>**When** confirma el método de pago,<br>**Then** la venta pasa a estado completado y se genera el comprobante.<br><br>**Escenario 2: Validación**<br>**Given** problemas de conexión con el servicio de cobro,<br>**When** la transacción falla,<br>**Then** aplica rollback al pago y notifica el error sin alterar la orden. |
| **US36** | Descuento Automático de Stock | **Como** dueño,<br>**deseo** que al confirmar una venta se reduzca automáticamente el inventario,<br>**para** evitar el doble registro manual y descuadres. | **Escenario 1: Flujo esperado**<br>**Given** una venta completada exitosamente,<br>**When** el sistema procesa el cierre de la transacción,<br>**Then** se descuentan atómicamente las unidades vendidas del stock del almacén.<br><br>**Escenario 2: Validación**<br>**Given** una venta que supera el stock físico de un producto en el último segundo,<br>**When** intenta descontar,<br>**Then** bloquea la finalización, aplica rollback y alerta al vendedor. |
| **US39** | Visualizar e imprimir boleta | **Como** vendedor,<br>**deseo** consultar e imprimir el comprobante de una venta,<br>**para** entregar al cliente el detalle de su compra. | **Escenario 1: Flujo esperado**<br>**Given** una venta confirmada,<br>**When** abro la boleta,<br>**Then** veo empresa, RUC, orden, fecha/hora de Lima, dirección, vendedor, cliente, productos, cantidades, precios y total.<br><br>**Escenario 2: Validación**<br>**Given** cambios posteriores de catálogo,<br>**When** consulto la boleta,<br>**Then** conserva sus datos históricos.<br><br>**Escenario 3: Validación**<br>**Given** una venta ajena,<br>**When** solicito la boleta,<br>**Then** responde 404. |

#### 3.1.2.4. EPIC-04 · Logística y Despacho

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US19** | Manifiesto de Despacho | **Como** logístico,<br>**deseo** agrupar ventas en un manifiesto,<br>**para** ordenar la ruta de entrega. | **Escenario 1: Flujo esperado**<br>**Given** ventas pendientes,<br>**When** selecciona y crea manifiesto,<br>**Then** se genera documento consolidado.<br><br>**Escenario 2: Validación**<br>**Given** ventas ya despachadas,<br>**When** intenta agruparlas,<br>**Then** el sistema las oculta o bloquea. |
| **US20** | Asignación de Conductor | **Como** logístico,<br>**deseo** vincular recursos al manifiesto,<br>**para** establecer responsables de entrega. | **Escenario 1: Flujo esperado**<br>**Given** manifiesto y recursos disponibles,<br>**When** asigna chofer y placa,<br>**Then** datos quedan vinculados al despacho.<br><br>**Escenario 2: Validación**<br>**Given** chofer ocupado,<br>**When** intenta asignarlo,<br>**Then** advierte sobre superposición. |
| **US21** | Actualización de Estado | **Como** logístico,<br>**deseo** cambiar el estado del envío,<br>**para** notificar su entrega efectiva. | **Escenario 1: Flujo esperado**<br>**Given** despacho "En Ruta",<br>**When** lo marca "Entregado",<br>**Then** ventas asociadas finalizan su ciclo.<br><br>**Escenario 2: Validación**<br>**Given** estado ilógico,<br>**When** intenta retroceder,<br>**Then** impide la transición. |
| **US22** | Incidencia en Ruta | **Como** logístico,<br>**deseo** anotar contratiempos logísticos,<br>**para** auditar retrasos en entregas. | **Escenario 1: Flujo esperado**<br>**Given** despacho activo,<br>**When** reporta incidente,<br>**Then** nota queda vinculada a la ruta.<br><br>**Escenario 2: Validación**<br>**Given** ruta sin eventos,<br>**When** consulta incidencias,<br>**Then** vista limpia sin errores. |

#### 3.1.2.5. EPIC-05 · Dashboard y Rentabilidad

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US23** | Dashboard: Tarjetas de Indicadores (KPIs) | **Como** dueño,<br>**deseo** visualizar tarjetas numéricas con métricas clave (ingresos del día, número de ventas),<br>**para** conocer el estado actual de un vistazo. | **Escenario 1: Flujo esperado**<br>**Given** datos financieros activos,<br>**When** carga el dashboard,<br>**Then** visualiza tarjetas con los totales de ingresos y operaciones al día de hoy.<br><br>**Escenario 2: Validación**<br>**Given** un negocio reciente sin datos procesados,<br>**When** carga las tarjetas,<br>**Then** visualiza los montos en cero sin que el sistema arroje errores. |
| **US24** | Reporte de Top Productos | **Como** dueño,<br>**deseo** identificar los artículos más vendidos,<br>**para** priorizar abastecimiento. | **Escenario 1: Flujo esperado**<br>**Given** ventas en el mes,<br>**When** consulta ranking,<br>**Then** obtiene lista descendente precisa.<br><br>**Escenario 2: Validación**<br>**Given** empate en ventas,<br>**When** genera reporte,<br>**Then** comparten posición alfabéticamente. |
| **US25** | Exportación de Datos | **Como** participante autorizado,<br>**deseo** descargar mis tablas a CSV,<br>**para** enviarlas a contabilidad. | **Escenario 1: Flujo esperado**<br>**Given** tabla filtrada en pantalla,<br>**When** hace clic en exportar,<br>**Then** descarga CSV respetando filtro activo.<br><br>**Escenario 2: Validación**<br>**Given** tabla vacía,<br>**When** intenta exportar,<br>**Then** archivo contiene solo cabeceras. |
| **US37** | Dashboard: Gráfico de Tendencias | **Como** dueño,<br>**deseo** visualizar un gráfico de barras/líneas con los ingresos en el tiempo,<br>**para** analizar el comportamiento financiero de la MYPE. | **Escenario 1: Flujo esperado**<br>**Given** transacciones históricas registradas,<br>**When** consulta el gráfico en el panel,<br>**Then** visualiza la tendencia de ventas agrupada por día o mes.<br><br>**Escenario 2: Validación**<br>**Given** un rango de fechas filtrado donde no hubo operaciones,<br>**When** filtra el gráfico,<br>**Then** muestra el lienzo en blanco con un mensaje amigable indicando que no hay datos. |
| **US38** | Dashboard: Panel de Resumen de Inventario | **Como** dueño,<br>**deseo** ver una sección en el dashboard que liste rápidamente los productos próximos a agotarse,<br>**para** tomar decisiones inmediatas de reabastecimiento. | **Escenario 1: Flujo esperado**<br>**Given** productos con stock por debajo de su cantidad mínima establecida,<br>**When** carga el panel principal,<br>**Then** los lista ordenados por nivel de criticidad (del más urgente al menos urgente).<br><br>**Escenario 2: Validación**<br>**Given** un inventario en estado óptimo,<br>**When** carga el panel de resumen,<br>**Then** muestra un indicador visual confirmando que todo el stock está saludable. |

#### 3.1.2.6. EPIC-06 · Notificaciones y Alertas

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US26** | Alerta de Stock Mínimo | **Como** participante autorizado,<br>**deseo** recibir avisos al acercarme a cero,<br>**para** reponer mercadería a tiempo. | **Escenario 1: Flujo esperado**<br>**Given** SKU con límite configurado,<br>**When** stock perfora límite,<br>**Then** dispara alerta visual.<br><br>**Escenario 2: Validación**<br>**Given** alerta ya enviada,<br>**When** stock baja más,<br>**Then** no duplica notificación. |
| **US27** | Alerta de Producto Vencido | **Como** almacenero,<br>**deseo** avisos preventivos de caducidad,<br>**para** ofertar artículos perecibles. | **Escenario 1: Flujo esperado**<br>**Given** lotes con caducidad,<br>**When** alcanza umbral de 7 días,<br>**Then** artículos se resaltan en rojo.<br><br>**Escenario 2: Validación**<br>**Given** producto ya vencido,<br>**When** intenta vender,<br>**Then** emite doble alerta de confirmación. |

#### 3.1.2.7. EPIC-07 · Roles y Permisos

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US28** | Creación de Usuarios | **Como** administrador,<br>**deseo** crear cuentas<br>**para** mis trabajadores,<br>**para** delegar accesos seguros. | **Escenario 1: Flujo esperado**<br>**Given** correo nuevo y rol elegido,<br>**When** envía invitación,<br>**Then** empleado recibe acceso.<br><br>**Escenario 2: Validación**<br>**Given** correo que ya pertenece a la empresa,<br>**When** intenta agregarlo,<br>**Then** indica que el usuario ya existe. |
| **US29** | Restricción por Roles | **Como** administrador,<br>**deseo** definir niveles de acceso operacionales,<br>**para** bloquear módulos confidenciales. | **Escenario 1: Flujo esperado**<br>**Given** usuario con rol almacenero,<br>**When** navega por menú,<br>**Then** no visualiza enlace a reportes.<br><br>**Escenario 2: Validación**<br>**Given** intento de acceso directo por URL a recurso prohibido,<br>**When** ejecuta petición,<br>**Then** API devuelve 403 Forbidden. |

#### 3.1.2.8. EPIC-08 · Perfil y preferencias

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US30** | Edición de Perfil Empresa | **Como** administrador,<br>**deseo** actualizar mis datos comerciales,<br>**para** mantener facturas e interfaz personalizadas. | **Escenario 1: Flujo esperado**<br>**Given** datos válidos,<br>**When** guarda actualización,<br>**Then** header refleja cambios.<br><br>**Escenario 2: Validación**<br>**Given** intento de modificar RUC base,<br>**When** guarda,<br>**Then** bloquea acción por seguridad fiscal. |
| **US31** | Cambio de Contraseña | **Como** usuario registrado,<br>**deseo** actualizar mi clave,<br>**para** asegurar mi cuenta. | **Escenario 1: Flujo esperado**<br>**Given** clave actual correcta y nueva válida,<br>**When** confirma cambio,<br>**Then** actualiza y cierra otras sesiones activas.<br><br>**Escenario 2: Validación**<br>**Given** contraseña actual incorrecta,<br>**When** intenta cambiarla,<br>**Then** rechaza la acción. |
| **US33** | Idioma de la aplicación | **Como** usuario,<br>**deseo** elegir inglés o español,<br>**para** comprender la interfaz a mi gusto. | **Escenario 1: Flujo esperado**<br>**Given** selector de idioma,<br>**When** elige "English",<br>**Then** textos estáticos se traducen al instante.<br><br>**Escenario 2: Validación**<br>**Given** contenido ingresado por usuario,<br>**When** cambia idioma,<br>**Then** dicho texto no se altera. |

#### 3.1.2.9. EPIC-09 · Landing page

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US05** | Propuesta de valor en landing | **Como** visitante,<br>**deseo** conocer la propuesta de valor de CeTe,<br>**para** evaluar si soluciona mis problemas operativos. | **Escenario 1: Flujo esperado**<br>**Given** acceso a la landing,<br>**When** consulta la propuesta,<br>**Then** identifica el problema logístico y la solución centralizada.<br><br>**Escenario 2: Validación**<br>**Given** acceso desde móvil,<br>**When** consulta la propuesta,<br>**Then** el contenido conserva legibilidad y diseño responsivo. |
| **US06** | Funcionalidades de landing | **Como** visitante,<br>**deseo** conocer las capacidades del producto,<br>**para** comprobar si cubre mis necesidades de negocio. | **Escenario 1: Flujo esperado**<br>**Given** consulta de capacidades,<br>**When** revisa su alcance,<br>**Then** encuentra módulos de inventario, ventas y reportes descritos.<br><br>**Escenario 2: Validación**<br>**Given** un usuario navegando,<br>**When** hace clic en funcionalidad en construcción,<br>**Then** el sistema informa que estará disponible próximamente. |
| **US07** | Modelo comercial y planes | **Como** visitante,<br>**deseo** consultar modalidades y planes de suscripción,<br>**para** evaluar una posible contratación<br>**para** mi MYPE. | **Escenario 1: Flujo esperado**<br>**Given** modalidades publicadas,<br>**When** las consulta,<br>**Then** distingue límites de usuarios y costos.<br><br>**Escenario 2: Validación**<br>**Given** selección de un plan,<br>**When** continúa el flujo,<br>**Then** es dirigido al registro con plan preseleccionado sin ejecutar cobros inmediatos. |
| **US08** | Contacto B2B | **Como** visitante corporativo,<br>**deseo** enviar un mensaje a ventas,<br>**para** solicitar una demostración personalizada. | **Escenario 1: Flujo esperado**<br>**Given** datos de contacto válidos,<br>**When** envía el formulario,<br>**Then** confirma el envío y notifica al equipo.<br><br>**Escenario 2: Validación**<br>**Given** un correo con formato inválido,<br>**When** intenta enviar,<br>**Then** resalta el error y bloquea el envío. |
| **US32** | Testimonios (Landing) | **Como** visitante,<br>**deseo** consultar experiencias de otras MYPES,<br>**para** ganar confianza. | **Escenario 1: Flujo esperado**<br>**Given** testimonios aprobados,<br>**When** hace scroll,<br>**Then** visualiza tarjetas.<br><br>**Escenario 2: Validación**<br>**Given** fallo de conexión,<br>**When** carga testimonios,<br>**Then** se oculta elegantemente. |
| **US34** | Términos del Servicio | **Como** visitante,<br>**deseo** leer las condiciones legales,<br>**para** conocer el uso de mi data. | **Escenario 1: Flujo esperado**<br>**Given** enlace en el footer,<br>**When** hace clic,<br>**Then** despliega políticas.<br><br>**Escenario 2: Validación**<br>**Given** lectura en móvil,<br>**When** abre términos,<br>**Then** texto es totalmente responsivo y legible. |
| **US42** | Idioma de landing y recursos | **Como** visitante,<br>**deseo** usar la landing y sus recursos en inglés o español,<br>**para** comprender la propuesta y continuar al producto. | **Escenario 1: Flujo esperado**<br>**Given** una primera visita,<br>**When** abro la landing,<br>**Then** usa en_US.<br><br>**Escenario 2: Validación**<br>**Given** es_419 seleccionado,<br>**When** recargo o abro guía, términos, privacidad y ética,<br>**Then** conserva el español.<br><br>**Escenario 3: Validación**<br>**Given** un móvil de 390px,<br>**When** navego,<br>**Then** el menú funciona sin desbordamiento. |

#### 3.1.2.10. EPIC-10 · Abastecimiento

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **US40** | Registrar orden de compra | **Como** encargado de almacén,<br>**deseo** registrar una orden a un proveedor,<br>**para** organizar el reabastecimiento sin confundirlo con la recepción física. | **Escenario 1: Flujo esperado**<br>**Given** proveedor y un producto con cantidad y costo válidos,<br>**When** creo la orden,<br>**Then** queda pendiente sin modificar stock.<br><br>**Escenario 2: Validación**<br>**Given** datos inválidos,<br>**When** envío la orden,<br>**Then** se rechaza sin crear registros. |
| **US41** | Recibir compra parcialmente | **Como** encargado de almacén,<br>**deseo** registrar entregas parciales,<br>**para** controlar el stock recibido y el saldo de una compra. | **Escenario 1: Flujo esperado**<br>**Given** una compra de 10 unidades,<br>**When** recibo 4 y luego 6,<br>**Then** registra ambas recepciones y suma 10 al stock.<br><br>**Escenario 2: Validación**<br>**Given** 6 pendientes,<br>**When** intento recibir 7,<br>**Then** rechaza sin modificar stock. |

### 3.1.3. Technical Stories

Los contratos pendientes se conservan como requisitos de evolución. Su presencia en esta tabla no significa que existan en Swagger. El estado se consulta en el Product Backlog.

#### 3.1.3.1. EPIC-01 · Autenticación y cuenta

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS01** | POST /api/v1/authentication/sign-up | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** datos nuevos de cuenta y empresa,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con cuenta y empresa.<br><br>**Escenario 2: Validación**<br>**Given** correo o RUC duplicado,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409. |
| **TS02** | POST /api/v1/authentication/sign-in | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** credenciales correctas,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con token y perfil.<br><br>**Escenario 2: Validación**<br>**Given** contraseña incorrecta,<br>**When** ejecuta el contrato,<br>**Then** obtiene 401 genérico. |
| **TS03** | POST /api/v1/authentication/sign-out | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** sesión vigente,<br>**When** ejecuta el contrato,<br>**Then** obtiene 204 y sesión revocada.<br><br>**Escenario 2: Validación**<br>**Given** token ya revocado en una consulta posterior,<br>**When** ejecuta el contrato,<br>**Then** obtiene 401. |
| **TS04** | POST /api/v1/auth/password-reset | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar US04. | **Escenario 1: Flujo esperado**<br>**Given** solicitud válida,<br>**When** servidor procesa,<br>**Then** responde 202 Accepted genérico.<br><br>**Escenario 2: Validación**<br>**Given** solicitudes masivas,<br>**When** procesa,<br>**Then** limita reintentos por rate limiting. |
| **TS32** | Docker y publicación de API y PostgreSQL | **Como** Developer,<br>**deseo** soportar US01 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** API y PostgreSQL configurados,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 en /health y persistencia tras reinicio.<br><br>**Escenario 2: Validación**<br>**Given** base inaccesible después de iniciar el servidor,<br>**When** ejecuta el contrato,<br>**Then** obtiene 503 en /health sin exponer secretos. |

#### 3.1.3.2. EPIC-02 · Gestión de Inventario

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS05** | GET /api/v1/inventory | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** sesión vigente,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con productos de la empresa.<br><br>**Escenario 2: Validación**<br>**Given** petición sin token,<br>**When** ejecuta el contrato,<br>**Then** obtiene 401. |
| **TS06** | POST /api/v1/inventory | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** SKU nuevo y precio válido,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con producto de stock cero.<br><br>**Escenario 2: Validación**<br>**Given** SKU ya registrado,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409. |
| **TS07** | POST /api/v1/inventory/{id}/entries | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** producto propio, cantidad positiva y motivo,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con stock y movimiento.<br><br>**Escenario 2: Validación**<br>**Given** producto de otra empresa,<br>**When** ejecuta el contrato,<br>**Then** obtiene 404. |
| **TS08** | POST /api/v1/inventory/{id}/exits | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** stock suficiente, cantidad positiva y motivo,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con stock y movimiento.<br><br>**Escenario 2: Validación**<br>**Given** cantidad mayor al stock,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409 sin cambios parciales. |
| **TS09** | GET /api/v1/inventory/{id}/history | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** producto propio,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con historial.<br><br>**Escenario 2: Validación**<br>**Given** producto ajeno,<br>**When** ejecuta el contrato,<br>**Then** obtiene 404. |

#### 3.1.3.3. EPIC-03 · Transacciones Comerciales

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS10** | GET /api/v1/sales | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** sesión vigente,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con ventas propias.<br><br>**Escenario 2: Validación**<br>**Given** petición sin token,<br>**When** ejecuta el contrato,<br>**Then** obtiene 401. |
| **TS11** | POST /api/v1/sales | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** orden válida y stock suficiente,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con venta, pago registrado y boleta atómicos.<br><br>**Escenario 2: Validación**<br>**Given** stock insuficiente en una línea,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409 y rollback completo. |
| **TS12** | GET /api/v1/sales/{id} | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar detalle de venta. | **Escenario 1: Flujo esperado**<br>**Given** solicitud de ID,<br>**When** servidor procesa,<br>**Then** responde 200 OK con ítems asociados.<br><br>**Escenario 2: Validación**<br>**Given** venta de otro tenant,<br>**When** procesa,<br>**Then** responde 403 Forbidden. |
| **TS13** | PATCH /api/v1/sales/{id}/cancel | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** administrador y venta completada sin despacho,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con anulación y reposición única.<br><br>**Escenario 2: Validación**<br>**Given** venta ya anulada,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409 sin reponer nuevamente. |
| **TS28** | GET /api/v1/sales/{id}/receipt | **Como** Developer,<br>**deseo** soportar US39 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** venta propia confirmada,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con instantánea histórica.<br><br>**Escenario 2: Validación**<br>**Given** venta de otra empresa,<br>**When** ejecuta el contrato,<br>**Then** obtiene 404. |
| **TS31** | Idempotencia y transacción serializable | **Como** Developer,<br>**deseo** soportar US35 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** UUID ya procesado y mismo contenido,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con la venta existente sin duplicar stock ni pago.<br><br>**Escenario 2: Validación**<br>**Given** mismo UUID con contenido diferente,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409. |
| **TS34** | Pruebas de dominio, HTTP y navegador | **Como** Developer,<br>**deseo** soportar US39 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** servicios de prueba disponibles,<br>**When** ejecuta el contrato,<br>**Then** obtiene suite de dominio, HTTP y navegador aprobada.<br><br>**Escenario 2: Validación**<br>**Given** incumplimiento de un resultado esperado,<br>**When** ejecuta el contrato,<br>**Then** obtiene código de salida no cero y diagnóstico sin credenciales. |

#### 3.1.3.4. EPIC-04 · Logística y Despacho

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS14** | GET /api/v1/dispatches | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** sesión vigente,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con despachos propios.<br><br>**Escenario 2: Validación**<br>**Given** petición sin token,<br>**When** ejecuta el contrato,<br>**Then** obtiene 401. |
| **TS15** | POST /api/v1/dispatches | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** ventas y recursos disponibles,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con despacho y asociaciones.<br><br>**Escenario 2: Validación**<br>**Given** venta ya asignada,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409. |
| **TS16** | PUT /api/v1/dispatches/{id} | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** despacho PENDING y estado solicitado IN_TRANSIT,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con transición.<br><br>**Escenario 2: Validación**<br>**Given** despacho PENDING y salto a DELIVERED,<br>**When** ejecuta el contrato,<br>**Then** obtiene 409. |
| **TS17** | POST /api/v1/dispatches/{id}/incidents | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** despacho IN_TRANSIT y descripción no vacía,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con incidencia y estado INCIDENT.<br><br>**Escenario 2: Validación**<br>**Given** descripción vacía,<br>**When** ejecuta el contrato,<br>**Then** obtiene 422. |

#### 3.1.3.5. EPIC-05 · Dashboard y Rentabilidad

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS18** | GET /api/v1/analytics/dashboard | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** administrador autenticado,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con métricas propias y día de Lima.<br><br>**Escenario 2: Validación**<br>**Given** rol Warehouse,<br>**When** ejecuta el contrato,<br>**Then** obtiene 403. |
| **TS35** | GET /api/v1/integrations/exchange-rates | **Como** Developer,<br>**deseo** soportar US23 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** proveedor externo disponible,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con USD/PEN, fuente y actualización.<br><br>**Escenario 2: Validación**<br>**Given** error HTTP o timeout del proveedor,<br>**When** ejecuta el contrato,<br>**Then** obtiene 503. |

#### 3.1.3.6. EPIC-06 · Notificaciones y Alertas

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS19** | GET /api/v1/notifications | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar alertas de sistema. | **Escenario 1: Flujo esperado**<br>**Given** solicitud autorizada,<br>**When** servidor procesa,<br>**Then** responde 200 OK con array de alertas no leídas.<br><br>**Escenario 2: Validación**<br>**Given** sin sesión,<br>**When** procesa,<br>**Then** responde 401 Unauthorized sin cruzar datos. |
| **TS20** | PATCH /api/v1/notifications/{id}/read | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** marcar alertas leídas. | **Escenario 1: Flujo esperado**<br>**Given** ID de alerta válido,<br>**When** servidor procesa,<br>**Then** responde 200 OK actualizando isRead.<br><br>**Escenario 2: Validación**<br>**Given** alerta ajena,<br>**When** procesa,<br>**Then** responde 404 Not Found. |

#### 3.1.3.7. EPIC-07 · Roles y Permisos

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS21** | GET /api/v1/users | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** administrador autenticado,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con usuarios sin contraseñas ni hashes.<br><br>**Escenario 2: Validación**<br>**Given** rol Warehouse,<br>**When** ejecuta el contrato,<br>**Then** obtiene 403. |
| **TS22** | POST /api/v1/users | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar el flujo de negocio asociado. | **Escenario 1: Flujo esperado**<br>**Given** administrador y empleado nuevo con rol permitido,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con perfil.<br><br>**Escenario 2: Validación**<br>**Given** rol no permitido,<br>**When** ejecuta el contrato,<br>**Then** obtiene 422. |
| **TS33** | Aislamiento de empresa y relaciones compuestas | **Como** Developer,<br>**deseo** soportar US29 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** sesión de empresa A y recurso de A,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 para la operación permitida.<br><br>**Escenario 2: Validación**<br>**Given** sesión de A y boleta de B,<br>**When** ejecuta el contrato,<br>**Then** obtiene 404 sin revelar datos ajenos. |

#### 3.1.3.8. EPIC-08 · Perfil y preferencias

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS23** | GET /api/v1/users/profile | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** cargar la vista de cuenta. | **Escenario 1: Flujo esperado**<br>**Given** solicitud válida,<br>**When** servidor procesa,<br>**Then** responde 200 OK con datos personales e idioma.<br><br>**Escenario 2: Validación**<br>**Given** condición inválida,<br>**When** procesa,<br>**Then** responde 401 sin sesión válida. |
| **TS24** | PUT /api/v1/users/profile | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar US30. | **Escenario 1: Flujo esperado**<br>**Given** datos editables válidos,<br>**When** servidor procesa,<br>**Then** responde 200 OK persistiendo cambios.<br><br>**Escenario 2: Validación**<br>**Given** payload inyectando cambio de rol,<br>**When** procesa,<br>**Then** ignora el campo o responde 400 Bad Request. |
| **TS25** | PUT /api/v1/users/password | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar US31. | **Escenario 1: Flujo esperado**<br>**Given** claves correctas,<br>**When** servidor procesa,<br>**Then** responde 204 No Content hasheando y guardando.<br><br>**Escenario 2: Validación**<br>**Given** hash actual incorrecto,<br>**When** procesa,<br>**Then** responde 400 Bad Request sin alterar credenciales. |

#### 3.1.3.9. EPIC-09 · Landing page

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS26** | POST /api/v1/contact-messages | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar US08. | **Escenario 1: Flujo esperado**<br>**Given** formulario público válido,<br>**When** servidor procesa,<br>**Then** responde 201 Created guardando solicitud.<br><br>**Escenario 2: Validación**<br>**Given** ataques por bots,<br>**When** procesa,<br>**Then** devuelve 429 Too Many Requests. |
| **TS27** | GET /api/v1/landing/plans | **Como** Developer,<br>**deseo** disponer de este contrato<br>**para** soportar US07. | **Escenario 1: Flujo esperado**<br>**Given** petición pública a la landing,<br>**When** servidor procesa,<br>**Then** responde 200 OK renderizando planes actuales.<br><br>**Escenario 2: Validación**<br>**Given** error de conectividad interna,<br>**When** procesa,<br>**Then** responde 500 Internal Server Error seguro. |

#### 3.1.3.10. EPIC-10 · Abastecimiento

| Story ID | Título | Historia | Criterios de aceptación |
| :--- | :--- | :--- | :--- |
| **TS29** | GET y POST /api/v1/purchases | **Como** Developer,<br>**deseo** soportar US40 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** proveedor, producto, cantidad y costo válidos,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con orden sin aumentar stock.<br><br>**Escenario 2: Validación**<br>**Given** cantidad no positiva,<br>**When** ejecuta el contrato,<br>**Then** obtiene 422. |
| **TS30** | POST /api/v1/purchases/{id}/receive | **Como** Developer,<br>**deseo** soportar US41 mediante este habilitador. | **Escenario 1: Flujo esperado**<br>**Given** compra con seis unidades pendientes y recepción de seis,<br>**When** ejecuta el contrato,<br>**Then** obtiene 200 con compra recibida y stock actualizado.<br><br>**Escenario 2: Validación**<br>**Given** seis pendientes e intento de recibir siete,<br>**When** ejecuta el contrato,<br>**Then** obtiene 422 sin alterar stock. |

## 3.2. Impact Mapping

En esta sección se presenta el Impact Mapping del modelo de negocio CeTe. Esto nos permite visualizar de manera estructurada los objetivos estratégicos del proyecto y cómo estos se relacionan con los actores involucrados y las funcionalidades que se implementarán, asegurándonos de que cada característica del producto tenga un propósito claro y medible.

<p align="center">
  <img src="Images/Impact-Mapping-1.png" width="800" alt="Impact Mapping de CeTe">
  <br><em>Figura 1: Captura del Impact Mapping hecho en UXPressia</em>
</p>

El Impact Mapping elaborado para CeTe ilustra de manera estratégica cómo las funcionalidades de nuestra plataforma tecnológica contribuyen a alcanzar nuestros objetivos de negocio. Para esta fase del proyecto, hemos definido un objetivo SMART (Business Goal) enfocado tanto en la adopción empresarial como en la penetración en el usuario final.

**Alineación del Business Goal 1:** Alcanzar 30 negocios (MYPES) suscritos a los planes de pago de CeTe en los primeros 6 meses tras el lanzamiento oficial de la plataforma. Para alcanzar esta meta, hemos identificado a tres actores clave del sector comercial que nos permitirán materializarla: los dueños/administradores de negocio, el personal logístico/almaceneros y los visitantes potenciales.
- En el caso de los dueños/administradores de negocio, el impacto que necesitamos generar es que monitoreen la salud y rentabilidad de su empresa en tiempo real, dejando atrás la incertidumbre de no saber dónde está su mercadería o si están ganando dinero. Como solución digital, provocaremos este impacto construyendo un Dashboard Gerencial y Analítico (Deliverable), el cual se materializa en historias de usuario enfocadas en consolidar métricas financieras, visualizar top de ventas y gestionar los roles de acceso (US23, US24, US25, US28, US29).
- Por el lado del personal logístico/almaceneros, el impacto esperado es que adopten CeTe como su canal centralizado para registrar ingresos y salidas, abandonando totalmente los conteos manuales y reportes en cuadernos. Para facilitar este comportamiento, implementaremos un Módulo de Inventario Inteligente (Deliverable), soportado por funcionalidades que permiten registrar entradas y mermas en segundos, buscar artículos ágilmente y generar notificaciones automáticas de stock mínimo y vencimientos (US09, US10, US11, US12, US13, US14, US26, US27).
- En cuanto a los visitantes MYPE, el impacto deseado es la comprensión rápida de la propuesta de valor para motivarlos a suscribirse. Para ello, implementaremos un Landing Page persuasivo (Deliverable), soportado por historias para visualizar planes, testimonios y el formulario de registro (US05, US06, US07, US08, US32, US34).

### 3.2.1. Metas medibles de validación AV2

Son hipótesis propuestas, todavía sin resultados ni línea base.

| Meta y plazo | Actor e impacto | Medición | US |
| :--- | :--- | :--- | :--- |
| G1. Reducir 30% el tiempo de una venta durante la ronda AV2. | Vendedor entrega una boleta con menos pasos. | Cronometrar el mismo caso antes y con CeTe y comparar medianas. | US15, US35, US36, US39 |
| G2. Lograr 90% de coincidencia del stock durante la validación AV2. | Operario distingue orden de compra y recepción física. | Conciliar inicial + recepciones - ventas - salidas + anulaciones con 3–5 operativos. | US10, US11, US14, US40, US41 |
| G3. Lograr 80% de éxito sin ayuda al consultar boleta y cambiar idioma en AV2. | Ambos segmentos comprenden el producto. | Registrar éxito, tiempo y errores con 3–5 personas por segmento. | US33, US39, US42 |

## 3.3. Product Backlog

La prioridad parte del valor de los flujos de venta, inventario, abastecimiento y entrega. La autenticación es una dependencia técnica. Esta revisión incluye 42 US y 35 TS como filas explícitas.

Los SP propuestos estiman complejidad e incertidumbre, no horas. Las TS vinculadas se incluyen en sus US para evitar una doble suma. Las tareas de ingeniería y horas se presentan por separado en 5.2.3. El estado «En revisión» señala que existe un incremento técnico relacionado; la aceptación completa de la historia requiere revisar todos sus criterios con el equipo. Los contratos que no existen siguen como pendientes.

### 3.3.1. Prioridades 1–20

| Orden | ID | Tipo | Título | Valor / US asociada | SP propuestos | Estado verificable |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 1 | US15 | US | Armado de Orden de Venta | Calcular el subtotal y total a cobrar. | 3 | En revisión |
| 2 | US35 | US | Procesamiento de Pago de Venta | Formalizar el ingreso comercial. | 3 | Parcial: pago registrado, sin pasarela |
| 3 | TS11 | TS | POST /api/v1/sales | US35 | Incluido en US | En revisión |
| 4 | TS31 | TS | Idempotencia y transacción serializable | US35 | Incluido en US | En revisión |
| 5 | US36 | US | Descuento Automático de Stock | Evitar el doble registro manual y descuadres. | 2 | En revisión |
| 6 | US39 | US | Visualizar e imprimir boleta | Entregar al cliente el detalle de su compra. | 5 | En revisión |
| 7 | TS12 | TS | GET /api/v1/sales/{id} | US39 | Incluido en US | Pendiente |
| 8 | TS28 | TS | GET /api/v1/sales/{id}/receipt | US39 | Incluido en US | En revisión |
| 9 | TS34 | TS | Pruebas de dominio, HTTP y navegador | US39 | Incluido en US | En revisión |
| 10 | US09 | US | Registro de Artículo (SKU) | Que esté disponible para futuras transacciones. | 3 | En revisión |
| 11 | TS06 | TS | POST /api/v1/inventory | US09 | Incluido en US | En revisión |
| 12 | US10 | US | Ingreso de Mercadería | Reflejar el abastecimiento del almacén. | 5 | En revisión |
| 13 | TS07 | TS | POST /api/v1/inventory/{id}/entries | US10 | Incluido en US | En revisión |
| 14 | US11 | US | Salida Manual de Mercadería | Reflejar consumos internos o ajustes. | 3 | En revisión |
| 15 | TS08 | TS | POST /api/v1/inventory/{id}/exits | US11 | Incluido en US | En revisión |
| 16 | US14 | US | Historial de Movimientos | Auditar discrepancias o mermas. | 3 | En revisión |
| 17 | TS09 | TS | GET /api/v1/inventory/{id}/history | US14 | Incluido en US | En revisión |
| 18 | US40 | US | Registrar orden de compra | Organizar el reabastecimiento sin confundirlo con la recepción física. | 5 | En revisión |
| 19 | TS29 | TS | GET y POST /api/v1/purchases | US40 | Incluido en US | En revisión |
| 20 | US41 | US | Recibir compra parcialmente | Controlar el stock recibido y el saldo de una compra. | 5 | En revisión |

### 3.3.2. Prioridades 21–40

| Orden | ID | Tipo | Título | Valor / US asociada | SP propuestos | Estado verificable |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 21 | TS30 | TS | POST /api/v1/purchases/{id}/receive | US41 | Incluido en US | En revisión |
| 22 | US19 | US | Manifiesto de Despacho | Ordenar la ruta de entrega. | 5 | En revisión |
| 23 | TS14 | TS | GET /api/v1/dispatches | US19 | Incluido en US | En revisión |
| 24 | TS15 | TS | POST /api/v1/dispatches | US19 | Incluido en US | En revisión |
| 25 | US20 | US | Asignación de Conductor | Establecer responsables de entrega. | 3 | En revisión |
| 26 | US21 | US | Actualización de Estado | Notificar su entrega efectiva. | 3 | En revisión |
| 27 | TS16 | TS | PUT /api/v1/dispatches/{id} | US21 | Incluido en US | En revisión |
| 28 | US22 | US | Incidencia en Ruta | Auditar retrasos en entregas. | 3 | En revisión |
| 29 | TS17 | TS | POST /api/v1/dispatches/{id}/incidents | US22 | Incluido en US | En revisión |
| 30 | US23 | US | Dashboard: Tarjetas de Indicadores (KPIs) | Conocer el estado actual de un vistazo. | 3 | En revisión |
| 31 | TS18 | TS | GET /api/v1/analytics/dashboard | US23 | Incluido en US | En revisión |
| 32 | TS35 | TS | GET /api/v1/integrations/exchange-rates | US23 | Incluido en US | En revisión |
| 33 | US38 | US | Dashboard: Panel de Resumen de Inventario | Tomar decisiones inmediatas de reabastecimiento. | 2 | En revisión |
| 34 | US17 | US | Historial de Ventas | Llevar el control de ingresos diarios. | 3 | Parcial: filtro de fechas pendiente |
| 35 | TS10 | TS | GET /api/v1/sales | US17 | Incluido en US | En revisión |
| 36 | US18 | US | Anulación de Venta | Corregir métricas y devolver stock. | 5 | En revisión |
| 37 | TS13 | TS | PATCH /api/v1/sales/{id}/cancel | US18 | Incluido en US | En revisión |
| 38 | US26 | US | Alerta de Stock Mínimo | Reponer mercadería a tiempo. | 5 | Parcial: alerta visual, bandeja pendiente |
| 39 | TS19 | TS | GET /api/v1/notifications | US26 | Incluido en US | Pendiente |
| 40 | TS20 | TS | PATCH /api/v1/notifications/{id}/read | US26 | Incluido en US | Pendiente |

### 3.3.3. Prioridades 41–60

| Orden | ID | Tipo | Título | Valor / US asociada | SP propuestos | Estado verificable |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 41 | US28 | US | Creación de Usuarios | Mis trabajadores,<br>para delegar accesos seguros. | 5 | Parcial: alta directa, correo de invitación pendiente |
| 42 | TS21 | TS | GET /api/v1/users | US28 | Incluido en US | En revisión |
| 43 | TS22 | TS | POST /api/v1/users | US28 | Incluido en US | En revisión |
| 44 | US29 | US | Restricción por Roles | Bloquear módulos confidenciales. | 5 | En revisión |
| 45 | TS33 | TS | Aislamiento de empresa y relaciones compuestas | US29 | Incluido en US | En revisión |
| 46 | US05 | US | Propuesta de valor en landing | Evaluar si soluciona mis problemas operativos. | 2 | En revisión |
| 47 | US06 | US | Funcionalidades de landing | Comprobar si cubre mis necesidades de negocio. | 2 | En revisión |
| 48 | US42 | US | Idioma de landing y recursos | Comprender la propuesta y continuar al producto. | 3 | En revisión |
| 49 | US34 | US | Términos del Servicio | Conocer el uso de mi data. | 2 | En revisión |
| 50 | US07 | US | Modelo comercial y planes | Evaluar una posible contratación para mi mype. | 2 | Parcial: propuesta sin suscripción ni cobro |
| 51 | TS27 | TS | GET /api/v1/landing/plans | US07 | Incluido en US | Pendiente |
| 52 | US01 | US | Registro de cuenta | Crear una cuenta administradora en cete. | 3 | En revisión |
| 53 | TS01 | TS | POST /api/v1/authentication/sign-up | US01 | Incluido en US | En revisión |
| 54 | TS32 | TS | Docker y publicación de API y PostgreSQL | US01 | Incluido en US | Público, aceptación del equipo pendiente |
| 55 | US02 | US | Inicio de sesión | Acceder al espacio de trabajo de mi empresa. | 3 | En revisión |
| 56 | TS02 | TS | POST /api/v1/authentication/sign-in | US02 | Incluido en US | En revisión |
| 57 | US03 | US | Cierre de sesión | Proteger mi cuenta y la información del negocio. | 2 | En revisión |
| 58 | TS03 | TS | POST /api/v1/authentication/sign-out | US03 | Incluido en US | En revisión |
| 59 | US04 | US | Recuperación de contraseña | Recuperar acceso si la he olvidado. | 5 | Pendiente |
| 60 | TS04 | TS | POST /api/v1/auth/password-reset | US04 | Incluido en US | Pendiente |

### 3.3.4. Prioridades 61–77

| Orden | ID | Tipo | Título | Valor / US asociada | SP propuestos | Estado verificable |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 61 | US08 | US | Contacto B2B | Solicitar una demostración personalizada. | 3 | Parcial: contacto GitHub, sin formulario B2B |
| 62 | TS26 | TS | POST /api/v1/contact-messages | US08 | Incluido en US | Pendiente |
| 63 | US12 | US | Registro de Mermas | Evitar que sean vendidos por error. | 2 | Pendiente |
| 64 | US13 | US | Buscador de Inventario | Localizarlos rápidamente sin listas largas. | 3 | En revisión |
| 65 | TS05 | TS | GET /api/v1/inventory | US13 | Incluido en US | En revisión |
| 66 | US16 | US | Validación Automática de Stock | No prometer mercadería inexistente. | 5 | En revisión |
| 67 | US24 | US | Reporte de Top Productos | Priorizar abastecimiento. | 3 | Pendiente |
| 68 | US25 | US | Exportación de Datos | Enviarlas a contabilidad. | 5 | Pendiente |
| 69 | US27 | US | Alerta de Producto Vencido | Ofertar artículos perecibles. | 3 | Pendiente |
| 70 | US30 | US | Edición de Perfil Empresa | Mantener facturas e interfaz personalizadas. | 2 | Pendiente |
| 71 | TS23 | TS | GET /api/v1/users/profile | US30 | Incluido en US | Pendiente |
| 72 | TS24 | TS | PUT /api/v1/users/profile | US30 | Incluido en US | Pendiente |
| 73 | US31 | US | Cambio de Contraseña | Asegurar mi cuenta. | 3 | Pendiente |
| 74 | TS25 | TS | PUT /api/v1/users/password | US31 | Incluido en US | Pendiente |
| 75 | US32 | US | Testimonios (Landing) | Ganar confianza. | 2 | Pendiente |
| 76 | US33 | US | Idioma de la aplicación | Comprender la interfaz a mi gusto. | 2 | En revisión |
| 77 | US37 | US | Dashboard: Gráfico de Tendencias | Analizar el comportamiento financiero de la mype. | 3 | Parcial: tendencia diaria, filtros pendientes |

Las 42 US suman **139 SP propuestos**. Las 38 US anteriores sumaban 121 SP; se corrige el texto que indicaba 34 historias. El equipo debe ratificar las estimaciones y capacidad. El tablero histórico enlazado es Trello; una captura de Jira no demuestra uso actual de Jira. Actualizar la herramienta realmente utilizada.
