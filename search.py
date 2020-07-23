# if 'google' in query:
    # speak('Searching google...')
from googlesearch import search
try: 
    # except ImportError: 
        # print("No module named 'google' found") 
    # to search 
    # query = query.replace("google", "")
     query = "Geeksforgeeks"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 