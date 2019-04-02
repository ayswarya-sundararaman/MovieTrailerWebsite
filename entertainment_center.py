
# coding: utf-8

# In[3]:

import media
import fresh_tomatoes

#create instances of different genres of movie.
toy_story=media.Movie("Toy Story 3",
              '''The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up
                to Woody to convince the other toys that they weren't abandoned and to return home. ''',
              "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0%2C0%2C300%2C450&optimize=true",
              "https://www.youtube.com/watch?v=xItITCJfM3E",
               "animation")

hotel_transylvania=media.Movie("Hotel Transylvania 2",'''Dracula and his friends try to bring out the monster in his half human,
                               half vampire grandson in order to keep Mavis from leaving the hotel.''',
  "https://is1-ssl.mzstatic.com/image/thumb/Video49/v4/cb/4d/3b/cb4d3b67-2c06-8e98-759f-3938332c2cf4/pr_source.jpg/268x0w.jpg",
  "https://www.youtube.com/watch?v=T3nqmGgnJe8","animation")

up=media.Movie("UP",'''Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, 
        inadvertently taking a young stowaway. ''',
        "http://www.movienewsletters.net/photos/059776R1.jpg",
        "https://www.youtube.com/watch?v=pkqzFUhGPJg",
        "animation")

it=media.Movie("IT",
        ''' A group of bullied kids band together to destroy a shape-shifting monster, 
         which disguises itself as a clown and preys on the children of Derry, their small Maine town''',
        '''http://urbanmediatoday.com/wp-content/uploads/2017/09/Movie-It.jpg''',
         "https://www.youtube.com/watch?v=hAUTdjf9rko","horror")

a_quiet_place=media.Movie("A Quiet Place",
              '''A family struggles for survival in a world where most humans have been 
              killed by blind but noise-sensitive creatures''',
             "https://upload.wikimedia.org/wikipedia/en/a/a0/A_Quiet_Place_film_poster.png",
              "https://www.youtube.com/watch?v=WR7cc5t7tv8","horror")

mama=media.Movie("Mama",
           '''Two girls reside in a jungle after their parents get murdered. When they are rescued years 
           later and begin a new life, they find that a shadowy feminine figure has accompanied them to their house ''',
           "https://a.ltrbxd.com/resized/sm/upload/ph/ik/j6/b9/kFMrQCo0Ue9GkeptoiB65FwF0lg-0-230-0-345-crop.jpg?k=45f3d69370",
           "https://www.youtube.com/watch?v=7Am7i7uM9r0","horror")

hacksaw_ridge=media.Movie("Hacksaw Ridge",
                    ''''World War II American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, 
                    refuses to kill people, and becomes the first man in American history to receive the Medal of 
                    Honor without firing a shot.
                    ''',
                   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Hacksaw_Ridge_poster.png/220px-Hacksaw_Ridge_poster.png",
                   "https://www.youtube.com/watch?v=s2-1hz1juBI","war")

american_sniper=media.Movie("American Sniper",
                      '''Even after returning home from the war in Iraq, Chris Kyle, 
                      a SEAL sniper, cannot let go of the horrors he has experienced. 
                      This begins to affect his marriage and his life.
                      Release    ''',
                      "http://www.gstatic.com/tv/thumb/v22vodart/10991238/p10991238_v_v8_aa.jpg",
                      "https://www.youtube.com/watch?v=99k3u9ay1gs",
                      "war")


threehundred=media.Movie("300",
               '''In the ancient battle of Thermopylae, King Leonidas and 300 Spartans fight against Xerxes 
               and his massive Persian army. They face insurmountable odds when they are betrayed by a Spartan reject.''',
               "https://nerdbasego.files.wordpress.com/2014/03/300-rise-of-an-empire-artemisia1.jpg",
               "https://www.youtube.com/watch?v=UrIbxk7idYA" ,
               "war")

split=media.Movie("Split",
            ''' Kevin, who is suffering from dissociative identity disorder and has 23 alter egos, 
            kidnaps three teenagers. They must figure out his friendly personas before he unleashes his 24th personality.''',
            "https://m.media-amazon.com/images/M/MV5BZTJiNGM2NjItNDRiYy00ZjY0LTgwNTItZDBmZGRlODQ4YThkL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_UX182_CR0,0,182,268_AL_.jpg",
             "https://www.youtube.com/watch?v=84TouqfIsiI","thriller")

The_mule=media.Movie("The Mule",
               '''A flawed yet enjoyable late-period Eastwood entry, The Mule stubbornly retains
               its footing despite a few missteps on its occasionally unpredictable path''',
               "https://assets.www.warnerbros.com/sites/default/files/movies/media/browser/The_Mule_Keyart.JPEG",
               "https://www.youtube.com/watch?v=N_QksSzK7sI","thriller") 

shutter_island=media.Movie("Shutter Island",
                    ''' In 1954, a U.S. Marshal investigates the disappearance of a murderer,
                    who escaped from a hospital for the criminally insane.''',
                    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                    "https://www.youtube.com/watch?v=5iaYLCiq5RM","thriller")

Captain_marvel=media.Movie("Captain Marvel",
                     '''Carol Danvers becomes one of the universe's most powerful heroes when Earth 
                     is caught in the middle of a galactic war between two alien races. ''',
                     "https://pbs.twimg.com/media/DmlfAGpVAAACEq6.jpg",
                    "https://www.youtube.com/watch?v=Z1BCujX3pw8","action")

avengers_infintiy_war=media.Movie("Avengers:Infinity War",
                     '''The Avengers and their allies must be willing to sacrifice all in an attempt to defeat
                     the powerful Thanos before his blitz of devastation and ruin puts an end to the universe ''',
                    "https://assets.nflxext.com/us/boxshots/hd1080/80219127.jpg",
                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8","action")

logan=media.Movie("Logan",
                     '''In a future where mutants are nearly extinct, an elderly and weary Logan leads a quiet life. But when Laura, a mutant child pursued by scientists,
                        comes to him for help, he must get her to safety. ''',
                    "https://i.ebayimg.com/images/g/fq8AAOSwfpVZF2Qv/s-l300.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo","action")

interstellar=media.Movie("Interstellar",
                   '''A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival. ''', 
                   "http://img.over-blog-kiwi.com/1/36/64/60/20150323/ob_23a5c4_illuminatiwatcherdotcom-interstellar-m.jpg",
                   "https://www.youtube.com/watch?v=0vxOhd4qlnA","scifi")

inception=media.Movie("Inception",
                   '''A thief who steals corporate secrets through the use of dream-sharing technology 
                   is given the inverse task of planting an idea into the mind of a CEO. ''', 
                   "https://images-na.ssl-images-amazon.com/images/I/51ShRC1YMrL.jpg",
                   "https://www.youtube.com/watch?v=d3A3-zSOBT4","scifi")

the_martian=media.Movie("The Martian",
                   '''An astronaut becomes stranded on Mars after his team assume him dead, and must 
                   rely on his ingenuity to find a way to signal to Earth that he is alive. ''', 
                   "https://i.pinimg.com/originals/3c/24/82/3c24828696df40f5feabaeaf0acade60.jpg",
                   "https://www.youtube.com/watch?v=ej3ioOneTy8","scifi")

#define a dictionary  called movies which stores the movies as keys with its genre as its value  
movies={toy_story:"animation",hotel_transylvania:"animation",up:"animation",it:"horror",
        a_quiet_place:"horror",mama:"horror",hacksaw_ridge:"war",american_sniper:"war",
        threehundred:"war",shutter_island:"thriller",The_mule:"thriller",split:"thriller",
        Captain_marvel:"action",avengers_infintiy_war:"action",logan:"action",
        interstellar:"scifi",the_martian:"scifi",inception:"scifi"}

fresh_tomatoes.open_movies_page(movies)


# In[ ]:



