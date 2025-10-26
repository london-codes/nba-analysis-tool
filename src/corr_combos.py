import pandas as pd
import numpy as np
from itertools import combinations
from itertools import product
from operator import itemgetter
import tkinter as tk
import os


# takes a pair of players and gives all possible permutations of two stats. 
# example array_stats=[PTS,AST] then 4 correlations will be calculated for PTS PTS, AST PTS, PTS AST, AST AST
def player_pair_all_permutations_rcoe(player1,player2,array_stats):
    #stat number index for the stat within the stats variable in the for loop
    stat1 = 0
    stat2 = 1
    corres = []

    # combines necessary data
    player1_needed_stats = player1[['Date','name'] + array_stats]
    player2_needed_stats = player2[['Date','name'] + array_stats]
    df = pd.merge(player1_needed_stats,player2_needed_stats, on='Date',suffixes=("_p1", "_p2"))

    # for each permutaion of array_stats makes a array holding r_coe, pair of stats used, and the two players names
    for stats in list(product(array_stats, repeat=2)):
        corr = [np.corrcoef(df[stats[stat1] + '_p1'], df[stats[stat2] + '_p2'])[0, 1],
              stats, df['name_p1'][0],df['name_p2'][0]] # df['name_p1'][0] grabs player name from name column
        corres.append(corr)
    return corres

# gives all combinations for 2 players in a team and all possible permutations for selected stats
def team_combinations(team,stats,selected_min_number_of_games):
    correlations=[]

    for player1, player2 in combinations(team, 2):
        #defintley not the most effeicenitent way but of the players don't have specific number of games played together doesn't calculate correlation
        test=pd.merge(player1,player2, on='Date')
        if len(test) < selected_min_number_of_games:
            continue
        r = player_pair_all_permutations_rcoe(player1, player2, stats)
        correlations.append(r)
    return correlations

# displays team_combinations in 2 scrollable boxes holding highest absolute value correlations, can be clicekd to graph
def all_correlation_combinations_interactive(team, selected_stats, pos_box, neg_box,selected_min_number_of_games):

    team_combo = team_combinations(team, selected_stats,selected_min_number_of_games)
    r_coe = 0

    #reset the widget so old text goes new text can now be inserted
    pos_box.delete(0, tk.END)
    neg_box.delete(0, tk.END)

    flat = [[float(item[r_coe])] + item[1:] for sublist in team_combo for item in sublist]
    sorted_flat = sorted(flat, key=itemgetter(r_coe))

    for row in sorted_flat[-60:][::-1]:
        formatted_row  = [f"{row[0]:.4f}"] + row[1:]
        pos_box.insert(tk.END, str(formatted_row ) + "\n")

    for row in sorted_flat[:60]:
        formatted_row  = [f"{row[0]:.4f}"] + row[1:]
        neg_box.insert(tk.END, str(formatted_row ) + "\n")

#UNUSED
# displays team_combinations in 2 scrollable boxes holding highest absolute value correlations
def all_correlation_combinations(team, selected_stats, pos_widget, neg_widget):

    team_combo = team_combinations(team, selected_stats)
    
    r_coe = 0
    # flatten the list and clean floats
    flat = [[float(item[r_coe])] + item[1:] for sublist in team_combo for item in sublist]
    sorted_flat = sorted(flat, key=itemgetter(r_coe))

    # clear old text
    pos_widget.delete("1.0", tk.END)
    neg_widget.delete("1.0", tk.END)

    # positive correlations (top 60)
    pos_widget.insert(tk.END, "=== Top Positive Correlations ===\n\n")
    for row in sorted_flat[-60:][::-1]:
        formatted_row  = [f"{row[0]:.4f}"] + row[1:]
        pos_widget.insert(tk.END, str(formatted_row ) + "\n")

    # negative correlations (top 60)
    neg_widget.insert(tk.END, "=== Top Negative Correlations ===\n\n")
    for row in sorted_flat[:60]:
        formatted_row  = [f"{row[0]:.4f}"] + row[1:]
        neg_widget.insert(tk.END, str(formatted_row ) + "\n")
 
