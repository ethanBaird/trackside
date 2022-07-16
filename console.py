import pdb
from models.driver import Driver
from models.race import Race
import repositories.drivers_repository as driver_repository
import repositories.races_repository as races_repository

driver_repository.delete_all()
races_repository.delete_all()

driver1 = Driver("Charles Leclerc", 100, 6, 10)
driver_repository.save(driver1)

driver2 = Driver("Carlos Sainz", 92, 1, 7)
driver_repository.save(driver2)

race1 = Race('Abu Dhabi', 'Yas Marina')
races_repository.save(race1)
race2 = Race('Bahrain', 'Bahrain International Circuit')
races_repository.save(race2)

result = races_repository.select(race2.id)




pdb.set_trace()