import webbrowser

class Movie():
    """ This class provides a way to store movie related information.
    The class variables are initialized here and have date stored in entertainmentcenter.py.
    """

    def __init__(self, movie_title, translated_title, movie_storyline,
                 poster_image, trailer_youtube,
                 imdb_page, imdb_rating, location, year,
                 saavn_page):
        self.title = movie_title
        self.translated_title = translated_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_page_url = imdb_page
        self.imdb_rating = imdb_rating
        self.location = location
        self.year = year
        self.saavn_page = saavn_page

# This method provides a way to show the movie trailer from YouTube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
