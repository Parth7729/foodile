import requests
from bs4 import BeautifulSoup as bs


def getRestaurants(city, food):

    url = 'https://www.zomato.com/'+city+'/restaurants/'+food
    # url  = "https://www.swiggy.com/dapi/restaurants/search/v3?lat=26.8466937&lng=80.94616599999999&str=burger&trackingId=undefined&submitAction=ENTER&queryUniqueId=9bb24f7d-95a2-c284-6e83-e3a2fea98fd7"

    allRestaurants = {'restaurants' : []}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

    for i in range(1,3):

        page = requests.get(url+f'?category={i}', headers=headers)
        soup = bs(page.content, 'lxml')

        for item in soup.find_all('div', {'class':'jumbo-tracker'}):
            res = {}
            divs = item.find_all('a')[1].find_all('div', recursive=False)
            res['name'] = divs[0].find('h4').text
            res['food_items'] = divs[1].find_all('p')[0].text.split(',')
            res['price'] = divs[1].find_all('p')[1].text
            res['link'] = 'https://www.zomato.com'+item.find('a')['href']
            # res.append(item.find('img', {'class':'fyZwWD'}))

            allRestaurants['restaurants'].append(res)

    return allRestaurants
        
    print(allRestaurants)

