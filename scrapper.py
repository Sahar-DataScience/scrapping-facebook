#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper
import json
import mysql.connector

#scrapper inputs
page_name = "AIatMeta"
posts_count = 5
browser = "chrome"
#proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
proxy = None
timeout = 60 #600 seconds
headless = False
#DB credentials
host_name = 'localhost'
user_name = 'asus'
password_db = "12345"
meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

json_data = meta_ai.scrap_to_json()

data_dict = json.loads(json_data)


scrapped_db = mysql.connector.connect(
  host=host_name,  
  user=user_name,  
  password=password_db 
)

mycursor = scrapped_db.cursor()


sql = "CREATE DATABASE IF NOT EXISTS facebook_db"  
mycursor.execute(sql)


scrapped_db = mysql.connector.connect(
  host=host_name,
  user=user_name,
  password=password_db,
  database="facebook_db"  
)
mycursor = scrapped_db.cursor()

sql = "CREATE TABLE IF NOT EXISTS fb_page ( \
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
        page_name VARCHAR(255) NOT NULL, \
        shares_count INT DEFAULT 0, \
        comments_count INT DEFAULT 0, \
        post_content TEXT, \
        post_date DATE NOT NULL \
        )"
mycursor.execute(sql)

for item_ in data_dict:
    page_name = data_dict[item_]['name']
    shares_count = data_dict[item_]['shares']
    comments_count = data_dict[item_]['comments']
    post_content = data_dict[item_]['content']
    post_date = data_dict[item_]['posted_on']
    
    sql = "INSERT INTO fb_page (page_name, shares_count, comments_count, post_content, post_date) VALUES (%s, %s, %s, %s, %s)"
    values = [
      (page_name, shares_count, comments_count, post_content, post_date)
    ]
    mycursor.executemany(sql, values)

scrapped_db.commit()  

scrapped_db.close()
