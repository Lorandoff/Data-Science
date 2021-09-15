#!/usr/bin/env python
# coding: utf-8

# In[60]:


get_ipython().system('pip install openpyxl')
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


# In[61]:


display(data)
data.info()
data.columns = data.columns.str.lower()
print(data.columns)
data.columns = ["year", "immigrants", "gdp"]
print(data.columns)


# In[64]:


year = st.sidebar.multiselect("Выберите год:", data["year"].unique())
new_df = data[data["year"].isin(year)]
show_df = st.sidebar.checkbox("Показать таблицу")
if show_df == True:
    st.subheader("Таблица")
    st.write(new_df)
fig,ax = plt.subplots()
ax = sns.heatmap(new_df.corr(), vmin = -1, vmax = 1, annot = True)
figure = go.Figure()
for i in ["immigrants", "gdp"]:
    figure.add_trace(go.Scatter(x = new_df["year"], y = new_df[i], name = i))
figure2 = go.Figure()
for i in ["immigrants", "gdp"]:
    figure2.add_trace(go.Bar(x = new_df["year"], y = new_df[i], name = i))
st.pyplot(fig)
st.plotly_chart(figure)
st.plotly_chart(figure2)


# In[ ]:




