import pytumblr
import random

# Authenticate via API Key
client = pytumblr.TumblrRestClient(KEY, SECRET)

# Make the request
wordsArr = []
for index in range(2, 510): #510
    url = client.posts('other-wordly', type='photo', limit=1, offset=index, filter='text')['posts'][0]['photos'][0]['original_size']['url']
    wordsArr.append(url)
