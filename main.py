import jukebox
import song

# Uncomment the import statements below to view the solution's behavior.
# import solution.jukebox_solution as jukebox
# import solution.song_solution as song

##############################################################################
# DO NOT EDIT BELOW THIS LINE!!!
##############################################################################

DEFAULT_SONGS = [
    song.Song("Here Comes the Sun", "The Beatles"),
    song.Song("Sweet Caroline", "Neil Diamond")
]

MENU_OPTIONS = [
    "View song list",
    "Play song",
    "View current song",
    "Stop current song",
    "Add new song",
    "Top 3 songs",
    "Quit"
]

player = jukebox.Jukebox(DEFAULT_SONGS)

def menu():
    print "Menu:"
    for option in enumerate(MENU_OPTIONS, 1):
        print "  {}: {}".format(option[0], option[1])

def view_song_list():
    print_songs()
    raw_input("(press enter)")

def print_songs():
    for song_tuple in enumerate(player.get_song_list(), 1):
        print "  {}: {}".format(song_tuple[0], song_tuple[1])

def play_song():
    print "Choose a song from the list:"
    print_songs()
    user_input = raw_input("Enter a song number: ")
    if not is_valid(user_input, len(player.get_song_list())):
        print "'{}' is not a valid selection.".format(user_input)
        return
    choice = int(user_input)
    player.play_song(choice - 1)
    print "Playing '{}'".format(player.current_song())
    raw_input("(press enter)")

def view_current_song():
    print "  Now playing: {}".format(player.current_song())
    raw_input("(press enter)")

def stop_current_song():
    print "  Stopped playing: {}".format(player.current_song())
    player.stop_current_song()
    raw_input("(press enter)")

def add_new_song():
    song_name = raw_input("Enter the song's title: ")
    artist = raw_input("Enter the song's artist: ")
    new_song = song.Song(song_name, artist)
    confirm = raw_input("Does '{}' look correct? (y/n): ".format(new_song))
    if confirm.lower() == "y":
        if player.add_song(new_song):
            print "'{}' added.".format(new_song)
        else:
            print "'{}' already exists.".format(new_song)
    else:
        print "New song cancelled."
    raw_input("(press enter)")

def most_popular_songs():
    for song in enumerate(player.get_most_popular_songs(3), 1):
        print "  {}: {} (plays: {})".format(song[0],
                                            song[1],
                                            song[1].times_played())
    raw_input("(press enter)")

def is_valid(user_input, length):
    try:
        int(user_input)
    except ValueError:
        return False
    if int(user_input) not in range(1, length + 1):
        return False
    return True

##############################################################################
# Main
print "Welcome to Jukebox V2!"
while True:
    menu()
    user_input = raw_input("Enter a number: ")
    if not is_valid(user_input, len(MENU_OPTIONS)):
        print "'{}' is not a valid selection.".format(user_input)
        continue
    choice = int(user_input)
    if choice == 1:
        view_song_list()
    elif choice == 2:
        play_song()
    elif choice == 3:
        view_current_song()
    elif choice == 4:
        stop_current_song()
    elif choice == 5:
        add_new_song()
    elif choice == 6:
        most_popular_songs()
    else:
        break

    print ""
