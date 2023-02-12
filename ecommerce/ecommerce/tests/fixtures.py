import pytest

@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("admin", "admin@admin.com", "password")
