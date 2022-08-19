#trackside
F1 flask app

After 4 weeks at CodeClan we undertook our first project. Working independently we were to create a flask application that allows a user to perform simple CRUD actions. I decided to work to design a sports scoring tracker for Formula 1, following this brief.

##MVP

the app should allow the user to view drivers, teams and some information about them
there should be a way to display race results and see season results for a particular driver
the app should display the current standings

##Extensions
the user should be able to add race results
all relevant information should update when a race result is submitted

What follows are instructions on how to run this application

#Try it yourself!

You'll need python3, postgreSQL and flask installed to run this.

To build the database strucutre and seed with starter data run the following in your CLI

```bash
createdb formula_1
psql -d formula_1 -f db/formula_1.sql
python3 seed.py
```

Then to run the app: 

```bash
flask run
```

Then visit http://127.0.0.1:5000/ to view the app. 

Race results for the first race of the season have been seeded, more can be added in the race results pages.

