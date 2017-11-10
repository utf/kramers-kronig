README
======

Introduction
------------

This repository provides a simple function to perform the Kramers-Kronig
transformation on the frequency-dependant imaginary dielectric function, to
obtain the real part of the dielectric function. The transformation is defined
as: <sup>[[1]](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.045112) </sup>

<p align="center">
<img src="https://cms.mpi.univie.ac.at/vasp/vasp/img610.png">
</p>

Where ε<sub>αβ</sub><sup>(1)</sup>(ω) is the real part of the dielectric constant
at energy, ω. P is the principle value, ε<sub>αβ</sub><sup>(2)</sup>(ω') is the
imaginary part of the dielectric constant and η is a small complex shift.

Together the full dielectric constant can be used to calculate the optical
absorption via the complex refractive index.


References
----------
[1]  M. Gajdoš, K. Hummer, G. Kresse, J. Furthmüller, and F. Bechstedt, "Linear optical properties in the PAW methodology", Phys. Rev. B **73**, 045112 (2006) DOI: [10.1103/PhysRevB.73.045112](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.045112)


Usage
-----

The `kkr.py` contains the function to perform the Kramers-Kronig transformation.

The `kkr` function expects the dielectric function, `eps_imag`, to be provided
as a `nx3x3` numpy array, containing the dielectric tensor on a regular energy
(photon frequency) grid.

The energy grid spacing, `de`, is also required.

A jupyter notebook has been provided, which gives a tutorial on how the script
should be used.

Requirements
------------

This script is currently compatible with Python 2.7 and Python 3.4.
Numpy is required for matrix operations.

License
-------

This script is made available under the MIT License.
