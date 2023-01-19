import streamlit as st
from collections import namedtuple
import math
import pandas as pd
import numpy as np
import plost                # this package is used to create plots/charts within streamlit
from PIL import Image       # this package is used to put images within streamlit
from api_connection import get_data_from_api       # keep this commented if not using it otherwise brakes the app

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data From API
outputs = get_data_from_api()

home_pos=[]
away_pos=[]
home_t=[]
away_t=[]
home_g=[]
away_g=[]
home_p=[]
away_p=[]
home_f=[]
away_f=[]
home=[]
form=[]
poss=[]
teams=[]
goals=[]
penalties=[]


for i in range(4):
    home_posession = outputs['matches'][i]['BallPossession']["OverallHome"]
    away_posession = outputs['matches'][i]['BallPossession']["OverallAway"]
    poss.append(home_posession)
    poss.append(away_posession)
    home_team = outputs['matches'][i]['Home']['Abbreviation']
    away_team = outputs['matches'][i]['Away']['Abbreviation']
    teams.append(home_team)
    teams.append(away_team)
    home_goals=outputs['matches'][i]['Home']['Score']
    away_goals=outputs['matches'][i]['Away']['Score']
    goals.append(home_goals)
    goals.append(away_goals)
    home_penalties=outputs['matches'][i]['HomeTeamPenaltyScore']
    away_penalties=outputs['matches'][i]['AwayTeamPenaltyScore']
    penalties.append(home_penalties)
    penalties.append(away_penalties)
    home_form=outputs['matches'][i]['Home']['Tactics']
    away_form=outputs['matches'][i]['Away']['Tactics']
    form.append(home_form)
    form.append(away_form)
    home_pos.append(home_posession)
    away_pos.append(away_posession)
    
    home_t.append(home_team)
    away_t.append(away_team)
    home_g.append(home_goals)
    away_g.append(away_goals)
    home_p.append(home_penalties)
    away_p.append(away_penalties)
    home_f.append(home_form)
    away_f.append(away_form)


matches = pd.DataFrame({'Home Teams': home_t})
matches['Away Teams'] = away_t

### Here starts the web app design

#Title
st.title("World Cup 2022 Matchday Stats")

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('WC_2022_Logo.png'))
a2.metric("Matchday", "December 2nd, 2022")
a3.dataframe(matches)

# Home and Away performance
b1, b2, b3, b4 = st.columns(4)
b1.table("Home Goals", home_g)
b2.metric("Away Goals", away_g)
b3.metric("Home Penalties Awarded", home_p)
b4.metric("Away Penalties Awarded", away_p)

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')              # text is created with markdown
    plost.time_hist(                        # histogram
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(                      # donut charts
        data=stocks,
        theta='q2',
        color='company')
