### visualization
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
#import multipolyfit as mpf

#%matplotlib inline


def main():
    with open(r"BrowserData.json", encoding='utf-8') as f:
        parsed = json.loads(f.read())
        #print(parsed)
    #    for b in parsed:
    #         time = parsed.get("time_usec")

    whole=[]
    for x in range(len(parsed['Browser History'])):
        #print(type(parsed['Browser History'][x]['time_usec']))
        whole.append(parsed['Browser History'][x]['title'])

    instance = []
    for t in range(len(parsed['Browser History'])):
        if whole[t].find("Google Search") == -1:
            continue
        else:
            instance.append(parsed['Browser History'][t]['title'])

    times = []
    readabletimes = []



    for t in range(len(parsed['Browser History'])):
        if whole[t].find("Google Search") == -1:
            continue
        else:
            times.append(parsed['Browser History'][t]['time_usec'])


    polarityarray = []
    polaritytime = []
    for t in range(len(instance)):
#    print(instance[1550])
        placeholder = str(instance[t])
        #print(placeholder)
        testvar = TextBlob(placeholder)
    #print(testvar)
        if testvar.sentiment.polarity != 0.0:
            polarityarray.append(testvar.sentiment.polarity)
            polaritytime.append(times[t])
#    for a in range(len(polaritytime)):
#        print(polarityarray[a],polaritytime[a])

    color_lis=[]
    for x in polarityarray:
        if x>0: color_lis.append(1)
        else:  color_lis.append(0)
#    X = polaritytime.values.reshape(-1, 1)
#    Y = polarityarray.values.reshape(-1, 1)
#    linear_regressor = LinearRegression()  # create object for the class
#    linear_regressor.fit(polaritytime, polarityarray)
    plt.scatter(polaritytime, polarityarray, label='skitscat', c=color_lis,cmap= plt.cm.RdYlGn ,  s = 10)
    plt.xlabel('Time in USEC')
    plt.ylabel('Polarity of Search')
    plt.title('Search Polarity History')
    plt.plot(polaritytime,polarityarray, color='black')
    plt.show()

            #print(placeholder)
            #print(testvar.sentiment)
            #print(testvar.sentiment.polarity)
    #print(type(placeholder))

if __name__ == "__main__":
    main()
