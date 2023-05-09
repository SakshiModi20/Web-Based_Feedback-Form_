from flask import Flask, render_template,request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client["business"]
collection = db["feedbacks"]
# ...


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        name = request.form.get("name", None)
        contact = request.form.get("contact", None)
        rating = request.form.get("rating")
        feedback = request.form.get("feedback")

        # Store the data in your MongoDB collection
        collection.insert_one({'name': name, 'contact': contact,'rating': rating, 'feedback': feedback})
        # Render a thank you page or redirect to the homepage
        return render_template('Thank_You.html')
    else:
        #Render the feedback form 
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


