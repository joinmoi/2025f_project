# project file 

from flask import Flask, render_template
# Create the Flask app
app = Flask(__name__)

# Home page route
@app.route("/")
def index():
    return "Welcome to our Flask Web Application!"

@app.route("/about")
def about(): 
    return render_template("about.html")

# This allows you to run the app directly
if __name__ == "__main__":
    app.run(debug=True)
