import webbrowser


class Movie ():
    """Class describing attributes an behavior of a Person.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title (str): title of the movie.
        movie_storyline (str): storyline of the movie
        post_image (str): image URL
        trailer_Youtube (str): Youtube URL

    Attributes:
        title (str): title of the movie.
        storyline (str): storyline of the movie
        poster_image_url (str): image URL
        trailer_youtube_url (str): Youtube URL
    """
    def __init__(self, movie_title, movie_storyline,
                 post_image, trailer_Youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = post_image
        self.trailer_youtube_url = trailer_Youtube
