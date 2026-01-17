from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Stores the latest location
location = {"lat": 0, "lon": 0}

@app.route("/")
def home():
    return "Server running"

@app.route("/driver")
def driver():
    return render_template("driver.html")

@app.route("/viewer")
def viewer():
    return render_template("viewer.html")

@app.route("/update_location", methods=["POST"])
def update_location():
    global location
    location = request.json
    return "OK"

@app.route("/get_location")
def get_location():
    return jsonify(location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
