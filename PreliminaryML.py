import json
from pandas import datetime
from matplotlib import pyplot
from textblob import TextBlob, Word
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
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
    for t in range(len(instance)):
#    print(instance[1550])
        placeholder = str(instance[t])
        #print(placeholder)
        textvar = TextBlob(placeholder)
        #correctspell = placeholder.correct()

    #print(testvar)
        if textvar.sentiment.polarity != 0.0:
            polarityarray.append(textvar.sentiment.polarity)

    X = polarityarray

    size = int(len(X) * 0.66)

    train, test = X[0:size], X[size:len(X)]

    history = [x for x in train]

    predictions = list()

    for t in range(len(test)):

        model = ARIMA(history, order=(2,1,0))

        model_fit = model.fit(disp=0)

#    print(model_fit.summary())

        output = model_fit.forecast()

        yhat = output[0]

        predictions.append(yhat)

        obs = test[t]

        history.append(obs)

        #print('predicted=%f, expected =%f' % (yhat,obs))



    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)

    pyplot.plot(test)

    pyplot.plot(predictions, color='red')



    pyplot.show()

    #y = [MoYrArray, CountArray]

#    plt.scatter(MoYrArray, CountArray, s =4, c ='b', label = 'Test')



#    plt.show()













    #for i in range(len(Rated)):
        ## Seperate the Google Searches from Web Browser History
        ## Create Frequency Graph with Timestamps
    #keylist = parsed.keys()
    #sorted(keylist)
    #for k in keylist:
#        print(k)
if __name__ =="__main__":
    main()
