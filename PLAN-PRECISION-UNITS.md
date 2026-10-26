# Plan de precisión numérica y conversiones de unidades

Fecha: 26 de octubre de 2026.

Repositorios: **Graf, rama `develop`**, y **OpenGraf, rama `master`**.

Estado: **pasos 1 a 3 completados; pasos 4 a 7 pendientes**.

Este documento reúne el contrato de aritmética acordado, la propuesta de
precisión y las correcciones de la revisión final. El seguimiento distingue el
trabajo completado de las etapas pendientes; la evidencia se registra en el
paso correspondiente.

El plan continúa el trabajo registrado en el
[plan histórico de once pasos](docs/plan-de-trabajo.md). Aquellos pasos describen
la primera implementación de units; las siete etapas siguientes corresponden a
esta revisión posterior y tienen su propio estado.

## Alcance y decisiones

La intervención comprende el motor numérico de Graf y la sección
`src/units` de OpenGraf. Otras secciones de OpenGraf todavía corresponden a una
versión anterior del lenguaje y no se consideran migradas por este trabajo.

La revisión se basó en OpenGraf
`613108b9181c185ac9d2c43854a6a68d428aacfb` y en las fuentes de Graf utilizadas
en el último checkpoint, `7da35b5fba689dee011ea5e41667d8b6dbd14359`.
Antes de implementar se deben actualizar las ramas indicadas, revisar los cambios
nuevos y adaptar las ubicaciones de código si fuera necesario. Esos identificadores
son referencias de la revisión, no una orden de retroceder las ramas.

### Contrato de aritmética de lecturas

Para sumar dos lecturas compatibles mediante `a.plus(b)`:

1. Comprobar compatibilidad de familia, dimensiones y referencias aplicables.
2. Expresar `b` en la escala y referencia de `a`.
3. Sumar los números de ambas lecturas.
4. Construir el resultado con la fábrica de `a`, pasando por su validación.

El nombre existente en el código es `celsius`.

| Expresión | Resultado esperado |
| --- | --- |
| `celsius(20).plus(celsius(5))` | 25 °C |
| `fahrenheit(20).plus(fahrenheit(5))` | 25 °F |
| `fahrenheit(celsius(20)).plus(fahrenheit(celsius(5)))` | 109 °F |
| `celsius(fahrenheit(celsius(20)).plus(fahrenheit(celsius(5))))` | 385/9 °C, aproximadamente 42,777… °C |
| `celsius(20).plus(celsius(10))` | 30 °C |
| `fahrenheit(celsius(20)).plus(fahrenheit(celsius(10)))` | 118 °F |
| `celsius(fahrenheit(celsius(20)).plus(fahrenheit(celsius(10))))` | 430/9 °C, aproximadamente 47,777… °C |

Las fracciones de la tabla expresan valores matemáticos. En las pruebas se
construirán con el protocolo racional de Graf, por ejemplo
`385.exact-quotient(9)`, sin usar un decimal truncado como expectativa.

Para una conversión afín `f(x) = a*x + b`, se cumple
`f(x) + f(y) = f(x+y) + b`. Cuando `b != 0`, sumar antes o después de
convertir puede producir cantidades distintas. Esa diferencia es parte del
contrato y no constituye una pérdida de precisión.

Se conserva lo siguiente:

- Conversión e igualdad física de una cantidad, sin operación intermedia.
- Sumas de lecturas en la escala del receptor.
- Multiplicación y división por escalares sobre la lectura, conservando la fábrica.
- Punto térmico menos punto térmico produce una diferencia.
- Punto más/menos diferencia produce un punto; diferencia más punto usa la
  fábrica del punto.
- Compatibilidad de familias y dimensiones, referencias explícitas y validación
  de cada resultado, incluido el límite de cero kelvin.
- Productos dimensionales, cocientes entre cantidades, potencias y raíces
  conservan sus restricciones existentes.

No se exige conmutatividad ni asociatividad general entre lecturas de escalas
distintas con desplazamiento. Los optimizadores y simplificadores tampoco deben
aplicar esas identidades a métodos de unidades sin demostrar que son válidas.
Dentro de una misma escala se conservan las propiedades de su aritmética numérica
en los casos exactos y para las expresiones válidas en su dominio.

Una cantidad convertida no conserva un origen aritmético oculto:
`fahrenheit(celsius(20))` y `fahrenheit(68)` deben operar del mismo modo.
No se introduce el espacio aritmético de la propuesta anterior ni un historial
de conversiones que altere las operaciones futuras.

En escalas logarítmicas se conserva la aritmética de lecturas ya definida.
Sumar niveles no calcula automáticamente una suma de potencias ni una mezcla
química. Los modelos físicos y sus referencias siguen siendo explícitos.

### Arquitectura y límites de la propuesta

Las familias y definiciones mantienen la herencia existente. Las medidas siguen
siendo instancias inmutables que componen un número, su fábrica y sus metadatos.
La extensibilidad continúa siendo local, mediante los protocolos existentes.

Mantener las convenciones de nombres: clases con sustantivos o adjetivo más
sustantivo; métodos que devuelven datos nombrados por su resultado; procedimientos
sin resultados con verbos. Los booleanos pueden usar `is`, los predicados pueden
seguir convenciones lógicas y los `assert` de gunit conservan sus nombres estándar.

No se propone un sistema de álgebra computacional completo ni un segundo motor
numérico dentro de OpenGraf. Se reutilizan los racionales, el despacho numérico y
el soporte simbólico de Graf. Cualquier ampliación simbólica debe responder a una
conversión concreta y tener límites de evaluación.

Debe distinguirse entre:

- Exactitud de un valor o de una expresión matemática.
- Aproximación numérica y su error.
- Precisión de trabajo solicitada a una función.
- Redondeo o formato de presentación.
- Incertidumbre de una medición o de un factor experimental.

El metadato `exact` de una definición de unidad no demuestra por sí solo que una
cantidad calculada sea exacta. Las fuentes, incertidumbres y ediciones de los
factores medidos se conservan; más dígitos de cálculo no aumentan su exactitud física.

## Seguimiento

| Paso | Entregable | Estado |
| --- | --- | --- |
| 1 | Contrato y pruebas de aritmética afín corregidos | Completado |
| 2 | Aritmética racional sin degradación implícita por tamaño | Completado |
| 3 | Representación y protocolo completos para aproximaciones | Completado |
| 4 | Precisión, redondeo, límites y errores controlados | Pendiente |
| 5 | Conversiones y operaciones de OpenGraf integradas | Pendiente |
| 6 | Matriz de regresión y compatibilidad de unidades | Pendiente |
| 7 | Documentación, validación integral y publicación | Pendiente |

El orden de dependencia es 1 → 2 → 3 → 4 → 5 → 6 → 7. Las regresiones se
escriben al comenzar cada cambio; el paso 6 completa la cobertura transversal,
no pospone todas las pruebas hasta el final.

## Paso 1. Corregir la especificación y el caso rojo

### Código y documentación afectados

- OpenGraf: `tests/units/temperature-points.graf`.
- Referencia de comportamiento: `src/units/core/unit.graf` y
  `src/units/core/temperature-point.graf`.
- Las aclaraciones de documentación se consolidan en el paso 7.

La suma implementada ya coincide con el contrato acordado. Este paso no requiere
cambiar su semántica.

En la revisión inicial había un cambio local pendiente con el método
`verify-temperature-sum-is-equivalent-after-fahrenheit-conversion`, que usaba
20 y 10 y esperaba incorrectamente 30 °C. Ese caso se incorpora como
`verify-temperature-sum-uses-fahrenheit-readings`, con la expectativa exacta
corregida a 430/9 °C y comprobación del resultado intermedio de 118 °F.

### Trabajo

1. Renombrar el método para expresar que la suma se hace en la escala usada.
2. Cambiar la expectativa del caso 20 y 10 a `430.exact-quotient(9)` °C.
3. Agregar el caso 20 y 5, con expectativa `385.exact-quotient(9)` °C.
4. Comprobar también los resultados intermedios: 118 °F y 109 °F.
5. Conservar los casos que suman lecturas nativas en Celsius, Fahrenheit, kelvin
   y Rankine.
6. Agregar la regresión de independencia del historial:
   `fahrenheit(celsius(20))` y `fahrenheit(68)`, al sumarse con el mismo
   operando, dan el mismo valor y la misma fábrica.

Las aserciones deben verificar magnitud exacta y fábrica. No basta con comprobar
que el resultado es distinto de 25 o de 30. El caso no se elimina ni se omite:
se convierte en una regresión con la expectativa correcta.

### Criterio de cierre

Los ejemplos de la tabla cumplen el contrato, las reglas de puntos y diferencias
siguen vigentes y la suite de temperatura no contiene el fallo deliberado de la
expectativa anterior.

### Evidencia de cierre del paso 1

Completado el 26 de octubre de 2026.

- El caso rojo inicial se reprodujo: 14 pruebas correctas, 1 fallida y 0 errores
  de carga; código de salida 1.
- Se corrigió el caso 20 y 10 y se agregó el caso 20 y 5. Ambos comprueban
  magnitudes exactas y fábricas, incluyendo los resultados de 118 °F y 109 °F.
- Las sumas nativas de 20 y 5 producen 25 en Celsius, Fahrenheit, kelvin y
  Rankine, conservando sus fábricas.
- La construcción directa `fahrenheit(68)` y la conversión
  `fahrenheit(celsius(20))`, sumadas con el mismo operando de 41 °F, producen
  ambas 109 °F.
- `graf test tests/units/temperature-points.graf`: **18 correctas, 0 fallidas,
  0 errores de carga; código de salida 0**. Las pruebas anteriores de puntos,
  diferencias, límites, extensiones e inmutabilidad se conservan.
- `graf test tests/units`: **519 correctas, 0 fallidas y 0 errores de carga;
  código de salida 0**, usando el runtime local de Graf/develop del checkpoint
  revisado, sin modificaciones del motor.
- `python3 tools/units_catalogue.py --check`: **655 archivos generados
  verificados**.
- `python3 tools/units_audit.py`: **302 fábricas y 302 casos de catálogo,
  519 casos de unidades y 8 ejemplos sincronizados**; código de salida 0.

El paso modifica las pruebas y este seguimiento. La implementación de units y
el motor de Graf conservan su comportamiento; las correcciones de precisión
siguen pendientes en los pasos siguientes.

## Paso 2. Conservar la aritmética racional exacta en Graf

### Archivos principales

- Graf: `Graf/Objects/Common/Number.cs`.
- Graf: `Graf/Objects/Common/Number.ExactArithmetic.cs`.
- Pruebas: `Graf.Testing/Interpreted/Math/ArithmeticOperationsTest.cs`.
- Pruebas: `Graf.Testing/Design/ValueObjects/ExactFactorsTest.cs`.
- Especificación: `Graf.Doc/Pending/Numeric-Operands-Design.md` y
  `Graf.Doc/Pending/Open-Work-Checklist.md`.

### Trabajo

Modificar `NormalizedNumericResult` para que los enteros y racionales exactos
no se conviertan a `float64` únicamente porque su numerador o denominador supera
`Int64`. La regla debe cubrir suma, resta, producto, cociente, potencias enteras,
recíproco y operaciones unarias que pasan por esa normalización.

Conservar la simplificación exacta a `int32`, `int64` o `integer` cuando
corresponda. Evitar también conversiones intermedias innecesarias a `double` en
las rutas de operandos exactos.

Mantener `exact-product` y `exact-quotient` por compatibilidad. La corrección
general evita exigir al usuario nuevas variantes especiales para cada operación.

Los operandos explícitos `float64` conservan un contrato documentado de coma
flotante. No cambiar la sintaxis de literales ni reinterpretar silenciosamente
un float mediante su texto decimal para presentarlo como el valor exacto que
el usuario pudo haber querido escribir.

Registrar el cambio de política en la cuestión pendiente existente sobre
promoción de racionales. Los tests antiguos que exigían esa degradación deben
actualizarse como un cambio explícito de especificación.

### Pruebas

- Renombrar y actualizar
  `ValidateTimesRationalDowncastsToFloat64AfterMagnitudeReductionAsync` para
  esperar el racional exacto.
- Actualizar los casos de `ExactFactorsTest` que exigen degradación ordinaria,
  manteniendo cobertura de la API exacta explícita.
- Construir `q = 1/10^40` como racional y verificar `(1+q)-1 = q`.
- Verificar conservación exacta al sumar cero, multiplicar por uno y dividir
  por uno, con numeradores y denominadores mayores que `Int64`.
- Cubrir cancelaciones, signos, potencias negativas, recíprocos, división por
  cero y simplificación a enteros.
- Mantener los casos de participación de floats y las combinaciones con valores
  simbólicos, con ambos órdenes de operandos.
- Probar que un resultado matemático de 30 decimales no pierde dígitos únicamente
  por una operación identidad posterior.

### Criterio de cierre

El tamaño de un racional exacto no causa pérdida de información. Las rutas
numéricas afectadas tienen regresiones y los cambios de tipos esperados están
explicados en la especificación.

### Evidencia de cierre del paso 2

Completado el 26 de octubre de 2026.

- Graf `f3795961932f2216bcf9cd4f257939c5eafa041d`, en la rama
  `cursor/exact-rational-arithmetic-d811`, basada en `develop`
  `7da35b5fba689dee011ea5e41667d8b6dbd14359`.
  Revisión: https://github.com/T-and-Q/Graf/pull/17.
- `NormalizedNumericResult` ya no convierte un entero o racional exacto a
  `float64` solo porque su numerador o denominador supera `Int64`. La ruta
  exacta no materializa un `double`. Un resultado con denominador 1 sigue
  democionando a `int32`, `int64` o `integer`.
- Un operando `float64` conserva la normalización binary64, incluido el
  desbordamiento no finito hacia racional. `0.1` sigue siendo float y `0.1(0)`
  el décimo exacto. No cambió la sintaxis de los literales.
- `exact-product` y `exact-quotient` permanecen como mensajes explícitos
  compatibles. La aritmética ordinaria ya conserva los factores exactos, así
  que no hace falta una variante especial para cada operación.
- `10^309 / 3` multiplicado por `1/10` es el racional exacto `10^308 / 3`.
  `(1 + 1/10^40) - 1` es `1/10^40`. Las identidades con numerador y denominador
  mayores que `Int64`, las cancelaciones, los signos, las potencias negativas,
  los recíprocos, la división por cero y la democión a entero quedaron cubiertos.
- `sin(1, 30).times(1)`, `plus(0)`, `over(1)` y `minus(0)` conservan el racional
  de 30 decimales. El mismo valor, ligado a una variable, también se conserva al
  operar por la derecha.
- La decisión quedó registrada en `Graf.Doc/Pending/Open-Work-Checklist.md` y
  `Graf.Doc/Pending/Numeric-Operands-Design.md`. La referencia de números, en
  español y en inglés, describe este contrato.
- `dotnet test Graf.Testing/Graf.Testing.csproj`: **2084 correctas, 0 fallidas
  y 2 omitidas preexistentes (`PrintedFormAsync`); código de salida 0**.
- `graf test tests/units`, con este runtime y sin cambios en el código de
  units: **519 correctas, 0 fallidas y 0 errores de carga; código de salida 0**.

El paso modifica el motor numérico de Graf, sus regresiones y la especificación.
La sección `src/units` de OpenGraf conserva su implementación; la integración de
las garantías de precisión sigue pendiente desde el paso 5.

## Paso 3. Conservar aproximaciones sin romper el protocolo numérico

### Archivos principales

- Graf: `Graf/Kernel/Numerics/DecimalResult.cs` y `AngleValue.cs`.
- Graf: `Graf/Objects/Common/Real.Logarithms.cs`,
  `Real.Trigonometry.cs`, `Real.Elementary.cs`,
  `Real.cs` y `Real.Comparison.cs`.
- Graf: protocolos de `Number`, `Irrational` y comparación/igualdad pertinentes.

### Trabajo

Actualmente algunas funciones calculan si su respuesta es exacta o aproximada,
pero pierden esa distinción al devolver la magnitud como un racional. Conservar
la información al producir el objeto numérico y durante operaciones posteriores.

Antes de escribir la representación, especificar su contrato de compatibilidad.
`ApproximateReal` es un nombre posible, no una clase ya decidida. Elegir la
representación más simple que conserve:

- Magnitud aproximada y estado de exactitud.
- Precisión de cálculo y cota de error, cuando esté disponible.
- Distinción entre una aproximación con fuente refinable y una entrada cuya
  información original ya se perdió.
- Propagación de esa información a través del protocolo numérico completo.

No confundir una cota desconocida con error cero. Incrementar la precisión de
trabajo no recupera información de una entrada ya redondeada. Si se conserva una
fuente exacta, puede reevaluarse; si no, debe respetarse la precisión disponible.

La integración debe cubrir operandos a izquierda y derecha, operaciones unarias,
funciones matemáticas, `number?`, `real?`, patrones más específicos,
`round`, `floor`, `ceil`, comparación, formato y conversiones a .NET.
Toda diferencia observable respecto de los resultados anteriores debe quedar
especificada y probada; heredar de `Real` no basta por sí solo.

Usar miembros virtuales y los protocolos existentes. No introducir listas de
nombres de clases, registros globales mutables ni flags ambientales para
seleccionar el comportamiento.

### Igualdad y redondeo

Mantener separadas la igualdad estructural/identidad de `equals`, la igualdad
numérica y la comparación aproximada con tolerancia explícita. Una tolerancia
no debe convertirse en la igualdad usada por patrones o claves de colecciones.

Si las cotas no permiten decidir una comparación o un redondeo, refinar cuando
haya una fuente que lo permita; de lo contrario, informar insuficiencia de
precisión. No inventar un booleano ni elegir arbitrariamente un entero.

Precisar también la relación entre el valor nuevo producido por un redondeo
explícito y el error respecto del valor anterior. Una aproximación no se vuelve
matemáticamente exacta solo porque su representación redondeada sea cero o un
entero. Las simplificaciones exactas demostrables siguen estando permitidas.

### Pruebas

- Resultados exactos reconocidos como exactos, incluidos casos especiales de
  trigonometría, raíces y logaritmos.
- Aproximaciones que conservan sus dígitos e información al operar.
- Ambos órdenes de operandos con enteros, racionales, floats y simbólicos.
- Patrones de argumentos y resultados, igualdad, comparaciones y redondeos.
- Aproximaciones que muestran cero o un entero sin perder su condición.
- Conversión explícita a tipos .NET sin fingir conservación de precisión mayor
  que la soportada por el destino.
- Compatibilidad de las aserciones de gunit con los tipos de resultados elegidos.

### Criterio de cierre

La representación está especificada, documentada y probada como parte del sistema
numérico de Graf. No se incorpora un objeto que conserve metadatos pero falle
en otras operaciones del protocolo.

### Evidencia de cierre del paso 3

Completado el 26 de octubre de 2026.

- Graf `0c7cdc2ea394120a50ecf521b6bdfd50576ded0a`, en la rama
  `cursor/approximate-reals-d811`, encima del paso 2
  `f3795961932f2216bcf9cd4f257939c5eafa041d`.
  Revisión: https://github.com/T-and-Q/Graf/pull/18.
- Un resultado redondeado es una `approximation`. Conserva el centro, las
  cifras decimales pedidas, la cota de medio lugar cuando las entradas eran
  exactas y una fuente refinable si esas entradas siguen siendo exactas.
  `real?` y `number?` coinciden. `rational?` no coincide. Un valor exacto sigue
  siendo `int32`, `int64`, `integer`, `rational` o `irrational`.
- `sin(1, 0)` y `log10(2, 0)` siguen siendo aproximaciones aunque su centro sea
  un entero o cero. `magnitude` devuelve ese centro como racional o entero.
- `equals` compara la representación. `equal-to` compara valores: dos redondeos
  de las mismas entradas exactas son iguales, y si la cota no decide se refina
  la fuente o se informa precisión insuficiente. Un `float64` sigue seleccionando
  binary64. Un operando simbólico sigue siendo simbólico en ambos órdenes.
- La cota de medio lugar es la ventana del redondeo entregado. El paso 4 precisa
  su relación con la función verdadera.
- `dotnet test Graf.Testing/Graf.Testing.csproj`: **2093 correctas, 0 fallidas
  y 2 omitidas preexistentes (`PrintedFormAsync`); código de salida 0**.
- `graf test tests/units`: **519 correctas, 0 fallidas y 0 errores de carga;
  código de salida 0**. Las comparaciones que antes exigían que el resultado
  redondeado fuera un racional exacto ahora leen `magnitude`. La ida y vuelta
  de una aproximación por una escala simbólica, como grados y radianes, queda
  para el paso 5: hoy puede permanecer como expresión simbólica.

## Paso 4. Definir precisión, error, redondeo y límites de cálculo

### Archivos principales

- Graf: `Graf/Kernel/Numerics/LogarithmMeasure.cs`,
  `ExponentialMeasure.cs`, `RadicalMeasure.cs`,
  `CircularMeasure*.cs` y las rutas de comparación simbólica.
- Pruebas: `TrigonometryTest.cs`, `LogarithmRootTest.cs`,
  `ElementaryOperationTest.cs`, `NumericLiteralTest.cs` y las nuevas
  regresiones numéricas necesarias.

### Trabajo

Conservar el significado de `precision` como posiciones decimales. Documentar
para cada API qué resultado y qué unidad controla, distinguiendo esa solicitud
de la precisión interna y del formato mostrado.

En particular, las inversas angulares de OpenGraf, como
`degrees.asin(x, 30)`, hoy definen la precisión en radianes antes de convertir.
Conservar ese contrato por compatibilidad y propagar la cota de error a grados;
no prometer automáticamente 30 decimales correctos en la lectura final.
Una API nueva de conversión debe indicar explícitamente dónde aplica su precisión.

Para una transformación exacta `y = a*x+b`, el error absoluto de entrada se
amplifica por `abs(a)`. Las rutas no lineales necesitan cotas acordes con su
dominio. Pasar el mismo entero de precisión a cada operación interna no demuestra
que el resultado compuesto cumpla el contrato.

Revisar los dígitos de guarda y los criterios de terminación. Usar cotas
justificadas o refinamiento con una garantía comprobable; que dos aproximaciones
sucesivas coincidan no constituye por sí solo una prueba de precisión.
Evitar redondeos intermedios innecesarios y conservar los modos de redondeo
documentados, incluidos los empates positivos y negativos.

Distinguir tres situaciones:

| Situación | Comportamiento |
| --- | --- |
| Dominio demostrado como inválido | Error aritmético o de dominio correspondiente |
| Dominio/comparación no decidible con la información disponible | Refinamiento o error de precisión |
| Presupuesto de cálculo agotado | Error controlado de precisión o recursos |

Un valor positivo muy pequeño redondeado a cero no demuestra que la entrada
matemática de un logaritmo fuera cero. Revisar especialmente esos casos y las
operaciones cercanas a singularidades.

### Recursos y propagación de errores

Definir límites razonables de trabajo, tamaño de los racionales y refinamiento,
con cancelación en los cálculos prolongados. Preservar los caminos exactos
rápidos que no necesitan materializar millones de decimales.

El agotamiento de recursos no debe producir una degradación silenciosa a
`float64`. Los errores deben seguir el mecanismo central de Graf y aparecer
como resultados con `ErrorLevel > 0`. Las excepciones .NET se convierten por
la ruta central existente; no se crea una ruta paralela para numerics.

### Pruebas

- Precisión cero, valores ordinarios y solicitudes de 15 y 30 decimales.
- Magnitudes pequeñas y grandes, cancelación y valores cercanos a singularidades.
- Empates de redondeo con ambos signos; `floor` y `ceil` en fronteras.
- Cotas tras cambiar escala, especialmente radianes a grados.
- Datos exactos frente a `float64`: incluir `0.1(0)` y `0.1`.
- Precisión inválida, presupuesto agotado y cancelación.
- Resultados esperados o cotas procedentes de referencias independientes de la
  misma ruta de código probada.
- Integración con `try` y gunit: captura del error de precisión, registro del
  fallo y continuación con el siguiente test.

### Criterio de cierre

Cada API tiene un contrato de precisión verificable. Cuando el motor no puede
cumplirlo, informa la limitación sin devolver un resultado como si estuviera
garantizado.

## Paso 5. Integrar las garantías en las unidades de OpenGraf

### Archivos y cambios

| Archivo de OpenGraf | Trabajo |
| --- | --- |
| `src/units/core/unit.graf` | Conservar la aritmética del receptor; revisar todas las rutas de conversión, comparación y construcción |
| `src/units/core/temperature-point.graf` y `temperature-difference.graf` | Conservar factores y desplazamientos exactos, validación y reglas de puntos/diferencias |
| `src/units/core/gauge-pressure.graf` | Conservar la precisión de escalas, referencias y presión absoluta |
| `src/units/core/logarithmic-unit.graf` y `logarithmic-reference.graf` | Transmitir precisión y evitar conversiones exponencial/logarítmica innecesarias |
| `src/units/core/angle.graf` y `compound.graf` | Conservar factores simbólicos y propagar precisión y errores |
| `src/units/core/prefix.graf` y definiciones | Verificar factores exactos y preservación de metadatos |
| `src/units/core/contextual.graf` y modelos asociados | Revisar la propagación numérica sin alterar los modelos físicos |

### Trabajo

Para transformaciones lineales y afines exactas, conservar todos los factores y
desplazamientos como números exactos. Reutilizar `Irrational` y sus
simplificaciones para factores como pi, respetando dominios y ramas cuando
corresponda.

En unidades logarítmicas, implementar conversiones directas de lecturas cuando
la relación sea conocida. Bels y decibels de la misma convención no necesitan
pasar por una exponencial y un logaritmo. Los cambios de referencia compatibles
pueden producir transformaciones afines; sus coeficientes deben permanecer
exactos o simbólicos cuando sea posible.

Conservar la distinción entre potencia y amplitud, las referencias y los modelos
explícitos. No deducir un modelo químico, eléctrico o físico únicamente a partir
de dimensiones coincidentes.

Eliminar los valores internos fijos de 15 decimales cuando ignoran una precisión
solicitada. El valor por defecto público puede seguir siendo 15. Reutilizar o
añadir sobrecargas compatibles para transmitir precisión durante conversiones y
operaciones mixtas, con el alcance definido en el paso 4.

La conversión entre fábricas iguales no debe provocar evaluaciones o redondeos
innecesarios. Los resultados siempre deben usar el protocolo de construcción
`quantity`, incluidas las validaciones sobrescritas por extensiones locales.

La presentación de menos decimales no modifica la cantidad almacenada.
`rounded` sí produce deliberadamente una cantidad redondeada. No exigir
recuperación exacta tras un redondeo explícito.

Si una corrección afecta al catálogo generado, actualizar
`tools/units-catalogue.json` o `tools/units_catalogue.py` y regenerar las
salidas pertinentes. No corregir únicamente el archivo generado. El generador
ya usa factores racionales; conservar esa propiedad.

### Criterio de cierre

Todas las familias conservan el contrato de lectura, la fábrica y las referencias,
y sus operaciones utilizan las garantías numéricas del motor sin implementar
aritmética alternativa dentro de OpenGraf.

## Paso 6. Completar la matriz de regresión y compatibilidad

### Suites principales de OpenGraf

- `tests/units/temperature-points.graf`.
- `tests/units/conversion.graf` y `arithmetic.graf`.
- `tests/units/reading-arithmetic.graf` y `contextual.graf`.
- `tests/units/logarithmic.graf`.
- `tests/units/angles.graf`, `trigonometry.graf` e
  `inverse-trigonometry.graf`.
- Suites de prefijos, potencias, cantidades compuestas, extensiones y catálogo.

### Matriz de aceptación

| Área | Propiedad que se comprueba |
| --- | --- |
| Lecturas nativas | Suma numérica en la escala utilizada |
| Escalas mixtas | Conversión del operando derecho y conservación de la fábrica izquierda |
| Escalas afines | Resultados independientes correctos; no exigir invariancia de la suma al convertir |
| Historial | Construcción directa y conversión equivalente operan igual en la misma fábrica |
| Conversión exacta | Ida y vuelta y rutas alternativas preservan el valor en dominios válidos |
| Conversión aproximada | Error compatible con la precisión y las cotas declaradas |
| Desplazamientos | Pequeños incrementos no desaparecen al sumar o restar referencias grandes |
| Catálogo y prefijos | Factores extremos conservados, fuentes y metadatos intactos |
| Ángulos | Pi simbólico, anclas exactas, dominio y precisión de funciones |
| Referencias | Presión manométrica y niveles referenciados conservan referencia y convención |
| Extensiones | Herencia, patrones, constructores sobrescritos e inmutabilidad |
| Errores | Tipos incompatibles, división por cero, dominios, precisión y recursos |

Usar igualdad estricta para resultados exactos. En resultados aproximados,
usar tolerancias justificadas, expresadas en la unidad correspondiente; una
tolerancia térmica representa una diferencia, no un punto con desplazamiento.

Combinar anclas independientes con propiedades de ida y vuelta: dos conversiones
equivocadas podrían cancelarse y pasar únicamente una prueba de round-trip.

Conservar los casos que no cambian de contrato. Actualizar expectativas únicamente
cuando una decisión del plan modifica la especificación; no aumentar tolerancias
para ocultar pérdidas de precisión ni marcar nuevas regresiones como omitidas.

### Criterio de cierre

La matriz está cubierta por pruebas ejecutadas y sus expectativas corresponden
a los contratos exactos, aproximados y de lectura que realmente aplican.

## Paso 7. Documentar, validar y publicar la implementación

### Documentación

En Graf, actualizar la referencia de números en ambos idiomas, las notas de
diseño y el checklist. Explicar el cambio de promoción de racionales, el contrato
de aproximación y las consecuencias observables en tipos y comparaciones.

En OpenGraf, actualizar `docs/units/operations.md`, `angles.md`,
`special.md`, `design.md`, `core.md`, `validation.md` y la guía de
migración cuando corresponda. Incluir los ejemplos de temperatura, el alcance
de cada parámetro de precisión y la distinción entre exactitud numérica,
presentación e incertidumbre física.

Actualizar este seguimiento con evidencia por etapa, conservando el historial
de los once pasos anteriores. El sitio y el PDF técnico deben generarse de las
mismas fuentes. Este plan de ingeniería, ubicado en la raíz del repositorio,
no altera por sí solo las páginas de la referencia técnica.

### Validación final

Ejecutar con las versiones actualizadas de ambos repositorios:

| Repositorio | Verificación |
| --- | --- |
| Graf/develop | `dotnet build Graf.sln` |
| Graf/develop | `dotnet test Graf.Testing/Graf.Testing.csproj` |
| OpenGraf/master | `graf test tests/units` |
| OpenGraf/master | `graf test tests/testing` |
| OpenGraf/master | `graf test tests/units-test.graf`, entrada de compatibilidad |
| OpenGraf/master | Ejemplos afectados y ejemplos ejecutables de documentación |
| OpenGraf/master | `python3 tools/units_catalogue.py --check` |
| OpenGraf/master | `python3 tools/units_audit.py --legacy-source` |
| OpenGraf/master | `python3 tools/docs_build.py` y revisión visual del PDF |
| OpenGraf/master | `python3 tools/docs_build.py --check` |

El comando `graf` utilizado debe corresponder al runtime de Graf/develop
validado, no a una instalación anterior. Se comprueban también los códigos de
salida y los errores de carga, además del número de tests aprobados.

La suite completa de Graf debe pasar salvo las omisiones preexistentes
documentadas. En OpenGraf, el criterio de aceptación cubre units y sus pruebas
auxiliares; no exige que módulos antiguos ajenos a esta migración pasen.

### Publicación y evidencia

- Hacer commits por cambios lógicos y documentar qué se verificó.
- Publicar primero la dependencia numérica de Graf y después la integración de
  OpenGraf, dejando identificados los commits compatibles.
- Cuando cambien las páginas técnicas, incluir el PDF actualizado y su manifiesto
  de construcción en el mismo conjunto de cambios.
- Preservar cambios locales ajenos al paso; revisar el contenido preparado antes
  de cada commit y verificar los commits publicados en remoto.
- No presentar resultados de checkpoints antiguos como si fueran ejecuciones
  de la implementación nueva.

### Criterio de cierre

Los siete pasos tienen evidencia de cumplimiento, ambos repositorios están
publicados en sus ramas previstas y la documentación técnica describe el
comportamiento realmente verificado.
