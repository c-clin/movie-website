import webbrowser
# allows Python to gain access to the code in the webbrowser module

class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_director, movie_box_office):
        '''
        Behavior: initializes the instances of the class Movie
        Input: different arguments within the instances
        Output: the desired information to the corresponding arguments
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.box_office = movie_box_office

    def show_trailer(self):
        '''
        Behavior: Automatically opens the web browser of the url when selected.
        Input: the desired instance.
        Output: the corresponding video the the instance
        ''' 
        webbrowser.open(self.trailer_youtube_url)





