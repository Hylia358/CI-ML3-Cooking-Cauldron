import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Recipe_Book'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/breakfast')
def breakfast():
    recipes = mongo.db.Recipes.find({
                               "Category_name": "Breakfast"})
    return render_template('breakfast.html',
                           recipes=recipes)


@app.route('/lunch')
def lunch():
    recipes = mongo.db.Recipes.find({
                               "Category_name": "Lunch"})
    return render_template('lunch.html',
                           recipes=recipes)


@app.route('/dinner')
def dinner():
    recipes = mongo.db.recipes.find({
                               "Category_name": "Dinner"})
    return render_template('dinner.html',
                           recipes=recipes)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_recipes', methods=['POST'])
def add_recipes():
    recipes = mongo.db.Recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('breakfast'))


@app.route('/add_rep')
def add_rep():
    return render_template('add_recipe.html')


@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
