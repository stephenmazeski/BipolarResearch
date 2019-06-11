# BipolarResearch
## Stephen Robert Mazeski
### Last updated 6/10/2019


Research for Bipolar Disorder

The files within this repository are current statuses of my manipulation of my google data.

PreliminaryML.py is my first attempt at a forecasting/machine learning technique based in sentiment analysis from the other scripts

They are all in standalone format in order for debugging purposes and conservation of memory. There are graphs associated with many of the scripts as well and for that reason I will remain in storing them in standalone here..

Requirements:::

1) Google Takeout data from web history

2) pip install 
    pandas
    matplotlib
    textblob
    numpy
    statmodels
    sklearn
    patsy
    
3) Name of input file must be consistent with how it appears on users personal machine (can alter as long as it is consistent with script)

4) My formatting is currently garbage but it ran before posting it here. I will clean it up as I find free time (Very busy this summer:( )

5) Textblob currently does not have a word bank. That being said, there will be inconsistencies in places where it ranks someones score for their search highly and poorly. This is a relatively easy change and is not my current focus.

6) I have chosen forecasing techniques based on the trends in my data. I found that on different times of the year I had higher scores and lower scores of sentiment based on if I was in school or not. This ARIMA can be changed in the future, however in my mind is the best case now.

6) The MSE I recieved for my personal web browsing history forcasing is MSE= 0.121. This currently is too good to be true, and I am sure there is some bug that is giving me these perfect answers. It is doubtful that any program could acheive a score this well.

