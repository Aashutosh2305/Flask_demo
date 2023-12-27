from flask import Flask, render_template , request


## create a simple flask application

app = Flask(__name__)

@app.route("/", methods=["GET"])

def welcome():
    return "<h2>Welcome to Aashutosh Page<h2>"


@app.route("/index",methods = ["GET"])

def index():
    return "<h2>welcome to Aashutosh index page<h2>"
# variable rule
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and score is : "+ str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has fail and the score is: " + str(score)


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')

    else:
        maths= float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        avereage_marks = (maths+science+history)/3

        return render_template('form.html',score = avereage_marks)




if __name__=="__main__":
    app.run(debug=True)
