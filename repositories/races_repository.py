from db.run_sql import run_sql
from models.race import Race

def save(race):
    sql = """
        INSERT INTO races (location, circuit)
        VALUES (%s, %s)
        RETURNING id
    """
    values = [race.location, race.circuit]
    results = run_sql(sql, values)
    id = results[0]["id"]
    
    race.id = id

def select_all():
    races = []
    sql = """
        SELECT  * FROM races
    """
    results = run_sql(sql)

    for row in results:
        race = Race(row['location'], row['circuit'], row['id'])
        races.append(race)
    return races

def select(id):
    sql = """
        SELECT * FROM races
        WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        race = Race(result['location'], result['circuit'], result['id'])
    return race

def update(race):
    sql = """
        UPDATE races
        SET (location, circuit) = (%s, %s)
        WHERE id = %s
    """
    values = [race.location, race.circuit, race.id]
    run_sql(sql, values)

def delete(id):
    sql = """
        DELETE FROM races
        WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = """
        DELETE FROM races
    """
    run_sql(sql)