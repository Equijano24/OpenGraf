# Unit catalogue

This table contains **290 linear/angular factories**. Each factory is
available as `units.<name>` and in `src/units/<name>.graf`. Import `src/units`
as shown in [the core API](core.md). [Prefixes](prefixes.md) also construct
local factories without registration. Symbols are metadata, not alternate labels.

Factors are relative to the coherent unit of the named family. All rational
factors are exact unless the row is marked **measured**. Symbolic pi remains
symbolic. See [sources and reviewed conventions](sources.md) for reference IDs.
The separate [special-unit reference](special.md) documents temperature points,
logarithmic scales and contextual conversions. This linear catalogue includes
temperature **differences**. The `catalogue.definition` relation enumerates all
302 named factories, including the 12 special definitions.

| Factory | Family | Symbol | Coherent factor | Source |
| --- | --- | --- | --- | --- |
| `meters` | `length` | m | 1 | BIPM-SI-9-v4.01 |
| `kilometers` | `length` | km | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `hectometers` | `length` | hm | 100 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `decameters` | `length` | dam | 10 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `decimeters` | `length` | dm | 1/10 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `centimeters` | `length` | cm | 1/100 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `millimeters` | `length` | mm | 1/1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `micrometers` | `length` | µm | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `nanometers` | `length` | nm | 1/1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `picometers` | `length` | pm | 1/1000000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `inches` | `length` | in | 127/5000 | international-yard-pound-1959 |
| `feet` | `length` | ft | 381/1250 | international-yard-pound-1959 |
| `yards` | `length` | yd | 1143/1250 | international-yard-pound-1959 |
| `miles` | `length` | mi | 201168/125 | international-yard-pound-1959 |
| `fathoms` | `length` | fathom | 1143/625 | international-yard-pound-1959 |
| `furlongs` | `length` | fur | 25146/125 | international-yard-pound-1959 |
| `nautical-miles` | `length` | nmi | 1852 | BIPM-SI-9-v4.01 |
| `astronomical-units` | `length` | au | 149597870700 | BIPM-SI-9-v4.01 |
| `angstroms` | `length` | Å | 1/10000000000 | BIPM-SI-9-v4.01 |
| `square-meters` | `area` | m² | 1 | BIPM-SI-9-v4.01 |
| `cubic-meters` | `volume` | m³ | 1 | BIPM-SI-9-v4.01 |
| `square-centimeters` | `area` | cm² | 1/10000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `cubic-centimeters` | `volume` | cm³ | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `square-millimeters` | `area` | mm² | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `cubic-millimeters` | `volume` | mm³ | 1/1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `square-kilometers` | `area` | km² | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `cubic-kilometers` | `volume` | km³ | 1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `square-inches` | `area` | in² | 16129/25000000 | international-yard-pound-1959 |
| `cubic-inches` | `volume` | in³ | 2048383/125000000000 | international-yard-pound-1959 |
| `square-feet` | `area` | ft² | 145161/1562500 | international-yard-pound-1959 |
| `cubic-feet` | `volume` | ft³ | 55306341/1953125000 | international-yard-pound-1959 |
| `square-yards` | `area` | yd² | 1306449/1562500 | international-yard-pound-1959 |
| `cubic-yards` | `volume` | yd³ | 1493271207/1953125000 | international-yard-pound-1959 |
| `ares` | `area` | a | 100 | BIPM-SI-9-v4.01 |
| `hectares` | `area` | ha | 10000 | BIPM-SI-9-v4.01 |
| `international-acres` | `area` | acre | 316160658/78125 | international-yard-pound-1959 |
| `barns` | `area` | b | 1/10000000000000000000000000000 | BIPM-SI-9-v4.01 |
| `liters` | `volume` | L | 1/1000 | BIPM-SI-9-v4.01 |
| `milliliters` | `volume` | mL | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `centiliters` | `volume` | cL | 1/100000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `deciliters` | `volume` | dL | 1/10000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `hectoliters` | `volume` | hL | 1/10 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `us-liquid-gallons` | `volume` | gal (US) | 473176473/125000000000 | NIST-SP811-2008 |
| `us-liquid-quarts` | `volume` | qt (US) | 473176473/500000000000 | NIST-SP811-2008 |
| `us-liquid-pints` | `volume` | pt (US) | 473176473/1000000000000 | NIST-SP811-2008 |
| `us-fluid-ounces` | `volume` | fl oz (US) | 473176473/16000000000000 | NIST-SP811-2008 |
| `imperial-gallons` | `volume` | gal (imp) | 454609/100000000 | NIST-SP811-2008 |
| `imperial-quarts` | `volume` | qt (imp) | 454609/400000000 | NIST-SP811-2008 |
| `imperial-pints` | `volume` | pt (imp) | 454609/800000000 | NIST-SP811-2008 |
| `imperial-fluid-ounces` | `volume` | fl oz (imp) | 454609/16000000000 | NIST-SP811-2008 |
| `petroleum-barrels` | `volume` | bbl | 9936705933/62500000000 | NIST-SP811-2008 |
| `grams` | `mass` | g | 1/1000 | BIPM-SI-9-v4.01 |
| `kilograms` | `mass` | kg | 1 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `milligrams` | `mass` | mg | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `micrograms` | `mass` | µg | 1/1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `tonnes` | `mass` | t | 1000 | BIPM-SI-9-v4.01 |
| `pounds` | `mass` | lb | 45359237/100000000 | international-yard-pound-1959 |
| `avoirdupois-ounces` | `mass` | oz | 45359237/1600000000 | international-yard-pound-1959 |
| `grains` | `mass` | gr | 6479891/100000000000 | international-yard-pound-1959 |
| `troy-ounces` | `mass` | oz t | 19439673/625000000 | international-yard-pound-1959 |
| `us-short-tons` | `mass` | ton (US) | 45359237/50000 | international-yard-pound-1959 |
| `imperial-long-tons` | `mass` | ton (imp) | 317514659/312500 | international-yard-pound-1959 |
| `slugs` | `mass` | slug | 8896443230521/609600000000 | international-yard-pound-1959; standard-gravity-9.80665 |
| `metric-carats` | `mass` | ct | 1/5000 | NIST-SP811-2008 |
| `technical-mass-units` | `mass` | utm | 196133/20000 | standard-gravity-9.80665 |
| `daltons` | `mass` | Da | 41513476723/25000000000000000000000000000000000000 **measured**, u=5.2e-37; CODATA 2022 | CODATA-2022-atomic-mass-constant |
| `seconds` | `duration` | s | 1 | BIPM-SI-9-v4.01 |
| `milliseconds` | `duration` | ms | 1/1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `microseconds` | `duration` | µs | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `nanoseconds` | `duration` | ns | 1/1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `minutes` | `duration` | min | 60 | BIPM-SI-9-v4.01 |
| `hours` | `duration` | h | 3600 | BIPM-SI-9-v4.01 |
| `days` | `duration` | d | 86400 | BIPM-SI-9-v4.01 |
| `weeks` | `duration` | week | 604800 | fixed-duration-convention |
| `julian-years` | `duration` | a (Julian) | 31557600 | fixed-duration-convention |
| `radians` | `angle` | rad | 1 | BIPM-SI-9-v4.01 |
| `degrees` | `angle` | ° | pi.over(180) | BIPM-SI-9-v4.01 |
| `turns` | `angle` | turn | pi.times(2) | BIPM-SI-9-v4.01 |
| `gradians` | `angle` | gon | pi.over(200) | BIPM-SI-9-v4.01 |
| `arcminutes` | `angle` | ′ | pi.over(10800) | BIPM-SI-9-v4.01 |
| `arcseconds` | `angle` | ″ | pi.over(648000) | BIPM-SI-9-v4.01 |
| `steradians` | `solid-angle` | sr | 1 | BIPM-SI-9-v4.01 |
| `meters-per-second` | `velocity` | m/s | 1 | BIPM-SI-9-v4.01 |
| `kilometers-per-hour` | `velocity` | km/h | 5/18 | BIPM-SI-9-v4.01 |
| `miles-per-hour` | `velocity` | mi/h | 1397/3125 | NIST-SP811-2008 |
| `knots` | `velocity` | kn | 463/900 | BIPM-SI-9-v4.01 |
| `feet-per-second` | `velocity` | ft/s | 381/1250 | NIST-SP811-2008 |
| `meters-per-second-squared` | `acceleration` | m/s² | 1 | BIPM-SI-9-v4.01 |
| `standard-gravities` | `acceleration` | gₙ | 196133/20000 | NIST-SP811-2008 |
| `gals` | `acceleration` | Gal | 1/100 | NIST-SP811-2008 |
| `meters-per-second-cubed` | `jerk` | m/s³ | 1 | BIPM-SI-9-v4.01 |
| `radians-per-second` | `angular-velocity` | rad/s | 1 | BIPM-SI-9-v4.01 |
| `degrees-per-second` | `angular-velocity` | °/s | pi.over(180) | BIPM-SI-9-v4.01 |
| `revolutions-per-minute` | `angular-velocity` | r/min | pi.over(30) | BIPM-SI-9-v4.01 |
| `radians-per-second-squared` | `angular-acceleration` | rad/s² | 1 | BIPM-SI-9-v4.01 |
| `hertz` | `frequency` | Hz | 1 | BIPM-SI-9-v4.01 |
| `kilohertz` | `frequency` | kHz | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megahertz` | `frequency` | MHz | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `gigahertz` | `frequency` | GHz | 1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `newtons` | `force` | N | 1 | BIPM-SI-9-v4.01 |
| `kilonewtons` | `force` | kN | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `dynes` | `force` | dyn | 1/100000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `kilogram-forces` | `force` | kgf | 196133/20000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `gram-forces` | `force` | gf | 196133/20000000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `tonne-forces` | `force` | tf | 196133/20 | standard-gravity-9.80665; international-yard-pound-1959 |
| `pound-forces` | `force` | lbf | 8896443230521/2000000000000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `ounce-forces` | `force` | ozf | 8896443230521/32000000000000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `kips` | `force` | kip | 8896443230521/2000000000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `us-short-ton-forces` | `force` | tonf (US) | 8896443230521/1000000000 | standard-gravity-9.80665; international-yard-pound-1959 |
| `pascals` | `pressure` | Pa | 1 | BIPM-SI-9-v4.01 |
| `kilopascals` | `pressure` | kPa | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megapascals` | `pressure` | MPa | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `hectopascals` | `pressure` | hPa | 100 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `bars` | `pressure` | bar | 100000 | NIST-SP811-2008; standard-gravity-9.80665 |
| `millibars` | `pressure` | mbar | 100 | NIST-SP811-2008; standard-gravity-9.80665 |
| `standard-atmospheres` | `pressure` | atm | 101325 | NIST-SP811-2008; standard-gravity-9.80665 |
| `technical-atmospheres` | `pressure` | at | 196133/2 | NIST-SP811-2008; standard-gravity-9.80665 |
| `torrs` | `pressure` | Torr | 20265/152 | NIST-SP811-2008; standard-gravity-9.80665 |
| `pounds-per-square-inch` | `pressure` | psi | 8896443230521/1290320000 | NIST-SP811-2008; standard-gravity-9.80665 |
| `pounds-per-square-foot` | `pressure` | psf | 8896443230521/185806080000 | NIST-SP811-2008; standard-gravity-9.80665 |
| `kilogram-forces-per-square-centimeter` | `pressure` | kgf/cm² | 196133/2 | NIST-SP811-2008; standard-gravity-9.80665 |
| `joules` | `energy` | J | 1 | BIPM-SI-9-v4.01 |
| `kilojoules` | `energy` | kJ | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `ergs` | `energy` | erg | 1/10000000 | NIST-SP811-2008 |
| `watt-hours` | `energy` | Wh | 3600 | NIST-SP811-2008 |
| `kilowatt-hours` | `energy` | kWh | 3600000 | NIST-SP811-2008 |
| `thermochemical-calories` | `energy` | cal (th) | 523/125 | NIST-SP811-2008 |
| `international-table-calories` | `energy` | cal (IT) | 10467/2500 | NIST-SP811-2008 |
| `thermochemical-kilocalories` | `energy` | kcal (th) | 4184 | NIST-SP811-2008 |
| `international-table-kilocalories` | `energy` | kcal (IT) | 20934/5 | NIST-SP811-2008 |
| `international-table-btus` | `energy` | Btu (IT) | 52752792631/50000000 | NIST-SP811-2008 |
| `foot-pound-force-energies` | `energy` | ft·lbf | 3389544870828501/2500000000000000 | NIST-SP811-2008 |
| `kilogram-force-meters-energy` | `energy` | kgf·m | 196133/20000 | NIST-SP811-2008 |
| `electronvolts` | `energy` | eV | 801088317/5000000000000000000000000000 | BIPM-SI-9-v4.01 |
| `kiloelectronvolts` | `energy` | keV | 801088317/5000000000000000000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megaelectronvolts` | `energy` | MeV | 801088317/5000000000000000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `watts` | `power` | W | 1 | BIPM-SI-9-v4.01 |
| `kilowatts` | `power` | kW | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megawatts` | `power` | MW | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `mechanical-horsepower` | `power` | hp (mechanical) | 37284993579113511/50000000000000 | NIST-SP811-2008 |
| `metric-horsepower` | `power` | hp (metric) | 588399/800 | NIST-SP811-2008 |
| `electrical-horsepower` | `power` | hp (electric) | 746 | NIST-SP811-2008 |
| `foot-pound-forces-per-second` | `power` | ft·lbf/s | 3389544870828501/2500000000000000 | NIST-SP811-2008 |
| `international-table-btus-per-second` | `power` | Btu (IT)/s | 52752792631/50000000 | NIST-SP811-2008 |
| `newton-meters` | `torque` | N·m | 1 | BIPM-SI-9-v4.01 |
| `pound-force-feet` | `torque` | lbf·ft | 3389544870828501/2500000000000000 | NIST-SP811-2008 |
| `pound-force-inches` | `torque` | lbf·in | 1129848290276167/10000000000000000 | NIST-SP811-2008 |
| `kilogram-force-meters` | `torque` | kgf·m | 196133/20000 | NIST-SP811-2008 |
| `kilogram-meters-per-second` | `momentum` | kg·m/s | 1 | BIPM-SI-9-v4.01 |
| `kilogram-square-meters-per-second` | `angular-momentum` | kg·m²/s | 1 | BIPM-SI-9-v4.01 |
| `kilogram-square-meters` | `moment-of-inertia` | kg·m² | 1 | BIPM-SI-9-v4.01 |
| `meters-to-the-fourth` | `area-moment-of-inertia` | m⁴ | 1 | BIPM-SI-9-v4.01 |
| `cubic-meters-section-modulus` | `section-modulus` | m³ | 1 | BIPM-SI-9-v4.01 |
| `kilograms-per-cubic-meter` | `density` | kg/m³ | 1 | BIPM-SI-9-v4.01 |
| `cubic-meters-per-kilogram` | `specific-volume` | m³/kg | 1 | BIPM-SI-9-v4.01 |
| `kilograms-per-second` | `mass-flow` | kg/s | 1 | BIPM-SI-9-v4.01 |
| `cubic-meters-per-second` | `volume-flow` | m³/s | 1 | BIPM-SI-9-v4.01 |
| `pascal-seconds` | `dynamic-viscosity` | Pa·s | 1 | BIPM-SI-9-v4.01 |
| `square-meters-per-second` | `kinematic-viscosity` | m²/s | 1 | BIPM-SI-9-v4.01 |
| `newtons-per-meter` | `surface-tension` | N/m | 1 | BIPM-SI-9-v4.01 |
| `reciprocal-meters` | `wavenumber` | m⁻¹ | 1 | BIPM-SI-9-v4.01 |
| `kelvin-differences` | `temperature-difference` | K | 1 | BIPM-SI-9-v4.01 |
| `joules-per-kelvin` | `heat-capacity` | J/K | 1 | BIPM-SI-9-v4.01 |
| `joules-per-kilogram-kelvin` | `specific-heat-capacity` | J/(kg·K) | 1 | BIPM-SI-9-v4.01 |
| `watts-per-meter-kelvin` | `thermal-conductivity` | W/(m·K) | 1 | BIPM-SI-9-v4.01 |
| `watts-per-square-meter-kelvin` | `heat-transfer-coefficient` | W/(m²·K) | 1 | BIPM-SI-9-v4.01 |
| `reciprocal-kelvins` | `thermal-expansion` | K⁻¹ | 1 | BIPM-SI-9-v4.01 |
| `watts-per-square-meter-heat` | `heat-flux` | W/m² | 1 | BIPM-SI-9-v4.01 |
| `joules-per-kilogram` | `specific-energy` | J/kg | 1 | BIPM-SI-9-v4.01 |
| `amperes` | `current` | A | 1 | BIPM-SI-9-v4.01 |
| `coulombs` | `charge` | C | 1 | BIPM-SI-9-v4.01 |
| `volts` | `potential` | V | 1 | BIPM-SI-9-v4.01 |
| `ohms` | `resistance` | Ω | 1 | BIPM-SI-9-v4.01 |
| `siemens` | `conductance` | S | 1 | BIPM-SI-9-v4.01 |
| `farads` | `capacitance` | F | 1 | BIPM-SI-9-v4.01 |
| `henries` | `inductance` | H | 1 | BIPM-SI-9-v4.01 |
| `webers` | `magnetic-flux` | Wb | 1 | BIPM-SI-9-v4.01 |
| `teslas` | `magnetic-flux-density` | T | 1 | BIPM-SI-9-v4.01 |
| `amperes-per-meter` | `magnetic-field-strength` | A/m | 1 | BIPM-SI-9-v4.01 |
| `ohm-meters` | `resistivity` | Ω·m | 1 | BIPM-SI-9-v4.01 |
| `siemens-per-meter` | `conductivity` | S/m | 1 | BIPM-SI-9-v4.01 |
| `volts-per-meter` | `electric-field-strength` | V/m | 1 | BIPM-SI-9-v4.01 |
| `farads-per-meter` | `permittivity` | F/m | 1 | BIPM-SI-9-v4.01 |
| `henries-per-meter` | `permeability` | H/m | 1 | BIPM-SI-9-v4.01 |
| `reciprocal-henries` | `magnetic-reluctance` | H⁻¹ | 1 | BIPM-SI-9-v4.01 |
| `henries-permeance` | `magnetic-permeance` | H | 1 | BIPM-SI-9-v4.01 |
| `ampere-turns` | `magnetomotive-force` | A | 1 | BIPM-SI-9-v4.01 |
| `volt-amperes` | `apparent-power` | V·A | 1 | BIPM-SI-9-v4.01 |
| `vars` | `reactive-power` | var | 1 | BIPM-SI-9-v4.01 |
| `coulombs-per-cubic-meter` | `electric-charge-density` | C/m³ | 1 | BIPM-SI-9-v4.01 |
| `amperes-per-square-meter` | `electric-current-density` | A/m² | 1 | BIPM-SI-9-v4.01 |
| `candelas` | `luminous-intensity` | cd | 1 | BIPM-SI-9-v4.01 |
| `lumens` | `luminous-flux` | lm | 1 | BIPM-SI-9-v4.01 |
| `lux` | `illuminance` | lx | 1 | BIPM-SI-9-v4.01 |
| `candelas-per-square-meter` | `luminance` | cd/m² | 1 | BIPM-SI-9-v4.01 |
| `lumen-seconds` | `luminous-energy` | lm·s | 1 | BIPM-SI-9-v4.01 |
| `diopters` | `optical-power` | m⁻¹ | 1 | BIPM-SI-9-v4.01 |
| `watts-per-square-meter` | `irradiance` | W/m² | 1 | BIPM-SI-9-v4.01 |
| `watts-per-square-meter-steradian` | `radiance` | W/(m²·sr) | 1 | BIPM-SI-9-v4.01 |
| `moles` | `amount-of-substance` | mol | 1 | BIPM-SI-9-v4.01 |
| `kilograms-per-mole` | `molar-mass` | kg/mol | 1 | BIPM-SI-9-v4.01 |
| `moles-per-cubic-meter` | `amount-concentration` | mol/m³ | 1 | BIPM-SI-9-v4.01 |
| `kilograms-per-cubic-meter-concentration` | `mass-concentration` | kg/m³ | 1 | BIPM-SI-9-v4.01 |
| `moles-per-kilogram` | `molality` | mol/kg | 1 | BIPM-SI-9-v4.01 |
| `katals` | `catalytic-activity` | kat | 1 | BIPM-SI-9-v4.01 |
| `joules-per-mole` | `molar-energy` | J/mol | 1 | BIPM-SI-9-v4.01 |
| `joules-per-mole-kelvin` | `molar-heat-capacity` | J/(mol·K) | 1 | BIPM-SI-9-v4.01 |
| `becquerels` | `radioactivity` | Bq | 1 | BIPM-SI-9-v4.01 |
| `grays` | `absorbed-dose` | Gy | 1 | BIPM-SI-9-v4.01 |
| `sieverts` | `equivalent-dose` | Sv | 1 | BIPM-SI-9-v4.01 |
| `coulombs-per-kilogram` | `exposure` | C/kg | 1 | BIPM-SI-9-v4.01 |
| `bits` | `information` | bit | 1 | BIPM-SI-9-v4.01 |
| `bits-per-second` | `information-rate` | bit/s | 1 | BIPM-SI-9-v4.01 |
| `kilograms-per-meter` | `mass-per-length` | kg/m | 1 | BIPM-SI-9-v4.01 |
| `kilograms-per-square-meter` | `mass-per-area` | kg/m² | 1 | BIPM-SI-9-v4.01 |
| `celsius-differences` | `temperature-difference` | Δ°C | 1 | BIPM-SI-9-v4.01 |
| `fahrenheit-differences` | `temperature-difference` | Δ°F | 5/9 | NIST-SP811-2008 |
| `grams-per-cubic-centimeter` | `density` | g/cm³ | 1000 | NIST-SP811-2008 |
| `pounds-per-cubic-foot` | `density` | lb/ft³ | 28349523125/1769802912 | NIST-SP811-2008 |
| `pounds-per-cubic-inch` | `density` | lb/in³ | 56699046250/2048383 | NIST-SP811-2008 |
| `liters-per-kilogram` | `specific-volume` | L/kg | 1/1000 | NIST-SP811-2008 |
| `liters-per-second` | `volume-flow` | L/s | 1/1000 | NIST-SP811-2008 |
| `liters-per-minute` | `volume-flow` | L/min | 1/60000 | NIST-SP811-2008 |
| `us-gallons-per-minute` | `volume-flow` | gal (US)/min | 157725491/2500000000000 | NIST-SP811-2008 |
| `poise` | `dynamic-viscosity` | P | 1/10 | NIST-SP811-2008 |
| `centipoise` | `dynamic-viscosity` | cP | 1/1000 | NIST-SP811-2008 |
| `stokes` | `kinematic-viscosity` | St | 1/10000 | NIST-SP811-2008 |
| `centistokes` | `kinematic-viscosity` | cSt | 1/1000000 | NIST-SP811-2008 |
| `grams-per-mole` | `molar-mass` | g/mol | 1/1000 | NIST-SP811-2008 |
| `moles-per-liter` | `amount-concentration` | mol/L | 1000 | NIST-SP811-2008 |
| `milligrams-per-liter` | `mass-concentration` | mg/L | 1/1000 | NIST-SP811-2008 |
| `ampere-hours` | `charge` | A·h | 3600 | NIST-SP811-2008 |
| `gauss` | `magnetic-flux-density` | G | 1/10000 | NIST-SP811-2008 |
| `maxwells` | `magnetic-flux` | Mx | 1/100000000 | NIST-SP811-2008 |
| `oersteds` | `magnetic-field-strength` | Oe | 1000.over(pi.times(4)) | NIST-SP811-2008 |
| `foot-candles` | `illuminance` | fc | 1562500/145161 | NIST-SP811-2008 |
| `foot-lamberts` | `luminance` | fL | 1.over(pi.times(0.09290304(0))) | NIST-SP811-2008 |
| `curies` | `radioactivity` | Ci | 37000000000 | NIST-SP811-2008 |
| `rutherfords` | `radioactivity` | Rd | 1000000 | NIST-SP811-2008 |
| `rads` | `absorbed-dose` | rad | 1/100 | NIST-SP811-2008 |
| `rems` | `equivalent-dose` | rem | 1/100 | NIST-SP811-2008 |
| `roentgens` | `exposure` | R | 129/500000 | NIST-SP811-2008 |
| `milliamperes` | `current` | mA | 1/1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `millivolts` | `potential` | mV | 1/1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `kilovolts` | `potential` | kV | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `kilohms` | `resistance` | kΩ | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megohms` | `resistance` | MΩ | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `microfarads` | `capacitance` | µF | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `nanofarads` | `capacitance` | nF | 1/1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `picofarads` | `capacitance` | pF | 1/1000000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `millihenries` | `inductance` | mH | 1/1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `microteslas` | `magnetic-flux-density` | µT | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `millisieverts` | `equivalent-dose` | mSv | 1/1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `microsieverts` | `equivalent-dose` | µSv | 1/1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `kilobecquerels` | `radioactivity` | kBq | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `bytes` | `information` | B | 8 | IEC-80000-13-2025 |
| `bytes-per-second` | `information-rate` | B/s | 8 | IEC-80000-13-2025 |
| `kilobits` | `information` | kbit | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megabits` | `information` | Mbit | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `gigabits` | `information` | Gbit | 1000000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `kilobytes` | `information` | kB | 8000 | IEC-80000-13-2025; BIPM-SI-9-v4.01 |
| `megabytes` | `information` | MB | 8000000 | IEC-80000-13-2025; BIPM-SI-9-v4.01 |
| `gigabytes` | `information` | GB | 8000000000 | IEC-80000-13-2025; BIPM-SI-9-v4.01 |
| `terabytes` | `information` | TB | 8000000000000 | IEC-80000-13-2025; BIPM-SI-9-v4.01 |
| `kilobits-per-second` | `information-rate` | kbit/s | 1000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `megabits-per-second` | `information-rate` | Mbit/s | 1000000 | BIPM-SI-9-v4.01; BIPM-SI-9-v4.01 |
| `kibibytes` | `information` | KiB | 8192 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `kibibits` | `information` | Kibit | 1024 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `mebibytes` | `information` | MiB | 8388608 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `mebibits` | `information` | Mibit | 1048576 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `gibibytes` | `information` | GiB | 8589934592 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `gibibits` | `information` | Gibit | 1073741824 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `tebibytes` | `information` | TiB | 8796093022208 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `tebibits` | `information` | Tibit | 1099511627776 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `pebibytes` | `information` | PiB | 9007199254740992 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `pebibits` | `information` | Pibit | 1125899906842624 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `exbibytes` | `information` | EiB | 9223372036854775808 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `exbibits` | `information` | Eibit | 1152921504606846976 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `zebibytes` | `information` | ZiB | 9444732965739290427392 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `zebibits` | `information` | Zibit | 1180591620717411303424 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `yobibytes` | `information` | YiB | 9671406556917033397649408 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `yobibits` | `information` | Yibit | 1208925819614629174706176 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `robibytes` | `information` | RiB | 9903520314283042199192993792 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `robibits` | `information` | Ribit | 1237940039285380274899124224 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `quebibytes` | `information` | QiB | 10141204801825835211973625643008 | IEC-80000-13-2025; IEC-80000-13-2025 |
| `quebibits` | `information` | Qibit | 1267650600228229401496703205376 | BIPM-SI-9-v4.01; IEC-80000-13-2025 |
| `ratios` | `ratio` | 1 | 1 | BIPM-SI-9-v4.01 |
| `percentages` | `ratio` | % | 1/100 | BIPM-SI-9-v4.01 |
| `per-milles` | `ratio` | ‰ | 1/1000 | BIPM-SI-9-v4.01 |
| `parts-per-million` | `ratio` | ppm | 1/1000000 | BIPM-SI-9-v4.01 |

## Family dimensions

The eight exponents are ordered as length, mass, duration, current, temperature,
amount of substance, luminous intensity and information. Kinds with equal
dimensions are intentionally separate; classification is explicit.

| Family | Exponents |
| --- | --- |
| `absorbed-dose` | 2, 0, -2, 0, 0, 0, 0, 0 |
| `acceleration` | 1, 0, -2, 0, 0, 0, 0, 0 |
| `amount-concentration` | -3, 0, 0, 0, 0, 1, 0, 0 |
| `amount-of-substance` | 0, 0, 0, 0, 0, 1, 0, 0 |
| `angle` | 0, 0, 0, 0, 0, 0, 0, 0 |
| `angular-acceleration` | 0, 0, -2, 0, 0, 0, 0, 0 |
| `angular-momentum` | 2, 1, -1, 0, 0, 0, 0, 0 |
| `angular-velocity` | 0, 0, -1, 0, 0, 0, 0, 0 |
| `apparent-power` | 2, 1, -3, 0, 0, 0, 0, 0 |
| `area` | 2, 0, 0, 0, 0, 0, 0, 0 |
| `area-moment-of-inertia` | 4, 0, 0, 0, 0, 0, 0, 0 |
| `capacitance` | -2, -1, 4, 2, 0, 0, 0, 0 |
| `catalytic-activity` | 0, 0, -1, 0, 0, 1, 0, 0 |
| `charge` | 0, 0, 1, 1, 0, 0, 0, 0 |
| `conductance` | -2, -1, 3, 2, 0, 0, 0, 0 |
| `conductivity` | -3, -1, 3, 2, 0, 0, 0, 0 |
| `current` | 0, 0, 0, 1, 0, 0, 0, 0 |
| `density` | -3, 1, 0, 0, 0, 0, 0, 0 |
| `duration` | 0, 0, 1, 0, 0, 0, 0, 0 |
| `dynamic-viscosity` | -1, 1, -1, 0, 0, 0, 0, 0 |
| `electric-charge-density` | -3, 0, 1, 1, 0, 0, 0, 0 |
| `electric-current-density` | -2, 0, 0, 1, 0, 0, 0, 0 |
| `electric-field-strength` | 1, 1, -3, -1, 0, 0, 0, 0 |
| `energy` | 2, 1, -2, 0, 0, 0, 0, 0 |
| `equivalent-dose` | 2, 0, -2, 0, 0, 0, 0, 0 |
| `exposure` | 0, -1, 1, 1, 0, 0, 0, 0 |
| `force` | 1, 1, -2, 0, 0, 0, 0, 0 |
| `frequency` | 0, 0, -1, 0, 0, 0, 0, 0 |
| `heat-capacity` | 2, 1, -2, 0, -1, 0, 0, 0 |
| `heat-flux` | 0, 1, -3, 0, 0, 0, 0, 0 |
| `heat-transfer-coefficient` | 0, 1, -3, 0, -1, 0, 0, 0 |
| `illuminance` | -2, 0, 0, 0, 0, 0, 1, 0 |
| `inductance` | 2, 1, -2, -2, 0, 0, 0, 0 |
| `information` | 0, 0, 0, 0, 0, 0, 0, 1 |
| `information-rate` | 0, 0, -1, 0, 0, 0, 0, 1 |
| `irradiance` | 0, 1, -3, 0, 0, 0, 0, 0 |
| `jerk` | 1, 0, -3, 0, 0, 0, 0, 0 |
| `kinematic-viscosity` | 2, 0, -1, 0, 0, 0, 0, 0 |
| `length` | 1, 0, 0, 0, 0, 0, 0, 0 |
| `luminance` | -2, 0, 0, 0, 0, 0, 1, 0 |
| `luminous-energy` | 0, 0, 1, 0, 0, 0, 1, 0 |
| `luminous-flux` | 0, 0, 0, 0, 0, 0, 1, 0 |
| `luminous-intensity` | 0, 0, 0, 0, 0, 0, 1, 0 |
| `magnetic-field-strength` | -1, 0, 0, 1, 0, 0, 0, 0 |
| `magnetic-flux` | 2, 1, -2, -1, 0, 0, 0, 0 |
| `magnetic-flux-density` | 0, 1, -2, -1, 0, 0, 0, 0 |
| `magnetic-permeance` | 2, 1, -2, -2, 0, 0, 0, 0 |
| `magnetic-reluctance` | -2, -1, 2, 2, 0, 0, 0, 0 |
| `magnetomotive-force` | 0, 0, 0, 1, 0, 0, 0, 0 |
| `mass` | 0, 1, 0, 0, 0, 0, 0, 0 |
| `mass-concentration` | -3, 1, 0, 0, 0, 0, 0, 0 |
| `mass-flow` | 0, 1, -1, 0, 0, 0, 0, 0 |
| `mass-per-area` | -2, 1, 0, 0, 0, 0, 0, 0 |
| `mass-per-length` | -1, 1, 0, 0, 0, 0, 0, 0 |
| `molality` | 0, -1, 0, 0, 0, 1, 0, 0 |
| `molar-energy` | 2, 1, -2, 0, 0, -1, 0, 0 |
| `molar-heat-capacity` | 2, 1, -2, 0, -1, -1, 0, 0 |
| `molar-mass` | 0, 1, 0, 0, 0, -1, 0, 0 |
| `moment-of-inertia` | 2, 1, 0, 0, 0, 0, 0, 0 |
| `momentum` | 1, 1, -1, 0, 0, 0, 0, 0 |
| `optical-power` | -1, 0, 0, 0, 0, 0, 0, 0 |
| `permeability` | 1, 1, -2, -2, 0, 0, 0, 0 |
| `permittivity` | -3, -1, 4, 2, 0, 0, 0, 0 |
| `potential` | 2, 1, -3, -1, 0, 0, 0, 0 |
| `power` | 2, 1, -3, 0, 0, 0, 0, 0 |
| `pressure` | -1, 1, -2, 0, 0, 0, 0, 0 |
| `radiance` | 0, 1, -3, 0, 0, 0, 0, 0 |
| `radioactivity` | 0, 0, -1, 0, 0, 0, 0, 0 |
| `ratio` | 0, 0, 0, 0, 0, 0, 0, 0 |
| `reactive-power` | 2, 1, -3, 0, 0, 0, 0, 0 |
| `resistance` | 2, 1, -3, -2, 0, 0, 0, 0 |
| `resistivity` | 3, 1, -3, -2, 0, 0, 0, 0 |
| `section-modulus` | 3, 0, 0, 0, 0, 0, 0, 0 |
| `solid-angle` | 0, 0, 0, 0, 0, 0, 0, 0 |
| `specific-energy` | 2, 0, -2, 0, 0, 0, 0, 0 |
| `specific-heat-capacity` | 2, 0, -2, 0, -1, 0, 0, 0 |
| `specific-volume` | 3, -1, 0, 0, 0, 0, 0, 0 |
| `surface-tension` | 0, 1, -2, 0, 0, 0, 0, 0 |
| `temperature-difference` | 0, 0, 0, 0, 1, 0, 0, 0 |
| `temperature-point` | 0, 0, 0, 0, 1, 0, 0, 0 |
| `thermal-conductivity` | 1, 1, -3, 0, -1, 0, 0, 0 |
| `thermal-expansion` | 0, 0, 0, 0, -1, 0, 0, 0 |
| `torque` | 2, 1, -2, 0, 0, 0, 0, 0 |
| `velocity` | 1, 0, -1, 0, 0, 0, 0, 0 |
| `volume` | 3, 0, 0, 0, 0, 0, 0, 0 |
| `volume-flow` | 3, 0, -1, 0, 0, 0, 0, 0 |
| `wavenumber` | -1, 0, 0, 0, 0, 0, 0, 0 |
