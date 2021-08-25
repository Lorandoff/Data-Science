#!/usr/bin/env python
# coding: utf-8

# In[60]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import openpyxl
data = pd.read_excel("Регрессия.xlsx", sheet_name = "Лист1")
data2 = pd.read_excel("Регрессия.xlsx", sheet_name = "GDP  immi work")
data3 = pd.read_excel("Регрессия 2.xlsx", sheet_name = "Immigration")
data4 = pd.read_excel("Регрессия 2.xlsx", sheet_name = "GDP Growth")
data6 = pd.read_excel("Регрессия 3.xlsx", sheet_name = "Immigration")
data7 = pd.read_excel("Регрессия 3.xlsx", sheet_name = "Лист1")



# In[61]:

data.columns = ["year", "immigrants(в 100 тыс)", "gdp"]
data["immigrants(в 100 тыс)"] = data["immigrants(в 100 тыс)"] / 100000
data2 = data2.dropna().reset_index(drop = True)
data2.columns = ["country", "immigrant", "GDP(2010-2019)"]
data2 = data2.tail(24)
for i in ["immigrant", "GDP(2010-2019)"]:
    data2[i] = data2[i].astype("float64")


data3.columns = ["country","migr", "migration", "0","1","2","3"]
data3 = data3.tail(279)
data3 = data3[["country","migration"]]
print(data4.columns)
data4 = data4[["Country Name", "2010-2019"]]
#data3["2010-2019"] = 1
data3["country"] = data3["country"].str.lower()
data3["country"] = data3["country"].str.replace("\xa0", "")
data4["Country Name"] = data4["Country Name"].str.lower()
print(data3[data3["country"] == "afghanistan"])
print(data4[data4["Country Name"] == "afghanistan"])
list1 = pd.DataFrame()
list2 = []
data4.columns = ["country", "2010-2019"]
data5 = data3.merge(data4, on = "country", how = "outer")
data5 = data5.dropna()
data5["migration"] = data5["migration"].astype("float64")
data5["2010-2019"] = data5["2010-2019"].astype("float64")
# In[64]:

page = st.sidebar.selectbox("Выберите страницу:", ["USA immig GDP","GDP immi work", "Immigration"])
if page == "USA immig GDP":
    year = st.sidebar.multiselect("Выберите год:", data["year"].unique())
    new_df = data[data["year"].isin(year)]
    show_df = st.sidebar.checkbox("Показать таблицу")
    if show_df == True:
        st.subheader("Таблица")
        st.write(new_df)
    fig,ax = plt.subplots()
    ax = sns.heatmap(new_df.corr(), vmin = -1, vmax = 1, annot = True)
    figure = go.Figure()
    for i in ["immigrants(в 100 тыс)", "gdp"]:
        figure.add_trace(go.Scatter(x = new_df["year"], y = new_df[i], name = i))
    figure2 = go.Figure()
    for i in ["immigrants(в 100 тыс)", "gdp"]:
        figure2.add_trace(go.Bar(x = new_df["year"], y = new_df[i], name = i))
    st.pyplot(fig)
    st.plotly_chart(figure)
    st.plotly_chart(figure2)
if page == "GDP immi work":
    country = st.sidebar.selectbox("Выберите страну:", data2["country"].unique())
    new_df2 = data2[data2["country"].isin([country])]
    new_df2.columns = ["country", "immigrant", "GDP(2010-2019)"]
    fig,ax = plt.subplots()
    ax = sns.heatmap(data2.corr(), vmin = -1, vmax = 1, annot = True)
    show_df = st.sidebar.checkbox("Показать таблицу")
    if show_df == True:
        st.subheader("Таблица")
        st.write(new_df2)
    show_scatter = st.sidebar.checkbox("Показать график")
    if show_scatter == True:
        st.subheader("График зависимостей")
        fig2 = px.scatter(data2, x = "immigrant", y = "GDP(2010-2019)", color = "country")
        st.plotly_chart(fig2)
    show_barplot = st.sidebar.checkbox("Показать столбчатую диаграмму")
    if show_barplot == True:
        st.subheader("Столбчатая диаграмма")
        fig3 = px.bar(data2, x = "immigrant", y = "GDP(2010-2019)", color = "country")
        st.plotly_chart(fig3)
    show_pie1 = st.sidebar.checkbox("Показать круговую диаграмму по иммигрантам")
    if show_pie1 == True:
        st.subheader("Круговая диаграмма по иммигрантам")
        fig4 = px.pie(data2, values = "immigrant", color = "country")
        st.plotly_chart(fig4)
    show_pie2 = st.sidebar.checkbox("Показать круговую диаграмму по GDP(2010-2019)")
    if show_pie2 == True:
        st.subheader("Круговая диаграмма по GDP(2010-2019)")
        fig5 = px.pie(data2, values = "GDP(2010-2019)", color = "country")
        st.plotly_chart(fig5)
    st.pyplot(fig)
if page == "Immigration":
    country2 = st.sidebar.selectbox("Выберите страну:", data5["country"].unique())
    new_df3 = data5[data5["country"].isin([country2])]
    data5.columns = ["country", "immigrant", "GDP(2010-2019)"]
    fig,ax = plt.subplots()
    ax = sns.heatmap(data5.corr(), vmin = -1, vmax = 1, annot = True)
    show_df = st.sidebar.checkbox("Показать таблицу")
    if show_df == True:
        st.subheader("Таблица")
        st.write(new_df3)
    show_scatter = st.sidebar.checkbox("Показать график")
    if show_scatter == True:
        st.subheader("График зависимостей")
        fig2 = px.scatter(data5, y = "immigrant", x = "GDP(2010-2019)", color = "country")
        st.plotly_chart(fig2)
    show_barplot = st.sidebar.checkbox("Показать столбчатую диаграмму")
    if show_barplot == True:
        st.subheader("Столбчатая диаграмма")
        fig3 = px.bar(data5[(data5["immigrant"] > 20) & (data5["GDP(2010-2019)"] > 2.3)], y = "immigrant", x = "GDP(2010-2019)", color = "country")
        st.plotly_chart(fig3)
    show_pie1 = st.sidebar.checkbox("Показать круговую диаграмму по иммигрантам")
    if show_pie1 == True:
        st.subheader("Круговая диаграмма по иммигрантам")
        fig4 = px.pie(data5[data5["immigrant"] > 30], values = "immigrant", color = "country")
        st.plotly_chart(fig4)
    show_pie2 = st.sidebar.checkbox("Показать круговую диаграмму по GDP(2010-2019)")
    if show_pie2 == True:
        st.subheader("Круговая диаграмма по GDP(2010-2019)")
        fig5 = px.pie(data5[data5["GDP(2010-2019)"] > 4.5], values = "GDP(2010-2019)", color = "country")
        st.plotly_chart(fig5)
    st.pyplot(fig)
# In[ ]:




