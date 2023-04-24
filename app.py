import psutil
from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    per_cpu = psutil.cpu_percent(percpu=True)
    mem_metric = psutil.virtual_memory().percent
    message = None
    if cpu_metric > 80 or mem_metric > 80:
        message = "High Cpu or Memory Utilization detected. Please Scale up"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric , message=message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

    