from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from load_csvs import load_groups_auto
from graph import graph_two
from corr_combos import all_correlation_combinations

# loading in data keys are names for teams and each key is a array holding the table for each player
teams = load_groups_auto()



#creates program
root = tk.Tk()
root.geometry("1500x700")


# default values for each button
array_of_all_stats=['PTS','AST','TRB','FGA','PAR','PA','PR','AR']
selected_team = tk.StringVar(value=list(teams.keys())[0])
selected_player1 = tk.StringVar(value='choose team')
selected_player2 = tk.StringVar(value='choose team')
selected_player1_stat = tk.StringVar(value='PTS')
selected_player2_stat = tk.StringVar(value='PTS')

# select team to get combinations for
team_dropdown = tk.OptionMenu(root, selected_team, *teams.keys())
team_dropdown.place(x=0,y=0)

# choose stats that will give all combinations in the text box
list_stats_selection = tk.Listbox(root, selectmode='multiple',height=8)
list_stats_selection.place(x=70,y=0)
list_stats_selection.insert(tk.END,*array_of_all_stats)

# select two players you want to see graph of
player1_dropdown = tk.OptionMenu(root, selected_player1, "")
player1_dropdown.place(x=900,y=0)
player2_dropdown = tk.OptionMenu(root, selected_player2, "")
player2_dropdown.place(x=1000,y=0)

# player1 stat choice and player 2 stat choice for graph
player1_stat = tk.OptionMenu(root, selected_player1_stat, *array_of_all_stats)
player1_stat.place(x=900,y=40)
player2_stat = tk.OptionMenu(root, selected_player2_stat, *array_of_all_stats)
player2_stat.place(x=1000,y=40)

# gives positive and negative correaltion scrollable boxes to see highest correlations
pos_box = ScrolledText(root, width=60, height=25)
pos_box.place(x=0, y=150)
neg_box = ScrolledText(root, width=60, height=25)
neg_box.place(x=400, y=150)

# give box for graph
graph_frame = tk.Frame(root, width=600, height=400)
graph_frame.place(x=900, y=150)


# updates the drop down menus for the visual graph
def update_players_for_graph_dropdown (team):

    # updates first dropdown
    menu = player1_dropdown["menu"]
    menu.delete(0, "end")
    for player in team:
        name = player['name'].iloc[0]   # get the player name from name column
        menu.add_command(label=name, command=lambda p=name: selected_player1.set(p))

    # updates 2nd dropdown
    menu = player2_dropdown["menu"]
    menu.delete(0, "end")
    for player in team:
        name = player['name'].iloc[0]
        menu.add_command(label=name, command=lambda p=name: selected_player2.set(p))

    # default dropdown values
    if team:
        selected_player1.set(team[0]['name'][0])
        selected_player2.set(team[0]['name'][0])
    

# gives all correlation values for all combinations of players and there stats. Also updates other dropdown for graph
def confirm_selection():
    choice = selected_team.get()                                  
    team_choice = teams[choice]                                 # creating array with each player table as elements
    update_players_for_graph_dropdown(team_choice)              # call function to change drop down menu for dropwdown 2
    
    indices = list_stats_selection.curselection()
    selected_stats= []                                          # get array of the selected stats
    for i in indices:
        selected_stats.append(array_of_all_stats[i])
    all_correlation_combinations(team_choice,selected_stats, pos_box, neg_box)


# function that calls to graph two players and there two stats for visual aid of something specifc you want to look at
def confirm_graph():

    for widget in graph_frame.winfo_children():
        widget.destroy()  # remove previous canvas

    # gets the player chosen in string form and selects that players data table form the dictionary
    player1 = next((player for player in teams[selected_team.get()] if player['name'][0] == selected_player1.get()), None)
    player2 = next((player for player in teams[selected_team.get()] if player['name'][0] == selected_player2.get()), None)
    # create new figure
    fig = graph_two(player1, player2, selected_player1_stat.get(), selected_player2_stat.get())
    
    # embed figure into the existing frame
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


#confirm team to get all correlations of
confirm_team = tk.Button(root, text="Confirm", command=confirm_selection)
confirm_team.place(x=0,y=40)

#confirm button for graph for two players and two stats
confirm_player_stat = tk.Button(root, text="Confirm", command=confirm_graph)
confirm_player_stat.place(x=900,y=80)

root.mainloop()
