from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


plt.style.use('seaborn')

@st.cache
def load_data():
    df= read_csv("waterquality.csv",encoding='latin1',index_col="LOCATIONS")
    return df

st.title("WATER QUALITY ANALYSIS")
st.sidebar.header("Project Options")

options = [
    'Overview','view dataset',
    'Biochemical Oxygen Demand in Different State','Temperature of water in different state',
    'pH value ','Conductivity','Dissolved Oxygen','NITRATE N NITRITE N','TOTAL COLIFORM',
    'Temperature','Total Coliform in Different State'
    ]

choice = st.sidebar.selectbox("select an option",options)

df = load_data()

if choice == options[0]:
    st.image("water.jpg")
    st.header("Water Quality Analysis")
    st.info('''We all know water is one of the most essential resource for our living.
     But as the development is increasing, we are exploiting water by wasting it and
     treating it with harmful materials which makes water impure and unfit for use.
     This is the reason it is very important to know the quality of water. 

    ''')
    color=st.sidebar.color_picker("select graph color")
    fig,ax = plt.subplots()
    df['STATE'].value_counts().plot.bar(title='Water Quality in Different state', xlabel='STATES',ax=ax,color=color)
    st.pyplot(fig)

elif choice == options[1]:
    st.dataframe(df)
    

elif choice == options[2]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax = plt.subplots()
    df.sort_values('BOD',ascending=False).head(25).plot.bar(x='STATE',y='BOD',figsize=(17,8),ax=ax,color =color)
    plt.title("BIOLOGICAL OXYGEN DEMAND OF OXYGEN")
    plt.xlabel("STATE")
    plt.ylabel("BOD")
    st.pyplot(fig)

elif choice == options[3]:
    color=st.sidebar.color_picker("select graph color")
    
    fig,ax = plt.subplots()
    df.head(30).plot.line(x='STATE',y='TEMP',figsize=(17,8),ax=ax,color=color)
    plt.title("Temperature")
    plt.xlabel("STATE")
    plt.ylabel("Temp")
    st.pyplot(fig)    

elif choice==options[4]:
    color=st.sidebar.color_picker("select graph color")    
    fig,ax=plt.subplots()
    df['pH'].head(10).plot.barh(figsize=(10,10),title='pH',ax=ax,color=color)
    plt.title('pH Value')                       
    st.pyplot(fig)

elif choice==options[5]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax=plt.subplots()
    df.sort_values('CONDUCTIVITY',ascending=False).head(25).plot.bar(x='STATE',y='CONDUCTIVITY',figsize=(17,8),ax=ax,color =color)
    plt.title("CONDUCTIVITY")
    plt.xlabel("STATE")
    plt.ylabel("Conductivity")
    st.pyplot(fig)


elif choice==options[6]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax=plt.subplots()
    df['DO'].head(10).plot.barh(figsize=(10,10),ax=ax,color=color)                    
    st.pyplot(fig)

elif choice==options[7]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax=plt.subplots()
    df['NITRATE_N_NITRITE_N'].head(20).plot.barh(figsize=(10,10),title='Nitrate of Water Of Diffferent location',ax=ax,color=color)                                          
    st.pyplot(fig)

elif choice==options[8]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax=plt.subplots()
    df['TOTAL_COLIFORM'].head(10).plot.barh(figsize=(10,10),ax=ax,color=color)                                    
    st.pyplot(fig)

elif choice==options[9]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax=plt.subplots()
    df['TEMP'].head(10).plot.bar(figsize=(10,10),ax=ax,color=color)  
    plt.title("Temperature" ) 
    st.pyplot(fig)   

elif choice==options[10]:
    color=st.sidebar.color_picker("select graph color")
    fig,ax=plt.subplots()
    df.head(30).plot.line(x='STATE',y='TOTAL_COLIFORM',figsize=(17,8),ax=ax,color=color)
    plt.title(" Total  Colfiform")
    plt.xlabel("STATE")
    plt.ylabel("Total Coliform")                 
    st.pyplot(fig)


 
