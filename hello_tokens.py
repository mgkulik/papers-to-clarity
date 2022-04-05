#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:24:49 2022

@author: magoncal
"""

import nltk
import os, re

#/home/magoncal/Documents/data/papers/lab_papers/lab_text/
path_to_files = input('Add the path where the papers are available as ".TXT": ')
files = sorted([f.path for f in os.scandir(path_to_files) if (re.search(r'\W*.txt', f.path))])
for comp in files:
    data = open(comp, 'r').read()
    main_subs = ["abstract", "introduction", "materiais*methods", "results*discussion"]
    r'(?<={0})(.*?)(?={1})'
    for row in data:
        row_main_subs = [(m.start(0), m.end(0)) for m in re.finditer(r'\b({0})\b'.format("abstract"), row)]
        
        bool(re.search(r'\b({0})\b'.format("abstract"), row.lower()))
    row_main_subs = [i for i, item in enumerate(fruit_list) if re.search('berry$', item)]
    
    [re.search(r'\b({0})\b'.format(word) for word in main_subs val for val in data 

               