import pdb
from models.driver import Driver
from models.race import Race
from models.result import Result
from models.score import Score
import repositories.drivers_repository as driver_repository
import repositories.races_repository as races_repository
import repositories.scores_repository as scores_repository
import repositories.results_repository as results_repository

results_repository.delete_all()
scores_repository.delete_all()
driver_repository.delete_all()
races_repository.delete_all()

p1 = Score(1, 25, True, True)
p2 = Score(2, 19, False, True)
p3 = Score(3, 15, False, True)
p4 = Score(4, 12, False, False)
p5 = Score(5, 10, False, False)
p6 = Score(6, 8, False, False)
p7 = Score(7, 6, False, False)
p8 = Score(8, 4, False, False)
p9 = Score(9, 2, False, False)
p10 = Score(10, 1, False, False)

scores = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
for score in scores:
    scores_repository.save(score)

#ferrari
d1 = Driver("Charles Leclerc", 'Ferarri', 0, 0, 0)
d2 = Driver("Carlos Sainz", 'Ferarri', 0, 0, 0)
#redbull
d3 = Driver("Max Verstappen", 'Red Bull', 0, 0, 0)
d4 = Driver("Sergio Perez", 'Red Bull', 0, 0, 0)
#mercedes
d5 = Driver('Lewis Hamilton', 'Mercedes-AMG', 0, 0, 0)
d6 = Driver("George Russell", "Mercedes-AMG", 0, 0, 0)
#mclaren
d7 = Driver('Lando Norris', 'McLaren', 0, 0, 0)
d8 = Driver('Daniel Ricciardo', 'McLaren', 0, 0, 0)
#alpine
d9 = Driver("Fernando Alonso", 'Alpine', 0, 0, 0)
d10 = Driver("Esteban Ocon", 'Alpine', 0, 0, 0)
#astonmartin
d11 = Driver("Sebastian Vettel", 'Aston Martin', 0, 0, 0)
d12 = Driver("Lance Stroll", 'Aston Martin', 0, 0, 0)
#haas
d13 = Driver("Mick Schumacher", 'Haas', 0, 0, 0)
d14 = Driver("Kevin Magnussen", 'Haas', 0, 0, 0)
#williams
d15 = Driver("Nicholas Latifi", 'Williams', 0, 0, 0)
d16 = Driver("Alex Albon", 'Williams', 0, 0, 0)
#alfaromeo
d17 = Driver("Valtteri Bottas", 'Alfa Romeo', 0, 0, 0)
d18 = Driver("Zhou Guanyou", 'Alfa Romeo', 0, 0, 0)
#alphatauri
d19 = Driver("Pierre Gasly", 'AlphaTauri', 0, 0, 0)
d20 = Driver("Yuki Tsunoda", 'AlphaTauri', 0, 0, 0)

drivers = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]
for driver in drivers:
    driver_repository.save(driver)

r1 = Race('Bahrain', 'Bahrain Intl Circuit')
r2 = Race('Saudi Arabia', 'Jeddah Corniche Circuit')
r3 = Race('Australia', 'Albert Park Circuit')
r4 = Race('Italy', 'Autodromo Enzo e Dino Ferrari')
r5 = Race('USA', 'Miami International Autodrome')
r6 = Race('Spain', 'Circuit de Barcelona-Catalunya')
r7 = Race('Monaco', 'Circuit de Monaco')
r8 = Race('Azerbaijan', 'Baku City Circuit')
r9 = Race('Canada', 'Circuit Gilles-Villeneuve')
r10 = Race('Great Britain', 'Silverstone Circuit')

races = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
for race in races:
    races_repository.save(race)

pdb.set_trace()