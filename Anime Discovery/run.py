from flask import Flask, render_template, redirect, request
import searching


app = Flask(__name__)

@app.route("/")
def index():
    # anime= main.main()
    return render_template("index.html")

# redirect to next page
@app.route('/verify', methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        name = request.form['search']
        
        # comple search operation here
        return redirect(f"/Results/{name}")

@app.route('/verify2', methods = ['POST', 'GET'])
def verify2():
    if request.method == 'POST':
        # comple search operation here
        return redirect(f"/")

@app.route('/Results/<name>')
def resultPage(name):
    
    anime= searching.main(name)
    return render_template("Results.html", results=anime)

app.run(host="0.0.0.0", port=80)