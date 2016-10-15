import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify

import json
app=Flask(__name__)
@app.route('/')
def djcons():
    return render_template("/index.html")

@app.route('/signup',methods=['GET','POST'])
def get_post_javascript_data():
    fromaddr = "shimlabiriyani@gmail.com"
    toaddr = "rohit.mercedesbenz@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = request.form.get('subject', 'not provided! :O')
    body = "Username - "+request.form.get('name', 'not provided! :O')+"\nEmail - "+request.form.get('email', 'not provided! :O')+"\nMessage -\n"+request.form.get('message', 'not provided! :O')
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "rohitunit4")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return jsonify(success=True,data="yes")
if __name__ == "__main__":
    app.run()
