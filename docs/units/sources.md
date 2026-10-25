# Sources and conversion policy

The catalogue must distinguish definitions, conventional conversion factors,
and measured constants. A printed decimal does not become exact unless its
source defines it as exact. Record historical or regional conventions in names
and metadata.

## Primary references

- BIPM, *The International System of Units (SI)*, ninth edition and published
  updates: <https://www.bipm.org/en/publications/si-brochure>.
- NIST, *SI Units*, links to the defining constants, base and derived units,
  prefixes, SP 330 and SP 811:
  <https://www.nist.gov/pml/owm/metric-si/si-units>.
- NIST, *Guide for the Use of the International System of Units (SI)*, SP 811,
  Appendix B: <https://www.nist.gov/pml/special-publication-811>.
- CODATA recommended values, distributed by NIST:
  <https://physics.nist.gov/cuu/Constants/>. Record the recommendation's year
  when using a measured value such as the atomic mass constant.

NIST's SI overview identifies seven base units, 22 derived units with special
names and 24 decimal prefixes. Its links and BIPM publications are the starting
points for checking current definitions; historical tables need edition checks.

## Reviewed angular definitions

The radian and degree factories were checked on 2026-10-24 against BIPM,
*SI Brochure*, ninth edition, version 4.01, Tables 4 and 8:
<https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf>.
The radian is the coherent SI unit of plane angle. One degree is exactly
(pi/180) radians; the implementation retains symbolic pi rather than a
rounded decimal factor. NIST SP 330 (2019) independently confirms that relation:
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.330-2019.pdf>.

These angular definitions remain unchanged. Step 8 implements the prefix
eligibility flags (radian yes, degree no) and the reviewed catalogue below.

## Secondary coverage reference

Kurt Gieck and Reiner Gieck, *Manual de fórmulas técnicas*. Alfaomega/Marcombo,
2003, ISBN 970-15-0840-8 (Alfaomega), ISBN 84-267-1330-0 (Marcombo), Spanish
copy supplied for this project. Bibliographic data was checked on PDF page 4.
The general nomenclature on PDF pages 9–10 and units section A1–A9 guide coverage,
not factors or architecture.

Open Graf's architecture and technical documentation are independently
organized. The handbook is not a specification of the library, and its wording,
tables or chapter organization are not copied into the implementation.

## Step 8 review and source identifiers

Reviewed on 2026-10-24. The [catalogue](catalogue.md) records a source ID on each
factory; `tools/units-catalogue.json` holds the reviewed data and source map.
`tools/units_catalogue.py` deterministically writes the Graf sources, catalogue
reference and per-factory integration checks. Run it with `--check` to verify
reproducibility. Hand-maintained physical anchors, defining equations and prefix
tables are independent of that generation.

| Source ID | Use and primary reference |
| --- | --- |
| `BIPM-SI-9-v4.01` | SI base/derived definitions and dimensions, Tables 2, 4–6; 24 decimal prefixes, Table 7; accepted/historical non-SI units, Table 8; all 10 binary prefixes, chapter 3. [Brochure](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf). |
| `IEC-80000-13-2025` | Binary prefix convention; edition 2 adds the newer prefixes. [Official publication](https://webstore.iec.ch/en/publication/87379). BIPM v4.01 explicitly lists robi/2^90 and quebi/2^100. NIST's [older binary summary](https://physics.nist.gov/cuu/Units/binary.html) also defines byte as 8 bit. |
| `NIST-SP811-2008` | [Appendix B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8): engineering/customary relationships. Rounded display factors are reconstructed from the exact defining conventions, rather than treated as new exact decimals. |
| `international-yard-pound-1959` | Yard 0.9144 m; foot 0.3048 m; inch 0.0254 m; avoirdupois pound 0.45359237 kg. [NBS 1959 report](https://nvlpubs.nist.gov/nistpubs/Legacy/MP/nbsmiscellaneouspub228.pdf). [NIST foot history](https://www.nist.gov/pml/us-surveyfoot) distinguishes the retired U.S. survey foot; catalogue feet/acres use the international foot. |
| `standard-gravity-9.80665` | Conventional standard gravity 9.80665 m/s², as listed in NIST B.8; force and gravitational engineering units explicitly use this convention, not local gravity. |
| `CODATA-2022-atomic-mass-constant` | Dalton conversion nominally 1.66053906892×10^-27 kg, standard uncertainty 5.2×10^-37 kg. [NIST SP 961, May 2024, CODATA 2022](https://physics.nist.gov/cuu/pdf/wall_2022.pdf). `exact: no`, edition and absolute uncertainty are stored; no uncertainty propagation for measurements is claimed. |
| `fixed-duration-convention` | A week is seven fixed 86400-second days; a Julian year is exactly 365.25 such days. These are fixed durations, not calendar arithmetic or a prediction of leap seconds. |

Exact derived conventions include 231 in³ per U.S. liquid gallon, 42 such
gallons per petroleum barrel, 128 U.S. fluid ounces per U.S. liquid gallon,
4.54609 L per Imperial gallon and 160 Imperial fluid ounces per Imperial gallon.
Mass conventions distinguish avoirdupois/troy ounces and short/long tons.
The calorie conventions are thermochemical (4.184 J) and International Table
(4.1868 J). The International Table Btu is exactly 1055.05585262 J; the exact
value is confirmed in [NBS gas heating-value guidance, A3.2.2](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir81-2401.pdf).
Mechanical horsepower is derived from 550 ft·lbf/s, metric horsepower from
75 kgf·m/s and electrical horsepower from 746 W. Slug and technical mass unit
use their named force/acceleration definitions. CGS conversions are explicitly
the conventional NIST SP 811 relationships; no implicit electromagnetic model
or measured vacuum constant is substituted.

## Coverage and corrections relative to the secondary reference

| Reference concern | Catalogue treatment |
| --- | --- |
| Space, angle and time | Metric/international geometry, square/cubic factories, angles, fixed durations, angular rates and acceleration. |
| Mechanics and fluids | Mass/force, energy/torque, pressure, momentum/inertia, density, flow and viscosities retain separate kinds. |
| Heat | Temperature differences, heat capacity, conductivity, expansion and heat flux. Absolute points and boundaries are step 9. |
| Electricity and magnetism | SI named units and coherent electrical/magnetic engineering units, including distinct active/apparent/reactive power kinds. |
| Light and optics | Photometric/radiometric kinds, luminance versus illuminance, optical power. |
| Chemistry, radiation and information | Linear chemical/radiation units and decimal/binary information units; reference/model-dependent conversions remain step 9. |
| Historical SI definitions in A1–A2 | Use the modern constant-based SI, not the prototype kilogram or older kelvin/ampere definitions. |
| Prefix table A3 | Expand the older coverage to all 24 current SI prefixes and 10 binary prefixes. |
| Rounded pound, gravity, mile and horsepower factors in A6–A9 | Use exact defining relations; printed rounded equalities do not define the catalogue values. |
| Imperial gallon, A9 (PDF page 20), item a63 | The printed cubic-meter equivalence is dimensionally inconsistent by a factor of 1000. Use 4.54609 L = 0.00454609 m³, independently checked against NIST. |
| Pressure and heat conventions | Torr is 101325/760 Pa; no equality with a temperature-dependent mercury column is assumed. Calorie/Btu/horsepower names state the convention. |

The catalogue is a finite reviewed set with extensible factories. Derived units
are unlimited; the implementation does not claim that every possible unit or
every handbook formula is a named catalogue entry. Absolute-temperature,
logarithmic, gauge/reference, chemical-hardness and dose-weighting models remain
in step 9. Documentation and code are organized independently from the handbook.

## Review rules

- Check dimensional consistency before accepting a tabulated factor.
- Verify powers of ten and squared/cubed prefixes independently.
- Distinguish mass from force and energy from torque, even where dimensions or
  informal naming could conceal the difference.
- Distinguish fixed durations from calendar periods and decay time from decay
  rate.
- Use current SI definitions for base units; identify obsolete definitions as
  historical rather than presenting them as current.
- Keep regional liquid measures, calorie conventions, standard gravity and
  measured physical constants explicit.
