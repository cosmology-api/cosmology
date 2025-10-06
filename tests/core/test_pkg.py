"""Test the Cosmology API compat library."""


def test_imported():
    """This is a namespace package, so it should be importable."""
    import cosmology.api  # noqa: PLC0415

    import cosmology  # noqa: PLC0415

    assert cosmology.__name__ == "cosmology"
    assert cosmology.api.__name__ == "cosmology.api"
