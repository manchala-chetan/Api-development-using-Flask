import pandas as pd 
import numpy as np 
import json

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)



def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams
    }

    return team_dict

def team_vs_teamAPI(team1, team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team1 in valid_teams and team2 in valid_teams:
        try:

            temp_df = matches[((matches['Team1']==team1) & (matches['Team2'] == team2)) | 
            ((matches['Team1']==team2) & (matches['Team2'] == team1))]
            total_matches = temp_df.shape[0]
            temp_df['WinningTeam'].value_counts()
            
            team_1_winning_team = temp_df['WinningTeam'].value_counts()[team1]
            team_2_winning_team = temp_df['WinningTeam'].value_counts()[team2]

            draws = total_matches - (team_1_winning_team + team_2_winning_team)

            response = {
                'total_matches': str(total_matches),
                team1: str(team_1_winning_team),
                team2: str(team_2_winning_team),
                'draws': str(draws)
            }
            
            return response
        except Exception as e:
            return {'Error: Something went wrong:',str(e)}
    else:
        return {'message':'Invalid Team name'}
