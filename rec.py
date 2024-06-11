import pandas as pd
import streamlit as  st

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capital',
 'Lucknow Super Giants',
 'Gujarat Titans']

data_batting = pd.read_csv('2023_batsman.csv')
data_bowling = pd.read_csv('alltime_bowling_stats.csv')

def recommend_batsmen(target_runs, team):
    # Filter data for the specified team
    team_data = data_batting[data_batting['Team'] == team]

    # Sort batsmen from the specified team based on average runs scored
    batsmen_sorted = team_data.sort_values(by=['Total Runs'], ascending=False)

    # Select top 4 batsmen
    recommended_batsmen = batsmen_sorted.head(4)['Batsman'].tolist()

    return recommended_batsmen

st.title('Recommendation for Batsmen')
target = st.number_input('Target')
col1, = st.columns(1)
with col1:
    team = st.selectbox('Select the batting team',sorted(teams))
recommended_batsmen = recommend_batsmen(target, team)
if st.button('Get recommendations'):
           st.header(f"From team {team} these players are capable to chase such target:")
           for i, batsman in enumerate(recommended_batsmen, 1):
            st.header(f"{i}. {batsman}")