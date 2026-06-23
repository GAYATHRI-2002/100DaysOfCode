from bs4 import BeautifulSoup
import requests

demo_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.in/My-Husbands-Wife-bestselling-Beautiful/dp/1035083019/?_encoding=UTF8&pd_rd_w=hNo5s&content-id=amzn1.sym.7998c9a0-d63d-4775-a557-86e41b560555&pf_rd_p=7998c9a0-d63d-4775-a557-86e41b560555&pf_rd_r=HXWPGDT0SGKAPXQ49P8B&pd_rd_wg=6WQ1y&pd_rd_r=0cabaf39-7d5d-40a8-9867-4d31e8b9eb0b&ref_=pd_hp_d_atf_dealz_cs"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
}

# response = requests.get(demo_url)
response = requests.get(live_url,headers = headers)


soup = BeautifulSoup(response.content, "html.parser")

# price = soup.find(name="span", class_="a-price-whole")
price = soup.find(name="span", class_="a-price-whole")

# print(price.text.strip("."))
if price:
    # Amazon India uses commas for thousands (e.g., 1,299.) - let's strip the dot
    print(price.text.strip("."))
else:
    print("Could not find the price. Amazon might be blocking the request or requiring a CAPTCHA.")
# print(soup.prettify())