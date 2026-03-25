# Arquitectura

## Descripción

El sistema utiliza una arquitectura simple basada en una API REST construida con FastAPI.

## Componentes

- Cliente: Swagger UI o navegador
- API: FastAPI
- Datos: almacenamiento en memoria

## Diagrama

```mermaid
graph TD
A[Cliente] --> B[FastAPI]
B --> C[Lógica de negocio]
C --> D[Memoria]

## Decisión técnica

Se decidió usar almacenamiento en memoria para simplificar el MVP y enfocarse en el flujo principal.

---

#  5. Guardar OpenAPI (OBLIGATORIO)

1. Ve a:
 http://127.0.0.1:8000/openapi.json  

2. Copia todo  

3. Guarda en:

```bash
docs/api/openapi.json
