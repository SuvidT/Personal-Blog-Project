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

def formated_date_time(datetime):
    date, time = datetime.split(" ")
    
    date = date.split("-")
    temp = date.pop(0)
    date.append(temp)

    if date[0] == '01':
        date[0] = 'January'
    elif date[0] == '02':
        date[0] = 'February'
    elif date[0] == '03':
        date[0] = 'March'
    elif date[0] == '04':
        date[0] = 'April'
    elif date[0] == '05':
        date[0] = 'May'
    elif date[0] == '06':
        date[0] = 'June'
    elif date[0] == '07':
        date[0] = 'July'
    elif date[0] == '08':
        date[0] = 'August'
    elif date[0] == '09':
        date[0] = 'September'
    elif date[0] == '10':
        date[0] = 'October'
    elif date[0] == '11':
        date[0] = 'November'
    elif date[0] == '12':
        date[0] = 'December'

    # Return formatted date and time
    formatted_date = f"{date[0]} {date[1]}, {date[2]}"
    return formatted_date, time

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
    title, datetime = render_json(articleName)
    date, time = formated_date_time(datetime)

    return render_template("article.html", title=title, date=date, content=content)
######################################

########## Execution of Websites ##########
if __name__ == '__main__':
    app.run(debug=True)
###########################################