from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

# @app.route('/index.html')
# def home_button():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)