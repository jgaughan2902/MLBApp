import streamlit as st
import pandas as pd
from pybaseball import standings
from pybaseball import schedule_and_record

@st.cache_resource
def load_data():
    data = standings(2026)
    return data

data = load_data()

options = ["AL East", "AL Central", "AL West",
     "NL East", "NL Central", "NL West"]

selection = st.selectbox("Label", options)

mapping = {
    "AL East" : 0,
    "AL Central" : 1,
    "AL West" : 2,
    "NL East" : 3,
    "NL Central" : 4,
    "NL West" : 5,
}

indexing_var = mapping[selection]

df = data[indexing_var]

st.dataframe(df)

options = [
    "Arizona Diamondbacks", 
    "__ Athletics",
    "Atlanta Braves",
    "Baltimore Orioles",
    "Boston Red Sox",
    "Chicago Cubs",
    "Chicago White Sox",
    "Cincinnati Reds",
    "Cleveland Guardians",
    "Colorado Rockies",
    "Detroit Tigers",
    "Houston Astros",
    "Kansas City Royals",
    "Los Angeles Angels",
    "Los Angeles Dodgers",
    "Miami Marlins",
    "Milwaukee Brewers",
    "Minnesota Twins",
    "New York Mets",
    "New York Yankees",
    "Philadelphia Phillies",
    "Pittsburgh Pirates",
    "San Diego Padres",
    "San Francisco Giants",
    "Seattle Mariners",
    "St. Louis Cardinals",
    "Tampa Bay Rays",
    "Texas Rangers",
    "Toronto Blue Jays",
    "Washington Nationals"
    ]

selection = st.selectbox("Choose Your Team!", options)

mapping = {
    "Arizona Diamondbacks" : "ARI", 
    "_______ Athletics" : "ATH",
    "Atlanta Braves" : "ATL",
    "Baltimore Orioles" : "BAL",
    "Boston Red Sox" : "BOS",
    "Chicago Cubs" : "CHC",
    "Chicago White Sox" : "CHW",
    "Cincinnati Reds" : "CIN",
    "Cleveland Guardians" : "CLE",
    "Colorado Rockies" : "COL",
    "Detroit Tigers" : "DET",
    "Houston Astros" : "HOU",
    "Kansas City Royals" : "KCR",
    "Los Angeles Angels" : "LAA",
    "Los Angeles Dodgers" : "LAD",
    "Miami Marlins" : "MIA",
    "Milwaukee Brewers" : "MIL",
    "Minnesota Twins" : "MIN",
    "New York Mets" : "NYM",
    "New York Yankees" : "NYY",
    "Philadelphia Phillies" : "PHI",
    "Pittsburgh Pirates" : "PIT",
    "San Diego Padres" : "SDP",
    "San Francisco Giants" : "SFG",
    "Seattle Mariners": "SEA",
    "St. Louis Cardinals" : "STL",
    "Tampa Bay Rays" : "TBR",
    "Texas Rangers" : "TEX",
    "Toronto Blue Jays" : "TOR",
    "Washington Nationals" : "WSN"
}

indexing_var = mapping[selection]

df = pd.DataFrame(schedule_and_record(2026, indexing_var))

st.dataframe(df)