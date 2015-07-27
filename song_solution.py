class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.play_count = 0

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist

    def play(self):
        self.play_count += 1

    def times_played(self):
        return self.play_count
