from flaskblog.models import user,Education,Skill,WorkExperience
import secrets
import os
from  flaskblog.flask_form import RegistrationForm,LoginForm,educatino_form
from flask import render_template,url_for,redirect,request  ,flash #the flash use for one time message to send on a html page
from flaskblog import app,bcrypt,db
from flask_login import login_user,current_user,logout_user,login_required


@app.route('/')
@app.route('/home')
@login_required
def home():
    print(current_user.image_file)
    image = url_for('static',filename  = '../static/profile_pic/'+current_user.image_file)
    return render_template('home.html' ,image = image)


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


# # things related to script password in flask.
# bcrypt  = Bcrypt()
# a = bcrypt.generate_password_hash('testing').decode('utf-8')
# bcrypt.check_password_hash(a,'testing')
# it will give true or false

def save_picture(from_pic):
        random_hex= secrets.token_hex(8)
        # _,f_ext = os.path.splitext(from_pic.)


@app.route('/register' , methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        
        file  = request.files["files"]
        print(file)
        if 'file' not in request.files:
            print("return 'there is no file in form!'")
        file  = request.files["files"]
        path = os.path.join(app.config['static/'], file.filename)
        file.save(path)
        
        
        # if request.method == 'POST':
            
                
        #     image = request.files['file']
        #     print("image")
        #     # print(image.filename)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print('error')
        u = user(username= form.username.data,last_name = form.last_name.data,job = form.job.data,email= form.email.data,password =  hashed_password,phone_no =form.phone_no.data)
        print('error111111111')

        db.session.add(u)
        db.session.commit()
        # flash(f'your account has been created thanks {user.username}')

        print('accound has created')
        flash(f'account create for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',form = form )


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    forms = LoginForm()
    if forms.validate_on_submit():
        
        users = user.query.filter_by(email=forms.email.data).first()
        # password = user.query.filter_by(email=forms.email.data).first().password
        print(users)
        # print(user.query.filter_by(email=forms.email.data).first().password)
        if users and bcrypt.check_password_hash(users.password,forms.password.data):
              login_user(users,remember=forms.remember.data)
              flash(f'You have logedin  {users.username}','success')
              next_page = request.args.get('next')
              if next_page:
                  return redirect(next_page)
              else:
                return redirect(url_for('home'))
        else:
            flash(f'cant logoin please check email {forms.email.data}','danger')
    return render_template('login.html',form = forms )


@app.route('/logout', methods=['GET','POST'])
@login_required

def logout():
    logout_user()
    flash(f'you have loged of from this site','success')
    return redirect(url_for('login'))


@app.route('/education',methods=['GET','POST'])
@login_required
def education():
    forms = educatino_form()
    print(len(current_user.education))
    
    length = len(list(current_user.education))
    print(length)
    print('Educaiton')
    
    if request.method == "POST":
        # name = request.args.get("name")
        # age = request.args.get("age")
        # request.form['name']: use indexing if you know the key exists
        # request.form.get('name'): use get if the key might not exist/
        # request.form.getlist('name'): use getlist if the key is sent multiple times and you want a list of values. get only returns the first value.
        print(request.form.get('city'))
        edu =  request.form.get('edu')
        c =request.form.get('address')
        year = request.form.get('year')
        end_year = request.form.get('end_year')
        d = request.form.get('dis')
        
        ed = Education(education=edu,year_from = str(year),year_to = str(end_year),address = c,dicription= d,user_id1 = current_user.id)
        db.session.add(ed)
        db.session.commit()

        print()

    if forms.validate_on_submit():
        
        ed = Education(education=forms.Educations.data,year_from = str(forms.year_from.data),year_to = str(forms.year_to.data),address = forms.From.data,dicription= forms.discription.data,user_id1 = current_user.id)
        db.session.add(ed)
        db.session.commit()
        print('commited ')
        return redirect(url_for('home'))
    
    
    return render_template('education.html',form = forms,length  = length)
    
@app.route('/skill',methods=['GET','POST'])
@login_required
def skill():
    # print(len(current_user.Skill))
    modals = Skill()

    if request.method == 'POST':
        print("sikll  section ")
        print(request.form.get('sk'))
        sk =  request.form.get('sk')
        le =request.form.get('le')
        print(le)
        
        s =  Skill(skill_of = str(sk),level = le,user_id2 = current_user.id )
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('skill'))
        
    return render_template('skill.html',context=modals)
    pass

@app.route('/workexperience',methods=['GET','POST'])
@login_required
def workexperience():
    modals = WorkExperience()

    if request.method == 'POST':
        print("sikll  section ")
        print(request.form.get('pos'))
        print(request.form.get('emp'))
        print(request.form.get('city'))
        print(request.form.get('year_from'))
        print( request.form.get('year_to'))
        print(request.form.get('desc'))
        
        # s =  Skill(skill_of = str(sk),level = le,user_id2 = current_user.id )
        # db.session.add(s)
        # db.session.commit()
        
        # return redirect(url_for('skill'))
    print(current_user.work_experience)
    return render_template('workexperience.html')
    pass
