"""Version tests."""

from cedro import __version__


def test_version():
    """Version is a non-empty string."""
    assert isinstance(__version__, str) and __version__
