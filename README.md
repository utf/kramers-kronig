README
======

Introduction
------------

This repository provides a simple function to perform the Kramers-Kronig
transformation on the frequency-dependant imaginary dielectric function, to
obtain the real part of the dielectric function. The transformation is defined
as: <sup>[[1]](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.045112) </sup>

$$\epsilon _{{\alpha \beta }}^{{(1)}}(\omega )=1+{\frac  {2}{\pi }}P\int _{0}^{{\infty }}{\frac  {\epsilon _{{\alpha \beta }}^{{(2)}}(\omega ')\omega '}{\omega '^{2}-\omega ^{2}+i\eta }}d\omega '$$

Where $\epsilon _{{\alpha \beta }}^{{(1)}}(\omega )$ is the real part of the dielectric constant
at energy, $\omega$. $P$ is the principle value, $\epsilon _{{\alpha \beta }}^{{(2)}}(\omega ')$ is the
imaginary part of the dielectric constant and $\eta$ is a small complex shift. A
larger $\eta$ results in a slight smoothing of the real dielectric function.

The dielectric constant can be used to calculate the optical
absorption via the complex refractive index.


References
----------
[1]  M. Gajdoš, K. Hummer, G. Kresse, J. Furthmüller, and F. Bechstedt, "Linear optical 
properties in the PAW methodology", Phys. Rev. B **73**, 045112 (2006)
DOI: [10.1103/PhysRevB.73.045112](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.045112)


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
