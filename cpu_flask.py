from flask import Flask ,render_template
import logging
import os
import psutil

ROOT_DIR=os.path.abspath(os.path.dirname(__file__))

logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - "
                      "%(name)s:%(lineno)d [-] %(funcName)s- %(message)s")

logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or memory utilization detected!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)


# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')