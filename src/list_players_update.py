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

#LVA
update_player_csv('https://www.basketball-reference.com/wnba/players/w/wilsoa01w/gamelog/2025/', 'aja')
update_player_csv('https://www.basketball-reference.com/wnba/players/g/graych01w/gamelog/2025/', 'chelsea')
update_player_csv('https://www.basketball-reference.com/wnba/players/l/loydje01w/gamelog/2025/', 'jewell')
update_player_csv('https://www.basketball-reference.com/wnba/players/s/smithna01w/gamelog/2025/', 'nalyssa')
update_player_csv('https://www.basketball-reference.com/wnba/players/y/youngja01w/gamelog/2025/', 'jackie')

#PHO
update_player_csv('https://www.basketball-reference.com/wnba/players/s/sabalsa01w/gamelog/2025/','satou')
update_player_csv('https://www.basketball-reference.com/wnba/players/w/whitcsa01w/gamelog/2025/','sami')
update_player_csv('https://www.basketball-reference.com/wnba/players/a/akoamo01w/gamelog/2025/','monique')
update_player_csv('https://www.basketball-reference.com/wnba/players/c/coppeka01w/gamelog/2025/','kahleah')
update_player_csv('https://www.basketball-reference.com/wnba/players/b/bonnede01w/gamelog/2025/','dewanna')
update_player_csv('https://www.basketball-reference.com/wnba/players/t/thomaal01w/gamelog/2025/','alyssa')

#MIN
update_player_csv('https://www.basketball-reference.com/wnba/players/h/hiedena01w/gamelog/2025/','natisha')
update_player_csv('https://www.basketball-reference.com/wnba/players/c/collina01w/gamelog/2025/','napheesa')
update_player_csv('https://www.basketball-reference.com/wnba/players/s/smithal01w/gamelog/2025/','alanna')
update_player_csv('https://www.basketball-reference.com/wnba/players/c/carlebr01w/gamelog/2025/','bridget')
update_player_csv('https://www.basketball-reference.com/wnba/players/m/mcbrika01w/gamelog/2025/','kayla')

#IND
update_player_csv('https://www.basketball-reference.com/wnba/players/s/simsod01w/gamelog/2025/','odyssey')
update_player_csv('https://www.basketball-reference.com/wnba/players/b/bostoal01w/gamelog/2025/','aliyah')
update_player_csv('https://www.basketball-reference.com/wnba/players/m/mitchke01w/gamelog/2025/','kelsey')
update_player_csv('https://www.basketball-reference.com/wnba/players/h/hullle01w/gamelog/2025/','lexie')
update_player_csv('https://www.basketball-reference.com/wnba/players/h/howarna01w/gamelog/2025/','natasha')
