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

update_player_csv('https://www.basketball-reference.com/players/c/curryst01/gamelog/2025','curry')
