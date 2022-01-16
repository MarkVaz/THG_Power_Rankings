# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:38:29 2022

@author: MC
"""

import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

header = st.container()
inputs = st.container()
footer = st.container()

Team_Dict = {'BOS':0,
             'ANA':0,
             'ARI':0,
             'BUF':0,
             'CAR':0,
             'CHI':0,
             'CGY':0,
             'DAL':0,
             'COL':0,
             'EDM':0,
             'NJD':0,
             'NYI':0,
             'CBJ':0,
             'NYR':0,
             'FLA':0,
             'MIN':0,
             'LAK':0,
             'OTT':0,
             'DET':0,
             'MTL':0,
             'PHI':0,
             'NSH':0,
             'PIT':0,
             'SJS':0,
             'STL':0,
             'TBL':0,
             'SEA':0,
             'WPG':0,
             'VAN':0,
             'VGK':0,
             'WSH':0,
             'TOR':0}

Team_List = ['VGK','BOS', 'ANA', 'ARI', 'BUF', 'CAR', 'CHI', 'CGY', 'DAL', 'COL', 'EDM', 'NJD', 'NYI', 'CBJ', 'NYR', 'FLA', 'MIN', 'LAK', 'OTT', 'DET', 'MTL', 'PHI', 'NSH', 'PIT', 'SJS', 'STL', 'TBL', 'SEA', 'WPG', 'VAN', 'WSH', 'TOR']

order_list = [i for i in range(1,33)]

length = len(Team_Dict)

with header:
    st.title('POWER RANKING FILE CREATOR')
    
    Date = st.text_input('Date of PR')
    
with inputs:
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    
    
    
    with col1:
        PR1 = st.selectbox('Rank 1', Team_List)
        PR9 = st.selectbox('Rank 9', Team_List)
        PR17 = st.selectbox('Rank 17', Team_List)
        PR25 = st.selectbox('Rank 25', Team_List)          
        
    with col2:
        PR2 = st.selectbox('Rank 2', Team_List)
        PR10 = st.selectbox('Rank 10', Team_List)
        PR18 = st.selectbox('Rank 18', Team_List)
        PR26 = st.selectbox('Rank 26', Team_List)
        
    with col3:
        PR3 = st.selectbox('Rank 3', Team_List)
        PR11 = st.selectbox('Rank 11', Team_List)
        PR19 = st.selectbox('Rank 19', Team_List)
        PR27 = st.selectbox('Rank 27', Team_List)
            
    with col4:
        PR4 = st.selectbox('Rank 4', Team_List)
        PR12 = st.selectbox('Rank 12', Team_List)
        PR20 = st.selectbox('Rank 20', Team_List)
        PR28 = st.selectbox('Rank 28', Team_List)
        
    with col5:
        PR5 = st.selectbox('Rank 5', Team_List)
        PR13 = st.selectbox('Rank 13', Team_List)
        PR21 = st.selectbox('Rank 21', Team_List)
        PR29 = st.selectbox('Rank 29', Team_List)
        
    with col6:
        PR6 = st.selectbox('Rank 6', Team_List)
        PR14 = st.selectbox('Rank 14', Team_List)
        PR22 = st.selectbox('Rank 22', Team_List)
        PR30 = st.selectbox('Rank 30', Team_List)
        
    with col7:
        PR7 = st.selectbox('Rank 7', Team_List)
        PR15 = st.selectbox('Rank 15', Team_List)
        PR23 = st.selectbox('Rank 23', Team_List)
        PR31 = st.selectbox('Rank 31', Team_List)
        
    with col8:
        PR8 = st.selectbox('Rank 8', Team_List)
        PR16 = st.selectbox('Rank 16', Team_List)
        PR24 = st.selectbox('Rank 24', Team_List)
        PR32 = st.selectbox('Rank 32', Team_List)
        
        
        
        
        
        
    PR_List = [PR1,
               PR2,
               PR3,
               PR4,
               PR5,
               PR6,
               PR7,
               PR8,
               PR9,
               PR10,
               PR11,
               PR12,
               PR13,
               PR14,
               PR15,
               PR16,
               PR17,
               PR18,
               PR19,
               PR20,
               PR21,
               PR22,
               PR23,
               PR24,
               PR25,
               PR26,
               PR27,
               PR28,
               PR29,
               PR30,
               PR31,
               PR32]
    rank = 0
    calculate = st.button('Create')
    
    if calculate:
        for item in PR_List:
            rank +=1
            Team_Dict[item] = rank
            
        Rank_df = pd.DataFrame.from_dict(Team_Dict, orient='index', columns=['Rank'])
        
        Rank_df['Date'] = Date
        
        Name = "Data/"+str(Date)+".csv"
        
        Rank_df.to_csv(Name)

            
        
        
        
        
            
        
        
        
        
            
        
    
    
    
        
    
    
    
    
    
    
    