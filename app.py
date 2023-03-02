
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/calories',methods=['POST','GET'])
def result():
    from main import caloriespred
    if request.method == 'POST':
        p=request.form.get("p"),
        g=request.form.get("g"),
        bp=request.form.get("bp"),
        st=request.form.get("st"),
        insulin=request.form.get("insulin"),
        bmi=request.form.get("bmi"),
        dpf=request.form.get("dpf"),
        age=request.form.get("age"),
        x=diabetes_predict(int(p[0]),int(g[0]),int(bp[0]),int(st[0]),int(insulin[0]),float(bmi[0]),float(dpf[0]),int(age[0]))
    y = Prediction.query.filter_by(user_name=session['user_name']).first()
    current_date = datetime.date.today()
    y.diabetes=x+"/"+str(current_date)
    db.session.add(y)
    db.session.commit()
    return redirect('/summary')

if __name__ == "__main__":
    app.run(debug=True)