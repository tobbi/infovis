# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class DataSet:
    
    country = 0
    admin1 = None
    SubDiv = None
    Year = 0
    List = None
    Cause = None
    Sex = 0
    Frmat = 0
    IM_Frmat = 0  
    Deaths = []
    
    def __init__(self):
        # Country,Admin1,SubDiv,Year,List,Cause,Sex,Frmat,IM_Frmat,Deaths1,Deaths2,Deaths3,Deaths4,Deaths5,Deaths6,Deaths7,Deaths8,Deaths9,Deaths10,Deaths11,Deaths12,Deaths13,Deaths14,Deaths15,Deaths16,Deaths17,Deaths18,Deaths19,Deaths20,Deaths21,Deaths22,Deaths23,Deaths24,Deaths25,Deaths26,IM_Deaths1,IM_Deaths2,IM_Deaths3,IM_Deaths4
        self.country = 0
        self.admin1 = None
        self.SubDiv = None
        self.Year = 0
        self.List = None
        self.Cause = None
        self.Sex = 0
        self.Frmat = 0
        self.IM_Frmat = 0  
        self.Deaths = []      
    
    def parse(self, row):
        i = 0
        while(i < len(row)):
            if i == 0:
                self.country = row[i]
            if i == 1:
                self.admin1 = row[i]
            if i == 2:
                self.SubDiv = row[i]
            if i == 3:
                self.Year = row[i]
            if i == 4:
                self.List = row[i]
            if i == 5:
                self.Cause = row[i]
            if i == 6:
                self.Sex = int(row[i])
            if i == 7:
                self.Frmat = row[i]
            if i == 8:
                self.IM_Frmat = row[i]
            
            if i > 8:
                self.Deaths.append(row[i])
            i += 1
            
    def get_total_deaths(self):
        total = 0
        for val in self.Deaths:
            if val == '':
                continue
            total += int(val)
        return total
        
    def get_country(self):
        return self.country
        
    def get_cause(self):
        return self.Cause
        
    def get_year(self):
        return self.Year
    
    def get_gender(self):
        if self.Sex == 1:
            return "male"
        return "female"
    
    def __str__(self):
        return "String representation of krams"
