import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
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


    #plt.hist(times)
            #for b in range(len(times)):
            #    epoch = datetime(1971,1,1)
            #    cookie_datetime = epoch + timedelta(microseconds=times[b])
            #    str(cookie_datetime)
            #    readabletimes.append(parsed['Browser History'][b]['title'])

    #    print(cookie_datetime)




    #print(len(instance))
    #print(instance[0])
#    for p in range(len(instance)):
#        print(instance[p], times[p])

    plt.hist(times, bins = 365, color ='r' )
    print(len(times))
    plt.xlabel('Time in USEC')
    plt.ylabel('Search Frequency Count')
    plt.title('Search Frequency in a Calendar Year')
    plt.show()
        ## Seperate the Google Searches from Web Browser History
        ## Create Frequency Graph with Timestamps
    #keylist = parsed.keys()
    #sorted(keylist)
    #for k in keylist:
#        print(k)
if __name__ =="__main__":
    main()
