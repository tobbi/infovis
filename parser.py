# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

import csv
import numpy
from desc import Desc
from cause import Cause
from country import Country
from dataset import DataSet            


class Parser:
    
    data_sets = []
    countries = []
    icd_vals = []
    last_num = 0
    last_country = ""
    top_causes = []
    last_year = 0
    ignore_causes = ["B000", "A000", "B00", "C001"]
    datasets = [] # country, year, causes
            
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
                self.datasets.append([])
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
                        print("%s: %s (%s cases) -> %s"
                            % (self.last_year,
                               self.get_icd7(c.get_id()),
                               c.get_cases(), c.get_id()))
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
                    if not cause in self.ignore_causes:
                        #self.datasets[dataset.get_country()][dataset.get_year()]\
                        #    .append(Cause(cause, self.last_num))
                        self.last_num = dataset.get_total_deaths()
                        self.top_causes.append(Cause(cause, self.last_num))
                        
        for c in self.top_causes:
            print("%s: %s (%s cases)"
                    % (self.last_year,
                       self.get_icd7(c.get_id()),
                       c.get_cases()))
    


