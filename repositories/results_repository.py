from copyreg import constructor
from lib2to3.pgen2 import driver
from unittest import result
from db.run_sql import run_sql
from models.result import Result

import repositories.scores_repository as scores_repository
import repositories.drivers_repository as drivers_repository
import repositories.races_repository as races_repository
import repositories.constructors_repository as constructors_repository

def save(result):
    sql = """
        INSERT INTO results (score_id, driver_id, constructor_id, race_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    values = [result.score.id, result.driver.id, result.constructor.id, result.race.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    result.id = id
    # adds result to driver
    driver = drivers_repository.select(result.driver.id)
    constructor = constructors_repository.select(result.constructor.id)

    driver.race(constructor, result)
    
    # saves change to db
    constructors_repository.update(constructor)
    drivers_repository.update(driver)
    



def select_all():
    race_results = []

    sql = "SELECT * FROM results"
    results = run_sql(sql)

    for row in results:
        race = races_repository.select(row['race_id'])
        driver = drivers_repository.select(row['driver_id'])
        score = scores_repository.select(row['score_id'])
        constructor = constructors_repository.select(row['constructor_id'])
        result = Result(score, driver, constructor, race, row['id'])
        race_results.append(result)
    return race_results

# results by race
def select_by_race(race_id):
    race_results = []
    sql = """
        SELECT * FROM results
        WHERE race_id = %s
    """
    values = [race_id]
    results = run_sql(sql, values)

    for row in results:
        race = races_repository.select(row['race_id'])
        driver = drivers_repository.select(row['driver_id'])
        score = scores_repository.select(row['score_id'])
        constructor = constructors_repository.select(row['constructor_id'])
        result = Result(score, driver, constructor, race, row['id'])
        race_results.append(result)
    return race_results

#results by driver
def select_by_driver(driver_id):
    driver_results = []
    sql = """
        SELECT * FROM results
        WHERE driver_id = %s
    """
    values = [driver_id]
    results = run_sql(sql, values)

    for row in results:
        race = races_repository.select(row['race_id'])
        driver = drivers_repository.select(row['driver_id'])
        score = scores_repository.select(row['score_id'])
        constructor = constructors_repository.select(row['constructor_id'])
        result = Result(score, driver, constructor, race, row['id'])
        driver_results.append(result)
    return driver_results
        


def delete_all():
    sql = """
        DELETE FROM results
    """
    run_sql(sql)