# Plan de trabajo y avance

Actualizado: 24 de octubre de 2026.

**Estamos al terminar el paso 3; el siguiente es el 4.** Hay 3 pasos completos
de 11. El diseño de units está documentado, pero su nueva implementación sigue
pendiente: `src/units` todavía contiene la versión antigua.

| Paso | Trabajo | Estado |
| --- | --- | --- |
| 1 | Actualizar ambos repositorios, usando `Graf/develop` y `OpenGraf/master`. | Completado en este checkpoint |
| 2 | Completar gunit: setups y tests mediante `try`, registro de fallos, continuación y `assert-fails` diferido con filtro de clase. | Completado |
| 3 | Revisar el descubrimiento: herencia pertinente, sobrescrituras y exclusión de objetos anidados, cuerpos de métodos y entornos importados. | Completado |
| 4 | Implementar `graf test`: archivos, carpetas, filtros, diagnósticos y códigos de salida. | **Siguiente** |
| 5 | Implementar `unit`, sus familias y las medidas como instancias inmutables con número, fábrica y dimensiones. | Pendiente; diseño acordado |
| 6 | Completar conversiones, aritmética mixta, dimensiones compuestas, potencias, comparación y extensibilidad local. | Pendiente |
| 7 | Integrar `common.math`: trigonometría, conversiones con π y precisión explícita, conservando los tipos numéricos de Graf. | Pendiente |
| 8 | Construir el catálogo y los prefijos decimales/binarios; verificar factores con BIPM, NIST y CODATA, usando Gieck como referencia de cobertura. | Pendiente |
| 9 | Resolver temperaturas absolutas y diferencias, unidades logarítmicas y conversiones con referencias o modelos explícitos. | Pendiente |
| 10 | Migrar la API antigua, actualizar ejemplos y probar cada unidad, operación, extensión y error con gunit y la suite completa de Graf. | Pendiente |
| 11 | Completar documentación técnica, catálogo, fuentes y migración; verificar sitio web y PDF y publicar los cambios de ambos repositorios. | Parcial: documentación inicial y checkpoints publicados; referencia final y PDF pendientes |

## Último checkpoint verificado

- Graf: la suite completa de `develop` tiene **1946 pruebas correctas, 0 fallos y 2 omisiones existentes**. Incluye 11 regresiones de ejecución/aserciones y 13 de descubrimiento de gunit.
- OpenGraf: las pruebas auxiliares [de ejecución](https://github.com/Equijano24/OpenGraf/blob/master/tests/testing/gunit-smoke.graf) y [de descubrimiento](https://github.com/Equijano24/OpenGraf/blob/master/tests/testing/gunit-discovery-smoke.graf) devuelven **5/0 y 6/0**, respectivamente.
- La documentación compila con `mkdocs build --strict`.

Estas pruebas validan el motor y la base de testing; todavía no validan la nueva
implementación de units. Véanse el [diseño](units/design.md), la
[validación pendiente](units/validation.md) y el [uso de gunit](testing.md).

## Alcance de la migración

OpenGraf contiene código y pruebas de una versión antigua de Graf. Se reescribe
**solo units**. El futuro `graf test` deberá apuntar a las nuevas pruebas de
`tests/units`, sin exigir que las demás secciones antiguas pasen. Las suites de
`tests/testing` comprueban gunit y no certifican compatibilidad de la biblioteca
antigua. El descubrimiento dispone de 13 regresiones y una prueba auxiliar de
OpenGraf con 6 casos; la implementación de units sigue pendiente.
