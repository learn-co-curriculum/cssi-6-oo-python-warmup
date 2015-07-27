class Jukebox:
    def __init__(self, default_song_list=[]):
        # Use list() to make a copy of the input list. This is so that adding
        # new items to self.song_list does not alter the DEFAULT_SONGS list
        # in main.py.
        self.song_list = list(default_song_list)
        self.current = None

    def get_song_list(self):
        return self.song_list

    def play_song(self, song_number):
        # Only play if the index is valid.
        if song_number in range(0, len(self.song_list)):
            song = self.song_list[song_number]
            self.current = song
            song.play()

    def current_song(self):
        return self.current

    def stop_current_song(self):
        self.current = None

    def add_song(self, song):
        if song not in self.song_list:
            self.song_list.append(song)
            return True
        return False

    def get_most_popular_songs(self, number_of_songs):
        return sorted(self.song_list,
                      key=lambda x: x.times_played(),
                      reverse=True)[:number_of_songs]
