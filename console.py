import pdb
from models.driver import Driver
from models.race import Race
from models.result import Result
from models.score import Score
from models.constructor import Constructor
import repositories.drivers_repository as driver_repository
import repositories.races_repository as races_repository
import repositories.scores_repository as scores_repository
import repositories.results_repository as results_repository
import repositories.constructors_repository as constructors_repository


results_repository.delete_all()
scores_repository.delete_all()
driver_repository.delete_all()
constructors_repository.delete_all()
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

c1 = Constructor('Ferrari', 0)
c2 = Constructor('Red Bull', 0)
c3 = Constructor('Mercedes', 0)
c4 = Constructor('Mclaren', 0)
c5 = Constructor('Alpine', 0)
c6 = Constructor('Aston Martin', 0)
c7 = Constructor('Haas', 0)
c8 = Constructor('Willaims', 0)
c9 = Constructor('Alfa Romeo', 0)
c10 = Constructor('AlphaTauri', 0)


constructors = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
for constructor in constructors:
    constructors_repository.save(constructor)

#ferrari
d1 = Driver("Charles Leclerc", c1, 0, 0, 0)
d2 = Driver("Carlos Sainz", c1, 0, 0, 0)
#redbull
d3 = Driver("Max Verstappen", c2, 0, 0, 0)
d4 = Driver("Sergio Perez", c2, 0, 0, 0)
#mercedes
d5 = Driver('Lewis Hamilton', c3, 0, 0, 0)
d6 = Driver("George Russell", c3, 0, 0, 0)
#mclaren
d7 = Driver('Lando Norris', c4, 0, 0, 0)
d8 = Driver('Daniel Ricciardo', c4, 0, 0, 0)
#alpine
d9 = Driver("Fernando Alonso", c5, 0, 0, 0)
d10 = Driver("Esteban Ocon", c5, 0, 0, 0)
#astonmartin
d11 = Driver("Sebastian Vettel", c6, 0, 0, 0)
d12 = Driver("Lance Stroll", c6, 0, 0, 0)
#haas
d13 = Driver("Mick Schumacher", c7, 0, 0, 0)
d14 = Driver("Kevin Magnussen", c7, 0, 0, 0)
#williams
d15 = Driver("Nicholas Latifi", c8, 0, 0, 0)
d16 = Driver("Alex Albon", c8, 0, 0, 0)
#alfaromeo
d17 = Driver("Valtteri Bottas", c9, 0, 0, 0)
d18 = Driver("Zhou Guanyou", c9, 0, 0, 0)
#alphatauri
d19 = Driver("Pierre Gasly", c10, 0, 0, 0)
d20 = Driver("Yuki Tsunoda", c10, 0, 0, 0)

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