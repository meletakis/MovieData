# MovieData
### Getting movies from themoviedb API and insert them to PostgresSQL

1. Instal required library for PostgreSQL Connection  
 ` pip install psycopg2==2.7 `
 * _WARNING! If the below error shown up execute the next command_  
 Error: You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.  
 ` sudo apt-get install libpq-dev python-dev `

2. Restore database from db folder

3. Set DB/API credentails in .config file

4. Run script:  
 ` python main.py `

**WARNING! Please be sure that you have PostgreSQL version 9.5**
