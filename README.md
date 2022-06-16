By Madhava Krishna

# Important

 Due to the maximum size of submission on Internshala, I had to remove the models for the binary classifier and the datasets for the time series. The former can be obtained after running the the script, but the <b>latter requires running all of the scripts in the 'web_scrape' subdirectory inside the 'Time Series' directory.</b>

# Introduction

Option 1 was chosen for task 1 and option 2 was chosen for task 2.


The directory structure is as follows:

1. Time Series: for task 1, wherein investing.com had to be scraped for data. This directory has 
    a) datasets, b) web_scrape, c) modeling.ipynb
    <br>'datasets' is a directory which contains all the scraped data in a csv format.
    <br> 'web_scrape' contains scripts for scraping the required data from Investing.com
    <br>'modeling.ipynb' has an implementation of a network for predicting the prices of BTC, which was chosen as the dependent variable.

    A brief overview of what had been done:
    The web_scrape directory contains a 'url_to_csv' module, which contains a class for making it easier to extract data from Investing.com. It requires 6 arguments: the url (which will be set to a default value in Investing.com if supplied None), the starting date, the ending date, the header tag (for the POSt method), the path of the directory to which the csv will be saved, and a unique ID which is used to derive the asset from Investing.com.

    Object-oriented programming practices were followed to create the class.

    All the script files use the same class to do their work and the datasets are saved in the 'datasets' directory.

    Each script file extracts data from 1 January, 2020 to 15 June, 2022.

    The modeling.ipynb uses the datasets and appends the Prices (only the Price column) to one main dataframe, then feeds it into a LSTM network to make predictions about BTC price. The features were chosen to be 'aluminium', 'copper', 'crude-oil', 'gold', 'natural-gas', 'sugar' and 'wheat'. The reason for the choice of these variables is to determine if increasing rate of daily commodities like crude-oil, natural-gas, sugar and wheat influences the buyers decision to hold crypto assets like BTC, and if metals like Copper, Aluminum which are used for manufacturing graphics cards, which are heavily used for mining purposes (not BTC, but could quite possibly be used in ASICs). And gold, since it is a precious metal and many people resort to it as a store of value.
    

    Given more time and resources, I would first try to get more knowledge about time series data and ways for modeling them. This was my first implementation of any time series model and despite having copied a lot of data from online sources (sources in the "Credits" section), I am absorbing substantial information from this time-limited challenge.

    I would try to incorporate more features and a lot more data points, if the above condition were satisfied.


2. binary classifier: for the second task, creating a binary classifier for classifying a project to be 'closed' or 'cancelled/distressed'. The Python notebook is named 'classifier.ipynb'. First, logistic regression was tried, which gave an accuracy of 86% on the training set. Then, a convolutional neural network was tested, which resulted in an accuracy of ~91% on the training set and ~91% on the validation set. The training only occurred on the numerical portion of the data and the textual data was left untouched (could possibly use it after text processing and employing ensemble learning to increase the accuracy of the network). 
    
    Dropout was used to reduce overfitting and activation functions were chosen to yield maximum accuracy with minimum time taken for training.





# Credits
    I am new to web-scraping and this was the first time I had attempted it. I am extremely thankful to Taiyo for providing me an opportunity to learn it. I must give due credit to Stackoverflow, in this <a href = "https://stackoverflow.com/questions/53890493/scraping-data-from-investing-com-for-btc-eth-using-beautifulsoup"> post</a>, which clarified how POST and GET methods work.
    Credits to Krish Naik's YouTube channel for information about LSTM networks. This was my first time implementing a time series prediction network.