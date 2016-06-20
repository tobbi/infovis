# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:16:41 2016

@author: tobiasmarkus
"""

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