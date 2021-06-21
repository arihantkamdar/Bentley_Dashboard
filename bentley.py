# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:48:24 2021

@author: Lenovo
"""

import streamlit as st
import pandas as pd
templates = ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]
import plotly.express as px
try:    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file)
        
            #data = pd.read_excel("D:/Streamlit/Audit_QK_Data_Example.xlsx")
            st.title("Bentley Dashboard")
            col_names = data.columns
            st.write("*created by SMIIT*")
            #if st.checkbox('Show dataframe'):
            #    data
            
            st.write("## Histograms and Pie Chart")
            
            option = st.selectbox(
                'Select Feature',
                 col_names)
            option2 = st.sidebar.selectbox('Type of chart', ['Histogram','Pie Chart'])
            
            
            if option2 == "Histogram":
                fig = px.histogram(data[option],x = option)
                st.plotly_chart(fig)
            
            #if option2 == "Pie Chart":
            
            if option2 == "Pie Chart":
                fig = px.pie(data[option],names = data[option])
                st.plotly_chart(fig)
                
                
            
            st.write("## Correlation plots ")
            
            attribute_1 = st.selectbox(
                'Select first Feature ',
                 col_names)
            
            attribute_2 = st.selectbox(
                'Select second Feature',
                 col_names)
            
            
            if st.checkbox('Add colour for 2d plot'):
                color_attribute_2d = st.selectbox(
                    'Select colour attribute for 3d',
                    col_names)
                fig_2 = px.scatter(data,x = attribute_1,y = attribute_2,color = color_attribute_2d)
                st.plotly_chart(fig_2)
            else:
                fig_2 = px.scatter(data,x = attribute_1,y = attribute_2)
                st.plotly_chart(fig_2)
            
            
            
            st.write("## Correlation plots in 3D ")
            
            
            attribute_3d1 = st.selectbox(
                'Select first Feature for 3d ',
                 col_names)
            
            attribute_3d2 = st.selectbox(
                'Select second Feature for 3d',
                 col_names)
            
            
            attribute_3d3 = st.selectbox(
                'Select third Feature for 3d',
                 col_names)
            
            
            if st.checkbox('Add color for 3d plot'):
                color_attribute = st.selectbox(
                    'Select colour attribute for 3d',
                    col_names)
                fig_3 = px.scatter_3d(data,x = attribute_3d1,y = attribute_3d2,z = attribute_3d3,color = color_attribute)
                st.plotly_chart(fig_3)
            else:
                fig_3 = px.scatter_3d(data,x = attribute_3d1,y = attribute_3d2,z = attribute_3d3)
                st.plotly_chart(fig_3)
            
            
            st.write("## Calculating the total Fault Points ")
            
            A1 = st.number_input('Number of A1 Faults',step = 1)
            A = st.number_input('Number of A Faults',step = 1)
            B1 = st.number_input('Number of B1 Faults',step = 1)
            B = st.number_input('Number of B Faults',step = 1)
            C1 = st.number_input('Number of C1 Faults',step = 1)
            C = st.number_input('Number of C Faults',step = 1)
            
            Total = 100*A1 + 80*A + 60*B1 + 40*B + 20*C1 + 10*C
            
            st.write("## The total Fault Points: ",Total)
            
            
            st.write("## The BC1 score is:", 2*B+1*C1)
            
            
            data = {
              "Total Faults": [400, 440,480, 520,560,600,640,680,720,760,800,840,880,920,940,1000,1040,1080,1120,1160,1200,1240],
              "QK": [1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.0]
            }
            
            df = pd.DataFrame(data)
            
            def roundup(x):
                return int(round(x / 40)) * 40
            
            Round_total = roundup(Total)
            try:
                QK = df["QK"].where(df["Total Faults"]== Round_total)
                QK.dropna(inplace = True)
                st.write("## The QK score is:", float(QK))
            
            except TypeError:
                if Total <400:
                    st.write("## The QK score is: < 1.0")
                else:
                    st.write("## The QK score is: > 3.0")
        except ValueError:
            st.write("Please choose a file")
except AssertionError:
    st.write("Error")