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

def over_under_count(sign, games, player1, player2, stat1, stat2):
    player1_average = round(player1[stat1].mean() * 2) / 2 # all games average not specifc to matched games rounded to nearest .5
    player2_average = round(player2[stat2].mean() * 2) / 2
    player1_array = games[stat1 + '_1'] # stats for the for the matching games
    player2_array = games[stat2 + '_2']
    both_above = 0
    both_below = 0
    if (sign > 0):
        for game in range(len(games)):
            if (player1_array[game] >= player1_average) and (player2_array[game] >= player2_average):
                both_above += 1
            elif (player1_array[game] <= player1_average) and (player2_array[game] <= player2_average):
                both_below += 1
    else:
        for game in range(len(games)):
            if (player1_array[game] >= player1_average) and (player2_array[game] <= player2_average):
                both_above += 1
            elif (player1_array[game] <= player1_average) and (player2_array[game] >= player2_average):
                both_below += 1
    return both_above, both_below, len(games), player1_average, player2_average
#what we want both above both below and both of those combine and for each of those there percentage: player names probably and len games

# gives graph of two chosen players and two chosen stats gives both non-standized graph
def graph_two(player1, player2, stat1, stat2):
    # Get matched games
    games = matching_games(player1, player2, stat1, stat2)

    # Correlation coefficient
    r_coe = np.corrcoef(games.loc[:, stat1 + '_1'], games.loc[:, stat2 + '_2'])[0, 1]

    # Over/under counts
    both_above, both_below, total_games, player1_average, player2_average = over_under_count(r_coe, games, player1, player2, stat1, stat2)

    # Percentages
    both_above_percent = round(both_above / total_games * 100, 1)
    both_below_percent = round(both_below / total_games * 100, 1)
    count_correlation = both_above + both_below
    count_correlation_percent = round(count_correlation / total_games * 100, 1)

    # Non-standardized scatter plot
    fig = Figure(figsize=(6, 5.5))
    ax = fig.add_subplot(111)
    ax.scatter(games[f'{stat1}_1'], games[f'{stat2}_2'], color='blue')
    ax.set_xlabel(f"{games['name_1'][0]} {stat1}")
    ax.set_ylabel(f"{games['name_2'][0]} {stat2}")

    # Add yellow average lines
    ax.axvline(player1_average, color='red', linestyle='--', alpha=0.3, label=f"{games['name_1'][0]} avg")
    ax.axhline(player2_average, color='red', linestyle='--', alpha=0.3, label=f"{games['name_2'][0]} avg")
    # Dynamic over/under labels
    if r_coe >= 0:
        over_label = f"Both above: {both_above}/{total_games} ({both_above_percent}%)"
        under_label = f"Both below: {both_below}/{total_games} ({both_below_percent}%)"
    else:
        over_label = f"{games['name_1'][0]} over: {both_above}/{total_games} ({both_above_percent}%)"
        under_label = f"{games['name_2'][0]} over: {both_below}/{total_games} ({both_below_percent}%)"

    # Clean, multi-line title
    ax.set_title(
        f"{games['name_1'][0]} {stat1} ({player1_average}) vs {games['name_2'][0]} {stat2} ({player2_average})\n"
        f"r_coefficient = {r_coe:.4f} | Count correlation = {count_correlation}/{total_games} ({count_correlation_percent}%)\n"
        f"{over_label} | {under_label}"
    )
    
    return fig

"""
f"{games['name_1'][0]} {stat1} vs {games['name_2'][0]} {stat2}\n"
    f"r_coefficient = {r_coe:.4f} | "
    f"Both over/both under = {count_correlation}/{same_number_games} "
    f"({count_correlation_percent:.1f}%)"

"""