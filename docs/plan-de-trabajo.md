# Plan de trabajo y avance

Actualizado: 24 de octubre de 2026.

**Estamos al terminar el paso 5; el siguiente es el 6.** Hay 5 pasos completos
de 11. `src/units` ya contiene el nuevo núcleo: `unit`, dimensiones, 25 familias,
definiciones locales y medidas inmutables. Conversiones, aritmética y catálogo
completo siguen pendientes.

| Paso | Trabajo | Estado |
| --- | --- | --- |
| 1 | Actualizar ambos repositorios, usando `Graf/develop` y `OpenGraf/master`. | Completado |
| 2 | Completar gunit: setups y tests mediante `try`, registro de fallos, continuación y `assert-fails` diferido con filtro de clase. | Completado |
| 3 | Revisar el descubrimiento: herencia pertinente, sobrescrituras y exclusión de objetos anidados, cuerpos de métodos y entornos importados. | Completado |
| 4 | Implementar `graf test`: archivos, carpetas, filtros, diagnósticos y códigos de salida. | Completado |
| 5 | Implementar `unit`, sus familias y las medidas como instancias inmutables con número, fábrica y dimensiones. | Completado |
| 6 | Completar conversiones, aritmética mixta, dimensiones compuestas, potencias, comparación y extensibilidad local. | **Siguiente** |
| 7 | Integrar `common.math`: trigonometría, conversiones con π y precisión explícita, conservando los tipos numéricos de Graf. | Pendiente |
| 8 | Construir el catálogo y los prefijos decimales/binarios; verificar factores con BIPM, NIST y CODATA, usando Gieck como referencia de cobertura. | Pendiente |
| 9 | Resolver temperaturas absolutas y diferencias, unidades logarítmicas y conversiones con referencias o modelos explícitos. | Pendiente |
| 10 | Migrar la API antigua, actualizar ejemplos y probar cada unidad, operación, extensión y error con gunit y la suite completa de Graf. | Pendiente |
| 11 | Completar documentación técnica, catálogo, fuentes y migración; verificar sitio web y PDF y publicar los cambios de ambos repositorios. | Parcial: documentación inicial y checkpoints publicados; referencia final y PDF pendientes |

## Último checkpoint verificado

- Graf: la suite completa de `develop` tiene **1955 pruebas correctas, 0 fallos y 2 omisiones existentes**. Incluye 11 regresiones de ejecución/aserciones, 13 de descubrimiento de gunit y 9 del comando de pruebas.
- OpenGraf: las pruebas auxiliares [de ejecución](https://github.com/Equijano24/OpenGraf/blob/master/tests/testing/gunit-smoke.graf) y [de descubrimiento](https://github.com/Equijano24/OpenGraf/blob/master/tests/testing/gunit-discovery-smoke.graf) devuelven sus suites para `graf test`; `graf test tests/testing` verifica **11 correctas, 0 fallidas y 0 errores de carga** (5 de ejecución y 6 de descubrimiento).
- OpenGraf units: `graf test tests/units` verifica **45 correctas, 0 fallidas y 0 errores de carga**. Incluye construcción, tipos numéricos, inmutabilidad, dimensiones de las 25 familias, compatibilidad, metadatos, extensiones locales, imports y entradas inválidas.
- La documentación compila con `mkdocs build --strict`; el [ejemplo del núcleo](units/core.md) se ejecuta con Graf actual.

Estas pruebas validan el motor, gunit y el nuevo núcleo de units. No certifican
las conversiones o el catálogo pendientes. Véanse la [API actual](units/core.md),
el [diseño completo](units/design.md), la
[validación pendiente](units/validation.md) y el [uso de gunit](testing.md).

## Alcance de la migración

OpenGraf contiene código y pruebas de una versión antigua de Graf. Se reescribe
**solo units**. `graf test` debe apuntar a las nuevas pruebas de
`tests/units`, sin exigir que las demás secciones antiguas pasen. Las suites de
`tests/testing` comprueban gunit y no certifican compatibilidad de la biblioteca
antigua. El descubrimiento dispone de 13 regresiones y una prueba auxiliar de
OpenGraf con 6 casos; el núcleo de units dispone ahora de sus propias pruebas.

El paso 4 también verifica filtros antes de ejecutar, imports relativos, aislamiento
entre archivos y códigos de salida `0`, `1`, `2` y `130`. Una ruta ausente o sin
tests coincidentes nunca se considera una comprobación exitosa.

El paso 5 reemplaza los antiguos archivos de units y documenta los nuevos nombres:
`distance` pasa a `length`, `weight` a `mass`, `information-unit` a `information`
y `temperature` se separa en puntos y diferencias. Las demás secciones antiguas
no se migran. El paso 6 añadirá operaciones a este núcleo, sin rehacerlo.
