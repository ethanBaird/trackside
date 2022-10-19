# trackside

A full stack flask application that allows a user to track formula 1 results.

## Contents 

* [Video](#video)
* [Technologies](#technologies)
* [Brief](#brief)
* [Installation](#installation)

<br>


## Video



https://user-images.githubusercontent.com/106377635/196726157-6d888abc-6b93-4275-a956-56b762c8cf1c.mp4



<br>


## Technologies

These are the main technologies we used to contruct the project.

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
* ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
* ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
* ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

<br>


## Brief

After 4 weeks at CodeClan we undertook our first project. Working independently we were to create a flask application that allows a user to perform simple CRUD actions. I decided to work to design a sports scoring tracker for Formula 1, following this brief.

**MVP**

A user should be able to:

- [x] view drivers, teams and some information about them
- [x] view race results and see season results for a particular driver
- [x] view the current season standings


**Extensions**

Some of the features currently in progress:

- [x] the user should be able to add race results
- [x] all relevant information should update when a race result is submitted

I've decided not to continue devloping this application. Purely for nostalgia reasons. I think that in years to come I'm going to watn to spin this up and remember what life was like when I was only a little code baby. At current I'm immensely proud that I was able to build this application with only 4 weeks coding experience!


<br>


## Installation

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
