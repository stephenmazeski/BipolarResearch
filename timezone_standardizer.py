import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob
import pandas as pd
#from sklearn import cross_validation
from pytz import timezone
import pytz
from tzwhere import tzwhere

tz = tzwhere.tzwhere()

def main():
    with open(r"C:\Users\steph\Desktop\Research\Location History.json", encoding='utf-8') as f:
        parsed = json.loads(f.read())
        #print(parsed)
    #    for b in parsed:
    #         time = parsed.get("time_usec")

    latitude7=[]
    longitude7 = []
    for x in range(len(parsed['locations'])):
        #print(type(parsed['Browser History'][x]['time_usec']))
        latitude7.append(parsed['locations'][x]['latitudeE7'])
        longitude7.append(parsed['locations'][x]['longitudeE7'])

    latitudeNORM=[]
    longitudeNORM = []

    for t in range(len(latitude7)):
        latitudeNORM.append(latitude7[t]/10**7)
        longitudeNORM.append(longitude7[t]/10**7)
    locations = []

    for i in range(len(latitudeNORM)):
        locations.append(tz.tzNameAt(longitudeNORM[i],latitudeNORM[i]))

    for i in range(len(locations)):
        print(locations[i])



if __name__ == "__main__":
    main()
