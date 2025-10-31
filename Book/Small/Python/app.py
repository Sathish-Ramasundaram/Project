from flask import Flask

app = Flask(__name__)       # Create the Flask app

@app.route('/')             # Define a route for the homepage
def home():
    return "Hello, Sathish! This is your first Flask app."

if __name__ == '__main__':
    app.run(debug=True)     # Run the app in debug mode