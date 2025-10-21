import pandas as pd
import os

folder_path = os.path.dirname(os.path.dirname(__file__))

#from data folder loads all csvs from each team folder as key in dicitonary and each key holds a array of each player df
def load_groups_auto():

    result = {}
    data_folder = os.path.join(folder_path, 'data')
    
    # iterate over each subfolder (team)
    for team_name in os.listdir(data_folder):
        team_path = os.path.join(data_folder, team_name)
        if os.path.isdir(team_path):
            dfs = []
            # iterate over each CSV in the team folder
            for file in os.listdir(team_path):
                if file.endswith('.csv'):
                    player_name = os.path.splitext(file)[0]
                    df = pd.read_csv(os.path.join(team_path, file))
                    df['name'] = player_name
                    dfs.append(df)
            result[team_name] = dfs
    return result
