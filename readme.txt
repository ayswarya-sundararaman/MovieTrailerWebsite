PROJECT NAME: Movie Trailer Website(Moviezz)

DESCRIPTION:
	-> The movie trailer website project is solely used to implement the Object Oriented Concepts in Python
	-> Using Classes we create different instances/objects of different Genres of movies.
	-> The Python input is dynamically given to create a movie block in the website which will display the trailer of the movie  
	   on click.
	-> Here each movie is an object of the class Movie() which will initialize its instance variables.

RUNNING DOCUMENTATION LOCALLY
   
   step1: If necessary ,Install Python version 3.7(64 bit) or Python 2.7 can also be used. 
   step2: Run the file [entertainment_center.py] .The successful execution will open the movie trailer website in your browser.
   step3: After the website opens in your browser click on the genres(Animation,horror etc) of movie trailer you want to watch. 
   step4: You will see all the genres of movie objects that was created in the entertainment_center.py displayed inside respective webpages (eg. fresh_tomatoes_action.html,fresh_tomatoes_thriller.html etc)

WHAT'S INCLUDED
within the download you'll find the following files:
						-media.py
						-entertainment_center.py
						-fresh_tomatoes.py
						-README.txt  
						-webpages folder(contains all the website related files.)
				
DOCUMENTATION

This MovieTrailerWebsite documentation, included in this repo in the root directory, is built with Python version 3.7.2(64 bit)  
The docs may also be run locally.						

BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an issue,
github.com/AyswaryaS95

CREATOR
-Ayswarya 
-github.com/AyswaryaS95

IMPORTANT FILES:
    
    ->fresh_tomatoes.py -- Python file contains the following contains following main functions:
    							imports:webbrowser,os,re
    							-> create_movie_tiles_content(): inputs:movies,genres
    							                 	. creates a HTML content for the page
    							                 	. Extracts the youtube ID from the url
    							                 	. Append the tile for the movie with its content filled 

    							->open_movies_page():inputs:movies
    												. creates and overwrites the output file(HTML page).
    												. there are 6 different output files for different genres of movies
    												 eg.(horror,thriller,war etc)
    												.based on the genres of the movie the movies are appeneded in their
    												 respective  output files. 

    							->write_output_page():inputs:output_file,movies,value
    												. Writes HTML script to the output file based on the genres.
    												. Replace the placeholder for the movie tiles with the actual dynamically  
    												  genrated content

    ->media.py -- Python file contains the class definition :
    							imports : webbrowser
                                ->__init__(): inputs: movie title, movie storyline, poster image, trailer youtube, movie genr
                                                    . initializes the instance variables for the object created.
                                ->show_trailer(): Opens the youtube trailer for the movie in a new window.

    ->entertainment_center.py -- All the movie objects are created here which passes their arguments to the __init__ function.
    							 imports:fresh_tomatoes,media	    

    
WEBPAGES FOLDER :  path:MovieTrailerWebsite/webpages

    contents: 

    ->index.html --> Contains HTML codes written to build the homepage of the movie trailer website(Moviezz):
    							. contains linked CSS,JAVASCRIPTS and JQuery

    ->fresh_tomatoes_action.html --> Contains HTML codes written to build the page to find all the dynamically created action 
                                     movies. Note:its one of the output file created when fresh_tomatoes.py is executed.

    ->fresh_tomatoes_thriller.html --> Contains HTML codes written to build the page to find all the dynamically created thriller 
                                     movies. Note:its one of the output file created when fresh_tomatoes.py is executed.

    ->fresh_tomatoes_horror.html --> ->Contains HTML codes written to build the page to find all the dynamically created horror 
                                     movies. Note:its one of the output file created when fresh_tomatoes.py is executed.

    ->fresh_tomatoes_scifi.html --> ->Contains HTML codes written to build the page to find all the dynamically created science
                                     fiction movies. Note:its one of the output file created when fresh_tomatoes.py is executed.

    ->fresh_tomatoes_war.html --> ->Contains HTML codes written to build the page to find all the dynamically created war movies. 
    								Note:its one of the output file created when fresh_tomatoes.py  is executed.

	->fresh_tomatoes_animation.html --> ->Contains HTML codes written to build the page to find all the dynamically created 
	                                animation movies. Note:its one of the output file created when fresh_tomatoes.py  is executed.

	->Other files and Folders : contains all the assets neccesary to build a responsive website. Example.(CSS,JS,images) 


    								








                                                                             
               
