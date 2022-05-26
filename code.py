
ans = dict()
racial_slurs = dict()
racial_slurs = {'black':4 ,'racist':2} #I have assumed these to be the racial slurs and give them rating how much they are (effective)

f = open('extracted-tweets.txt',encoding='cp437') #opened my text file which contains tweets


def countingsinn(text):
    degree_of_profanity  = 0 #initialized degree of profanity with zero
    s = text.split(" ")
    for i in s: #for every line,there is check on whether any racial slurs present or not.
        if i in racial_slurs: # if there is any we increament our degree of profanity by one 
            degree_of_profanity  += racial_slurs[i] 
    ans[degree_of_profanity] = s 
    print(ans,end='\n') #degree of profanity will be printed with the tweet

for line in f:#basic loop to pass every single tweet 
    tweet = str(line)
    countingsinn(tweet)


