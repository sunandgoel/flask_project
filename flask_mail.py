from flask import Flask
from flask_mail import Mail
from flasgger import Swagger
from flasgger import swag_from


app = Flask(__name__)
mail = Mail(app)
swagger = Swagger(app)
# users = [("me","goel.sunand@gmail.com"),("sunand","yosunand@yahoo.com")]

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yofarhanrao@gmail.com'
app.config['MAIL_PASSWORD'] = 'ddxbwciwpososytf'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


users = [
    {
        'name':'sunand1',
        'email':'goel.sunand@gmail.com'
    },
    {
        'name':'sunand2',
        'email':'yosunand@yahoo.com'
    },
    {
        'name':'sunand3',
        'email':'yofarhanrao@gmail.com'
    }
]

from flask_mail import Message

@app.route("/mail/<mail_id>")
@swag_from('mail.yml')
def index(mail_id):
    if mail_id== "prod-GL":
        # if problem in bulk mail refer https://pythonhosted.org/Flask-Mail/ bulk mail setion
        for user in users:                  
            message = 'just to test'
            subject = "hello, %s" % user['name']
            msg = Message(
            sender="yofarhanrao@gmail.com",
            recipients=[user['email']],
            body=message,
            subject=subject)

            with app.open_resource("invoice.pdf") as fp:  
                # msg.attach("invoice.pdf", "application/pdf", fp.read()) 
                msg.attach("download.jpg",content_type="application/octet-stream") 
            mail.send(msg)
        
        return 'Sent'

    else:
        return 'error'
   
if __name__ == '__main__':
   app.run(debug = True)