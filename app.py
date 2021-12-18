import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
teams = ['West Indies', 'Afghanistan', 'New Zealand', 'Sri Lanka',
         'South Africa', 'Australia', 'India', 'Pakistan', 'England',
         'Bangladesh']

cities = ['Colombo', 'Sharjah', 'Christchurch', 'Mount Maunganui',
          'Johannesburg', 'Nagpur', 'Sydney', 'Chandigarh', 'Lauderhill',
          'Nottingham', 'Barbados', 'Centurion', 'Wellington', 'Lahore',
          'Pallekele', 'Manchester', 'Mirpur', 'Cardiff', 'Dubai',
          'Cape Town', 'St Lucia', 'Auckland', 'Harare', 'Durban',
          'Hamilton', 'Dhaka', 'Southampton', 'Kolkata', 'Chittagong',
          'London', 'Abu Dhabi', 'Bangalore', 'Delhi', 'Melbourne', 'Mumbai',
          'Guyana', 'St Kitts', 'Trinidad', 'Hambantota', 'Adelaide']

st.title('T20 Score Predictor')

col1, col2 = st.columns(2)

with col1:
    bowling_team = None
    teams_ = [team for team in teams if team != bowling_team]
    batting_team = st.selectbox('Select Batting team', sorted(teams_))
with col2:
    teams_ = [team for team in teams if team != batting_team]
    bowling_team = st.selectbox('Select Bowling team', sorted(teams_))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs_done = st.number_input('Overs Completed(Works for over > 5)')
with col5:
    wickets = st.number_input('Wickets Gone')

last_five = st.number_input('Runs Scored in last 30 balls or 5 overs')

if st.button('Predict Score'):
    ball = str(overs_done).split('.')
    balls_left = 120 - ((int(ball[0]) * 6) + int(ball[1]))
    wickets_left = 10 - wickets
    crr = current_score / overs_done

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city],
                             'current_score': [current_score],
                             'balls_left': [balls_left], 'wickets_left': [wickets_left], 'crr': [crr],
                             'last_five': last_five})
    score = pipe.predict(input_df)
    st.header('The Projected Score is ' + str(int(score[0])))
