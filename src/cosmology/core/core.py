"""The Cosmology library."""

from __future__ import annotations

from typing import Any

from cosmology.api import CosmologyAPI, CosmologyAPINamespace

__all__: list[str] = []


def get_namespace(
    *cosmos: CosmologyAPI[Any],
    api_version: str | None = None,
) -> CosmologyAPINamespace:
    """Return the namespace for the given cosmology.

    Parameters
    ----------
    cosmos : `~astropy.cosmology.Cosmology`, positional-only
        The cosmology object(s) to get the namespace for.
    api_version : str | None, optional
        The array API version, by default `None`.

    Returns
    -------
    namespace : `~astropy.cosmology.core.CosmologyNamespace`
        The namespace object for the given cosmology.
    """
    namespaces: set[CosmologyAPINamespace] = {
        x.__cosmology_namespace__(api_version=api_version)
        for x in cosmos
        if isinstance(x, CosmologyAPI)
    }

    if not namespaces:
        msg = "Unrecognized cosmology input"
        raise ValueError(msg)
    elif len(namespaces) != 1:
        msg = f"Multiple namespaces for cosmology inputs: {namespaces}"
        raise ValueError(msg)

    return namespaces.pop()
