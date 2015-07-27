class Jukebox:
    def __init__(self, default_song_list=[]):
        # Initialize the Jukebox here!
        # |default_song_list| is a list of Song objects.
        pass

    def get_song_list(self):
        # Return all the songs in this Jukebox as a list of Song objects.
        pass

    def play_song(self, song_index):
        # Play the Song at |song_index|. Do not play the song if |song_index|
        # is not a valid index in the Song list.
        pass

    def current_song(self):
        # Return the current Song being played by the Jukebox.
        pass

    def stop_current_song(self):
        # Stop the current Song being played by the Jukebox.
        pass

    def add_song(self, song):
        # Add a new Song object |song| to the Jukebox, if there is not already
        # a Song in the Jukebox with the same name and title. Returns True if
        # the song was added, False otherwise.
        pass

    def get_most_popular_songs(self, number_of_songs):
        # Returns the top |number_of_songs| Songs, orderd by play count. For
        # example, jukebox.get_most_popular_songs(5) should return a list of
        # length 5, where the 0th item has the largest times_played(), the
        # 1st item has the next largest times_played(), etc. Ties can be
        # returned in any order.

        # For now, just return the same list as get_song_list(). Delete this
        # when implementing your own version of this function.
        return self.get_song_list()
