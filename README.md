# Object-oriented Python Day 6 Warm-up!

## Instructions:
Fork and clone this lab, then complete the exercises below.

### 1. Jukebox Redux! 

This lab is a play off of the [Jukebox Lab](https://learn.co/tracks/google-cssi/5-python-advanced/python-labs/jukebox-lab) -- thought don't worry, you don't need to complete the Jukebox Lab to do this lab!

The first part of this lab is to simply see the working product that you're going to create.

1. Open `main.py` in Atom.
2. Uncomment the `import` statements that load the solution modules. **Don't** look at the solution source, though!
```python
# Uncomment the import statements below to view the solution's behavior.
import solution.jukebox_solution as jukebox 
import solution.song_solution as song
```
3. In the Terminal, run `python main.py` to run the working Jukebox. Try out a few commands, etc.
  * If there appears to be a bug in the behavior, tell Victoria :) 
4. When you're done playing around, comment out the solution import statements again.
```python
# Uncomment the import statements below to view the solution's behavior.
# import solution.jukebox_solution as jukebox 
# import solution.song_solution as song
```
5. Try running `python main.py` again. Most of the commands should be broken. To fix it, you'll be implementing behavior in `song.py` and `jukebox.py`

### 2. Objects: `__init__` and `__str__`

`main.py` is a program that creates and calls methods on a single `Jukebox` and multiple `Song` objects. In other words, `main.py` is a "client" of `Jukebox` and `Song`. In order for `main.py` to work correctly, you'll have to implement the behavior within `song.py` and `jukebox.py`.


1. Open `song.py` and `jukebox.py` in Atom.

  **Note:** You'll notice the method bodies all end in `pass`. `pass` is a statement that does nothing in Python. Since indentation matters in Python, a function body cannot actually be empty. Therefore, we use `pass` in the methods of `song.py` and `jukebox.py` to indicate an empty, unimplemented function body. You can delete `pass` as soon as you've written any other statement in the function body.

2. Implement `__init__` and `__str__` in `song.py`. The comments in the file will tell you the intended behavior.

  **Note:** Remember that `__init__` is a special method representing the constructor for the Song object. `__str__` is another special method that will be called on a Song object whenever it is `print`ed (or when `str()` is called on it)

3. Implement `__init__` and `get_song_list` in `jukebox.py`. The comments in the file will tell you the intended behavior.

4. Test out your object by running `python main.py`, and try out the "View song list" command.
  
  `main.py` adds two songs to the Jukebox by default, so you should see:
```
  1: Here Comes the Sun - The Beatles
  2: Sweet Caroline - Neil Diamond
```

### 3. Adding state to objects
1. Implement `play` and `times_played` in `song.py`. The comments in the file will tell you the intended behavior.
2. Implement `play_song`, `current_song`, and `stop_current_song` in `jukebox.py`. The comments in the file will tell you the intended behavior.
3. Test out your object by running `python main.py`, and try out the "Play song", "View current song", "Stop current song", and "Top 3 songs" commands.

  Here's an example of what you should see (with the menu text removed):
```
Enter a number: 2
Choose a song from the list:
  1: Here Comes the Sun - The Beatles
  2: Sweet Caroline - Neil Diamond
Enter a song number: 2
Playing 'Sweet Caroline - Neil Diamond'
```
```
Enter a number: 3
  Now playing: Sweet Caroline - Neil Diamond
```
```
Enter a number: 2
Choose a song from the list:
  1: Here Comes the Sun - The Beatles
  2: Sweet Caroline - Neil Diamond
Enter a song number: 1
Playing 'Here Comes the Sun - The Beatles'
```
```
Enter a number: 3
  Now playing: Here Comes the Sun - The Beatles
```
```
Enter a number: 4
  Stopped playing: Here Comes the Sun - The Beatles
```
```
Enter a number: 3 
  Now playing: None
```
```
Enter a number: 2
Choose a song from the list:
  1: Here Comes the Sun - The Beatles
  2: Sweet Caroline - Neil Diamond
Enter a song number: 1
Playing 'Here Comes the Sun - The Beatles'
```
```
Enter a number: 6
  1: Here Comes the Sun - The Beatles (plays: 2)
  2: Sweet Caroline - Neil Diamond (plays: 1)
```

### 4. Creating objects and `__eq__`
1. Implement `__eq__` in `song.py`. The comments in the file will tell you the intended behavior.

  **Note:** Like `__init__` and `__str__`, `__eq__` is another special method in Python. `__eq__` gets called whenever the `==` operator is applied to two objects of that type. 
2. Implement `add_song` in `jukebox.py`. The comments in the file will tell you the intended behavior.
3. Test out your object by running `python main.py`, and try out the "Add new song" command, then "View song list" to make sure it added.

  Here's an example of what you should see (with the menu text removed):
```
Enter a number: 5
Enter the song's title: Baby Love
Enter the song's artist: The Supremes
Does 'Baby Love - The Supremes' look correct? (y/n): y
'Baby Love - The Supremes' added.
```
```
Enter a number: 1
  1: Here Comes the Sun - The Beatles
  2: Sweet Caroline - Neil Diamond
  3: Baby Love - The Supremes
```
```
Enter a number: 5   
Enter the song's title: Come See About Me
Enter the song's artist: The Supremes
Does 'Come See About Me - The Supremes' look correct? (y/n): y
'Come See About Me - The Supremes' added.
```
```
Enter a number: 2
Choose a song from the list:
  1: Here Comes the Sun - The Beatles
  2: Sweet Caroline - Neil Diamond
  3: Baby Love - The Supremes
  4: Come See About Me - The Supremes
Enter a song number: 4
Playing 'Come See About Me - The Supremes'
```
```
Enter a number: 5
Enter the song's title: Come See About Me
Enter the song's artist: The Supremes
Does 'Come See About Me - The Supremes' look correct? (y/n): y
'Come See About Me - The Supremes' already exists.
```

### 5. Extra Credit: Comparisons

1. **Extra Credit:** Implement `get_most_popular_songs` in `jukebox.py`. The comments in the file will tell you the intended behavior.
  **Hint:** You may want to use the `sorted()` function.
