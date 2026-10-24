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

## Secondary coverage reference

Kurt Gieck and Reiner Gieck, *Manual de fórmulas técnicas*, Spanish edition
supplied for this project. Use this handbook to identify engineering quantity
families and conventional units worth supporting. Verify bibliographic edition
details against the supplied copy before preparing the final bibliography.

Open Graf's architecture and technical documentation are independently
organized. The handbook is not a specification of the library, and its wording,
tables or chapter organization are not copied into the implementation.

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
