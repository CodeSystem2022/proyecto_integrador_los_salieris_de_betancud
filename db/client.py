from pymongo import MongoClient
from config import settings

MONGODB_URI = settings.MONGODB_URI

#conexion con mongodb
client_db= MongoClient(MONGODB_URI).app_gastos
