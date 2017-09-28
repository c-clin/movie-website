import media
# this command tells Python that we will be using the contents from the media file
import fresh_tomatoes
# this command tells Python that we will be using contents from the fresh_tomatoes file



interstellar = media.Movie("Interstellar",
                           "An attempt to save mankind by transporting a team of researchers through the wormhole and across the galaxy to find an inhabitable planet.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                           "Christopher Nolan",
                           "675.1 Million")


inception = media.Movie("Inception",
                        "A thief with the rare ability to enter people's dreams and steal their secrets is offered an impossible task at which if succeeded, would be a perfect crime.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "Christopher Nolan",
                        "825.5 Million")
                        

the_big_sick = media.Movie("The Big Sick",
                           "A Pakistani comic struggle to stay in a relationship with an America girl against his traidional Muslim believes and a sudden illness from his girlfriend.",
                           "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg",
                           "https://www.youtube.com/watch?v=jcD0Daqc3Yw",
                           "Michael Showalter",
                           "30.6 Million")

                        
zootopia = media.Movie("Zootopia",
                       "Story about a rabbit in the police force struggling to pursue her dream as the first bunny cop.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                       "Byron Howard, Rich Moore",
                       "1.024 Billion")



pitch_perfect = media.Movie("Pitch Perfect",
                            "The Barden Bellas are an all-girls a capella group trying to regain their success after a disasterous fail at the finals.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b9/Pitch_Perfect_movie_poster.jpg",
                            "https://www.youtube.com/watch?v=H3GfsNuzLmI",
                            "Jason Moore",
                            "115.4 Million")


wolf_of_wallstreet = media.Movie("The Wolf of Wallstreet",
                                 "A penny stockbroker led the defrauding of a massive securities scam that involved a widespread Wall Street corruption.",
                                 "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                 "https://www.youtube.com/watch?v=iszwuX1AK6A",
                                 "Martin Scorsese",
                                 "392 Million")

movies = [interstellar, inception, the_big_sick, zootopia, pitch_perfect, wolf_of_wallstreet]

fresh_tomatoes.open_movies_page(movies)

