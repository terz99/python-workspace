import media
import fresh_tomatoes

shawshank_redemption = media.Movie('Shawshank Redemption', 'A inocent prisoner escapes prison', 'http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm', 'https://www.youtube.com/watch?v=NmzuHjWmXOc')
batman_begins = media.Movie('Batman Begins', 'A super hero story', 'http://www.gstatic.com/tv/thumb/movieposters/35903/p35903_p_v8_ae.jpg', 'https://www.youtube.com/watch?v=neY2xVmOfUM')
batman_the_dark_knight = media.Movie('Batman: The Dark Knight', 'A super hero story #2', 'http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg', 'https://www.youtube.com/watch?v=EXeTwQWrcwY')
batman_the_dark_knight_rises = media.Movie('Batman: The Dark Knight Rises', 'A super hero story #3', 'http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z', 'https://www.youtube.com/watch?v=GokKUqLcvD8')
pirates_of_the_caribean = media.Movie('Pirates of the Caribean', 'A pirate story', 'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-a15t4g_367ea5c5.jpeg?region=0,0,300,450', 'https://www.youtube.com/watch?v=KpFMVcZ4o7U')
wonder_woman = media.Movie('Wonder Woman', 'A female super hero story', 'http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H', 'https://www.youtube.com/watch?v=VSB4wGIdDwo')

movies = [shawshank_redemption, batman_begins, batman_the_dark_knight, batman_the_dark_knight_rises, pirates_of_the_caribean, wonder_woman]
fresh_tomatoes.open_movies_page(movies)