#Topic - We have to restrict the news ticker to 140 characters
#coded by-Hemant Ingle


headlines = ["Local man Eaten by bear",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Fireman Rescues cat Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"] # this is the news string provided

news_ticker = "" #we create an empty  list to make a new string
for headline in headlines: # use of for loop to iterate through each headline
    news_ticker += headline + ">>>>>" # add the news elements to news_ticker list
    #print(news_ticker)
    if len(news_ticker) >= 140: # if  the length of news_ticker is greater than 140 then execute the loop below
        news_ticker = news_ticker[:140] # new news ticker variable will crop the list and limit it to 140 characters
        #break # break this loop

print(news_ticker) #print the result
#Thanks for watching
