"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def omega_baryon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega baryon; the effective baryon density/critical density at z=0."""
    return cosmo.Ob0


@singledispatch
def rho_baryon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Baryon density at z = 0 in Msol Mpc-3."""
    return cosmo.Ob0 * cosmo.critical_density0


def omega_baryon(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent baryon density parameter.

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
    return cosmo.Ob(z)


@singledispatch
def rho_baryon(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent baryon density in Msol Mpc-3.

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
    return cosmo.Ob(z) * cosmo.critical_density(z)
