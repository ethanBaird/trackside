from flask import Flask, Blueprint, redirect, render_template, request

from models.race import Race
from models.result import Result
import repositories.races_repository as races_repository
import repositories.drivers_repository as drivers_repository
import repositories.scores_repository as scores_repository
import repositories.results_repository as results_repository
import repositories.constructors_repository as constructors_repository

results_blueprint = Blueprint('results', __name__)

# new '/races/new'
@results_blueprint.route('/results/new')
def new():
    races = races_repository.select_all()
    scores = scores_repository.select_all()
    drivers = drivers_repository.select_all()
    return render_template('results/new.html', races=races, drivers=drivers, scores=scores)

# create '/results/new' method=['POST']
@results_blueprint.route('/results/new', methods=['POST'])
def create():
    # gets race details from form
    id = request.form['race_id']
    race = races_repository.select(id)
    # gets scoring info from scores table
    scores = scores_repository.select_all()
    # for each possible score outcome creates and saves a result
    position = 1
    for score in scores:
        driver_id = request.form[f'p{position}']
        driver = drivers_repository.select(driver_id)
        result = Result(score, driver, driver.constructor, race)
        results_repository.save(result)
        position += 1
    return redirect('/races')

# standings
@results_blueprint.route('/standings')
def standings():
    positions = range(1, 20)
    drivers = drivers_repository.select_all()
    drivers.sort(key=lambda x: x.points, reverse=True)
    constructors = constructors_repository.select_all()
    constructors.sort(key=lambda x: x.points, reverse=True)
    return render_template('standings/index.html', positions=positions, drivers=drivers, constructors=constructors)