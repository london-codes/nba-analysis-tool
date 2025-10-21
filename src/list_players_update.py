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


#Golden state
#update_player_csv('https://www.basketball-reference.com/players/h/horfoal01/gamelog/2025','al') no 2025 was on bos
update_player_csv('https://www.basketball-reference.com/players/c/curryst01/gamelog/2025','curry')
update_player_csv('https://www.basketball-reference.com/players/b/butleji01/gamelog/2025','butler')
update_player_csv('https://www.basketball-reference.com/players/g/greendr01/gamelog/2025','draymond')
update_player_csv('https://www.basketball-reference.com/players/k/kuminjo01/gamelog/2025','jonathan')
update_player_csv('https://www.basketball-reference.com/players/p/podzibr01/gamelog/2025','brandin')
update_player_csv('https://www.basketball-reference.com/players/h/hieldbu01/gamelog/2025','buddy')
"""
#min
update_player_csv('https://www.basketball-reference.com/players/r/reidna01/gamelog/2025','naz')
update_player_csv('https://www.basketball-reference.com/players/m/mcdanja02/gamelog/2025','jaden')
update_player_csv('https://www.basketball-reference.com/players/g/goberru01/gamelog/2025','rudy')
update_player_csv('https://www.basketball-reference.com/players/c/conlemi01/gamelog/2025','mike')
update_player_csv('https://www.basketball-reference.com/players/e/edwaran01/gamelog/2025','anthony')
update_player_csv('https://www.basketball-reference.com/players/r/randlju01/gamelog/2025','julius')
update_player_csv('https://www.basketball-reference.com/players/d/divindo01/gamelog/2025','donte')

#okc
update_player_csv('https://www.basketball-reference.com/players/g/gilgesh01/gamelog/2025','shai')
update_player_csv('https://www.basketball-reference.com/players/d/dortlu01/gamelog/2025','luguentz')
update_player_csv('https://www.basketball-reference.com/players/w/wiggiaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/h/holmgch01/gamelog/2025','chet')
update_player_csv('https://www.basketball-reference.com/players/w/wallaca01/gamelog/2025','cason')
update_player_csv('https://www.basketball-reference.com/players/c/carusal01/gamelog/2025','alex')
update_player_csv('https://www.basketball-reference.com/players/h/harteis01/gamelog/2025','isaiah')

#tor
update_player_csv('https://www.basketball-reference.com/players/p/poeltja01/gamelog/2025','jakob')
update_player_csv('https://www.basketball-reference.com/players/d/dickgr01/gamelog/2025','gradey')
update_player_csv('https://www.basketball-reference.com/players/b/barrerj01/gamelog/2025','RJ')
update_player_csv('https://www.basketball-reference.com/players/q/quickim01/gamelog/2025','immanuel') #injuired a lot 2025
update_player_csv('https://www.basketball-reference.com/players/b/barnesc01/gamelog/2025','scottie')
#update_player_csv('https://www.basketball-reference.com/players/i/ingrabr01/gamelog/2025','brandon') no 2025
