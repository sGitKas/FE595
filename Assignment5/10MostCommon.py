#Script that finds the 10 most common descriptions for characters.

# Synopsis
# 10MostCOmmon script will group the sentences together and see if there is any pattern in the characters.


from textblob import TextBlob, Word, Blobber
import fileinput
import pandas as pd

df = pd.DataFrame(columns = ['Sentence', 'Sex', 'sentiment'])

def findSexFromLine(line):
    if line.find("She's a") != -1:
        return 'F'
    elif line.find("He's a") != -1:
        return 'M'
    else:
        return 'UNKNOWN'

# Lets assign a sentiment score for each sentence
with open('combined.txt', 'r') as file:
    for line in file:
      #  print(line)
        textBlob= TextBlob(line)
       # print(textBlob.sentiment)
        df=df.append({'Sentence' : line.strip() , 'Sex' : findSexFromLine(line), 'sentiment': textBlob.sentiment.polarity}, ignore_index=True )


grouped_sentences= df.groupby('Sentence').count()

common_sentences = grouped_sentences.sort_values('sentiment', ascending=False)
TenMostCommonCharacters= common_sentences .head(10)
print(TenMostCommonCharacters)

# We see from above that the characters are all completely unique but for the two copies of charecter we seem to have in the files.

# so lets create a new column and just look at the third work describing the charecter and find the most common third word
#new dataframe to hold the split data. 3 here the first n spaces to split by
new = df["Sentence"].str.split(" ", n=3, expand=True)

# making separate third word column from new data frame
df["ThirdWord"] = new[2]
grouped_Third_data = df.groupby('ThirdWord').count()

CommonThird = grouped_Third_data.sort_values('sentiment', ascending=False)
TenMostCommonThird = CommonThird.head(10)

# now we can see the most commonly used charecter descriptions
print(TenMostCommonThird)

