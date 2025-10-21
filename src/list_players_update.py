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

#Golden state
update_player_csv('https://www.basketball-reference.com/players/c/curryst01/gamelog/2025','curry')
update_player_csv('https://www.basketball-reference.com/players/b/butleji01/gamelog/2025','butler')
update_player_csv('https://www.basketball-reference.com/players/g/greendr01/gamelog/2025','draymond')
update_player_csv('https://www.basketball-reference.com/players/k/kuminjo01/gamelog/2025','jonathan')
update_player_csv('https://www.basketball-reference.com/players/p/podzibr01/gamelog/2025','brandin')
update_player_csv('https://www.basketball-reference.com/players/h/hieldbu01/gamelog/2025','buddy')

#okc
update_player_csv('https://www.basketball-reference.com/players/g/gilgesh01/gamelog/2025','shai')
update_player_csv('https://www.basketball-reference.com/players/d/dortlu01/gamelog/2025','luguentz')
update_player_csv('https://www.basketball-reference.com/players/w/wiggiaa01/gamelog/2025','aaron')
update_player_csv('https://www.basketball-reference.com/players/h/holmgch01/gamelog/2025','chet')
update_player_csv('https://www.basketball-reference.com/players/w/wallaca01/gamelog/2025','cason')
update_player_csv('https://www.basketball-reference.com/players/c/carusal01/gamelog/2025','alex')
update_player_csv('https://www.basketball-reference.com/players/h/harteis01/gamelog/2025','isaiah')

