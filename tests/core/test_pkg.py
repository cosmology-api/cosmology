"""Test the Cosmology API compat library."""


def test_imported():
    """This is a namespace package, so it should be importable."""
    import cosmology
    import cosmology.api

    assert cosmology.__name__ == "cosmology"
    assert cosmology.api.__name__ == "cosmology.api"
