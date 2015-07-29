from flask import Flask, render_template
app = Flask(__name__)

restaurants = {
    "best": "my favourite restaurant"
}

@app.route('/')
def root():
    return render_template("index.html")


def doThing(name):
    return "Hello, " + name

# Providing API endpoint
@app.route("/endpoint")
def endpoint():
    return restaurants["best"]

@app.route("/add/restaurant/<name>/<description>")
def add_restaurant(name, description):
    return doThing(name) + ", " + description

if __name__ == "__main__":
    app.run(debug=True)
