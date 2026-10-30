# Diccionario de datos · CeTe AV2

[Volver al diseño](../04-Chapter-4.md#48-database-design) · [Revisión técnica](revision-informe.md)

Este diccionario describe el esquema físico de `CeTe-Api/schema.sql`. Se contrastó con un `pg_dump --schema-only` de PostgreSQL local el 30/10/2026: coinciden tablas, columnas, claves y los ocho índices únicos de negocio. No contiene registros ni credenciales.

**Convenciones.** `PK`: clave primaria; `FK`: clave foránea; `AK`: clave alternativa; `UQ`: índice único. Las 35 tablas tienen `Id uuid` como PK. Las 33 tablas de empresa tienen `TenantId → Tenants.Id` y AK `(TenantId, Id)`. `Tenants` y `SubscriptionPlans` son la excepción. Todos los campos actuales son `NOT NULL`, salvo `StockLots.ExpiresAt`.

Los vínculos entre tablas de empresa usan FK compuestas `(TenantId, XId) → (TenantId, Id)` y `ON DELETE RESTRICT`. El tenant se valida también mediante filtros EF Core; el esquema no configura políticas de Row-Level Security de PostgreSQL.

## Identidad y empresa

<a id="tenants"></a>

<details>
<summary><strong>Tenants</strong> · Empresa propietaria de los datos y sus datos comerciales.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `Ruc` | `text` | No | — |
| `Address` | `text` | No | — |

**Índices únicos adicionales:** `(Ruc)`.

</details>

<a id="subscriptionplans"></a>

<details>
<summary><strong>SubscriptionPlans</strong> · Catálogo global de planes; contratación pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `MonthlyPrice` | `numeric(18,2)` | No | — |

**Índices únicos adicionales:** ninguno.

</details>

<a id="tenantsubscriptions"></a>

<details>
<summary><strong>TenantSubscriptions</strong> · Vínculo empresa–plan; flujo de suscripción pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `SubscriptionPlanId` | `uuid` | No | FK (SubscriptionPlanId) → SubscriptionPlans (Id) |
| `Status` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="users"></a>

<details>
<summary><strong>Users</strong> · Cuenta de acceso, hash y rol efectivo de autorización.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Username` | `text` | No | — |
| `PasswordHash` | `text` | No | — |
| `Role` | `text` | No | — |
| `Active` | `boolean` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** `(Username)`.

</details>

<a id="roles"></a>

<details>
<summary><strong>Roles</strong> · Catálogo de roles de cada empresa.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="userroles"></a>

<details>
<summary><strong>UserRoles</strong> · Asociación cuenta–rol, creada junto con el alta.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `UserId` | `uuid` | No | FK (TenantId, UserId) → Users (TenantId, Id) |
| `RoleId` | `uuid` | No | FK (TenantId, RoleId) → Roles (TenantId, Id) |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, RoleId) → Roles (TenantId, Id); FK (TenantId, UserId) → Users (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="usersessions"></a>

<details>
<summary><strong>UserSessions</strong> · Sesión con vencimiento y revocación.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `UserId` | `uuid` | No | FK (TenantId, UserId) → Users (TenantId, Id) |
| `ExpiresAt` | `timestamp with time zone` | No | — |
| `Revoked` | `boolean` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, UserId) → Users (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

## Inventario

<a id="warehouses"></a>

<details>
<summary><strong>Warehouses</strong> · Almacén de la empresa; se crea uno al registrar la cuenta.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `Address` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="locations"></a>

<details>
<summary><strong>Locations</strong> · Ubicaciones internas; sin flujo operativo.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `WarehouseId` | `uuid` | No | FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |
| `Code` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="categories"></a>

<details>
<summary><strong>Categories</strong> · Categorías; sin FK desde Products ni flujo operativo.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="products"></a>

<details>
<summary><strong>Products</strong> · Identidad del SKU, precio, umbral y estado activo.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Sku` | `text` | No | — |
| `Name` | `text` | No | — |
| `UnitPrice` | `numeric(18,2)` | No | — |
| `MinimumStock` | `numeric(18,2)` | No | — |
| `Active` | `boolean` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** `(TenantId, Sku)`.

</details>

<a id="productvariants"></a>

<details>
<summary><strong>ProductVariants</strong> · Variantes vinculadas al producto; flujo pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `ProductId` | `uuid` | No | FK (TenantId, ProductId) → Products (TenantId, Id) |
| `Sku` | `text` | No | — |
| `AttributesJson` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ProductId) → Products (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="stocklots"></a>

<details>
<summary><strong>StockLots</strong> · Lotes y vencimiento; sin enlace al saldo o movimiento.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `ProductId` | `uuid` | No | FK (TenantId, ProductId) → Products (TenantId, Id) |
| `Code` | `text` | No | — |
| `ExpiresAt` | `timestamp with time zone` | Sí | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ProductId) → Products (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="stockbalances"></a>

<details>
<summary><strong>StockBalances</strong> · Saldo mutable por empresa, producto y almacén.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `ProductId` | `uuid` | No | FK (TenantId, ProductId) → Products (TenantId, Id) |
| `WarehouseId` | `uuid` | No | FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |
| `Quantity` | `numeric(18,2)` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ProductId) → Products (TenantId, Id); FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |

**Índices únicos adicionales:** `(TenantId, ProductId, WarehouseId)`.

</details>

<a id="inventorymovements"></a>

<details>
<summary><strong>InventoryMovements</strong> · Movimiento firmado con motivo, autor y fecha.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `ProductId` | `uuid` | No | FK (TenantId, ProductId) → Products (TenantId, Id) |
| `WarehouseId` | `uuid` | No | FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |
| `UserId` | `uuid` | No | FK (TenantId, UserId) → Users (TenantId, Id) |
| `Quantity` | `numeric(18,2)` | No | — |
| `Reason` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ProductId) → Products (TenantId, Id); FK (TenantId, UserId) → Users (TenantId, Id); FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

## Abastecimiento

<a id="suppliers"></a>

<details>
<summary><strong>Suppliers</strong> · Proveedor identificado por nombre al registrar una compra.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `Contact` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="purchaseorders"></a>

<details>
<summary><strong>PurchaseOrders</strong> · Cabecera de orden; no representa recepción física.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `SupplierId` | `uuid` | No | FK (TenantId, SupplierId) → Suppliers (TenantId, Id) |
| `WarehouseId` | `uuid` | No | FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |
| `Status` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, SupplierId) → Suppliers (TenantId, Id); FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="purchaseorderlines"></a>

<details>
<summary><strong>PurchaseOrderLines</strong> · Cantidad pedida, costo y cantidad acumulada recibida.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `PurchaseOrderId` | `uuid` | No | FK (TenantId, PurchaseOrderId) → PurchaseOrders (TenantId, Id) |
| `ProductId` | `uuid` | No | FK (TenantId, ProductId) → Products (TenantId, Id) |
| `Quantity` | `numeric(18,2)` | No | — |
| `UnitCost` | `numeric(18,2)` | No | — |
| `ReceivedQuantity` | `numeric(18,2)` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ProductId) → Products (TenantId, Id); FK (TenantId, PurchaseOrderId) → PurchaseOrders (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="goodsreceipts"></a>

<details>
<summary><strong>GoodsReceipts</strong> · Cabecera de cada recepción física con su autor.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `PurchaseOrderId` | `uuid` | No | FK (TenantId, PurchaseOrderId) → PurchaseOrders (TenantId, Id) |
| `UserId` | `uuid` | No | FK (TenantId, UserId) → Users (TenantId, Id) |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, PurchaseOrderId) → PurchaseOrders (TenantId, Id); FK (TenantId, UserId) → Users (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="goodsreceiptlines"></a>

<details>
<summary><strong>GoodsReceiptLines</strong> · Cantidad recibida contra una línea de la orden.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `GoodsReceiptId` | `uuid` | No | FK (TenantId, GoodsReceiptId) → GoodsReceipts (TenantId, Id) |
| `PurchaseOrderLineId` | `uuid` | No | FK (TenantId, PurchaseOrderLineId) → PurchaseOrderLines (TenantId, Id) |
| `Quantity` | `numeric(18,2)` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, GoodsReceiptId) → GoodsReceipts (TenantId, Id); FK (TenantId, PurchaseOrderLineId) → PurchaseOrderLines (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

## Ventas

<a id="customers"></a>

<details>
<summary><strong>Customers</strong> · Maestro de clientes; Sales usa CustomerName y no tiene FK hacia este maestro.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `Contact` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="sales"></a>

<details>
<summary><strong>Sales</strong> · Venta, total calculado, estado y hash de idempotencia.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `CustomerName` | `text` | No | — |
| `WarehouseId` | `uuid` | No | FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |
| `UserId` | `uuid` | No | FK (TenantId, UserId) → Users (TenantId, Id) |
| `TotalAmount` | `numeric(18,2)` | No | — |
| `Status` | `text` | No | — |
| `RequestHash` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, UserId) → Users (TenantId, Id); FK (TenantId, WarehouseId) → Warehouses (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="salelines"></a>

<details>
<summary><strong>SaleLines</strong> · Detalle histórico con SKU, nombre, cantidad y precio.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `SaleId` | `uuid` | No | FK (TenantId, SaleId) → Sales (TenantId, Id) |
| `ProductId` | `uuid` | No | FK (TenantId, ProductId) → Products (TenantId, Id) |
| `Sku` | `text` | No | — |
| `Name` | `text` | No | — |
| `Quantity` | `numeric(18,2)` | No | — |
| `UnitPrice` | `numeric(18,2)` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ProductId) → Products (TenantId, Id); FK (TenantId, SaleId) → Sales (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="payments"></a>

<details>
<summary><strong>Payments</strong> · Registro del método y monto, sin procesamiento bancario.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `SaleId` | `uuid` | No | FK (TenantId, SaleId) → Sales (TenantId, Id) |
| `Method` | `text` | No | — |
| `Amount` | `numeric(18,2)` | No | — |
| `Status` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, SaleId) → Sales (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="salesreceipts"></a>

<details>
<summary><strong>SalesReceipts</strong> · Instantánea comercial del comprobante académico.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `SaleId` | `uuid` | No | FK (TenantId, SaleId) → Sales (TenantId, Id) |
| `Number` | `text` | No | — |
| `CompanyName` | `text` | No | — |
| `Ruc` | `text` | No | — |
| `Address` | `text` | No | — |
| `Cashier` | `text` | No | — |
| `IssuedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, SaleId) → Sales (TenantId, Id) |

**Índices únicos adicionales:** `(TenantId, Number)`; `(TenantId, SaleId)`.

</details>

## Logística

<a id="drivers"></a>

<details>
<summary><strong>Drivers</strong> · Maestro de conductores; sin FK desde Dispatches.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Name` | `text` | No | — |
| `License` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="vehicles"></a>

<details>
<summary><strong>Vehicles</strong> · Maestro de vehículos; sin FK desde Dispatches.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `LicensePlate` | `text` | No | — |
| `Capacity` | `numeric(18,2)` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="dispatches"></a>

<details>
<summary><strong>Dispatches</strong> · Despacho con conductor y placa como texto y máquina de estados.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `DriverName` | `text` | No | — |
| `LicensePlate` | `text` | No | — |
| `Status` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="dispatchsales"></a>

<details>
<summary><strong>DispatchSales</strong> · Asociación exclusiva de una venta a un despacho.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `DispatchId` | `uuid` | No | FK (TenantId, DispatchId) → Dispatches (TenantId, Id) |
| `SaleId` | `uuid` | No | FK (TenantId, SaleId) → Sales (TenantId, Id) |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, DispatchId) → Dispatches (TenantId, Id); FK (TenantId, SaleId) → Sales (TenantId, Id) |

**Índices únicos adicionales:** `(TenantId, SaleId)`.

</details>

<a id="dispatchstops"></a>

<details>
<summary><strong>DispatchStops</strong> · Paradas ordenadas; flujo pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `DispatchId` | `uuid` | No | FK (TenantId, DispatchId) → Dispatches (TenantId, Id) |
| `Address` | `text` | No | — |
| `Sequence` | `integer` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, DispatchId) → Dispatches (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="deliveryattempts"></a>

<details>
<summary><strong>DeliveryAttempts</strong> · Intentos por parada; flujo pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `DispatchStopId` | `uuid` | No | FK (TenantId, DispatchStopId) → DispatchStops (TenantId, Id) |
| `Outcome` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, DispatchStopId) → DispatchStops (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="dispatchincidents"></a>

<details>
<summary><strong>DispatchIncidents</strong> · Incidencia del despacho con fecha y descripción.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `DispatchId` | `uuid` | No | FK (TenantId, DispatchId) → Dispatches (TenantId, Id) |
| `Description` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, DispatchId) → Dispatches (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

## Devoluciones

<a id="returns"></a>

<details>
<summary><strong>Returns</strong> · Cabecera de devolución; flujo pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `SaleId` | `uuid` | No | FK (TenantId, SaleId) → Sales (TenantId, Id) |
| `Reason` | `text` | No | — |
| `CreatedAt` | `timestamp with time zone` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, SaleId) → Sales (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

<a id="returnlines"></a>

<details>
<summary><strong>ReturnLines</strong> · Línea devuelta vinculada al detalle de venta; flujo pendiente.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `ReturnId` | `uuid` | No | FK (TenantId, ReturnId) → Returns (TenantId, Id) |
| `SaleLineId` | `uuid` | No | FK (TenantId, SaleLineId) → SaleLines (TenantId, Id) |
| `Quantity` | `numeric(18,2)` | No | — |
| `Resolution` | `text` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id); FK (TenantId, ReturnId) → Returns (TenantId, Id); FK (TenantId, SaleLineId) → SaleLines (TenantId, Id) |

**Índices únicos adicionales:** ninguno.

</details>

## Notificaciones

<a id="notifications"></a>

<details>
<summary><strong>Notifications</strong> · Mensaje y clave para deduplicación; sin bandeja ni generación operativa.</summary>

| Columna | Tipo PostgreSQL | Nulo | Clave / relación |
| :--- | :--- | :---: | :--- |
| `Id` | `uuid` | No | PK |
| `Message` | `text` | No | — |
| `EventKey` | `text` | No | — |
| `IsRead` | `boolean` | No | — |
| `TenantId` | `uuid` | No | FK (TenantId) → Tenants (Id) |

**Índices únicos adicionales:** `(TenantId, EventKey)`.

</details>

## Lectura correcta del esquema

- Una FK exige que exista el padre; no obliga a que una cabecera tenga líneas. La aplicación exige al menos una línea al confirmar una venta o despacho.
- `SaleLines` y `SalesReceipts` guardan datos históricos. No se reconstruye la boleta con el precio o el nombre actuales del catálogo.
- `InventoryMovements.Quantity` usa signo: entrada positiva y salida negativa. Su `Reason` contiene la referencia textual; no hay FK específica hacia la venta o recepción.
- `Payments` admite varias filas por venta en el esquema, pero el flujo actual crea una y la consulta de boleta espera una sola. El diseño de pagos divididos requiere ajuste previo.
- `GoodsReceiptLines` referencia una recepción y una línea de compra. Las FK actuales no garantizan por sí solas que ambas correspondan a la misma orden; el caso de uso lo determina desde la orden recibida.
- No existen `CHECK` para cantidades, precios o estados. Esas reglas se validan en dominio/aplicación y deben reforzarse mediante migraciones.

## Fuentes verificables

- [Esquema SQL](https://github.com/Nexxus-ops/CeTe-Api/blob/codex/av2-corrections/schema.sql).
- [Configuración EF Core](https://github.com/Nexxus-ops/CeTe-Api/blob/codex/av2-corrections/Infrastructure/CeTeDb.cs).
- [Entidades](https://github.com/Nexxus-ops/CeTe-Api/blob/codex/av2-corrections/Domain/Entities.cs).
