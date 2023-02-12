import pytest
import pytest_mock


@pytest.fixture
def mock_requests_get(mocker: pytest_mock.plugin.MockerFixture):
    mock = mocker.patch('requests.get')
    mock.return_value.__enter__.return_value.json.return_value = {
        'title': 'Lorem Ipsum',
        'extract': 'Lorem ipsum dolor sit amet',
    }
    return mock
