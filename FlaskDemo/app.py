#Flask App routing
from flask import Flask,render_template,request,redirect,url_for,jsonify

#create a flask application
app = Flask(__name__)      #initialize flask

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome to My Channel</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

#variable rule
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is : "+ str(score)

@app.route('/failure/<int:score>')
def failure(score):
    return "The person has failed and the score is :"+ str(score)


@app.route('/form',methods = ["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
     
        average_marks = (maths+science+history)/3

        if average_marks >= 50:
            result = "Success!!"
        else:
            result = "failure!"

        return redirect(url_for(result,score=average_marks))
        # return render_template("form.html",score=average_marks)

@app.route('/api',methods=['POST'])    
def caculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val + b_val)
    

if __name__ == "__main__": 
    app.run(debug=True)