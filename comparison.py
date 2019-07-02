import requests,json
import datetime
import os

query_list = ['Elizabeth Warren','Karmala Harris','Bernie Sanders','Joe Biden']
# #track results from the us headlines
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=249c9841b86f429fb5978c351097bf08')
# response = requests.get(url)
# print response.json()

# #track results from specific news source (e.g. bbc)
# url = ('https://newsapi.org/v2/top-headlines?'
#        'sources=bbc-news&'
#        'apiKey=249c9841b86f429fb5978c351097bf08')
# response = requests.get(url)
# print response.json()

#track results from specific keyword 

#Jane's Key
path = os.getcwd()  
today = datetime.datetime.now().strftime('%Y-%m-%d')
if not os.path.exists('top_stories_results'):
   os.makedirs('top_stories_results')
for name in query_list:
   url = ('https://newsapi.org/v2/everything?'
       'q='+ name + '&'
       'from='+today+'&'
       'pageSize=100&'
       'sortBy=popularity&'
       'page=1&'
       'apiKey=249c9841b86f429fb5978c351097bf08'
       )
   response = requests.get(url).json()
   with open(os.path.join(path,'top_stories_results',name+'-'+today),'w') as f:
      json.dump(response,f)
       

# #Funing's key
# url_page2 = ('https://newsapi.org/v2/everything?'
#        'q='+ query_phrase + '&'
#        'from=2019-06-23&'
#         'pageSize=100&'
#        'sortBy=popularity&'
#        'page=2&'
#         'apiKey=f5cfd03ab89c4b1aa95f36c2ea5c2d8e'
#        )
#different date
# url3 = ('https://newsapi.org/v2/everything?'
#        'q='+ query_phrase + '&'
#        'from=2019-06-25&'
#        'pageSize=100&'
#        'sortBy=popularity&'
#        'page=1&'
#         'apiKey=249c9841b86f429fb5978c351097bf08'
#        )



#print (response)



#headlines_json = r.json 

#grab headline urls
#headline_dict = []
#for i in range(headlines_json['totalResults']):
#    headline_urls.append(headlines_json['articles'][i]['url'])
