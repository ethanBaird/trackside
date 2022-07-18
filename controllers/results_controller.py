from flask import Flask, Blueprint, redirect, render_template, request

import repositories.results_repository as results_repository
import repositories.scores_repository as scores_repository
import repositories.drivers_repository as drivers_repository
import repositories.races_repository as races_repository

results_blueprint = Blueprint("results", __name__)

#show one - on race page
@results_blueprint.route('/races/results/<race_id>')
def race_results(race_id):
    results = results_repository.select(race_id)
    return render_template('races/results/index.html', results=results)

