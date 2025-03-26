from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

'''
Random routes when we haven't decided anything
'''
@app.route("/user/<name>")
def name(name):
    return f"Hello, {escape(name)}"

@app.route("/post/<int:id>")
def post(id):
    return f"Post: {escape(id)}"

'''
Important and main templates
'''
@app.route('/home')
def home():
    return "<h1>Personal Blod"

########## Execution of Websites ##########
if __name__ == '__main__':
    app.run(debug=True)