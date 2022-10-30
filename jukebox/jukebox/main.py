class User:
    def __init__(self, name):
        self.name = name
        self.credits = 0


class Album:
    class Song:
        def __init__(self, title, duration):
            self.title = title
            self.duration = duration


    def __init__(self, title, artist, songs):
        self.title = title
        self.artist = artist
        self.songs = [Album.Song(song[0], song[1]) for song in songs]