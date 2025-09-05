from bs4 import BeautifulSoup
import requests 
import re


def get_avg_price_from_divar(query):
    header = {
    "user-agent" : "Mozilla.5.0"
    }
    URL = f"https://divar.ir/s/isfahan?q={query}"

    response = requests.get(URL , headers=header)

    with open("divar.html" , "w" , encoding='utf-8') as f :
        f.write(response.text)

    with open("divar.html" , "r" , encoding='utf-8') as f :
        html = f.read()

    if response.status_code != 200 :
        return None 
    
    soup = BeautifulSoup(html , features="html.parser")

    price_list = []

    items = soup.find_all(name= "div" , class_="kt-post-card__description")

    for item in items :
        text = item.text 
        match = re.search(pattern=r"(\d[\d,]*)\s*تومان" , string= text  )
        if match :
            price_text = match.group(1).replace("," ,"")
        try:
            price = int(price_text)
            price_list.append(price)
        except:
            continue 
        if len(price_list) >= 20 :
            break 
    if not price_list:  #این خط یعنی اگر لیست خالی باشد 
        return None
    
    return round(sum(price_list) / len(price_list))


print(get_avg_price_from_divar(query="لپتاپ"))

