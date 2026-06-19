from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None
    if request.method == "POST":
        try:
            numbers = request.form["numbers"]
            data = [float(x.strip()) for x in numbers.split(",")]
            results = {
                "mean": np.mean(data),
                "median": np.median(data),
                "std": np.std(data),
                "variance": np.var(data)
            }
        except Exception:
            error = "Please enter valid numbers separated by commas."
    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    app.run(debug=True)
