from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html" , card_nums = 3 , card_color = "aqua")

@app.route("/play/<int:nums>")
def play_cards(nums):
    return render_template("index.html" , card_nums = nums, card_color = "aqua")

@app.route("/play/<int:nums>/<color>")
def play_cards_with_colors(nums, color):
    return render_template("index.html" , card_nums = nums, card_color = color)
    

if __name__ == "__main__":
    app.run(debug=True)