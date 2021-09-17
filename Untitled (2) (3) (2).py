#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install seaborn')
get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install plotly')
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.color_palette("viridis")
data_14_3 = pd.read_csv("data-1-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_14_4 = pd.read_csv("data-2-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")  
data_15_1 = pd.read_csv("data-3-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_15_2 = pd.read_csv("data-4-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_15_3 = pd.read_csv("data-5-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_15_4 = pd.read_csv("data-6-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_16_1 = pd.read_csv("data-7-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_16_2 = pd.read_csv("data-8-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_16_3 = pd.read_csv("data-9-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_16_4 = pd.read_csv("data-10-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_17_1 = pd.read_csv("data-11-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_17_2 = pd.read_csv("data-12-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_17_3 = pd.read_csv("data-13-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_17_4 = pd.read_csv("data-14-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_18_1 = pd.read_csv("data-15-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_18_2 = pd.read_csv("data-16-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_18_3 = pd.read_csv("data-17-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_18_4 = pd.read_csv("data-18-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_19_1 = pd.read_csv("data-19-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_19_2 = pd.read_csv("data-20-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_19_3 = pd.read_csv("data-21-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_19_4 = pd.read_csv("data-22-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_20_1 = pd.read_csv("data-23-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_20_2 = pd.read_csv("data-24-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_20_3 = pd.read_csv("data-25-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_20_4 = pd.read_csv("data-26-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_21_1 = pd.read_csv("data-27-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")
data_21_2 = pd.read_csv("data-28-structure-1.csv",encoding = "cp1251", sep = ";", thousands = " ", decimal = ",")

display(data_20_4)
dictinary = [data_14_3,data_14_4,data_15_1,data_15_2,data_15_3,data_15_4,data_16_1,data_16_2,data_16_3,data_16_4,data_17_1,
             data_17_2,data_17_3,data_17_4,data_18_1,data_18_2,data_18_3,data_18_4,data_19_1,data_19_2,data_19_3,data_19_4,
             data_20_1,data_20_2, data_20_3, data_20_4, data_21_1, data_21_2]
dictinary_year = ["2014_3","2014_4","2015_1","2015_2","2015_3", "2015_4", "2016_1","2016_2","2016_3","2016_4","2017_1","2017_2",
                  "2017_3","2017_4","2018_1","2018_2","2018_3","2018_4","2019_1","2019_2","2019_3","2019_4","2020_1","2020_2",
                  "2020_3","2020_4","2021_1","2021_2"]

for i in range(len(dictinary)):
    dictinary[i] = dictinary[i].dropna(axis = 1)
    dictinary[i].columns = ["id","name","money"]
    dictinary[i]["money"] = dictinary[i]["money"].astype("float64")
    
for dic,year in zip(dictinary,dictinary_year):
    dic["year"] = year
    


print(dictinary[0])
dictinary[0].info()
data = pd.DataFrame()
for i in range(len(dictinary)):
    dictinary[i] = pd.DataFrame(data = dictinary[i],columns = ["id","name","money","year"])
    data = pd.concat([data,dictinary[i]], ignore_index = True)
    
print(data.head(15))
data.info()


# In[3]:


#display(data)
#data = data.dropna(axis = 1)
#display(data)
#print(data.columns)
#data.columns = ["id","name","money"]
#data.info()
#print(data["money"].min(), data["money"].max())
#data["money"] = data["money"].str.split
#def category(row):
    #if "-" in row:
        #return row
    
#dataa = data
#dataa["i"] = data["money"].apply(category)
#print(dataa["i"])
#dataa["money"] = dataa["money"].infer_objects()
#print(dataa)
#dataa.info()
#data["money"] = pd.to_numeric(data["money"], downcast = "unsigned")
#display(data)
#data.info()
#data["money"] = data["money"].apply(abs)
#data["money"] = data["money"].str.replace("-","")
#data["money"] = data["money"].str.replace(",",".", regex = True)
#display(data)
#data_3.columns = ["id","name","money"]
#data_3["money"] = data_3["money"].str.replace(" ","")
#data["money"] = data["money"].str.replace(" ","")
#print(data)
#data_3["money"] = data_3["money"].apply(lambda x: float(x.split()[0].replace(",",".")))
#data["money"] = data["money"].apply(lambda x: float(x.split()[0].replace(",",".")))
#data["money"] = pd.convert_objects(data["money"],convert_numeric = True)
#data.info()
#display(data)
#print(data_3)
#data["money"] = data["money"] * 1000 * 1000
#data["money"] = data["money"] * 1000 * 1000
plt.figure(figsize = (10,10),dpi = 80)
plt.hlines(y = data["name"], xmin = data["money"].min(), xmax = data["money"].max())
plt.show()
plt.figure(figsize = (10,10), dpi = 80)
sns.barplot(data = data, x  = "name",y = "money")
plt.xticks(rotation = 90)
plt.show()
plt.figure(figsize = (10,10), dpi = 80)
sns.barplot(data = data, x = "year", y = "money", hue = "name")
plt.title("2 квартал 2021")
plt.xticks(rotation = 90)
plt.show()
for i in list(data["name"].unique()):
    data_want = data[data["name"] == i]
    #plt.figure(figsize = (5,5), dpi = 70)
    #sns.barplot(data = data_want, x = "year", y = "money", hue = "name")
    #plt.xticks(rotation = 90)
    #plt.show()

data_group = data.groupby(["name","year"], as_index = False).mean()
print(data_group)
fig = px.bar(data, x = "year", y = "money", color = "name", barmode = "overlay")
fig.show()

fig1 = px.line(data_group, x = "year", y = "money", color = "name")
fig1.show()


# In[4]:


get_ipython().system('pip install dash')
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

all_continents = data.name.unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(
        id="checklist",
        options=[{"label": x, "value": x} 
                 for x in all_continents],
        value=all_continents[3:],
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="line-chart"),
])

@app.callback(
    Output("line-chart", "figure"), 
    [Input("checklist", "value")])
def update_line_chart(continents):
    mask = data_group.name.isin(name)
    fig = px.line(data_group[mask], 
        x="year", y="money", color='name')
    return fig

app.run_server(debug=True)


# In[6]:


get_ipython().system('pip install streamlit')

import streamlit as st

names = st.sidebar.multiselect("Город выбери", data_group["name"].unique())

year = st.sidebar.multiselect("Год выбери", data_group["year"].unique())

new_df = data_group[(data_group["name"].isin(names)) & (data_group["year"].isin(year))]
st.write(new_df)
fig = px.line(new_df, x = "year", y = "money", color = "name")
st.plotly_chart(fig)


# In[ ]:





# In[ ]:





# In[ ]:




