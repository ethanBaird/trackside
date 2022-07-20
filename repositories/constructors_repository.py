from db.run_sql import run_sql
from models.constructor import Constructor

def save(constructor):
    sql = """
        INSERT INTO constructors (name, points)
        VALUES (%s, %s)
        RETURNING id
    """
    values = [constructor.name, constructor.points]
    results = run_sql(sql, values)
    id = results[0]["id"]
    
    constructor.id = id

def select(id):
    sql = """
        SELECT * FROM constructors
        WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        constructor = Constructor(result['name'], result['points'], result['id'])
    return constructor

def select_all():
    constructors = []
    sql = """
        SELECT * FROM constructors
    """
    results = run_sql(sql)

    for row in results:
        constructor = Constructor(row['name'], row['points'], row['id'])
        constructors.append(constructor)
    return constructors

def update(constructor):
    sql = """
        UPDATE constructors
        SET (name, points) = (%s, %s)
        WHERE id = %s
    """
    values = [constructor.name, constructor.points, constructor.id]
    run_sql(sql, values)

def delete_all():
    sql = """
        DELETE FROM constructors
    """
    run_sql(sql)