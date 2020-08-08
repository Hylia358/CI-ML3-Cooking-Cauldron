import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Recipe_Book'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html',
                           recipes=mongo.db.Recipes.find())

@app.route('/lunch')
def lunch():
    return render_template('lunch.html',
                           recipes=mongo.db.Recipes.find())


@app.route('/dinner')
def dinner():
    return render_template('dinner.html',
                           recipes=mongo.db.Recipes.find())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
