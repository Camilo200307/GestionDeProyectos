import xmlrpc.client
from dotenv import load_dotenv
import os
 
load_dotenv(override=False)


#  database: 'dogsy-test',
#   username: 'admin',

url = os.environ.get("URL")
db = os.environ.get("DB")
username = os.environ.get("USER")
password = os.environ.get("PASSWORD")

print("==============>")
print(url)
print(db)
print(username)
print(password)
print("==============>")



# aplicacion FLASK
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/products")
def product():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    version = common.version()

    print("PRUEBA")
    print(version)

    uid = common.authenticate(db, username, password, {})

    # Llamada a metodo a traves de execute_kw
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    products = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[]], {'fields': ['description', 'name', 'barcode'], 'context' :{'lang': "es_ES"}})

    return jsonify(products)

