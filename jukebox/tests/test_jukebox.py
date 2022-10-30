from jukebox.main import User
import pytest


# Arrange
@pytest.fixture
def user():
    return User("John Doe")


class TestUser:
    def test_user_has_name(self, user):
        # Assert
        assert hasattr(user, "name")


    def test_user_has_credits(self, user):
        # Assert
        assert hasattr(user, "credits")