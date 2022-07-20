from db.run_sql import run_sql

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