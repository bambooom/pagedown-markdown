
from flask import Flask, render_template, redirect, url_for
from flask.ext.wtf import Form
from wtforms import SubmitField
from flask_pagedown.fields import PageDownField
from flask_pagedown import PageDown
from flaskext.markdown import Markdown

app = Flask(__name__)
pagedown = PageDown(app)
Markdown(app)
app.config['SECRET_KEY'] = "test"

class PageDownFormExample(Form):
    pagedown = PageDownField('Enter your markdown')
    pagedown2 = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')

text=None
text2=None

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
    form = PageDownFormExample()
    global text
    global text2
    if form.validate_on_submit():
        text = form.pagedown.data
        text2 = form.pagedown2.data
        return redirect(url_for('home'))
    return render_template('index.html', form=form, text=text, text2=text2)

@app.route('/', methods=["GET"])
def home():
	#global text
	global text2
	return render_template('home.html', text2="\n"+text2)


if __name__ == '__main__':
	app.run(debug=True)