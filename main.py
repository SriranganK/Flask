from flask import Flask ,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
	return render_template("index.html")
@app.route("/submit",methods= ["GET","POST"])
def submit():
	name = request.form['firstname']
	return render_template("submit.html",jinga =name)
if __name__ == '__main__':
	app.run(debug=True,port=4000)
