"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch
from typing import cast

from cosmology.api import StandardCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


# ----------------------------------------------
# Hubble


def hubble_parameter0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Hubble parameter at z=0."""
    return cosmo.H0


def dimensionless_hubble_parameter0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Dimensionless Hubble parameter at z=0."""
    return cosmo.h


def hubble_distance(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Hubble distance in Mpc."""
    return cosmo.hubble_distance


def hubble_time(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Hubble time in Gyr."""
    return cosmo.hubble_time


def hubble_parameter(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
    """Hubble function :math:`H(z)` in km s-1 Mpc-1.

    Parameters
    ----------
    cosmo : StandardCosmologyAPI, positional-only
        The cosmology.
    z : Array
        The redshift(s) at which to evaluate the Hubble parameter.

    Returns
    -------
    Array
    """
    return cosmo.H(z)


def standardized_hubble_function(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
    """Standardised Hubble function :math:`E(z) = H(z)/H_0`.

    Parameters
    ----------
    cosmo : StandardCosmologyAPI, positional-only
        The cosmology.
    z : Array
        The redshift(s) at which to evaluate efunc.

    Returns
    -------
    Array
    """
    return cosmo.efunc(z)


def inv_standardized_hubble_function(
    cosmo: StandardCosmologyAPI,
    z: ArrayT,
    /,
) -> ArrayT:
    """Inverse of ``efunc``.

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
    return cosmo.inv_efunc(z)


# ----------------------------------------------
# Temperature


def Tcmb0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """CMB temperature at z = 0 in K."""
    return cosmo.Tcmb0


def Tcmb(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
    """Redshift-dependent CMB temperature in K.

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
    return cosmo.Tcmb(z)


# ----------------------------------------------
# Curvature density


def omega_curve0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega curvature; the effective curvature density/critical density at z=0."""
    return cosmo.Ok0


def rho_curve0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Curvature density at z = 0 in Msol Mpc-3."""
    return cosmo.Ok0 * cosmo.critical_density0


def omega_curve(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


def rho_curve(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


# ----------------------------------------------
# Matter density


def omega_matter0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega matter; the effective matter density/critical density at z=0."""
    return cosmo.Om0


def rho_matter0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Matter density at z = 0 in Msol Mpc-3."""
    return cosmo.Om0 * cosmo.critical_density0


def omega_matter(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


def rho_matter(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


# ----------------------------------------------
# Cold dark matter density


def omega_dm0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega dark matter; the effective dark matter density/critical density at z=0."""
    return cosmo.Odm0


@singledispatch
def rho_dm0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Dark matter density at z = 0 in Msol Mpc-3."""
    return cosmo.Odm0 * cosmo.critical_density0


def omega_dm(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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
def rho_dm(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


# ----------------------------------------------
# Baryon density


def omega_baryon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega baryon; the effective baryon density/critical density at z=0."""
    return cosmo.Ob0


@singledispatch
def rho_baryon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Baryon density at z = 0 in Msol Mpc-3."""
    return cosmo.Ob0 * cosmo.critical_density0


def omega_baryon(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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
def rho_baryon(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


# ----------------------------------------------
# Photon density


def omega_photon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega photon; the effective radiation density/critical density at z=0."""
    return cosmo.Ogamma0


@singledispatch
def rho_photon0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Photon density at z = 0 in Msol Mpc-3."""
    return cosmo.Ogamma0 * cosmo.critical_density0


def omega_photon(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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
def rho_photon(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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


# ----------------------------------------------
# Neutrino density (and related)


def omega_neutrino0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega neutrino; the effective neutrino density/critical density at z=0."""
    return cosmo.Onu0


@singledispatch
def rho_neutrino0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Neutrino density at z = 0 in Msol Mpc-3."""
    return cosmo.Onu0 * cosmo.critical_density0


def omega_neutrino(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
    """Redshift-dependent neutrino density parameter.

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
    return cosmo.Onu(z)


@singledispatch
def rho_neutrino(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
    """Redshift-dependent neutrino density in Msol Mpc-3.

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
    return cosmo.Onu(z) * cosmo.critical_density(z)


def N_eff(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Effective number of neutrino species.

    Parameters
    ----------
    cosmo : StandardCosmologyAPI, positional-only
        The cosmology.

    Returns
    -------
    Array
    """
    return cosmo.Neff


def mass_nu(cosmo: StandardCosmologyAPI[ArrayT], /) -> tuple[ArrayT, ...]:
    """Neutrino mass in eV.

    Parameters
    ----------
    cosmo : StandardCosmologyAPI, positional-only
        The cosmology.

    Returns
    -------
    tuple[Array, ...]
        Tuple of neutrino masses in eV.
    """
    return cast("tuple[ArrayT, ...]", cosmo.m_nu)


# ----------------------------------------------
# Dark energy density


def omega_de0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega dark energy; the effective dark energy density/critical density at z=0."""
    return cosmo.Ode0


@singledispatch
def rho_de0(cosmo: StandardCosmologyAPI[ArrayT], /) -> ArrayT:
    """Dark energy density at z = 0 in Msol Mpc-3."""
    return cosmo.Ode0 * cosmo.critical_density0


def omega_de(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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
def rho_de(cosmo: StandardCosmologyAPI, z: ArrayT, /) -> ArrayT:
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
