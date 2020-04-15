from flask import Flask,render_template,request,url_for, redirect
import add
app = Flask(__name__)

#def sum(a,b):
    #return a+b

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'sum %s' % name

@app.route('/predict',methods=['POST'])
def predict():
        a=request.form['n1']
        b=request.form['n2']
        a=float(a)
        b=float(b)
        output=add.sum(a,b)
        return redirect(url_for('success', name = output))

if __name__ == '__main__':
    app.run(debug=True)
