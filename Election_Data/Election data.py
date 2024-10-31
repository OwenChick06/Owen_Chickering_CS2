# Owen Chickering
# 10/31/24
# Sources: w3schools, py4e
# Help recieved: Harrison Servedia


import plotly #imports plotly library
import plotly.graph_objects as go
import pandas #imports pandas


fhand = open(r"cleaned_trump_speech_transcript.txt") #opens file for writing

counts = dict() #creates a dictionary called counts
for line in fhand: #for every line in the file
    words = line.split() #split each line into words
    for word in words: #for every word
        if word not in counts: #if word hasnt been counted
            word = word.lower() #lowercase the word
            counts[word] = 1 #set the word count to one
        else: #if the word is already in the library: then
            counts[word] += 1 #adds one to the existing count
for key, value in dict(counts).items(): #for every value in counts
        if value <= 8: #if the value is less than 8
            del counts[key] #delete it 

import plotly.express as px #Imports plotly express library
dictToDF = {"Word" : counts.keys(), "Count": counts.values()} #turns dictionary into "2 dimensional data structure"
fig = px.pie(dictToDF, title='Trump Speech', values="Count", names="Word") #creates the pie chart with set parameters
fig.show() #shows pie chart in your web page