# Containerized scraping service

An ETL tool based on [facebook-page-scraper](https://github.com/shaikhsajid1111/facebook_page_scraper) which is coded in python and selenium, Fastapi, MySQL and containerised with docker 🐳. 

The fastapi app and MySql database are hosted on different containers for failover and fault-tolerance reasons. the two docker containers are connected with bridge network.

The images and their respective containers were built using `docker-compose up` 🐙.

## Description 
1. Scraper accesses the public desired Facebook page through Chrome browser.
2. Collects the data from the desired number of posts (page_name, shares, reaction counts, comments, content, posts_date).
3. Accesses the database as a non-root user with granted privileged permissions to create and modify any Database in MySQL server.
4. Create the database if it doesn’t exist, create the table, insert the data in columns.

## Getting Started
* set up local virtual environment.
  installing requirements
  python 3.11 and pip3
  ````
  facebook-page-scraper
  webdriver-manager
  fastapi
  ````
  docker desktop and VScode
## Testing
* on local environment
  ````
  git clone https://github.com/Sahar-DataScience/scrapping-facebook
  cd scrapping-facebook
  uvicorn app.main:app --reload
  ````
  then access `http://127.0.0.1:8000/docs#/default/scrape_scrape_post` and add inputs on test_input.sh
* containerization
    ````
    git clone https://github.com/Sahar-DataScience/scrapping-facebook.git
    cd scrapping-facebook
    docker-compose up
    ````
## Results
<p align='center'>
<img src='https://github.com/Sahar-DataScience/scrapping-facebook/blob/main/doc/input_test.png' width='40%'/>
<img src='https://github.com/Sahar-DataScience/scrapping-facebook/blob/main/doc/200.png' width='70%'/>
<img src='https://github.com/Sahar-DataScience/scrapping-facebook/blob/main/doc/db.png' width='45%'/>
<img src='https://github.com/Sahar-DataScience/scrapping-facebook/blob/main/doc/columns.png' width='45%'/>
</p>



> [!WARNING]
> inside the app container, the scraper couldn't open chrome browser (or any other browser) although chrome web driver installed and the docker base image was pulled from selenium-standalone-chrome [check this](https://github.com/Sahar-DataScience/scrapping-facebook/blob/main/doc/500.png)

## Troubleshooting issues 🎯
* https://stackoverflow.com/questions/47955548/docker-image-with-python3-chromedriver-chrome-selenium
* https://stackoverflow.com/questions/29781266/docker-using-container-with-headless-selenium-chromedriver?rq=4
* https://stackoverflow.com/questions/71311507/modulenotfounderror-no-module-named-app-fastapi-docker
* https://stackoverflow.com/questions/38504257/mysql-scripts-in-docker-entrypoint-initdb-are-not-executed
  
> [!TIP]
> * further enhancements can be applied like hiding credentials in .gitignore and .dockerignore.
> * enhancing the schemas of the database.
> * using multistage build to lightweight the containers.
> * deploy the service on cloud with cron job that makes it work every 24h for example.

## Resources 📚
* https://fastapi.tiangolo.com/deployment/docker/
* https://hub.docker.com/_/mysql
* https://medium.com/@Aramayis12/docker-without-docker-compose-a8b18bf92cc6
* https://stackoverflow.com/questions/41768157/how-to-link-containers-in-docker
* Gimini google 
