from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ninja")
def ninja():
    return render_template('turtle.html')

@app.route("/ninja/<color>")
def choosecolor(color):
    color = color.lower()
    colors = ['blue', 'orange','red','purple']
    for i in colors:
        if color == i:
            return render_template('missing.html', hello=i)

    return render_template('missing.html', hello="notapril")

app.run(debug=True)
    
    



