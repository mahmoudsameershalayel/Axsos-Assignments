from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "dojo_fruit_store"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def create_checkout():
    order = {
        'strawberry': request.form['strawberry'],
        'raspberry': request.form['raspberry'],
        'apple': request.form['apple'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'student_id': request.form['student_id']
    }
    order['total'] = int(order['strawberry']) + int(order['raspberry']) + int(order['apple'])
    session['order'] = order
    print(f"Charging {order['first_name']} {order['last_name']} for {order['total']} fruits.")
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    if 'order' not in session:
        return redirect('/')
    return render_template("checkout.html", **session['order'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
