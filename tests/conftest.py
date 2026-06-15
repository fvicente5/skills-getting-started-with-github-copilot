from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

ORIGINAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: restore baseline in-memory store before each test.
    app_module.activities.clear()
    app_module.activities.update(deepcopy(ORIGINAL_ACTIVITIES))

    yield

    # Cleanup: leave state clean even if a test fails mid-execution.
    app_module.activities.clear()
    app_module.activities.update(deepcopy(ORIGINAL_ACTIVITIES))
