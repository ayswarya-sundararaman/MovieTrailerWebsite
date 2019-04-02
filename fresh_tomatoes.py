import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Go Movies</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <link href="assets/lib/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
    <link id="color-scheme" href="assets/css/colors/default.css" rel="stylesheet">
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script src="assets/lib/jquery/dist/jquery.js"></script>
    <script src="assets/lib/bootstrap/dist/js/bootstrap.min.js"></script>
    <script src="assets/js/main.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    
    <div class="container">
    <div class="main showcase-page">
        <section class="module-medium" id="demos">
          <div class="container">
            <div class="row multi-columns-row">
              {movie_tiles}
          </div>
          </div>
        </section>
      </div> 
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-4 col-sm-6 col-xs-12 movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <a class="content-box">
                  <div class="content-box-image"><img src="{poster_image_url}" alt="Landing" width="700" height="940"></div>
                  <h3 class="content-box-title font-serif">{movie_title}</h3>{story_line}</a>
                  </div>
'''

def create_movie_tiles_content(movies,genre):
    # The HTML content for this section of the page
    content = ''
    #create movie content based on the genre
    for key,value in movies.items():
        if value == genre:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', key.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', key.trailer_youtube_url)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled 
            content += movie_tile_content.format(
                movie_title=key.title,
                poster_image_url=key.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
            	story_line=key.storyline)
        else:
            continue
    return content

def write_output_page(output_file,movies,value):
    #Write to the output HTML page.
    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies,value))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    
def open_movies_page(movies):
    
    # Create or overwrite the output file
    default=open('webpages\\index.html') 
    # Create output files for each genre of movies.
    for key,value in movies.items():
        if value == "animation":
            output_file = open('webpages\\fresh_tomatoes_animation.html', 'w')
            write_output_page(output_file,movies,value)
            continue
        elif value == "horror":
            output_file = open('webpages\\fresh_tomatoes_horror.html','w')
            write_output_page(output_file,movies,value)
            continue
        elif value == "thriller":
            output_file = open('webpages\\fresh_tomatoes_thriller.html','w')
            write_output_page(output_file,movies,value)
            continue
        elif value == "action":
            output_file = open('webpages\\fresh_tomatoes_action.html','w')
            write_output_page(output_file,movies,value)
            continue
        elif value == "scifi":
            output_file = open('webpages\\fresh_tomatoes_scifi.html','w')
            write_output_page(output_file,movies,value)
            continue
        elif value == "war":
            output_file = open('webpages\\fresh_tomatoes_war.html','w')
            write_output_page(output_file,movies,value)
            continue    
            
            
    # open the output file in the browser
    url = os.path.abspath(default.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
