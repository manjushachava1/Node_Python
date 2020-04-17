# Python program to read 
# json file  
import json 
  
# Opening JSON file 
f = open('countries.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in data: 
    print(i['name'])
  
# Closing file 
f.close() 
