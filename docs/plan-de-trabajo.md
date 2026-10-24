# Plan de trabajo y avance

Actualizado: 24 de octubre de 2026.

**Estamos al terminar el paso 2; el siguiente es el 3.** Hay 2 pasos completos
de 11. El diseño de units está documentado, pero su nueva implementación sigue
pendiente: `src/units` todavía contiene la versión antigua.

| Paso | Trabajo | Estado |
| --- | --- | --- |
| 1 | Actualizar ambos repositorios, usando `Graf/develop` y `OpenGraf/master`. | Completado en este checkpoint |
| 2 | Completar gunit: setups y tests mediante `try`, registro de fallos, continuación y `assert-fails` diferido con filtro de clase. | Completado |
| 3 | Revisar el descubrimiento: herencia pertinente, sobrescrituras y exclusión de objetos anidados, cuerpos de métodos y entornos importados. | **Siguiente** |
| 4 | Implementar `graf test`: archivos, carpetas, filtros, diagnósticos y códigos de salida. | Pendiente |
| 5 | Implementar `unit`, sus familias y las medidas como instancias inmutables con número, fábrica y dimensiones. | Pendiente; diseño acordado |
| 6 | Completar conversiones, aritmética mixta, dimensiones compuestas, potencias, comparación y extensibilidad local. | Pendiente |
| 7 | Integrar `common.math`: trigonometría, conversiones con π y precisión explícita, conservando los tipos numéricos de Graf. | Pendiente |
| 8 | Construir el catálogo y los prefijos decimales/binarios; verificar factores con BIPM, NIST y CODATA, usando Gieck como referencia de cobertura. | Pendiente |
| 9 | Resolver temperaturas absolutas y diferencias, unidades logarítmicas y conversiones con referencias o modelos explícitos. | Pendiente |
| 10 | Migrar la API antigua, actualizar ejemplos y probar cada unidad, operación, extensión y error con gunit y la suite completa de Graf. | Pendiente |
| 11 | Completar documentación técnica, catálogo, fuentes y migración; verificar sitio web y PDF y publicar los cambios de ambos repositorios. | Parcial: documentación inicial y checkpoints publicados; referencia final y PDF pendientes |

## Último checkpoint verificado

- Graf: [cb36721](https://github.com/T-and-Q/Graf/commit/cb367219cfadb15f51d67ce2852e77cfe4cc8bfa), con **1933 pruebas correctas, 0 fallos y 2 omisiones existentes**. Incluye 11 regresiones de gunit.
- Open Graf: [5da1364](https://github.com/Equijano24/OpenGraf/commit/5da13641cfc80ad3463dc5bccf6147f5035c233e), con una [prueba ejecutable de gunit](https://github.com/Equijano24/OpenGraf/blob/5da13641cfc80ad3463dc5bccf6147f5035c233e/tests/testing/gunit-smoke.graf) que devuelve **5 correctas y 0 fallidas**.
- La documentación compila con `mkdocs build --strict`.

Estas pruebas validan el motor y la base de testing; todavía no validan la nueva
implementación de units. Véanse el [diseño](units/design.md), la
[validación pendiente](units/validation.md) y el [uso de gunit](testing.md).
