# coding: utf-8

import numpy as np
import math


def kkr(de, eps_imag, cshift=1e-6):
    """Calculate the Kramers-Kronig transformation on imaginary part of dielectric

    Doesn't correct for any artefacts resulting from finite window function.

    Args:
        de (float): Energy grid size at which the imaginary dielectric constant
            is given. The grid is expected to be regularly spaced.
        eps_imag (np.array): A numpy array with dimensions (n, 3, 3), containing
            the imaginary part of the dielectric tensor.
        cshift (float, optional): The implemented method includes a small
            complex shift. A larger value causes a slight smoothing of the
            dielectric function.

    Returns:
        A numpy array with dimensions (n, 3, 3) containing the real part of the
        dielectric function.
    """
    eps_imag = np.array(eps_imag)
    nedos = eps_imag.shape[0]
    cshift = complex(0, cshift)
    w_i = np.arange(0, nedos*de, de, dtype=np.complex_)
    w_i = np.reshape(w_i, (nedos, 1, 1))

    def integration_element(w_r):
        factor = w_i / (w_i**2 - w_r**2 + cshift)
        total = np.sum(eps_imag * factor, axis=0)
        return total * (2/math.pi) * de + np.diag([1, 1, 1])

    return np.real([integration_element(w_r) for w_r in w_i[:, 0, 0]])
