from flask import Flask, render_template, request
import joblib
#instance of an app
app = Flask(__name__)

model = joblib.load('dib_79.pkl')

@app.route('/')
def Welcome():
    return 'Welcome'

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/contact', methods=['POST'])
def contact():
    #Exp = request.form.get('exp')
    #email = request.form.get('mail')
    #contact = request.form.get('phone')
    #address = request.form.get('address')
    #print(Exp, email, contact, address)

    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')
    
    pred = model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])

    if pred[0] == 1:
        out = 'diabetic'
    else:
        out = 'not diabetic'

    return render_template('blog.html', predicted_text = f'the person is {out}')

#run the app
if __name__ == '__main__':
    app.run(debug=True)
