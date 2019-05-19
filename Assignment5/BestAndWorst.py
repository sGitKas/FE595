# Script that finds the best and worst character of each gender (based on sentiment analysis)
# And  groups them together into the original format of the joke.

# Synopsis
# Best and Worst script will assign a sentiment to each of the sentences and finds the best and the worst characters.


from textblob import TextBlob, Word, Blobber
import fileinput
import pandas as pd

# Create a dataframe to store the obtained sentences and their corresponding sentiment scores
df = pd.DataFrame(columns = ['Sentence', 'Sex', 'sentiment'])

# We need to determine if this description is about a male or a female charecter. Lets write a utility def for that
def findSexFromLine(line):
    if line.find("She's a") != -1:
        return 'F'
    elif line.find("He's a") != -1:
        return 'M'
    else:
        return 'UNKNOWN'

# Lets assign a sentiment score for each sentence using the utlity we just wrote
with open('combined.txt', 'r') as file:
    for line in file:
      #  print(line)
        textBlob= TextBlob(line)
       # print(textBlob.sentiment)
        df=df.append({'Sentence' : line.strip() , 'Sex' : findSexFromLine(line), 'sentiment': textBlob.sentiment.polarity}, ignore_index=True )


# Pandas dataframes allow several analytical actions to be performed on them, such as filtering and grouping.
#Filter for males and sort by sentiment
df_filteredMale = df[df.Sex=='M']
df_filteredMale.sort_values('sentiment', inplace=True, ascending=False)

# The 0 will now have the descrition with the most positive description and the -1 which is the last will have the worst description
dfBestAndWorstMale = df_filteredMale.iloc[[0, -1]]

# Lets see the best and worst male
print(dfBestAndWorstMale)

#Filter for Females and sort by sentiment
df_filteredFemale = df[df.Sex=='F']
df_filteredFemale.sort_values('sentiment', inplace=True, ascending=False)
dfBestAndWorstFemale = df_filteredFemale.iloc[[0, -1]]

# Lets see the best and worst female
print(dfBestAndWorstFemale)

# Group the charectoer into the original format of a joke.
bestMaleAndFemale = dfBestAndWorstMale.iloc[0].Sentence  + " "+ dfBestAndWorstFemale.iloc[0].Sentence +" Together they fight crime."
worstMaleAndFemale = dfBestAndWorstMale.iloc[-1].Sentence  + " "+ dfBestAndWorstFemale.iloc[-1].Sentence+" Together they fight crime."

#Print the results
print("Best Male And Female descriptions = "  +"  "+ bestMaleAndFemale)
print("Worst Male And Female descriptions = "  +"  "+ worstMaleAndFemale)

