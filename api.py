from flask import Flask, request
from HLEmail import HLEmail

#Create app instance
app = Flask(__name__)

#Instantiate HLEmail
hlemail = HLEmail("email", "password")

@app.route("/send_html_email", methods=["POST"])
def send_html_email():
	hlemail.send_html_email( request.form["email"], request.form["message"] )

@app.route("/send_email", methods=["POST"])
def send_email():
	hlemail.send_email( request.form["email"], request.form["message"] )

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="80")
