
# coding: utf-8

# In[ ]:

import webbrowser

#Create a class movie which contains attributes of movies like its title,storyline etc
#Contains functions show_trailer() which shows trailer based on its movie objects.
#Contains init function which initializes the instance variables.
class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,movie_genre):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.moive_genre=movie_genre
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

