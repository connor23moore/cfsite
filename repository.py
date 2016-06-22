import pymongo

host = 'localhost'
port = 27017
dbname = 'vehicles'

mongo_conn = pymongo.MongoClient(host)

table = mongo_conn[dbname].car

class CarRepository:
  def create_car(self, name, color):

    table.insert_one({
      name: name,
      color: color
    })

  def get_all_cars(self):
    return list(table.find())
