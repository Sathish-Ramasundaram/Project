from flask import Flask

app = Flask(__name__)

@app.route('/getPage')  # This route handles requests to /getPage
def show_page():
    return "This is the GET page!"

@app.route('/about')
def about_page():
    return "This is the About page. Welcome, Sathish!"

if __name__ == '__main__':
    app.run(debug=True)

'''
How to run this program
python program-name.py
click the link
put /getPage
or
/about

'''