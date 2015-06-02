import fresh_tomatoes

# Definition of our Movie class
class Movie:
    title= '';
    poster_image_url = '';
    trailer_youtube_url = '';
    imdb = '';

    def __init__ (self, title, art, youtube, imdb):
        self.title = title;
        self.poster_image_url = art;
        self.trailer_youtube_url = youtube;
        self.imdb = imdb;

# This is the array of movies
movies = [];

movies.append(Movie('Clueless',
    'http://upload.wikimedia.org/wikipedia/en/2/21/Clueless.jpg',
    'https://www.youtube.com/watch?v=RS0KyTZ3Ie4',
    'http://www.imdb.com/title/tt0112697/'));

movies.append(Movie('Uncle Buck',
    'http://upload.wikimedia.org/wikipedia/en/8/8c/Uncle_buck.jpg',
    'https://www.youtube.com/watch?v=zXEzA1egFL4',
    'http://www.imdb.com/title/tt0098554/?ref_=nv_sr_1'));

# Call the code to open a browser and display our favorite movies
fresh_tomatoes.open_movies_page(movies);
