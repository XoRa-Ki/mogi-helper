from flask import Flask, render_template, redirect, url_for, request
from functions import *

app = Flask(__name__)


@app.route('/')
def home() :
    return "Test"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('PNF404.html'), 404


@app.route('/manager', methods=['GET', 'POST'])
def manager() :
    if request.method == 'POST' :
        #Redirects to the new generated link that keep track of the mogi
        #The display link will be found on the new page
        #Need : database, link generator (done), code from line 26 to line 83 in the mogi-manager.py
        return redirect(url_for('runner'))
    else :
        #Display the form that ask for the informations needed to generate the link
        return render_template('initializer.html')

@app.route('/runner',  methods=['GET', 'POST'])
def runner() :
    if request.method == 'POST' :
        #update data / update display
        #or post and display results
        return 
    else :
        #get data, display current state of mogi
        #unique url using link_gen ?
        return


@app.route('/tracks')
def tracks() :
    return "Tracks"


@app.route('/bill')
def bill() :
    return "Bill Extends !!!"
