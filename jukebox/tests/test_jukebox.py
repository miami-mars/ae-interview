from jukebox.main import User, Album
import pytest


# Arrange
@pytest.fixture
def user():
    return User("John Doe")


@pytest.fixture
def album():
    songs = [
        ["American Idiot", "2:54"],
        ["Jesus of Suburbia", "9:08"],
        ["Holiday", "3:52"],
        ["Bouldevard of Broken Dreams", "4:22"],
        ["Are We the Waiting", "2:42"],
        ["St. Jimmy", "2:56"],
        ["Give Me Novacaine", "3:25"],
        ["She's a Rebel", "2:00"],
        ["Extraordinary Girl", "3:33"],
        ["Letterbomb", "4:05"],
        ["Wake Me Up When September Ends", "4:45"],
        ["Homecoming", "9:18"],
        ["Whatsername", "4:14"]
    ]
    return Album("American Idiot", "Green Day", songs)


class TestUser:
    def test_user_has_name(self, user):
        # Assert
        assert hasattr(user, "name")

    def test_user_has_credits(self, user):
        # Assert
        assert hasattr(user, "credits")

    @pytest.mark.parametrize("dollars, expected", [(1, 3), (2, 7), (3, 10), (5, 18), (8, 28), (10, 36), (21, 75)])
    def test_user_add_credits(self, user, dollars, expected):
        user.add_credits(dollars)
        assert user.credits == expected

    @pytest.mark.parametrize("dollars", [0, -1, -100])
    def test_user_add_credits_less_than_one(self, user, dollars): 
        with pytest.raises(ValueError):
            assert user.add_credits(dollars)


class TestAlbum:
    def test_album_has_title(self, album):
        # Assert
        assert hasattr(album, "title")

    def test_album_has_artist(self, album):
        # Assert
        assert hasattr(album, "artist")

    def test_album_has_songs(self, album):
        # Assert
        assert hasattr(album, "songs")

    def test_album_song_has_title(self, album):
        # Assert
        assert hasattr(album.songs[0], "title")

    def test_album_song_has_duration(self, album):
        # Assert
        assert hasattr(album.songs[0], "duration")