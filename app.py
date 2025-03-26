from flask import Flask, render_template
import markdown
from markupsafe import escape

app = Flask(__name__)

def render_md(filename):
    with open(f"articles/{filename}", "r", encoding="utf-8") as f:
        content = f.read()
    return markdown.markdown(content)

@app.route('/')
def index():
    return "<h1>This is the intro page</h1>"

@app.route('/home')
def home():
    return "<h1>Personal Blog</h1>"

@app.route('/article/<articleName>')
def article(articleName):
    # 1) check if file exists with OS
    # 2) if not render a template
    # 3) if yes then render it with the content template
    # 4) make a content template in templates folder
    pass

########## Execution of Websites ##########
if __name__ == '__main__':
    app.run(debug=True)