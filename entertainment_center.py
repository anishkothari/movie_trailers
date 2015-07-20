import media
import fresh_tomatoes

andaz_apna_apna = media.Movie("Andaz Apna Apna", "A movie to make you laugh!",
                        "https://upload.wikimedia.org/wikipedia/en/1/15/Andaz_Apna_Apna.jpg",
                        "https://youtu.be/fd_w7Qw8biU")

jaane_bhi_do_yaaro = media.Movie("Jaane Bhi Do Yaaro",
                        "One of the funniest movies ever",
                        "https://upload.wikimedia.org/wikipedia/en/6/6e/Jaane_Bhi_Do_Yaaro_1983_film_poster.jpg",
                        "https://youtu.be/spkmLziFFg4")

choti_si_baat = media.Movie("Choti Si Baat", "An interesting love story",
                       "https://upload.wikimedia.org/wikipedia/en/f/f6/Chhoti_Si_Baat.jpg",
                       "https://www.youtube.com/watch?v=ah4KCyj-NT4")

aamir = media.Movie("Aamir", "What would you do?",
                    "https://upload.wikimedia.org/wikipedia/en/1/1f/Aamir_poster.jpg",
                    "https://youtu.be/vHgYGTvMpBw")

anand = media.Movie("Anand", "A dying man lives his life to the fullest",
                    "https://upload.wikimedia.org/wikipedia/en/c/c9/Anand_film.jpg",
                    "https://youtu.be/tfGX2AEaMUU")

queen = media.Movie("Queen", "A women goes on her honeymoon",
                    "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",
                    "https://youtu.be/KGC6vl3lzf0")

movies = [andaz_apna_apna, jaane_bhi_do_yaaro, choti_si_baat, aamir, anand, queen]
#print(media.Movie.VALID_RATINGS)
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
