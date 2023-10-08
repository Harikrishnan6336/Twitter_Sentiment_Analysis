import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt

class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        # authenticating
        consumerKey = '#'
        consumerSecret = '#'
        accessToken = '#'
        accessTokenSecret = '#'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        cnt = 0
        
        # input for term to be searched and how many tweets to search
        searchTerm = input("Enter Keyword to search about: ")
        NoOfTerms = 50

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

        # Open/create a file to write(replace w with a for append) data to
        csvFile = open('tweets.csv', 'w')

        # Use csv writer
        csvWriter = csv.writer(csvFile)

        # creating some variables to store info
        polarity = 0
        positive = 0
        spositive = 0
        negative = 0
        snegative = 0
        neutral = 0

        # iterating through tweets fetched
        for tweet in self.tweets:
            
            #Append to temp so that we can store in csv later.Use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later
            cnt=cnt+1
            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.5):
                positive += 1
            elif (analysis.sentiment.polarity > 0.5 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.5 and analysis.sentiment.polarity <= 0):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.5):
                snegative += 1

        #Exit from the program if no tweet is found        
        if(cnt == 0):
            print("There is no tweets mentioning the given keyword.")
            exit()
       # print('The sentiment Analysis results after analysing on '+ str(cnt)  + ' tweets.')
        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        positive = self.percentage(positive, cnt)
        spositive = self.percentage(spositive, cnt)
        negative = self.percentage(negative, cnt)
        snegative = self.percentage(snegative, cnt)
        neutral = self.percentage(neutral, cnt)

        # finding average reaction
        polarity = polarity / cnt

        
        if (polarity == 0):
            senti = "Neutral"
        elif (polarity > 0 and polarity <= 0.5):
            senti = "Positive"
        elif (polarity > 0.5 and polarity <= 1):
            senti = "Strongly Positive"
        elif (polarity > -0.5 and polarity <= 0.0):
            senti = "Negative"
        elif (polarity > -1 and polarity <= -0.5):
            senti = "Strongly Negative"

            # printing out data
        print("General reaction of people on " + searchTerm + " by analyzing " + str(cnt) + " tweets is " + senti)

     
        self.plotPieChart(positive, spositive, negative, snegative, neutral, searchTerm, cnt)

    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        #The first parameter pattern is searched in the third parameter string and is replaced by the second parameter
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return temp


    def plotPieChart(self, positive, spositive, negative, snegative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Strongly Positive [' + str(spositive) + '%]','Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
        sizes = [ spositive,positive, neutral, negative, snegative]
        colors = ['gold','yellow',  'green','red','darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=0)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

def DownloadData(self):
        # authenticating
        consumerKey = '#'
        consumerSecret = '#'
        accessToken = '#'
        accessTokenSecret = '#'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        cnt = 0
        
        # input for term to be searched and how many tweets to search
        searchTerm = input("Enter Keyword to search about: ")
        NoOfTerms = int(input("Enter the number of tweets to analyze: "))  # Prompt for the number of tweets to analyze



if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()

