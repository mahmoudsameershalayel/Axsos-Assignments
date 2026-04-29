from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def default_board():
    return render_template("board.html", rows=8, cols=8 , color1 = "brown" , color2 = "white")

@app.route('/<int:cols>')
def specific_cols_board(cols):
    return render_template("board.html", rows=8, cols=cols , color1 = "brown" , color2 = "white")

@app.route('/<int:rows>/<int:cols>')
def specific_board(rows,cols):
    return render_template("board.html", rows=rows, cols=cols , color1 = "brown" , color2 = "white")

@app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
def custom_board(rows, cols, color1, color2):
    return render_template("board.html", rows=rows, cols=cols , color1 = color1 , color2 = color2)

if __name__ == "__main__":
    app.run(debug = True)