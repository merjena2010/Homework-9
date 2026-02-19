from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Home page with your specific name
    return render_template('home.html', name="Merjen")

@app.route('/about')
def about():
    # Bio reflecting your age and passion
    my_bio = "I am Merjen, a 15-year-old student and dedicated tennis player. I love the challenge of the court and the logic of coding!"
    return render_template('about.html', bio=my_bio)

@app.route('/hobbies')
def hobbies():
    # Your actual hobbies list
    hobbies_list = ["Playing Tennis", "Coding with Flask", "Listening to Music", "Traveling"]
    return render_template('hobbies.html', hobbies=hobbies_list)

if __name__ == '__main__':
    app.run(debug=True)