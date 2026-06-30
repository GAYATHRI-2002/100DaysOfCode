from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://www.amazon.in/")
driver.get("https://www.amazon.in/Girl-Glass-Case-girls-safer/dp/0143454374/?_encoding=UTF8&pd_rd_w=bAok9&content-id=amzn1.sym.7998c9a0-d63d-4775-a557-86e41b560555&pf_rd_p=7998c9a0-d63d-4775-a557-86e41b560555&pf_rd_r=TM77QVDM9MQ9RFSSW9Z8&pd_rd_wg=jFdw5&pd_rd_r=1b5b90cd-3323-4e55-8b79-2822c5f077ec&ref_=pd_hp_d_atf_dealz_cs")
# driver.close()
book_price = driver.find_element(By.CLASS_NAME, value="a-price-whole" )
print(f"The price of the book is {book_price.text}")
driver.quit()