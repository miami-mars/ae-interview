class User:
    def __init__(self, name):
        self.name = name
        self.credits = 0

    def add_credits(self, dollar_amount):
        if dollar_amount < 1:
            raise ValueError("Please Enter a Whole-Number Dollar Amount!")

        while dollar_amount != 0:
            if dollar_amount / 5 >= 1:
                dollar_amount -= (difference := dollar_amount % 5)
                self.credits += (dollar_amount / 5) * 18
                dollar_amount = difference
            if dollar_amount / 2 >= 1:
                dollar_amount -= (difference := dollar_amount % 2)
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

if __name__ == "__main__":
    """
    user_exit = False
    current_user = None
    playlist = []

    with open("sample_data.json") as album_data:
        raw_data = json.loads(album_data)

    # import_albums function will return a list of Album data types
    albums = import_albums(raw_data)

    while not user_exit:
        Display Options
            1. Select User
            2. Pay for credits
            3. Select a song

        if 1:
            Display Options
                1. Create new user
                2. Select from list

            if 1:
                User Creation Process. Probably just enter name.
            elif 2:
                Display list and select from list available. Just names, we don't want to show credits.
        elif 2:
            Check if current_user is None
                "continue" to go back to beginning of while loop
            Enter a dollar amount
            Use the current_user.add_credits() to assign credits to user
        elif 3:
            Display Albums to select from with the XX-YY code next to
            the song names.
            song_selection = input("What Song will you select?: ")
            Use song_selection to get the title + duration from the song
            playlist.append[[title, duration]]

        Check how much time has elapsed.
        Check if playlist[0] has a list
        playlist[0][0] - elapsed time

        if playlist[0][1] <= 0:00:
            playlist.pop(0)

        Display playlist update
        if playlist[0]:
            print(f"Currently Playing: {playlist[0][0]}")
        if playlist[1]:
            print(f"Up next: {playlist[1][0]}")
    """