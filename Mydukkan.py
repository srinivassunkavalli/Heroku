from flask import Flask,render_template
app=Flask(__name__)
@app.route('/login1')
def login1():
    return render_template("login1.html")
if __name__=="__main__":
    app.run(debug=True)