from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

@app.route("/")
def index():
    return "You reached the index"

@app.route("/scrape")
def scrape():
    #return "You reached the scrape"
    # test to call scrape mars script
    mars_data = scrape_mars.scrape_all()
    #print(mars_data) # print the dictionary that is returned from the scrape all script
    return mars_data


if __name__ == "__main__":
    app.run()