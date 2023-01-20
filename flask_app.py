from flask import render_template,Flask,request
import smtplib
import pickle

from email.mime.text import MIMEText
from flask import session
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "SECRET_KEY"


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="SailIndia",
    password="PASSWORD",
    hostname="SailIndia.mysql.pythonanywhere-services.com",
    databasename="SailIndia$saildetails",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class user97(db.Model):
    __tablename__ = 'sail_details'
    id =db.Column(db.Integer,db.Sequence('seq_book',start=1),primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(40))



def send_email(reciveremail):
    try:
        with open('input','rb') as fp:
            k=pickle.load(fp)
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'sailatindia@gmail.com '
        password = 'PASSWORD'
        sender = 'sailatindia@gmail.com '
        targets = reciveremail
        targets=targets.casefold()
        if targets not in k:
            k.append(targets)
            with open('input','wb') as fp1:
                pickle.dump(k,fp1)
            name=targets.split('@')
            name=name[0]
            session['name1']=name
            msg = MIMEText('Hello  {} !,Welcome to Sail India Enjoy your ride with SailIndia And Explore Incredible India.Here after you will receive our site updates of our site .Once again Enjoy travel Around INDIA.   \n \n\n                          Thank You  \n\n \n                                                 -Team Sail India'.format(name))
            msg['Subject'] = 'Sail_INDIA -Reg'
            msg['From'] = sender
            msg['To'] = targets

            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(sender, targets, msg.as_string())
            server.quit()

    except :
        with open('input','wb') as fp:
            pickle.dump([],fp)
        with open('input','rb') as fp:
            k=pickle.load(fp)
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'sailatindia@gmail.com '
        password = 'PASSWORD'
        sender = 'sailatindia@gmail.com '
        targets = reciveremail
        targets=targets.casefold()
        if targets not in k:
            k.append(targets)
            with open('input','wb') as fp1:
                pickle.dump(k,fp1)
            name=targets.split('@')
            session['name1']=name
            name=name[0]
            msg = MIMEText('Hello  {} !,Welcome to Sail India Enjoy your ride with SailIndia And Explore Incredible India.Here after you will receive our site updates of our site .Once again Enjoy travel Around INDIA.   \n \n\n                            Thank You  \n\n \n                                                   -Team Sail India'.format(name))
            msg['Subject'] = 'Sail_INDIA -Reg'
            msg['From'] = sender
            msg['To'] = targets

            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(sender, targets, msg.as_string())
            server.quit()


#session['row']=sail_details.fetchone()
#row = result.fetchone()
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        session['reciveremail']=request.form['email']
        send_email(session['reciveremail'])
        try:
            register = user97(username =session['name1'], email =session['reciveremail'])
            db.session.add(register)
            db.session.commit()
        except:
            pass
        return render_template('done.html')
    else :
        return render_template("getintouch.html")



@app.route('/admin',methods=['GET','POST'])
def adminpannel():
    otp = 'PASSWORD'
    #send_otp(otp)
    if request.method == 'POST':
        passw=request.form['pass']
        if passw != otp:
            return render_template('admin.html')
        else:
            row=user97.query.all()
            return render_template('show.html',books=row)
    else:
        return render_template('admin.html')







@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/weatherpage2')
def weatherpage2():
    return render_template('weather2.html')

@app.route('/weatherpage3')
def weatherpage3():
    return render_template('weather3.html')

@app.route('/weatherpage4')
def weatherpage4():
    return render_template('weather4.html')

@app.route('/home/state/ANDRAPRADESH')
def state_ANDRAPRADESH():
    return render_template('ANDRAPRADESH.html')

@app.route('/home/state/ARUNACHALPRADESH')
def state_ARUNACHALPRADESH():
    return render_template('ARUNACHALPRADESH.html')

@app.route('/home/state/ASSAM')
def state_ASSAM():
    return render_template('ASSAM.html')

@app.route('/home/state/BIHAR')
def state_BIHAR():
    return render_template('BIHAR.html')

@app.route('/home/state/CHHATTISGARH')
def state_CHHATTISGARH():
    return render_template('CHHATTISGARH.html')

@app.route('/home/state/GOA')
def state_GOA():
    return render_template('GOA.html')

@app.route('/home/state/GUJARAT')
def state_GUJARAT():
    return render_template('GUJARAT.html')

@app.route('/home/state/HARYANA')
def state_HARYANA():
    return render_template('HARYANA.html')

@app.route('/home/state/HIMACHALPRADESH')
def state_HIMACHALPRADESH():
    return render_template('HIMACHALPRADESH.html')

@app.route('/home/state/JHARKHAND')
def state_JHARKHAND():
    return render_template('JHARKHAND.html')

@app.route('/home/state/KARNATAKA')
def state_KARNATAKA():
    return render_template('KARNATAKA.html')

@app.route('/home/state/KERALA')
def state_KERALA():
    return render_template('KERALA.html')

@app.route('/home/state/MADHYAPRADESH')
def state_MADHYAPRADESH():
    return render_template('MADHYAPRADESH.html')

@app.route('/home/state/MAHARASHTRA')
def state_MAHARASHTRA():
    return render_template('MAHARASHTRA.html')

@app.route('/home/state/MANIPUR')
def state_MANIPUR():
    return render_template('MANIPUR.html')

@app.route('/home/state/MEGHALAYA')
def state_MEGHALAYA():
    return render_template('MEGHALAYA.html')

@app.route('/home/state/MIZORAM')
def state_MIZORAM():
    return render_template('MIZORAM.html')

@app.route('/home/state/NAGALAND')
def state_NAGALAND():
    return render_template('NAGALAND.html')

@app.route('/home/state/ODISHA')
def state_ODISHA():
    return render_template('ODISHA.html')

@app.route('/home/state/PUNJAB')
def state_PUNJAB():
    return render_template('PUNJAB.html')

@app.route('/home/state/RAJASTHAN')
def state_RAJASTHAN():
    return render_template('RAJASTHAN.html')

@app.route('/home/state/SIKKIM')
def state_SIKKIM():
    return render_template('SIKKIM.html')

@app.route('/home/state/TAMILNADU')
def state_TAMILNADU():
    return render_template('TAMILNADU.html')

@app.route('/home/state/TELANGANA')
def state_TELANGANA():
    return render_template('TELANGANA.html')

@app.route('/home/state/TRIPURA')
def state_TRIPURA():
    return render_template('TRIPURA.html')

@app.route('/home/state/UTTARPRADESH')
def state_UTTARPRADESH():
    return render_template('UTTARPRADESH.html')

@app.route('/home/state/UTTARAKHAND')
def state_UTTARAKHAND():
    return render_template('UTTARAKHAND.html')

@app.route('/home/state/WESTBENGAL')
def state_WESTBENGAL():
    return render_template('WESTBENGAL.html')

@app.route('/home/UnionTerritories/ANDAMANANDNICOBAR')
def UnionTerritories_ANDAMANANDNICOBAR():
    return render_template('ANDAMANANDNICOBAR.html')

@app.route('/home/UnionTerritories/DADRAANDNAGARHAVELI')
def UnionTerritories_DADRAANDNAGARHAVELI():
    return render_template('DADRAANDNAGARHAVELI.html')

@app.route('/home/UnionTerritories/LAKSHADWEEP')
def UnionTerritories_LAKSHADWEEP():
    return render_template('LAKSHADWEEP.html')

@app.route('/home/UnionTerritories/PUDUCHERRY')
def UnionTerritories_PUDUCHERRY():
    return render_template('PUDUCHERRY.html')

@app.route('/home/UnionTerritories/CHANDIGARH')
def UnionTerritories_CHANDIGARH():
    return render_template('CHANDIGARH.html')

@app.route('/home/UnionTerritories/DAMANANDDIU')
def UnionTerritories_DAMANANDDIU():
    return render_template('DAMANANDDIU.html')

@app.route('/home/UnionTerritories/NEWDELHI')
def UnionTerritories_NEWDELHI():
    return render_template('NEWDELHI.html')

@app.route('/home/UnionTerritories/JAMMUANDKASHMIR')
def UnionTerritories_JAMMUANDKASHMIR():
    return render_template('JAMMUANDKASHMIR.html')

@app.route('/home/UnionTerritories/LADAKH')
def UnionTerritories_LADAKH():
    return render_template('LADAKH.html')



