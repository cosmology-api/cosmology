"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def omega_de0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega dark energy; the effective dark energy density/critical density at z=0."""
    return cosmo.Ode0


@singledispatch
def rho_de0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Dark energy density at z = 0 in Msol Mpc-3."""
    return cosmo.Ode0 * cosmo.critical_density0


def omega_de(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent dark energy density parameter.

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
    return cosmo.Ode(z)


@singledispatch
def rho_de(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent dark energy density in Msol Mpc-3.

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
    return cosmo.Ode(z) * cosmo.critical_density(z)
