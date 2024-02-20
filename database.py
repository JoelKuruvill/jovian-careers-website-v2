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