from flask import Flask, Blueprint, redirect, render_template, request

from models.race import Race
import repositories.races_repository as races_repository

races_blueprint = Blueprint("races", __name__)

#index
@races_blueprint.route('/races')
def races():
    races = races_repository.select_all()
    return render_template('races/index.html', races=races)

# show '/races/<id>'
@races_blueprint.route('/races/<id>')
def show(id):
    race = races_repository.select(id)
    return render_template('races/show.html', race=race)

# new '/races/new'
@races_blueprint.route('/races/new')
def new():
    return render_template('races/new.html')

# create '/races/new' method=['POST']
@races_blueprint.route('/races/new', methods=['POST'])
def create():
    location = request.form['location']
    circuit = request.form['circuit']
    race = Race(location, circuit)
    races_repository.save(race)
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