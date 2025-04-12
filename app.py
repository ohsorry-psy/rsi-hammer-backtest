from flask import Flask, render_template, request, send_file
from generate_chart import generate_combined_chart
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    symbol = request.form["symbol"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    commission = float(request.form.get("commission", 0.2)) / 100

    chart_path = generate_combined_chart(symbol, start_date, end_date, commission)
    if chart_path and os.path.exists(chart_path):
        return send_file(chart_path, mimetype='image/png')
    else:
        return "차트 생성 실패"

if __name__ == "__main__":
    app.run(debug=True)

