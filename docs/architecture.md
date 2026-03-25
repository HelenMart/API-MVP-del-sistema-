# Arquitectura

## Descripción

El sistema utiliza una arquitectura simple basada en una API REST construida con FastAPI.

## Componentes

- Cliente: Swagger UI o navegador  
- API: FastAPI  
- Datos: almacenamiento en memoria  



## Decisión técnica

Se decidió usar almacenamiento en memoria para simplificar el MVP y enfocarse en el flujo principal.

### Guardar OpenAPI (OBLIGATORIO)
Ve a:
- http://127.0.0.1:8000/openapi.json
Copia todo
#### Guarda  :
docs/api/openapi.json

## Diagrama

```mermaid
graph TD
A[Cliente] --> B[FastAPI]
B --> C[Lógica de negocio]
C --> D[Memoria]
