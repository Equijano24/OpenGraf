# Plan de trabajo y avance

Actualizado: 24 de octubre de 2026.

**Estamos al terminar el paso 6; el siguiente es el 7.** Hay 6 pasos completos
de 11. `src/units` contiene el nuevo núcleo y sus operaciones: conversiones,
aritmética mixta, compuestos dimensionales, potencias, raíces y comparación.
Trigonometría, catálogo y reglas de unidades especiales siguen pendientes.

| Paso | Trabajo | Estado |
| --- | --- | --- |
| 1 | Actualizar ambos repositorios, usando `Graf/develop` y `OpenGraf/master`. | Completado |
| 2 | Completar gunit: setups y tests mediante `try`, registro de fallos, continuación y `assert-fails` diferido con filtro de clase. | Completado |
| 3 | Revisar el descubrimiento: herencia pertinente, sobrescrituras y exclusión de objetos anidados, cuerpos de métodos y entornos importados. | Completado |
| 4 | Implementar `graf test`: archivos, carpetas, filtros, diagnósticos y códigos de salida. | Completado |
| 5 | Implementar `unit`, sus familias y las medidas como instancias inmutables con número, fábrica y dimensiones. | Completado |
| 6 | Completar conversiones, aritmética mixta, dimensiones compuestas, potencias, comparación y extensibilidad local. | Completado |
| 7 | Integrar `common.math`: trigonometría, conversiones con π y precisión explícita, conservando los tipos numéricos de Graf. | Completado |
| 8 | Construir el catálogo y los prefijos decimales/binarios; verificar factores con BIPM, NIST y CODATA, usando Gieck como referencia de cobertura. | **Siguiente** |
| 9 | Resolver temperaturas absolutas y diferencias, unidades logarítmicas y conversiones con referencias o modelos explícitos. | Pendiente |
| 10 | Migrar la API antigua, actualizar ejemplos y probar cada unidad, operación, extensión y error con gunit y la suite completa de Graf. | Pendiente |
| 11 | Completar documentación técnica, catálogo, fuentes y migración; verificar sitio web y PDF y publicar los cambios de ambos repositorios. | Parcial: documentación inicial y checkpoints publicados; referencia final y PDF pendientes |

## Último checkpoint verificado

- Graf: la suite completa de `develop` tiene **1980 pruebas correctas, 0 fallos y 2 omisiones existentes**. Incluye 13 regresiones de ejecución/aserciones, 13 de descubrimiento de gunit y 9 del comando de pruebas.
- OpenGraf: las pruebas auxiliares [de ejecución](https://github.com/Equijano24/OpenGraf/blob/master/tests/testing/gunit-smoke.graf) y [de descubrimiento](https://github.com/Equijano24/OpenGraf/blob/master/tests/testing/gunit-discovery-smoke.graf) devuelven sus suites para `graf test`; `graf test tests/testing` verifica **11 correctas, 0 fallidas y 0 errores de carga** (5 de ejecución y 6 de descubrimiento).
- OpenGraf units: `graf test tests/units` verifica **110 correctas, 0 fallidas y 0 errores de carga**. Incluye las 45 del núcleo, 32 de operaciones y 33 de ángulos, trigonometría, precisión y extensiones. Las nuevas aserciones comprueban también que cada operación devuelva exactamente un resultado.
- La documentación compila con `mkdocs build --strict`; los ejemplos del [núcleo](units/core.md), de [operaciones](units/operations.md) y de [ángulos](units/angles.md) se ejecutan con Graf actual.

Estas pruebas validan el motor, gunit, el núcleo, las operaciones y los ángulos de units. No
certifican el catálogo ni las reglas especiales que siguen pendientes. Véanse la [API actual](units/core.md),
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
no se migran. El paso 6 añade operaciones a este núcleo, sin rehacerlo.

El paso 6 conserva la fábrica izquierda en sumas y operaciones escalares,
clasifica compuestos solo de forma explícita, propaga errores numéricos y verifica
extensiones mediante `factory.quantity`. Rechaza la aritmética genérica sobre puntos
de temperatura y valores con offset; sus reglas especializadas quedan en el 9.

Este checkpoint corrige además `gunit.assert-fails` en Graf: conserva las variables
locales del test y ejecuta los efectos del cuerpo una vez. Dos regresiones .NET
reprodujeron el fallo antes del arreglo. El runner sigue llamando cada setup y
test mediante el deferreval `try` de Graf.

## Revisión de nombres previa al paso 7

Se revisaron las adiciones de los pasos 1–6 en Graf y OpenGraf. Las funciones que
devuelven datos usan nombres de resultado (`quantity`, `definition`,
`test-report`); las clases usan sustantivos y los procedimientos de prueba usan
verbos de verificación. Se actualizaron los consumidores y la documentación.
El detalle y el mapa de migración están en [convenciones de nombres](naming.md).
La revisión de nombres se conserva. Tras completar el paso 7 hay **7 pasos completos** y el **8 es el siguiente**.


## Paso 7 completado

Se agregan `src/units/radians.graf` y `src/units/degrees.graf`, con una familia
angular compartida en `src/units/core/angle.graf`. Las conversiones conservan π
simbólico; las seis funciones circulares devuelven números y las siete inversas
producen medidas en la unidad de la fábrica. Precisión opcional: 15 por defecto,
con delegación explícita a `common.math`. Los ejemplos, rangos y errores están en
la [referencia angular](units/angles.md).

Graf incorpora 23 regresiones y el soporte aritmético/de comparación para
operandos simbólicos a la derecha, cancelación exacta y formas equivalentes en π.
La promoción numérica existente puede convertir racionales grandes a `float64`
en operaciones posteriores; se documenta el límite y la cuestión pendiente en
Graf, sin redefinir esa regla desde OpenGraf.

El siguiente paso construye el catálogo y los prefijos. `meters` y las demás
fábricas públicas del catálogo aún no se agregan; los ejemplos de longitudes
siguen creando definiciones locales. Las reglas especializadas del paso 9,
la migración completa y la verificación del PDF final siguen pendientes.
