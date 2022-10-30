class User:
    def __init__(self, name):
        self.name = name
        self.credits = 0

    def add_credits(self, dollar_amount):
        if dollar_amount < 1:
            raise ValueError("Please Enter a Whole-Number Dollar Amount!")
        
        while dollar_amount != 0:
            if dollar_amount / 5 >= 1:
                (difference := dollar_amount % 5)
                dollar_amount -= difference
                self.credits += (dollar_amount / 5) * 18
                dollar_amount = difference
            if dollar_amount / 2 >= 1:
                (difference := dollar_amount % 2)
                dollar_amount -= difference
                self.credits += (dollar_amount / 2) * 7
                dollar_amount = difference
            if dollar_amount == 1:
                self.credits += 3
                dollar_amount = 0


class Album:
    class Song:
        def __init__(self, title, duration):
            self.title = title
            self.duration = duration


    def __init__(self, title, artist, songs):
        self.title = title
        self.artist = artist
        self.songs = [Album.Song(song[0], song[1]) for song in songs]