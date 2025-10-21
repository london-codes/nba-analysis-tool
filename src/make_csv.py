import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
#ex: make_player_csv("https://www.basketball-reference.com/wnba/players/w/willico01w/gamelog/2025/",'courtney')

#wnba specifcally
#don't request to fast or too much because basket ball refernce will block your request.

#makes a csv file for a player using basket ball reference data, give url for specifc year game log for player
#and input the name you want the csv file to be named which is also what will show up in program.


# gets data from basketball reference website
def get_data_using_url(url):
    time.sleep(5)                                                    # only runs every 5 seconds to not overwhelm basketball refernce
    res = requests.get(url)
    soup=BeautifulSoup(res.text, "lxml")

     
    table = soup.find('table', {'id': 'wnba_pgl_basic'})             # gets regular season table
    col_names_html = table.find('tr')                                # gets HTML code for column names
    col_names = [title.text for title in col_names_html.find_all('th')]# gets column names for df


    all_data_html = table.find('tbody')                              # gets raw HTML code for all the rows of our table we are making
    all_data = []
    rows_html = all_data_html.find_all('tr')                         # grabs tag for each row
    for a_row_html in rows_html:
        elements_html = a_row_html.find_all('td')                    # goes into each tag for row and collects each element for making the row
        row = []
        for element_html in elements_html:
            row.append(element_html.text)
        if row == []:                                                # checks if row is empty means it was a row that just repeated  the columns names
            continue
        all_data.append(row)
    df = pd.DataFrame(all_data, columns=col_names[1:])               # [1:] slices of the rk column since I don't grab it when collecting the data
    return df


# function makes the data usable for calculations
def clean_data(df):

    # renaming some unamed stuff
    cols = df.columns.tolist()
    cols[3] = 'Where'
    cols[5] = 'Result'
    df.columns = cols

    columns_to_keep = [
        'Date', 'Tm', 'Where', 'Opp', 'Result',
        'MP', 'FGA', '3P', '3PA', 'FT', 'FTA',
        'ORB', 'DRB', 'TRB', 'AST', 'PTS'   
    ]
    table3 = df[columns_to_keep]

    # remove rows where the player did not play
    skip_vals = ['Inactive', 'Did Not Play', 'Did Not Dress','Not With Team']
    table4 = table3.loc[~table3['MP'].isin(skip_vals)].reset_index(drop=True)
    table5 = table4.loc[table4['Date'].notna()].reset_index(drop=True)


    # change necessary columns to numeric variables
    for col in table5.columns:
        if col not in ['Date', 'pos', 'Tm', 'Opp', 'Result', 'MP', 'Where']:
            table5[col] = pd.to_numeric(table5[col], errors='coerce')

    return table5


#update or make new player csv
def update_player_csv(url,name):
    data = clean_data(get_data_using_url(url))
    data['name'] = name


    # creates data folder if not there
    folder = 'data'
    os.makedirs(folder, exist_ok=True)

    # puts player into team that they have most recently played for
    team_folder = data['Tm'][len(data)-1]
    team_path = os.path.join(folder, team_folder)
    os.makedirs(team_path, exist_ok=True)

 
    # save CSV inside 'data' folder
    file_path = os.path.join(team_path, name + '.csv')
    data.to_csv(file_path, index=False)

