from flask import Flask
from flask import render_template

from . import models
from . import forms
from . import config
from . import tasks


app = Flask(__name__)
app.config.from_object(config.default)
queue = tasks.setup_rq(app)

@app.route('/', methods=['GET','POST'])
def hello_world():
    form = forms.NewMovieIdea()
    return render_template('base.html', form=form)
