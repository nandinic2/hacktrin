import json, requests
url = "https://newsapi.org/v2/everything?q=women%20empowerment&from=2019-03-03&sortBy=popularity&apiKey=daa824d68c6d40ad906270db91cd405f"
data = requests.get(url).json()

def call(data):
    count = -1
    titles = []
    links = []
    for n in data["articles"]:
        headline = n["title"]
        titles.append(headline)
        link = n['url']
        links.append(link)
    for n in titles:
        return titles
    for n in links:
        return links


    # for n in images:
    #     length -=1
    #     total.append(images[length])

#print(call(data))
