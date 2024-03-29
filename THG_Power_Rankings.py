# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:19:18 2022

@author: MC
"""
import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(layout="wide")

#select which columns to be parsed for dates, variable used in case changes needed to be made in future
parse_dates = [2]

#Create dataframes for each Weekly Power Ranking
PR_Oct_09 = pd.read_csv('Data/Oct-09-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Oct_23 = pd.read_csv('Data/Oct-23-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Oct_30 = pd.read_csv('Data/Oct-30-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

PR_Nov_06 = pd.read_csv('Data/Nov-06-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Nov_13 = pd.read_csv('Data/Nov-13-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Nov_20 = pd.read_csv('Data/Nov-20-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Nov_27 = pd.read_csv('Data/Nov-27-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

PR_Dec_04 = pd.read_csv('Data/Dec-04-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Dec_11 = pd.read_csv('Data/Dec-11-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Dec_18 = pd.read_csv('Data/Dec-18-21.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

PR_Jan_01 = pd.read_csv('Data/Jan-01-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Jan_08 = pd.read_csv('Data/Jan-08-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Jan_15 = pd.read_csv('Data/Jan-15-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Jan_22 = pd.read_csv('Data/Jan-22-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Jan_29 = pd.read_csv('Data/Jan-29-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

PR_Feb_12 = pd.read_csv('Data/Feb-12-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Feb_19 = pd.read_csv('Data/Feb-19-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Feb_26 = pd.read_csv('Data/Feb-26-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

PR_Mar_05 = pd.read_csv('Data/Mar-05-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Mar_12 = pd.read_csv('Data/Mar-12-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Mar_17 = pd.read_csv('Data/Mar-17-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Mar_26 = pd.read_csv('Data/Mar-26-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

PR_Apr_02 = pd.read_csv('Data/Apr-02-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Apr_09 = pd.read_csv('Data/Apr-09-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Apr_16 = pd.read_csv('Data/Apr-16-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Apr_23 = pd.read_csv('Data/Apr-23-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})
PR_Apr_30 = pd.read_csv('Data/Apr-30-22.csv', parse_dates = parse_dates).rename(columns={'Unnamed: 0':'Team'})

#dictionay containing the dataframes and the date associated with them.
Dict_of_PR_dfs = {'April 30th':PR_Apr_30,
                  'April 23rd':PR_Apr_23,
                  'April 16th':PR_Apr_16,
                  'April 9th':PR_Apr_09,
                  'April 2nd':PR_Apr_02,
                  'March 26th':PR_Mar_26,
                  'March 17th':PR_Mar_17,
                  'March 12th':PR_Mar_12,
                  'March 5th':PR_Mar_05,
                  'February 26th':PR_Feb_26,
                  'February 19th':PR_Feb_19,
                  'February 12th':PR_Feb_12,
                  'January 29th':PR_Jan_29,
                  'January 22nd':PR_Jan_22,
                  'January 15th':PR_Jan_15,
                  'January 8th':PR_Jan_08,
                  'January 1st':PR_Jan_01,
                  'December 18th':PR_Dec_18,
                  'December 11th':PR_Dec_11,
                  'December 4th':PR_Dec_04,
                  'November 27th':PR_Nov_27,
                  'November 20th':PR_Nov_20,
                  'November 13th':PR_Nov_13,
                  'November 6th':PR_Nov_06,
                  'October 30th':PR_Oct_30,
                  'October 23rd':PR_Oct_23,
                  'October 9th':PR_Oct_09}
List_of_dfs = []

PR_items = Dict_of_PR_dfs.items()

for key, value in PR_items:
    List_of_dfs.append(value)
                

#List_of_dfs = [PR_Oct_09,PR_Oct_23,PR_Oct_30,PR_Nov_06,PR_Nov_13,PR_Nov_20,PR_Nov_27,PR_Dec_04,PR_Dec_11,PR_Dec_18,PR_Jan_01,PR_Jan_08,PR_Jan_15,PR_Jan_22,PR_Jan_29]

Teams_List = ['VGK','BOS', 'ANA', 'ARI', 'BUF', 'CAR', 'CHI', 'CGY', 'DAL', 'COL', 'EDM', 'NJD', 'NYI', 'CBJ', 'NYR', 'FLA', 'MIN', 'LAK', 'OTT', 'DET', 'MTL', 'PHI', 'NSH', 'PIT', 'SJS', 'STL', 'TBL', 'SEA', 'WPG', 'VAN', 'WSH', 'TOR']

Teams_List = sorted(Teams_List)

All_List =  ['ALL'] + Teams_List 

None_List = ['None'] + Teams_List

Pacific = ['ANA','SJS','LAK','CGY','VAN','VGK','EDM']

#Create Streamlit containers
Header = st.container()
Rankings = st.container()
Graphs1 = st.container()
Graphs2 = st.container()
Footer = st.container()

with Header:
    st.title("Welcome to THG's Power Ranking Fan Page")
    st.text("This project showcases 'The Hockey Guy' Power Rankings of NHL Teams in the 21/22 season")
    st.text("This is a fan site and in no way takes credit for the data provided")
    st.text("Below is a link to THG's youtube page where all the info can be found")
    st.markdown('https://www.youtube.com/channel/UC_AFyA9FqrZ57bb9QRH77wg' ,unsafe_allow_html=True)
    st.text('Hope you enjoy the data visualizations!')
    st.text('-M.Vaz')
    
with Rankings:
    st.header('Power Ranking Data')
    st.text('Simply select the Power Ranking Date, and up to three teams to see how they stack up!')
    st.text('Or just leave it as "ALL" and "None" to see all rankings')
    
    col1,col2 = st.columns((1,4))
    with col1:
        PR_Date = st.selectbox('Pick PR', Dict_of_PR_dfs)
        
        Team_Select =st.selectbox('Pick Team', All_List)
        
        Team_2_Select =st.selectbox('Pick 2nd Team', None_List)
        
        Team_3_Select =st.selectbox('Pick 3rd Team', None_List)
        
    
    
    for team , value in PR_items:
        if team == PR_Date:
            selected_df = value
    
    Display_Data = selected_df.drop(['Date'], axis = 1).sort_values(by = ['Rank'])
    
    Display_Team = Display_Data[Display_Data['Team']==Team_Select]
    
    Display_2_List = [Team_Select, Team_2_Select]
    
    Display_3_List = [Team_Select, Team_2_Select, Team_3_Select]
    
    Display_2_Teams = Display_Data.loc[(Display_Data['Team'] == Team_Select) | (Display_Data['Team'] == Team_2_Select)]
    
    Display_3_Teams = Display_Data.loc[(Display_Data['Team'] == Team_Select) | (Display_Data['Team'] == Team_2_Select) | (Display_Data['Team'] == Team_3_Select) ]
    
    
    #To hide the index from the visualized df
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    
    with col2:
        
        if Team_Select == 'ALL':
            
            st.dataframe(Display_Data)
        
        elif Team_3_Select != 'None':
            
            st.dataframe(Display_3_Teams)
        
        elif Team_2_Select != 'None':
            
            st.dataframe(Display_2_Teams)      
        
            
        else:
            
            st.dataframe(Display_Team)
    
with Graphs1:
    
    st.header('Visualization of Ranking over the Season')
    st.text('Simply select the team, and see there seasonal progression')
        
    col3,col4 = st.columns((2,5))
        
    Combined_df = pd.concat(List_of_dfs)
        
    with col3:
            
        Team = st.selectbox('Pick Team', Teams_List)
        
    Date_sorted_df = Combined_df.sort_values(by = ['Date'])
        
    Selected_df = Date_sorted_df[Date_sorted_df['Team']==Team].reset_index(drop = True)
        
    Selected_df = Selected_df.drop(['Team'], axis = 1)
        
    Selected_df['Date'] = Selected_df['Date'].dt.date
        
    Selected_Graph = (alt.Chart(Selected_df, width = 600, height = 700)
                        .mark_line()
                        .configure_title(fontSize = 24)
                        .configure_axis(titleFontSize = 20)
                        .encode(x=alt.X("Date:T", title = 'Date of Power Ranking'),
                                y= alt.Y("Rank:Q", scale = alt.Scale(domain=(32, 0)),title = 'Power Ranking'),
                                tooltip = ['Rank'])
                        #.interactive()
                        .properties(title = "Ranking over Time"))

        
        
    with col4:
        #displays graph
        st.altair_chart(Selected_Graph)
        
                
    Highest_Rank = Selected_df['Rank'].max()
        
    Lowest_Rank = Selected_df['Rank'].min()
        
    Average_Rank = Selected_df['Rank'].mean().round(1)
        
    Current_Rank = Selected_df.loc[Selected_df['Date'] == Selected_df['Date'].max(), 'Rank'].item()
        
    with col3:
        st.text(' ')
            
        st.text('Highest Rank: '+str(Lowest_Rank))
            
        st.text(' ')
            
        st.text(' ')
            
        st.text('Average Rank: '+str(Average_Rank))
            
        st.text(' ')
            
        st.text(' ')
            
        st.text('Lowest Rank: '+str(Highest_Rank))
            
        st.text(' ')
            
        st.text(' ')
            
        st.text('Current Rank: '+str(Current_Rank))
with Graphs2:

    col5,col6 = st.columns((2,5))



        
with Footer:
    
    st.text('Thanks for checking out my app!')
    st.text('Any suggestions, contact me! markchris.vaz@gmail.com')
    
    
    
    
    