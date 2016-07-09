"""
"""
from __future__ import print_function, division
from ._version import __version__


def test(doctest=True, verbose=False, coverage=False):
    """
    Run the test suite.

    Uses `py.test <http://pytest.org/>`__ to discover and run the tests. If you
    haven't already, you can install it with `conda
    <http://conda.pydata.org/>`__ or `pip <https://pip.pypa.io>`__.

    Parameters:

    * doctest : bool
        If ``True``, will run the doctests as well (code examples that start
        with a ``>>>`` in the docs).
    * verbose : bool
        If ``True``, will print extra information during the test run.
    * coverage : bool
        If ``True``, will run test coverage analysis on the code as well.
        Requires ``pytest-cov``.

    Returns:

    * exit_code : int
        The exit code for the test run. If ``0``, then all tests pass.

    """
    import pytest
    args = []
    if verbose:
        args.append('-v')
    if coverage:
        args.append('--cov-report term-missing --cov={}'.format(__name__))
    if doctest:
        args.append('--doctest-modules')
    args.append('--pyargs {}'.format(__name__))
    return pytest.main(' '.join(args))
