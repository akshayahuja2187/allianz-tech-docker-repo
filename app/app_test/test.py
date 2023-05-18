#!/usr/bin/python3
import pytest
import requests

@pytest.fixture(scope="session")
def kube_ip(pytestconfig):
    return pytestconfig.getoption("ip")

@pytest.mark.rest
def test_get_request(kube_ip):
  """Test making a GET request and verifying the output."""

  # Make the request.
  response = requests.get(f'http://{kube_ip}:30036')

  # Verify the status code.
  assert response.status_code == 200

  # Verify the content type.
  assert response.headers['Content-Type'] == 'text/html'

  # Verify the body.
  assert b'Everything looks good at this point.' in response.content
  assert b'Hi This is Akshay's nginx website' in response.content