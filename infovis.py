# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:25:49 2016

@author: tobiasmarkus
"""
#from parser import *
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_total(dataset):
    dataset["total_deaths"] = dataset.loc[:, 'Deaths1':'IM_Deaths4'].sum(axis=1)
    
def sanitize(dataset):
    dataset = dataset.ix[(dataset.total_deaths > 0)] # Sanitize data
    return dataset    
    
def icd_version(dataset, version):
    print("Setting ICD version %s to dataset..." % version)
    dataset["icd_version"] = version

def query(dataset, year, country, gender):
    d = dataset
    if(country != None):
        d = d.ix[(d.Country == country)]
    if(year != None):
        d = d.ix[(d.Year == year)]
    if(gender != None):
        d = d.ix[(d.Sex == gender)]
        
    d = d.ix[(d.total_deaths > 0)]
    d = d.ix[(d.Cause != "A000") & (d.Cause != "B00") & (d.Cause != "AAA")] # Filter data set
    d = d.sort_values(["Country", "Year", "total_deaths"], ascending=False) # Sort data set
    #d = d.head(10) # First 10 rows
    #print(d.loc[:, ("Country", "Year", "Cause", "total_deaths")])
    #print()
    return d
    
def parse_old():
    from parser import Parser
    p = Parser();
    p.parse_countries("country_codes")
    p.parse_desc("icd7_desc")
    p.parse("MortIcd7");
    p.parse("MortIcd8");
    p.parse("MortIcd9");
    p.parse("MortIcd10_part1")
    p.parse("MortIcd10_part2")
    
def aggregate():
    print("Reading ICD7...")
    icd7 = pd.read_csv("MortIcd7")
    icd_version(icd7, 7)
    print("Reading ICD8...")
    icd8 = pd.read_csv("Morticd8")
    icd_version(icd8, 8)
    print("Reading ICD9...")
    icd9 = pd.read_csv("MortIcd9")
    icd_version(icd9, 9)
    print("Reading ICD10 part 1...")
    icd10_1 = pd.read_csv("Morticd10_part1")
    icd_version(icd10_1, 10)
    print("Reading ICD10 part 2...")
    icd10_2 = pd.read_csv("Morticd10_part2")
    icd_version(icd10_2, 10)
    print("Concatenating...")
    total = pd.concat([icd7, icd8, icd9, icd10_1, icd10_2])
    print("Calculating totals...")
    calculate_total(total)
    print("Sanitizing...")
    total = sanitize(total)
    print("Saving CSV...")
    total.to_csv("total.csv")
    
def split_into_countries(dataset, country):
    d = dataset
    d = d.ix[(d.Country == country)]
    d.to_csv("datasets/%s.csv" % country)
    
def read_and_display():
    print("Reading total...")
    countries = pd.read_csv("country_codes")
    death_stats = pd.read_csv("total.csv")

    # 1125 = Deutschland
    print("Querying...")
    result = query(death_stats, None, 2010, 1)
    result = result.sort_values(["Year", "total_deaths"], ascending=[True, False])

    #print(result.loc[:, ("Country", "Year", "Cause", "total_deaths")])
    #countries = something.sort_values("Country", ascending=False)[:10]

    print("Sanitizing...")
    #result = result.ix[(result.total_deaths > 10000)]
    #result = result.head(1000)
    
    sns.set_style("darkgrid")
    #bar_plot = sns.barplot(x=result["Cause"], y=result["total_deaths"],
    #                        palette="muted")
    
    #sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
    #              palette={"male": "g", "female": "m"},
    #              markers=["^", "o"], linestyles=["-", "--"]);

    sns.factorplot(x="Year", y="total_deaths", hue="Cause", data=result, capsize=.2, legend_out=True, size=50, col="Country")
    plt.xticks(rotation=90)
    plt.show()

#aggregate()
read_and_display()