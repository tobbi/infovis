# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:19:01 2016

@author: tobiasmarkus
"""

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
