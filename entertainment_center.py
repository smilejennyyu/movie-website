import media
import fresh_tomatoes


# create 6 movie objects
pitch_perfect_url = ('https://images-na.ssl-images-amazon.com/'
                     'images/I/515IUyibrcL._AC_UL320_SR202,320_.jpg')
pitch_perfect = media.Movie("Pitch Perfect",
                            "Beca is cajoled into joining The Bellas.",
                            pitch_perfect_url,
                            "https://www.youtube.com/watch?v=8dItOM6eYXY")
hobbit_url = ('https://ia.media-imdb.com/images/M/MV5BMTcwNTE4MTUxMl5BMl'
              '5BanBnXkFtZTcwMDIyODM4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg')
hobbit = media.Movie("The Hobbit",
                     "The Hobbit consists three high fantasy adventure films.",
                     hobbit_url,
                     "https://www.youtube.com/watch?v=JTSoD4BBCJc")
ready_player_one_url = ('https://ia.media-imdb.com/images/M/MV5BY2JiY'
                        'TNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3X'
                        'kEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_UX182_'
                        'CR0,0,182,268_AL_.jpg')
ready_player_one = media.Movie("Ready Player One",
                               """The creator of a VR world releases a
                                videe to challenge all OASIS users to
                                find his Easter Egg.""",
                               ready_player_one_url,
                               "https://www.youtube.com/watch?v=axf7gHBdgDQ")
divergent = media.Movie("Divergent",
                        """In a world divided by factions based on virtues,
                        Tris learns she's Divergent and won't fit in.""",
                        """https://ia.media-imdb.com/images/M/MV5BMTYxMzYwODE4OV5BMl5BanBnXkFtZTgwNDE5MzE2MDE@._V1_UX182_
                        CR0,0,182,268_AL_.jpg""",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")
intership = media.Movie("Intership",
                        """Two salesmen whose careers have been torpedoed by the digital age
                         find their way into a internship at Google.""",
                        """https://ia.media-imdb.com/images/M/MV5BMjM1MzczMDgwOV5BMl5BanBnXkFtZTcwMDM4NjM2OQ@@._V1_UX182_
                        CR0,0,182,268_AL_.jpg""",
                        "https://www.youtube.com/watch?v=cdnoqCViqUo")
the_imitation_game_url = ('https://ia.media-imdb.com/images/M/MV5BOTgwMz'
                          'FiMWYtZDhlNS00ODNkLWJiODAtZDVhNzgyNzJhYjQ4L'
                          '2ltYWdlXkEyXkFqcGdeQXVyNzEzOTYxNTQ@._V1_UX182'
                          '_CR0,0,182,268_AL_.jpg')
the_imitation_game = media.Movie("The Imitation Game",
                                 """Alan Turing tries to crack the Enigma
                                  code""",
                                 the_imitation_game_url,
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")

# put movie objects into an array
movies = [pitch_perfect, hobbit, ready_player_one,
          divergent, intership, the_imitation_game]

# open all the movies in the browser
fresh_tomatoes.open_movies_page(movies)
