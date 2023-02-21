"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def omega_curve0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega curvature; the effective curvature density/critical density at z=0."""
    return cosmo.Ok0


@singledispatch
def rho_curve0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Curvature density at z = 0 in Msol Mpc-3."""
    return cosmo.Ok0 * cosmo.critical_density0


def omega_curve(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent curvature density parameter.

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
    return cosmo.Ok(z)


@singledispatch
def rho_curve(cosmo: StandardCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent curvature density in Msol Mpc-3.

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
    return cosmo.Ok(z) * cosmo.critical_density(z)
