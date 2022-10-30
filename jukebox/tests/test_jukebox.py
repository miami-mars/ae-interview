from jukebox import User

class TestUser:
    def user_has_name(self):
        user = User("John Doe")
        assert hasattr(user, name)
