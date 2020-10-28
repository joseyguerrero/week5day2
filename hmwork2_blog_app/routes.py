# Import the app variable from the init
from hmwork2_blog_app import app

# Import specific packages from Flask
from flask import render_template,request

# Import Our Form(s)
from hmwork2_blog_app.forms import UserInfoForm

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')


# GET == Gathering Info
# POST == Sending Info
@app.route('/avenregister', methods = ['GET','POST'])
def avenregister():
    #Init our Form
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get information from the form
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes from the form
        print(name,phone,email,password)
    return render_template('avenregister.html',user_form = form)