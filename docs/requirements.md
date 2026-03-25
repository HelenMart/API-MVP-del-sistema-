# Requerimientos

## Historias de usuario

1. Como usuario quiero crear un pedido para registrar una compra (Must)
2. Como usuario quiero consultar un pedido por ID (Must)
3. Como usuario quiero actualizar el estado de un pedido (Must)
4. Como usuario quiero ver todos los pedidos (Should)
5. Como usuario quiero validar datos ingresados (Must)
6. Como usuario quiero recibir errores claros (Must)
7. Como usuario quiero eliminar pedidos (Could)
8. Como usuario quiero persistencia en base de datos (Won’t)

## Ejemplo Given / When / Then

### Crear pedido
- Given: datos válidos
- When: se envía POST /orders
- Then: el pedido se crea correctamente
