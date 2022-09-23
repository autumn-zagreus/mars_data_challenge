from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
# use flask pymongo to set up the connection to the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    return "You reached the index"

@app.route("/scrape")
def scrape():
    # reference to a database collection (table)
    marsTable = mongo.db.marsData

    # drop the table if it exists
    mongo.db.marsData.drop()

    #return "You reached the scrape"
    # call scrape mars script
    mars_data = scrape_mars.scrape_all()
    #print(mars_data) # print the dictionary that is returned from the scrape all script
    #return mars_data
    # take dictionary, load into mongodb
    marsTable.insert_one(mars_data)


if __name__ == "__main__":
    app.run()