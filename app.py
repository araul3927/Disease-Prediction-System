import csv
import diseaseprediction
from myproject import app,db
from flask import render_template,redirect,request,url_for,flash,abort,Flask
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm,RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash

with open('Testing.csv', newline='') as f:
    reader = csv.reader(f)
    symptoms = next(reader)
    symptoms = symptoms[:len(symptoms) - 1]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('main.html', symptoms=symptoms)

@app.route('/Welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are out !!")
    return redirect(url_for('home'))



@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('logged in successfully!')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user= User(email=form.email.data,
                   username=form.username.data,
                   password=form.password.data)


        db.session.add(user)
        db.session.commit()
        flash("Thanks for Registration!")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)



@app.route('/disease_predict', methods=['POST'])
def disease_predict():
    selected_symptoms = []
    if (request.form['Symptom1'] != "") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if (request.form['Symptom2'] != "") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if (request.form['Symptom3'] != "") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if (request.form['Symptom4'] != "") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if (request.form['Symptom5'] != "") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])
    if (request.form['Symptom6'] != "") and (request.form['Symptom6'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom6'])
    if (request.form['Symptom7'] != "") and (request.form['Symptom7'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom7'])
    if (request.form['Symptom8'] != "") and (request.form['Symptom8'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom8'])
    if (request.form['Symptom9'] != "") and (request.form['Symptom9'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom9'])
    if (request.form['Symptom10'] != "") and (request.form['Symptom10'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom10'])

    # disease_list = []
    # for i in range(7):
    #     disease = diseaseprediction.dosomething(selected_symptoms)
    #     disease_list.append(disease)
    # return render_template('disease_predict.html',disease_list=disease_list)
    disease = diseaseprediction.dosomething(selected_symptoms)
    return render_template('disease_predict.html', disease=disease, symptoms=symptoms)




if __name__ == '__main__':
    app.run(debug=True)
