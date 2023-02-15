import pytest
import pytest_mock


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def mock_requests_get(mocker: pytest_mock.plugin.MockerFixture):
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock_get
