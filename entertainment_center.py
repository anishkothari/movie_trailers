import media
import fresh_tomatoes

# These are variables with movie information as specified in the Movie() class in media.py

andaz_apna_apna = media.Movie(
    "Andaz Apna Apna",
    "To Each His Own",
    "Two men woo a wealthy heiress and her friend",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Andaz_Apna_Apna.jpg",
    "https://youtu.be/fd_w7Qw8biU",
    "http://www.imdb.com/title/tt0109117/",
    "8.8",
    "Bhopal and Ooty, India",
    "1994",
    "http://www.saavn.com/s/album/hindi/Andaz-Apna-Apna-1994/C,nNoMcpMbI_")

jaane_bhi_do_yaaro = media.Movie(
    "Jaane Bhi Do Yaaro",
    "Let it Be, Friends",
    "2 photographers take on a hilarious assignment",
    "https://upload.wikimedia.org/wikipedia/en/6/6e/Jaane_Bhi_Do_Yaaro_1983_film_poster.jpg",
    "https://youtu.be/spkmLziFFg4",
    "http://www.imdb.com/title/tt0085743",
    "8.6",
    "Bombay, India",
    "1983",
    "https://youtu.be/jsvLiTZANPk")

choti_si_baat = media.Movie(
    "Chhoti Si Baat",
    "One Small Thing",
    "A painfully shy man learns how to fall in love",
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Chhoti_Si_Baat.jpg",
    "https://www.youtube.com/watch?v=ah4KCyj-NT4",
    "http://www.imdb.com/title/tt0072777/?ref_=fn_al_tt_1",
    "8.3",
    "Bombay, India",
    "1979",
    "http://www.saavn.com/s/album/hindi/Baton-Baton-Mein-Choti-Si-Baat-Rajnigandha-Angoor-2005/hWaB-ZxdnNQ_")

oye_lucky = media.Movie(
    "Oye Lucky! Lucky Oye!",
    "Hey Lucky!",
    "A kind-hearted thief cannot stop stealing",
    "https://upload.wikimedia.org/wikipedia/en/d/d0/Oyelucky.jpg",
    "https://youtu.be/3paPF30NJhg",
    "http://www.imdb.com/title/tt1292703/",
    "7.9",
    "Delhi, India",
    "2008",
    "http://www.saavn.com/s/album/hindi/Oye-Lucky-Lucky-Oye-2008/G1Ft8EapZqw_")

anand = media.Movie(
    "Anand",
    "Happiness",
    "A dying man lives his life to the fullest",
    "https://upload.wikimedia.org/wikipedia/en/c/c9/Anand_film.jpg",
    "https://youtu.be/tfGX2AEaMUU",
    "http://www.imdb.com/title/tt0066763/?ref_=fn_al_tt_1",
    "8.9",
    "Bombay, India",
    "1971",
    "http://www.saavn.com/s/album/hindi/Anand-1971/p1LAI,l4KAc_")

queen = media.Movie(
    "Queen",
    "Queen",
    "A woman goes on her honeymoon alone",
    "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",
    "https://youtu.be/KGC6vl3lzf0",
    "http://www.imdb.com/title/tt3322420/?ref_=fn_al_tt_1",
    "8.5",
    "Delhi, Paris, Amsterdam",
    "2014",
    "http://www.saavn.com/s/album/hindi/Queen-2014/z-faq6NoX0w_")

# The information from the movie variables are rendered in fresh_tomatoes.py to HTML
movies = [andaz_apna_apna, jaane_bhi_do_yaaro, choti_si_baat, oye_lucky, anand, queen]
fresh_tomatoes.open_movies_page(movies)
