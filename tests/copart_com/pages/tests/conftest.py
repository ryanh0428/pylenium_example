import pytest

from tests.copart_com.pages.CopartPages import CopartPages


@pytest.fixture
def copart(py):
    return CopartPages(py)