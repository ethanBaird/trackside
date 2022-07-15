import pdb
from models.driver import Driver
import repositories.drivers_repository as driver_repository

driver_repository.delete_all()

driver1 = Driver("Charles Leclerc", 100, 6, 10)
driver_repository.save(driver1)

driver2 = Driver("Carlos Sainz", 92, 1, 7)
driver_repository.save(driver2)

driver1_update = Driver("Charles Leclerc", 200, 6, 11, driver1.id)

results = driver_repository.update(driver1_update)



pdb.set_trace()