#from sqlalchemy import create_engine
#print(sqlalchemy.__version__)

#Code used here to connect to MongoDB is provided from MongoDB for Python version 3.11
from pymongo.mongo_client import MongoClient
import os

uri = os.environ['DB_CONNECTION_STRING']

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
#try:
#  client.admin.command('ping')
#  print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#  print(e)


def load_jobs_from_db():
  database = client["DB-Web-App"]
  collection_name = database["webAppData"]
  results = collection_name.find({})
  #back on track!
  jobs = []
  for row in results:
    print(row)
    jobs.append(row)
  return jobs


def load_job_from_db(id):
  database = client["DB-Web-App"]
  collection_name = database["webAppData"]
  result = collection_name.find_one({"_id": format(id)})
  #TY Replit AI :)
  if not result:
    return None
  else:
    return result


#Working with MongoDB not MySQL..
def add_application_to_db(job_id, application):
  database = client["DB-Web-App"]
  collection_name = database["webAppApplications"]
  collection_name.insert_one(application)
