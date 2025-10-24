import pandas as pd
import numpy as np
from matplotlib.figure import Figure


# matching dates of games for two players for two stats
def matching_games(player1, player2, stat1, stat2):
    xin = player1[['Date', stat1, 'name']].rename(
        columns={stat1: f"{stat1}_1", "name": "name_1"}
    )
    yin = player2[['Date', stat2, 'name']].rename(
        columns={stat2: f"{stat2}_2", "name": "name_2"}
    )
    return pd.merge(xin, yin, on="Date")


# gives graph of two chosen players and two chosen stats gives both non-standized graph
def graph_two(player1, player2, stat1, stat2):

    # making a table where game dates are mached with wanted qualities and standardizing it
    games = matching_games(player1, player2, stat1, stat2)

    # display correlation coefficient
    r_coe = np.corrcoef(games.loc[:,stat1 + '_1'], games.loc[:,stat2 + '_2'])[0, 1] #[0, 1] is just selecting the right number out of a matrix

    # display the amount of games where both players went over there average or both players went below the average
    #if statment t osee of r_coe is positive so then we wont both over under both over otherwise its alterantive

    average_player1 = player1[stat1].mean()
    average_player2 = player2[stat2].mean()
    player1_array = games[stat1 + '_1']
    player2_array = games[stat2 + '_2']
    print(games)
    print(len(games))
    both_above = 0
    both_below = 0
    print(player1_array)
    print(player2_array)
    for game in range(len(games)):
        if (player1_array[game] >= average_player1) and (player2_array[game] >= average_player2):
            both_above += 1
        elif (player1_array[game] <= average_player1) and (player2_array[game] <= average_player2):
            both_below += 1
    print(average_player1)
    print(average_player2)
    print(both_below)
    print(both_above)
    print(len(games))
    # non-standardized graph
    fig = Figure(figsize=(6, 5.5))
    ax = fig.add_subplot(111)

    # scatter plot 
    ax.scatter(games[f'{stat1}_1'], games[f'{stat2}_2'], color='blue')
    ax.set_xlabel(f"{games['name_1'][0]} {stat1}")                                 # games['name_1'][0] gets name from name column
    ax.set_ylabel(f"{games['name_2'][0]} {stat2}")
    ax.set_title('Compare same game stats between players\n' +
                 'correlation coefficient = '+ str(round(r_coe,4)) + '\n'+
                 'testing')

    # could add standardized table
    return fig