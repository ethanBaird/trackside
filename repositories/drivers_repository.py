
from db.run_sql import run_sql
from models.driver import Driver

def save(driver):
    sql = """
        INSERT INTO drivers (name, points, wins, podiums)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    values = [driver.name, driver.points, driver.wins, driver.podiums]
    results = run_sql(sql, values)
    id = results[0]["id"]
    driver.id = id


def select_all():
    drivers = []
    sql = """
        SELECT  * FROM drivers
    """
    results = run_sql(sql)

    for row in results:
        driver = Driver(row['name'], row['points'], row['wins'], row['podiums'], row['id'])
        drivers.append(driver)
    return drivers

def select(id):
    sql = """
        SELECT * FROM drivers
        WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        driver = Driver(result['name'], result['points'], result['wins'], result['podiums'], result['id'])
    return driver

def update(driver):
    sql = """
        UPDATE drivers
        SET (name, points, wins, podiums) = (%s, %s, %s, %s)
        WHERE id = %s
    """
    values = [driver.name, driver.points, driver.wins, driver.podiums, driver.id]
    run_sql(sql, values)

def delete(id):
    sql = """
        DELETE FROM drivers
        WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = """
        DELETE FROM drivers
    """
    run_sql(sql)