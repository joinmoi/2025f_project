# project file 

from flask import Flask
# Create the Flask app
app = Flask(__name__)

# Home page route
@app.route("/")
def index():
    return "Welcome to our Flask Web Application!"

# This allows you to run the app directly
if __name__ == "__main__":
    app.run(debug=True)
