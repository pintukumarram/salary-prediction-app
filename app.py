from flask import Flask, render_template, request
from model import predict_salary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        experience = float(request.form["experience"])
        salary = predict_salary(experience)
        return render_template("index.html", prediction=f"Predicted Salary for {experience} years of experience is: ₹{salary:.2f}")
    return render_template("index.html", prediction="")

if __name__ == "__main__":
    app.run(debug=True)
