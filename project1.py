#!/usr/bin/env python
# coding: utf-8

# In[6]:

#py -m pip install -r requirements.txt
import plotly
import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as sts
import numpy as np
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

#display(data_20_4)
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
    


#print(dictinary[0])
#dictinary[0].info()
data = pd.DataFrame()
for i in range(len(dictinary)):
    dictinary[i] = pd.DataFrame(data = dictinary[i],columns = ["id","name","money","year"])
    data = pd.concat([data,dictinary[i]], ignore_index = True)
    
#print(data.head(15))
#data.info()





data_group = data.groupby(["name","year"], as_index = False).mean()
data_sum_to_year = data.groupby("year", as_index = False).sum()

listing = st.sidebar.selectbox("Выберите страницу", ["Графики", "Предсказания"])

if listing == "Графики":
  names = st.sidebar.multiselect("Город выбери", data_group["name"].unique())
  year = st.sidebar.multiselect("Год выбери", data_group["year"].unique())
  new_df = data_group[(data_group["name"].isin(names)) & (data_group["year"].isin(year))]
  #st.write(new_df)
  show_df = st.sidebar.checkbox("Показать таблицу")
  if show_df == True:
      st.subheader("Таблица")
      st.markdown("Дефицит / Профицит бюджета для каждого квартала")
      st.write(new_df)
    
    
  fig = px.line(new_df, x = "year", y = "money", color = "name")
  st.markdown("Общая доля доходов за все года") 
  fig1 = px.pie(data_sum_to_year , values = "money", color = "year")
  fig2 = px.bar(new_df, x = "year", y = "money", color = "name")

  show_fig2 = st.sidebar.checkbox("Показать график баров")
  show_fig1 = st.sidebar.checkbox("Показать диаграмму долей за все года")
  if show_fig2 == True:
      st.subheader("График")
      st.plotly_chart(fig2)
  if show_fig1 == True:
      st.subheader("Диаграмма долей")
      st.plotly_chart(fig1)
  st.plotly_chart(fig)
  #st.pyplot(fig3)


if listing == "Предсказания":
  fig3,ax = plt.subplots()
  name = st.selectbox("Город выбирай", data_group["name"].unique())
  new_data = data_group[data_group["name"].isin([name])]
  number = st.number_input("Введите значение")
  norm = sts.norm(new_data["money"].mean(),np.std(new_data["money"]))
  result = norm.cdf(1 - number)
  st.write(result)
  ax.hist(new_data["money"], density = True, bins = 50)
  st.pyplot(fig3)

# In[ ]:





# In[ ]:




