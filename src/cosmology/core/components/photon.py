"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def omega_photon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega photon; the effective radiation density/critical density at z=0."""
    return cosmo.Ogamma0


@singledispatch
def rho_photon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Photon density at z = 0 in Msol Mpc-3."""
    return cosmo.Ogamma0 * cosmo.critical_density0


def omega_photon(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent photon density parameter.

    Parameters
    ----------
    cosmo : StandardCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.Ogamma(z)


@singledispatch
def rho_photon(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent photon density in Msol Mpc-3.

    Parameters
    ----------
    cosmo : StandardCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.Ogamma(z) * cosmo.critical_density(z)
