from jukebox.main import User, Album
import pytest


# Arrange
@pytest.fixture
def user():
    return User("John Doe")


@pytest.fixture
def album():
    return Album("American Idiot", "Green Day")


class TestUser:
    def test_user_has_name(self, user):
        # Assert
        assert hasattr(user, "name")


    def test_user_has_credits(self, user):
        # Assert
        assert hasattr(user, "credits")


class TestAlbum:
    def test_album_has_title(self, album):
        # Assert
        assert hasattr(album, "title")

    def test_album_has_artist(self, album):
        # Assert
        assert hasattr(album, "artist")
