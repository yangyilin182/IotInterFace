import pytest

@pytest.fixture(params=[("100","1"),("101","2")])
def push_data(request):
    return request.param