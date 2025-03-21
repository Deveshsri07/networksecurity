from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus  # ✅ Import for escaping special characters

uri = "mongodb+srv://{}:{}@cluster0.wpkaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(
    quote_plus("DeveshSrivastava"),  # ✅ Escape username
    quote_plus("Devesh@123")  # ✅ Escape password
)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
