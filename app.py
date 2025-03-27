from os.path import exists
from flask import Flask, render_template
import markdown
import json
from markupsafe import escape

app = Flask(__name__)

########## File Reading Functions ##########
def render_md(filename):
    with open(f"articles/{filename}.md", "r", encoding="utf-8") as f:
        content = f.read()
    return markdown.markdown(content)

def render_json(filename):
    with open("articleDates.json", "r") as f:
        data = json.load(f)
    return filename, data[filename]
############################################

########## Routes and Pages ##########

##### 404 page not found #####
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
##############################

##### base route #####
@app.route('/')
def index():
    return "<h1>This is the intro page</h1>"
######################


@app.route('/home')
def home():
    return "<h1>Personal Blog</h1>"

@app.route('/articles/<articleName>')
def article(articleName):
    file_path = f"articles/{escape(articleName)}.md"
    
    if not exists(file_path):
        return render_template('404.html'), 404

    content = render_md(articleName)
    title, date = render_json(articleName)

    return render_template("article.html", title=title, date=date, content=content)
######################################

########## Execution of Websites ##########
if __name__ == '__main__':
    app.run(debug=True)
###########################################