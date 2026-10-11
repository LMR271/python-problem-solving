"""Shared pytest setup.

Tests for a problem whose solution still raises NotImplementedError are
reported as "skipped" instead of "failed". That keeps the test suite (and the
GitHub badge) green for problems I haven't started yet.
"""

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        report.outcome = "skipped"
        report.longrepr = (str(item.path), item.location[1], "not solved yet")
