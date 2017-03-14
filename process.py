#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re

# read the file's name and append '.srt'
file_Name = sys.argv[1]
if file_Name.find(".srt") == -1:
    file_Name += ".srt"

def check_contain_english(check_str):
    for en in check_str:
         if re.search('^[a-zA-Z]+$', en):
            return True
    return False

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# process the file
with open(file_Name,"r") as f:
    with open("new_" + file_Name,"w") as new_f:
        for line in f.readlines():
            if check_contain_english(line) and not check_contain_chinese(line):
                continue
            else:
                new_f.write(line)
