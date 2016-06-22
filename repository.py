import pymongo

host = 'localhost'
port = 27017
dbname = 'car'

mongo_conn = pymongo.MongoClient(host)

table = mongo_conn[dbname].car

class CarRepository:
  def create_car(self, name, color):
    table = mongo_conn[dbname].car

    table.insert_one({
      name: name,
      color: color
    })

  def get_all_cars(self):
    table = mongo_conn[dbname].car

    return list(table.find())
