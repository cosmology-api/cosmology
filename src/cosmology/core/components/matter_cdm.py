"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def omega_dm0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega dark matter; the effective dark matter density/critical density at z=0."""
    return cosmo.Odm0


@singledispatch
def rho_dm0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Dark matter density at z = 0 in Msol Mpc-3."""
    return cosmo.Odm0 * cosmo.critical_density0


def omega_dm(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent dark matter density parameter.

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
    return cosmo.Odm(z)


@singledispatch
def rho_dm(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent dark matter density in Msol Mpc-3.

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
    return cosmo.Odm(z) * cosmo.critical_density(z)
