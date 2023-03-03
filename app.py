
from flask import Flask, render_template, request,redirect
from main import caloriespred
app = Flask(__name__)

value=False

@app.route("/")
def index():
    value=False
    return render_template("index.html",value=value)

@app.route('/calories',methods=['POST'])
def result():
    if request.method == 'POST':
        name=request.form.get("name")
        gender=request.form.get("gender"),
        age=request.form.get("age"),
        height=request.form.get("height"),
        weight=request.form.get("weight"),
        duration=request.form.get("duration"),
        heartrate=request.form.get("hrate"),
        bodytemp=request.form.get("temperature"),
        x=caloriespred(int(gender[0]),int(age[0]),float(height[0]),float(weight[0]),float(duration[0]),float(heartrate[0]),float(bodytemp[0]))
        value=True
    return render_template('index.html',answer=x,value=value,name=name)

if __name__ == "__main__":
    app.run(debug=True)