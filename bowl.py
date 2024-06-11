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

#data_batting = pd.read_csv('2023_batsman.csv')
data_bowling = pd.read_csv('2023 Bowler.csv')

def recommend_bowler(target_runs, team):
    # Filter data for the specified team
    team_data = data_bowling[data_bowling['Teams'] == team]

    # Sort batsmen from the specified team based on average runs scored
    bowler_sorted = team_data.sort_values(by=['Econ'], ascending=False)

    # Select top 4 batsmen
    recommended_bowler = bowler_sorted.head(5)['Player'].tolist()

    return recommended_bowler

st.title('Recommendation for Bowlers')
target = st.number_input('Target')
col1, = st.columns(1)
with col1:
    team = st.selectbox('Select the bowling team',sorted(teams))
recommended_bowler = recommend_bowler(target, team)
if st.button('Get recommendations'):
           st.header(f"From team {team} these players are capable to defend such target:")
           for i, bowling in enumerate(recommended_bowler, 1):
            st.header(f"{i}. {bowling}")



