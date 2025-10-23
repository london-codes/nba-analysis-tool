from make_csv import update_player_csv


"""
Module for updating or creating player CSVs from Basketball Reference.

Usage:
    - Use update_player_csv(url, player_name) to update an existing csv file with the name inputed or add a 
    player not already in the data base.
    - To add a player you need to navigate to basketball reference and find the gamelog page with the specifc year
    you want.

Important Notes:
    - 5 second limit between each call of the update_player_csv function to avoid the rate limit and being blocked.

"""
    #   updates:
"""
#cleveland
update_player_csv('https://www.basketball-reference.com/players/a/allenja01/gamelog/2025','jarrett')
update_player_csv('https://www.basketball-reference.com/players/m/mobleev01/gamelog/2025','evan')
update_player_csv('https://www.basketball-reference.com/players/m/merrisa01/gamelog/2025','sam')
update_player_csv('https://www.basketball-reference.com/players/m/mitchdo01/gamelog/2025','donovan')
update_player_csv('https://www.basketball-reference.com/players/t/tysonja01/gamelog/2025','jaylon')
#update_player_csv('https://www.basketball-reference.com/players/h/huntede01/gamelog/2025','de andre') only played last half of season with cle
#update_player_csv('https://www.basketball-reference.com/players/b/balllo01/gamelog/2025','lonzo') no 2025 was on chi
"""
#den
update_player_csv('https://www.basketball-reference.com/players/m/murraja01/gamelog/2025','jamal')
update_player_csv('https://www.basketball-reference.com/players/g/gordoaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/b/braunch01/gamelog/2025','christian')
update_player_csv('https://www.basketball-reference.com/players/w/watsope01/gamelog/2025','peyton')
#update_player_csv('https://www.basketball-reference.com/players/b/brownbr01/gamelog/2025','bruce') # no 2025
update_player_csv('https://www.basketball-reference.com/players/j/jokicni01/gamelog/2025','nikola')
#update_player_csv('https://www.basketball-reference.com/players/j/johnsca02/gamelog/2025','cameron') # no 2025


"""
#Golden state
#update_player_csv('https://www.basketball-reference.com/players/h/horfoal01/gamelog/2025','al') no 2025 was on bos
update_player_csv('https://www.basketball-reference.com/players/c/curryst01/gamelog/2025','curry')
update_player_csv('https://www.basketball-reference.com/players/b/butleji01/gamelog/2025','butler')
update_player_csv('https://www.basketball-reference.com/players/g/greendr01/gamelog/2025','draymond')
update_player_csv('https://www.basketball-reference.com/players/k/kuminjo01/gamelog/2025','jonathan')
update_player_csv('https://www.basketball-reference.com/players/p/podzibr01/gamelog/2025','brandin')
update_player_csv('https://www.basketball-reference.com/players/h/hieldbu01/gamelog/2025','buddy')
""""""
#ind
update_player_csv('https://www.basketball-reference.com/players/n/nembhan01/gamelog/2025','andrew')
update_player_csv('https://www.basketball-reference.com/players/n/nesmiaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/m/mathube01/gamelog/2025','bennedict')
update_player_csv('https://www.basketball-reference.com/players/s/siakapa01/gamelog/2025','pascal')


#min
update_player_csv('https://www.basketball-reference.com/players/r/reidna01/gamelog/2025','naz')
update_player_csv('https://www.basketball-reference.com/players/m/mcdanja02/gamelog/2025','jaden')
update_player_csv('https://www.basketball-reference.com/players/g/goberru01/gamelog/2025','rudy')
update_player_csv('https://www.basketball-reference.com/players/c/conlemi01/gamelog/2025','mike')
update_player_csv('https://www.basketball-reference.com/players/e/edwaran01/gamelog/2025','anthony')
update_player_csv('https://www.basketball-reference.com/players/r/randlju01/gamelog/2025','julius')
update_player_csv('https://www.basketball-reference.com/players/d/divindo01/gamelog/2025','donte')

#nyk
update_player_csv('https://www.basketball-reference.com/players/r/robinmi01/gamelog/2025','mitchell') # did not play like entire 3/4 2025
update_player_csv('https://www.basketball-reference.com/players/m/mcbrimi01/gamelog/2025','miles')
update_player_csv('https://www.basketball-reference.com/players/h/hartjo01/gamelog/2025','josh')
update_player_csv('https://www.basketball-reference.com/players/a/anunoog01/gamelog/2025','OG')
update_player_csv('https://www.basketball-reference.com/players/b/brunsja01/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/b/bridgmi01/gamelog/2025','mikal')
update_player_csv('https://www.basketball-reference.com/players/t/townska01/gamelog/2025','karl-anthony')
#update_player_csv('https://www.basketball-reference.com/players/y/yabusgu01/gamelog/2025','guershon') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/c/clarkjo01/gamelog/2025','jordan') # no 2025

# orlando
update_player_csv('https://www.basketball-reference.com/players/c/cartewe01/gamelog/2025','wendell')
update_player_csv('https://www.basketball-reference.com/players/s/suggsja01/gamelog/2025','jalen')
update_player_csv('https://www.basketball-reference.com/players/w/wagnefr01/gamelog/2025','franz')
update_player_csv('https://www.basketball-reference.com/players/b/blackan01/gamelog/2025','anthony')
update_player_csv('https://www.basketball-reference.com/players/b/banchpa01/gamelog/2025','paolo') # played last half 2025
#update_player_csv('https://www.basketball-reference.com/players/b/banede01/gamelog/2025','desmond') # no 2025
#update_player_csv('https://www.basketball-reference.com/players/j/jonesty01/gamelog/2025','tyus') # no 2025
"""
"""
#okc
update_player_csv('https://www.basketball-reference.com/players/g/gilgesh01/gamelog/2025','shai')
update_player_csv('https://www.basketball-reference.com/players/d/dortlu01/gamelog/2025','luguentz')
update_player_csv('https://www.basketball-reference.com/players/w/wiggiaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/h/holmgch01/gamelog/2025','chet')
update_player_csv('https://www.basketball-reference.com/players/w/wallaca01/gamelog/2025','cason')
update_player_csv('https://www.basketball-reference.com/players/c/carusal01/gamelog/2025','alex')
update_player_csv('https://www.basketball-reference.com/players/h/harteis01/gamelog/2025','isaiah')

"""
#pho/phx
update_player_csv('https://www.basketball-reference.com/players/a/allengr01/gamelog/2025','grayson')
update_player_csv('https://www.basketball-reference.com/players/o/onealro01/gamelog/2025','royce')
update_player_csv('https://www.basketball-reference.com/players/b/bookede01/gamelog/2025','devin')
update_player_csv('https://www.basketball-reference.com/players/d/dunnry01/gamelog/2025','ryan')
update_player_csv('https://www.basketball-reference.com/players/i/ighodos01/gamelog/2025','oso')
update_player_csv('https://www.basketball-reference.com/players/g/gilleco01/gamelog/2025','collin') # played last half 2025
#update_player_csv('https://www.basketball-reference.com/players/b/brookdi01/gamelog/2025','dillon') # no 2025


"""
#tor
update_player_csv('https://www.basketball-reference.com/players/p/poeltja01/gamelog/2025','jakob')
update_player_csv('https://www.basketball-reference.com/players/d/dickgr01/gamelog/2025','gradey')
update_player_csv('https://www.basketball-reference.com/players/b/barrerj01/gamelog/2025','RJ')
update_player_csv('https://www.basketball-reference.com/players/q/quickim01/gamelog/2025','immanuel') #injuired a lot 2025
update_player_csv('https://www.basketball-reference.com/players/b/barnesc01/gamelog/2025','scottie')
#update_player_csv('https://www.basketball-reference.com/players/i/ingrabr01/gamelog/2025','brandon') no 2025
"""






