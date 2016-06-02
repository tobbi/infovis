# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

import csv

class Desc:
    
    code = 0
    name = ""    
    
    def __init__(self):
        self.code = 0
        self.name = ""
        
    def parse(self, row):
        i = 0
        while(i < len(row)):
            if i == 0:
                self.code = row[i]
            if i == 1:
                self.name = row[i]
            i += 1

class Cause:
    
    id = 0
    cases = 0
    
    def __init__(self, id, cases):
        self.id = id
        self.cases = cases
    
    def set_id(self, id):
        self.id = id
        
    def set_cases(self, cases):
        self.cases = cases
        
    def get_id(self):
        return self.id
    
    def get_cases(self):
        return self.cases

class Country:

    code = 0
    name = ""    
    
    def __init__(self):
        self.code = 0
        self.name = ""
        
    def parse(self, row):
        i = 0
        while(i < len(row)):
            if i == 0:
                self.code = row[i]
            if i == 1:
                self.name = row[i]
            i += 1
            

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

class Parser:
    
    data_sets = []
    countries = []
    icd_vals = []
    last_num = 0
    last_country = ""
    top_causes = []
    last_year = 0
            
    def get_country(self, code):
        for c in self.countries:
            if c.code == code:
              return c.name
        return ""
        
    def get_icd7(self, code):
        for c in self.icd_vals:
            if "A" + c.code == code:
                return c.name + " (" + c.code + ")"
            if "B" + c.code == code:
                return c.name + " (" + c.code + ")"
            if c.code == code:
                return c.name + " (" + c.code + ")"
        return code

    def parse_countries(self, filename = None):
        if filename is None:
            print("No filename specified. Exiting.")
            return
    
        print("Parsing started...")
        first_row = True
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if first_row:
                    first_row = False
                    continue
                country = Country()
                country.parse(row)
                self.countries.append(country)
                
    def parse_desc(self, filename = None):
        if filename is None:
            print("No filename specified. Exiting.")
            return
    
        print("Parsing started...")
        first_row = True
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if first_row:
                    first_row = False
                    continue
                desc = Desc()
                desc.parse(row)
                self.icd_vals.append(desc)

    def print_top(self):
        pass       
    
    def add_cause(self, cause):
        for c in self.top_causes:
            if c.cases > cause.cases:
                continue
            #print c.name
    
    def parse(self, filename = None):
        if filename is None:
            print("No filename specified. Exiting.")
            return
    
        print("Parsing started...")
        first_row = True
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if first_row:
                    first_row = False
                    continue
                dataset = DataSet()
                dataset.parse(row)
                self.data_sets.append(dataset)
#                print("Total deaths in %s for %s from %s for gender %s: %s"
#                % (str(dataset.get_year()),
#                   str(self.get_country(dataset.get_country())),
#                   str(self.get_icd7(dataset.get_cause())),
#                   str(dataset.get_gender()),
#                   str(dataset.get_total_deaths())))

                #print(dataset.get_year())
                if (dataset.get_country() != self.last_country) \
                or (dataset.get_year()    != self.last_year):

                    for c in self.top_causes:
                        print("%s: %s (%s cases)"
                            % (self.last_year,
                               self.get_icd7(c.get_id()),
                               c.get_cases()))
                    if dataset.get_country() != self.last_country \
                       or self.last_country == "":

                        print("###################################")
                        print(self.get_country(dataset.get_country()) + ":")
                        print("###################################")
                        self.last_country = dataset.get_country()
                    self.last_year = dataset.get_year()
                    self.last_num = 0
                    self.top_causes = []
                
                if dataset.get_total_deaths() > self.last_num:
                    cause = dataset.get_cause()
                    if cause != "B000" and cause != "A000":
                        self.last_num = dataset.get_total_deaths()
                        self.top_causes.append(Cause(cause, self.last_num))
                        
        for c in self.top_causes:
            print("%s: %s (%s cases)"
                    % (self.last_year,
                       self.get_icd7(c.get_id()),
                       c.get_cases()))
                # Country,Admin1,SubDiv,Year,List,Cause,Sex,Frmat,IM_Frmat,Deaths1,Deaths2,Deaths3,Deaths4,Deaths5,Deaths6,Deaths7,Deaths8,Deaths9,Deaths10,Deaths11,Deaths12,Deaths13,Deaths14,Deaths15,Deaths16,Deaths17,Deaths18,Deaths19,Deaths20,Deaths21,Deaths22,Deaths23,Deaths24,Deaths25,Deaths26,IM_Deaths1,IM_Deaths2,IM_Deaths3,IM_Deaths4
    


p = Parser();
p.parse_countries("country_codes")
p.parse_desc("icd7_desc")
p.parse("MortIcd7");