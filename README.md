# webscrapper
Simple application to get sample information from webpages. May be extended for more advanced operations.

* Backend: Python FastAPI
  - list of Python packages into pip-requirements.txt file
* DB: MySQL

# prepare for deployment
* Docker and docker-compose installed
* Environment variables are defined in .env file
* MySQL on default port 3306

to run: `docker-compose up --build -d`

# after deploy
for localhost usage:
* http://localhost:9000 (port may be different based on changes in .env file)
* http://localhost:9000/docs - available nodes (link on main page)