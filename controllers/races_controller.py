from flask import Flask, Blueprint, redirect, render_template, request

from models.race import Race
from models.result import Result
import repositories.races_repository as races_repository
import repositories.drivers_repository as drivers_repository
import repositories.scores_repository as scores_repository
import repositories.results_repository as results_repository

races_blueprint = Blueprint("races", __name__)

#index
@races_blueprint.route('/races')
def races():
    races = races_repository.select_all()
    results = results_repository.select_all()
    return render_template('races/index.html', races=races, results=results)

# show '/races/<id>'
@races_blueprint.route('/races/<id>')
def show(id):
    race = races_repository.select(id)
    results = results_repository.select(id)
    return render_template('races/show.html', race=race, results=results)

# new '/races/new'
@races_blueprint.route('/races/new')
def new():
    scores = scores_repository.select_all()
    drivers = drivers_repository.select_all()
    return render_template('races/new.html', drivers=drivers, scores=scores)

# create '/races/new' method=['POST']
@races_blueprint.route('/races/new', methods=['POST'])
def create():
    location = request.form['location']
    circuit = request.form['circuit']
    race = Race(location, circuit)
    races_repository.save(race)
    
    # create result for each form option
    scores = scores_repository.select_all()
    position = 1
    for score in scores:
        driver_id = request.form[f'p{position}']
        driver = drivers_repository.select(driver_id)
        result = Result(score, driver, 'constructor', race)
        results_repository.save(result)
        position += 1

    return redirect('/races')

# edit 'races/<id>/edit
@races_blueprint.route('/races/<id>/edit')
def edit(id):
    race = races_repository.select(id)
    return render_template('races/edit.html', race=race)

# update 'races/<id> method ['POST']
@races_blueprint.route('/races/<id>/edit', methods=['POST'])
def update(id):
    location = request.form['location']
    circuit = request.form['circuit']

    driver = Race(location, circuit, id)
    races_repository.update(driver)
    return redirect('/races')

# delete 'drivers/<id>/delete
@races_blueprint.route('/races/<id>/delete', methods=['POST'])
def delete(id):
    races_repository.delete(id)
    return redirect('/races')

