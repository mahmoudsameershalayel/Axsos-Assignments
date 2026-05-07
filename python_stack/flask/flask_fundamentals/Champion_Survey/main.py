from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['user_name']
    location = request.form['location']
    language = request.form['language']
    experience = request.form['experience']
    techs =  request.form.getlist('techs')
    comment = request.form['comment']

    return render_template("result.html",
                           name=name,
                           location=location,
                           language=language,
                           experience = experience,
                           techs = techs,
                           comment=comment)


if __name__ == "__main__":
    app.run(debug = True)