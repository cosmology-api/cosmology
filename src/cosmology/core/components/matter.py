"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def omega_matter0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega matter; the effective matter density/critical density at z=0."""
    return cosmo.Om0


@singledispatch
def rho_matter0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Matter density at z = 0 in Msol Mpc-3."""
    return cosmo.Om0 * cosmo.critical_density0


def omega_matter(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent matter density parameter.

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
    return cosmo.Om(z)


@singledispatch
def rho_matter(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent matter density in Msol Mpc-3.

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
    return cosmo.Om(z) * cosmo.critical_density(z)
