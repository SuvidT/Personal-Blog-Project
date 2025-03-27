from os.path import exists
from flask import Flask, render_template
import markdown
import json
from markupsafe import escape

app = Flask(__name__)

def render_md(filename):
    with open(f"articles/{filename}.md", "r", encoding="utf-8") as f:
        content = f.read()
    return markdown.markdown(content)

def render_json(filename):
    with open("articleDates.json", "r") as f:
        data = json.load(f)
    return filename, data[filename]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return "<h1>This is the intro page</h1>"

@app.route('/home')
def home():
    return "<h1>Personal Blog</h1>"

@app.route('/articles/<articleName>')
def article(articleName):
    # 1) check if file exists with OS
    file_path = f"articles/{escape(articleName)}.md"
    if not exists(file_path):
        # 2) if not render a template
        return render_template('404.html'), 404

    # 3) if yes then render it with the content template
    content = render_md(articleName)
    title, date = render_json(articleName)
    return render_template("article.html", title=title, date=date, content=content)

########## Execution of Websites ##########
if __name__ == '__main__':
    app.run(debug=True)