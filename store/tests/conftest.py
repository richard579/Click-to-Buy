from django.contrib.auth.models import user
from rest_framework.testimport APIClient
import pytest


@pytest.ficture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate
