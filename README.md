# formula_1_app
F1 flask app

# Getting Started



To build the database strucutre and seed with starter data run

```bash
createdb formula_1
psql -d formula_1 -f db/formula_1.sql
python3 seed.py
```

To run the app: 

```bash
flask run
```

Then visit http://localhost:5000 to view the app. 

Race results for the first race of the season have been seeded, more can be added in the race results pages.

