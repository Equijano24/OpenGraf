# Plan de trabajo y avance

Actualizado: 25 de octubre de 2026.

**Los 11 pasos están completados.** Units y su documentación técnica están
validados; el sitio estático y el PDF se generan desde las mismas fuentes.
Units dispone de 302 fábricas con nombre, los 24 prefijos SI y 10 binarios,
aritmética dimensional, trigonometría, temperaturas y conversiones especiales.
Los contextos y modelos físicos se suministran explícitamente.

| Paso | Trabajo | Estado |
| --- | --- | --- |
| 1 | Actualizar ambos repositorios, usando `Graf/develop` y `OpenGraf/master`. | Completado |
| 2 | Completar gunit: setups y tests mediante `try`, registro de fallos, continuación y `assert-fails` diferido con filtro de clase. | Completado |
| 3 | Revisar el descubrimiento: herencia pertinente, sobrescrituras y exclusión de objetos anidados, cuerpos de métodos y entornos importados. | Completado |
| 4 | Implementar `graf test`: archivos, carpetas, filtros, diagnósticos y códigos de salida. | Completado |
| 5 | Implementar `unit`, sus familias y las medidas como instancias inmutables con número, fábrica y dimensiones. | Completado |
| 6 | Completar conversiones, aritmética mixta, dimensiones compuestas, potencias, comparación y extensibilidad local. | Completado |
| 7 | Integrar `common.math`: trigonometría, conversiones con π y precisión explícita, conservando los tipos numéricos de Graf. | Completado |
| 8 | Construir el catálogo y los prefijos decimales/binarios; verificar factores con BIPM, NIST y CODATA, usando Gieck como referencia de cobertura. | Completado |
| 9 | Resolver temperaturas absolutas y diferencias, unidades logarítmicas y conversiones con referencias o modelos explícitos. | Completado |
| 10 | Migrar la API antigua, actualizar ejemplos y probar cada unidad, operación, extensión y error con gunit y la suite completa de Graf. | Completado |
| 11 | Completar documentación técnica, catálogo, fuentes y migración; verificar sitio web y PDF y publicar los cambios de ambos repositorios. | Completado: fuentes, sitio estático y PDF verificados; cambios publicados |

## Último checkpoint verificado

- Graf `develop`: **2076 pruebas correctas, 0 fallos y 2 omisiones existentes**.
  Se incorporaron antes del paso 9 los deferrevals nuevos hasta
  `7da35b5fba689dee011ea5e41667d8b6dbd14359`, incluidas sus pruebas de `expression.map`.
- `graf test tests/units`: **506 correctas, 0 fallidas y 0 errores de carga**.
  Son las 489 anteriores más 17 casos de migración (4 originales y 13 grupos nuevos).
- `graf test tests/units-test.graf`: **4 correctas**; ya incluidas en las 506.
- `graf test tests/testing`: **11 correctas, 0 fallidas y 0 errores de carga**.
- `python3 tools/units_catalogue.py --check`: **655 archivos generados verificados**.
- Documentación: `mkdocs build --strict` y siete ejemplos ejecutables verificados (incluido el quickstart).
  La documentación sigue siendo una referencia técnica, con Markdown compartido
  para sitio y PDF. El [PDF descargable](downloads/open-graf-units.pdf) incluye
  índice, destinos internos, referencias y tablas con encabezados repetidos.

El [catálogo lineal](units/catalogue.md) conserva sus 290 entradas. Las 12
[definiciones especiales](units/special.md) completan el inventario de 302.
`catalogue.definition` enumera ambas partes; los contextos locales no se registran.

## Paso 9 completado

- Cuatro escalas de puntos térmicos y sus diferencias: límites en cero kelvin,
  conversiones exactas, punto menos punto y punto más/menos diferencia.
- Bels, decibels y nepers con convenciones de potencia/amplitud separadas; pH
  a partir de actividad. Precisión explícita mediante `common.math`.
- Niveles con referencia retenida en cada medida: cambio de referencia,
  comparación y recuperación de la magnitud lineal.
- Presión manométrica con referencia explícita; modelos de relación
  amplitud/potencia, actividad, base química equivalente y ponderación de dosis.
- Factores, dominios y supuestos documentados con fuentes primarias. Las
  pruebas incluyen anclas independientes, errores, inmutabilidad y extensiones.

Graf no requirió modificaciones del motor para implementar este paso. Se
conservan sus reglas de promoción numérica y el uso de `try` en gunit.

## Paso 10 completado

Se migran las cuatro pruebas originales a gunit y se conserva su archivo de
entrada. Las 31 fábricas históricas tienen reemplazo o decisión explícita:
correcciones de nombres, prefijos binarios, puntos térmicos, grados y referencias
coherentes. La [guía de migración](units/migration.md) cubre también datos
almacenados, extensiones, formato y comparación sin dependencias de la API vieja.

`tools/units_audit.py --legacy-source` verifica el inventario histórico contra
el commit conservado, 302 casos de fábrica y seis ejemplos sincronizados con
sus referencias. La [matriz de validación](units/validation.md) enlaza las suites
de unidades, operaciones, extensiones y errores. Graf no requirió cambios propios.

## Paso 11 completado

La [referencia técnica](index.md) reúne API, catálogo, prefijos, reglas especiales,
migración, fuentes y validación. Se revisaron las declaraciones de estado y se
añadió un quickstart ejecutable. La navegación de MkDocs determina también el
orden del PDF; no hay un manuscrito separado ni una adaptación del libro de Gieck.

`tools/docs_build.py` produce los dos formatos. `--check` detecta PDF desactualizado,
hash incorrecto, enlaces/recursos locales ausentes y anclas HTML rotas. La generación
comprueba los 302 nombres de fábricas en el PDF, sus destinos internos y los
márgenes de texto. El sitio se verificó en escritorio y móvil; el PDF se renderizó
con Poppler para revisión visual. El [manifiesto](downloads/build.json) registra
la huella de las fuentes y las medidas del artefacto publicado.

El sitio queda listo para desplegar en un alojamiento estático; este trabajo no
configura un servicio de hosting. Graf no requirió cambios propios en los pasos
9–11; su rama `develop` y la publicación de OpenGraf están verificadas.

## Alcance y decisiones vigentes

OpenGraf contiene otras secciones de una versión antigua de Graf. Se reescribe
**solo units**: el objetivo de prueba es `tests/units`, más `tests/testing` para
gunit. Las secciones y pruebas antiguas restantes no se consideran migradas.

Las familias y definiciones usan herencia; las medidas son instancias inmutables
que componen un número con su fábrica y dimensiones. La extensibilidad es local,
sin registro global mutable. Las reglas de nombres se mantienen en
[convenciones y migración](naming.md).

El libro de Gieck sirve como referencia de cobertura. Las definiciones se
contrastan con BIPM, NIST, CODATA y las fuentes específicas de cada dominio;
las correcciones y la bibliografía están en [fuentes](units/sources.md).
La promoción ordinaria de racionales grandes de Graf sigue siendo una cuestión
del lenguaje; las conversiones de escala usan su protocolo exacto explícito.
