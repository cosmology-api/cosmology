"""The Cosmology library."""

from __future__ import annotations

from functools import singledispatch

from cosmology.api import BackgroundCosmologyAPI
from cosmology.api._array_api import ArrayT

__all__: list[str] = []


def scale_factor0(cosmo: BackgroundCosmologyAPI[ArrayT], /) -> ArrayT:
    """Scale factor at z=0."""
    return cosmo.scale_factor0


def scale_factor(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependenct scale factor.

    The scale factor is defined as :math:`a = a_0 / (1 + z)`.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        The redshift(s) at which to evaluate the scale factor.

    Returns
    -------
    Array
    """
    return cosmo.scale_factor(z)


# ----------------------------------------------
# Omega


def omega_total0(cosmo: BackgroundCosmologyAPI[ArrayT], /) -> ArrayT:
    """Omega total; the total density/critical density at z=0."""
    return cosmo.Otot0


@singledispatch
def rho_total0(cosmo: BackgroundCosmologyAPI[ArrayT], /) -> ArrayT:
    """Total density at z = 0 in Msol Mpc-3."""
    return cosmo.Otot0 * cosmo.critical_density0


def omega_total(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    r"""Redshift-dependent total density parameter.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array
        Input redshifts.

    Returns
    -------
    Array
    """
    return cosmo.Otot(z)


@singledispatch
def rho_total(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent total density in Msol Mpc-3.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array
        Input redshifts.

    Returns
    -------
    Array
    """
    return cosmo.Otot(z) * cosmo.critical_density(z)


# ----------------------------------------------
# Density


def critical_density0(cosmo: BackgroundCosmologyAPI[ArrayT], /) -> ArrayT:
    """Critical density at z = 0 in Msol Mpc-3."""
    return cosmo.critical_density0


def critical_density(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent critical density in Msol Mpc-3."""
    return cosmo.critical_density(z)


# ----------------------------------------------
# Time


def age(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Age of the universe in Gyr at redshift ``z``.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.age(z)


def lookback_time(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Lookback time to redshift ``z`` in Gyr.

    The lookback time is the difference between the age of the Universe now
    and the age at redshift ``z``.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.lookback_time(z)


# ----------------------------------------------
# Comoving distance


def comoving_distance(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    r"""Comoving line-of-sight distance :math:`d_c(z)` in Mpc.

    The comoving distance along the line-of-sight between two objects
    remains constant with time for objects in the Hubble flow.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.comoving_distance(z)


def comoving_transverse_distance(
    cosmo: BackgroundCosmologyAPI[ArrayT],
    z: ArrayT,
    /,
) -> ArrayT:
    r"""Transverse comoving distance :math:`d_M(z)` in Mpc.

    This value is the transverse comoving distance at redshift ``z``
    corresponding to an angular separation of 1 radian. This is the same as
    the comoving distance if :math:`\Omega_k` is zero (as in the current
    concordance Lambda-CDM model).

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.comoving_transverse_distance(z)


def comoving_volume(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    r"""Comoving volume in cubic Mpc.

    This is the volume of the universe encompassed by redshifts less than
    ``z``. For the case of :math:`\Omega_k = 0` it is a sphere of radius
    `comoving_distance` but it is less intuitive if :math:`\Omega_k` is not.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array
        Input redshift.

    Returns
    -------
    Array
    """
    return cosmo.comoving_volume(z)


def differential_comoving_volume(
    cosmo: BackgroundCosmologyAPI[ArrayT],
    z: ArrayT,
    /,
) -> ArrayT:
    r"""Differential comoving volume in cubic Mpc per steradian.

    If :math:`V_c` is the comoving volume of a redshift slice with solid
    angle :math:`\Omega`, this function returns

    .. math::

        \mathtt{dvc(z)}
        = \frac{1}{d_H^3} \, \frac{dV_c}{d\Omega \, dz}
        = \frac{x_M^2(z)}{E(z)}
        = \frac{\mathtt{xm(z)^2}}{\mathtt{ef(z)}} \;.

    """
    return cosmo.differential_comoving_volume(z)


# ----------------------------------------------
# Angular diameter distance


def angular_diameter_distance(
    cosmo: BackgroundCosmologyAPI[ArrayT],
    z: ArrayT,
    /,
) -> ArrayT:
    """Angular diameter distance :math:`d_A(z)` in Mpc.

    This gives the proper (sometimes called 'physical') transverse
    distance corresponding to an angle of 1 radian for an object
    at redshift ``z`` ([1]_, [2]_, [3]_).

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array, positional-only
        Input redshift.

    Returns
    -------
    Array

    References
    ----------
    .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 421-424.
    .. [2] Weedman, D. (1986). Quasar astronomy, pp 65-67.
    .. [3] Peebles, P. (1993). Principles of Physical Cosmology, pp 325-327.
    """
    return cosmo.angular_diameter_distance(z)


# ----------------------------------------------
# Luminosity distance


def luminosity_distance(cosmo: BackgroundCosmologyAPI[ArrayT], z: ArrayT, /) -> ArrayT:
    """Redshift-dependent luminosity distance in Mpc.

    This is the distance to use when converting between the bolometric flux
    from an object at redshift ``z`` and its bolometric luminosity [1]_.

    Parameters
    ----------
    cosmo : BackgroundCosmologyAPI, positional-only
        The cosmology.
    z : Array
        Input redshift.

    Returns
    -------
    Array

    References
    ----------
    .. [1] Weinberg, 1972, pp 420-424; Weedman, 1986, pp 60-62.
    """
    return cosmo.luminosity_distance(z)
