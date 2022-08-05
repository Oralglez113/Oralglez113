#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


pip install beautifulsoup4


# In[22]:


import requests
from bs4 import BeautifulSoup

def stock_price(symbol: str = ("")) -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px) W(100%)"
    return soup.find("div", class_=class_).find("fin-streamer").text

def var_price(symbol: str = ("")) -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px) W(100%)"
    return soup.find("div", class_=class_).find("span").text

print("Ticker")
ticker= input()


if __name__ == "__main__":
    for symbol in ticker.split():
        print(f"Current {symbol:<1} stock price is {stock_price(symbol):>10}")
        
if __name__ == "__main__":
    for symbol in ticker.split():
        print(f"Current {symbol:<1} var price is {var_price(symbol):>10}")


# In[ ]:




